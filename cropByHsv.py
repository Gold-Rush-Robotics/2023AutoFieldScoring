import cv2 as cv
import numpy as np

def cropByHSV(img:cv.Mat, lower_hsv:np.array, upper_hsv:np.array):
    #create mask 
    hsvImg = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    blur = cv.medianBlur(hsvImg, 15)
    mask = cv.inRange(blur, lower_hsv, upper_hsv)
    masked = cv.bitwise_and(blur, blur, mask = mask)

    #convert masked to grayscale
    gray = cv.cvtColor(masked, cv.COLOR_BGR2GRAY)

    edges = cv.Canny(gray,50,150,apertureSize=3)
    lines_list =[]
    lines = cv.HoughLinesP(
            edges, # Input edge image
            rho=1, # Distance resolution in pixels
            theta=np.pi/180, # Angle resolution in radians
            threshold=50, # Min number of votes for valid line
            minLineLength=5, # Min allowed length of line
            maxLineGap=50 # Max allowed gap between line for joining them
            )
    for points in lines:
      # Extracted points nested in the list
        x1,y1,x2,y2=points[0]
        # Draw the lines joing the points
        # On the original image
        cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
        # Maintain a simples lookup list for points
        lines_list.append([(x1,y1),(x2,y2)])
     
    cv.imshow("img", img)



