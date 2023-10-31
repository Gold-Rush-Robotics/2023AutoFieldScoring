import cv2
import numpy as np
import time
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    check, frame = cam.read()
    font = cv2.FONT_HERSHEY_DUPLEX
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray_blurred = cv2.blur(gray, (3, 3))
    

       
    
    detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 60,param2 = 25, minRadius = 2, maxRadius = 16)



    if detected_circles is not None:
        detected_circles = np.uint16(np.around(detected_circles))
  
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            
        # Draw the circumference of the circle.
            #x,y,w,h = cv2.boundingRect(cnt)
           
            cv2.circle(img, (a, b), r, (0, 255, 0), 2)
  
        # Draw a small circle (of radius 1) to show the center.
            cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
            cv2.rectangle(img,(a-r,b-r),(a+r,b+r),(0,0,0),2)
            cropped_image = img[(a-r):(b-r),(a+r):(b+r)]
            
            print(cv2.mean(cropped_image))
            time.sleep(.1)
    cv2.imshow("Detected Circle", img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break