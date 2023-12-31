import cv2 as cv
import numpy as np

if __name__ == "__main__":
    #initialize cam object
    cam = cv.VideoCapture(0)
    #capture images to warm up camera
    for i in range(6):
        img = cam.read()

    #select region
    ret, img = cam.read()
    r = cv.selectROI("image", img)

    #show cropped image
    cropped_image = img[int(r[1]):int(r[1]+r[3]), 
                      int(r[0]):int(r[0]+r[2])]
    cv.imshow("cropped", cropped_image)
    key = cv.waitKey(0)

    #compute average h color val and standard deviation
    hsv = cv.cvtColor(cropped_image, cv.COLOR_BGR2HSV)
    (h, s, v) = cv.split(hsv.astype("float"))

    #print
    print(f"Mean: {np.mean(h) : .2f}")
    print(f"Standard Deviation: {np.std(h) : .2f}")

    