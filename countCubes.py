import cv2 as cv
import numpy as np

blue0 = (50, 20, 408, 290)
blue1 = (405, 170, 124, 162)
red = (475, 27, 129, 131)

def red_pipeline(img:cv.Mat):
    imCrop = img[int(red[1]):int(red[1]+red[3]), int(red[0]):int(red[0]+red[2])]
    hsv = cv.cvtColor(imCrop, cv.COLOR_BGR2HSV)
    cubePixels = 0
    for row in hsv:
        for h, _, _ in row:
            if not(h > 2 and h < 19):
                cubePixels += 1
    print(f"Red: {np.round(cubePixels/833) : .2f}")
    cv.imshow("Red", imCrop)


def blue_pipeline(img:cv.Mat):
    imCrop0 = img[int(blue0[1]):int(blue0[1]+ blue0[3]), int(blue0[0]):int(blue0[0]+blue0[2])]
    imCrop1 = img[int(blue1[1]):int(blue1[1]+ blue1[3]), int(blue1[0]):int(blue1[0]+blue1[2])]
    hsv0 = cv.cvtColor(imCrop0, cv.COLOR_BGR2HSV)
    hsv1 = cv.cvtColor(imCrop1, cv.COLOR_BGR2HSV)
    cubePixels = 0
    for row in hsv0:
        for h, _, _ in row:
            if h > 13 and h < 33:
                cubePixels += 1
    for row in hsv1:
        for h, _, _ in row:
            if h > 20 and h < 40:
                cubePixels += 1
    print(f"Blue: {np.round(cubePixels/3333) : .2f}")
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
        blue_pipeline(img)
        key = cv.waitKey(1)
        if key == ord('q'):
            break
