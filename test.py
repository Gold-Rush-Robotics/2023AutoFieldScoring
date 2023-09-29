import cv2 as cv

camnum = 0
cam = cv.VideoCapture(camnum)

if not cam.isOpened():
    print(f"No camera {camnum}")
    exit()

ret, frame = cam.read()

cv.imwrite(f"cam{camnum}.png", frame)