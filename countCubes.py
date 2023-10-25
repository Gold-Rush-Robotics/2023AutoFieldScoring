import cv2 as cv
import numpy as np
from cropByHsv import cropByHSV

#roi coordinates
blue0 = (50, 20, 408, 290)
blue1 = (405, 170, 124, 162)
red = (475, 27, 129, 131)

def red_pipeline(img:cv.Mat):
    #crop image and convert to hsv
    imCrop = img[int(red[1]):int(red[1]+red[3]), int(red[0]):int(red[0]+red[2])]
    hsv = cv.cvtColor(imCrop, cv.COLOR_BGR2HSV)
    #define color bounds
    lower_h = np.array([2, 0, 0], dtype = "uint8")
    upper_h = np.array([19, 255, 255], dtype = "uint8")
    #create color mask
    mask = cv.inRange(hsv, lower_h, upper_h)
    #count cubes
    output = cv.bitwise_and(hsv, hsv, mask = mask)
    print(f"Small Cubes: {np.sum(output)}")
    cv.imshow("Red", imCrop)
    cv.imshow("mask", mask)


def blue_pipeline(img:cv.Mat):
    #crop images
    imCrop0 = img[int(blue0[1]):int(blue0[1]+ blue0[3]), int(blue0[0]):int(blue0[0]+blue0[2])]
    imCrop1 = img[int(blue1[1]):int(blue1[1]+ blue1[3]), int(blue1[0]):int(blue1[0]+blue1[2])]
    #switch imgs to hsv
    hsv0 = cv.cvtColor(imCrop0, cv.COLOR_BGR2HSV)
    hsv1 = cv.cvtColor(imCrop1, cv.COLOR_BGR2HSV)
    #define color bounds for mask
    lower_h = np.array([28,0, 0], dtype = "uint8")
    upper_h = np.array([33, 255, 255], dtype = "uint8")
    #create mask and count cubes
    mask0 = cv.inRange(hsv0, lower_h, upper_h)
    mask1 = cv.inRange(hsv1, lower_h, upper_h)
    output0 = cv.bitwise_and(hsv0, hsv0, mask = mask0)
    output1 = cv.bitwise_and(hsv1, hsv1, mask = mask1)
    cubePixels = np.sum(output0) + np.sum(output1)
    cubes = np.round(cubePixels/870000)

    #show images
    print(f"Large Cubes: {cubes}")
    cv.imshow("Blue", imCrop0)
    cv.imshow("Blue corner", imCrop1)

if __name__ == "__main__":
    #initialize cam object
    cam = cv.VideoCapture(0)
    #read cam images to warm-up cameras 
    for i in range(6):
        ret, img = cam.read()
    while True:
        ret, img = cam.read()
        #red_pipeline(img)
        #blue_pipeline(img)
        lower_hsv = np.array([[5, 0, 167]], dtype = "uint8")
        upper_hsv = np.array([15, 255, 255], dtype = "uint8")
        lines = cropByHSV(img, lower_hsv, upper_hsv)

        x0, y0 = lines[0]
        x1, y1 = lines[2]
        cv.line(img, x0, y0, 255, 10)
        cv.line(img, x1, y1, 255, 10)


        cv.imshow("img", img)
        key = cv.waitKey(1)
        if key == ord('q'):
            break
