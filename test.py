import cv2 as cv
import numpy as np

blue = (44, 13, 420, 308)
red = (467, 19, 135, 141)

def red_pipeline(img:cv.Mat):
    imCrop = img[int(red[1]):int(red[1]+red[3]), int(red[0]):int(red[0]+red[2])]
    hsv = cv.cvtColor(imCrop, cv.COLOR_BGR2HSV)
    """ cubePixels = 0
    for row in imCrop:
        for h, _, _ in row:
            if h > 5 and h < 7:
                cubePixels += 1
    print(cubePixels) """

    print(cv.mean(hsv))
    cv.imshow("test", imCrop)


def blue_pipeline(img:cv.Mat):
    imCrop = img[int(blue[1]):int(blue[1]+ blue[3]), int(blue[0]):int(blue[0]+blue[2])]
    cv.imshow("test2", imCrop)

if __name__ == "__main__":

    cam = cv.VideoCapture(0)
    while True:
        ret, img = cam.read()
        red_pipeline(img)
        blue_pipeline(img)
        key = cv.waitKey(0)
        if key == ord('q'):
            break