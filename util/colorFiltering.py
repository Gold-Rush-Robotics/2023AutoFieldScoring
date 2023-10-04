import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
cv2.namedWindow('Trackbar window')

#Open webcam, choose the nbr change '0' to nbr of your webcam
capture = cv2.VideoCapture(0)

# create trackbars for color change
cv2.createTrackbar('H_high','Trackbar window',0,255,nothing)
cv2.createTrackbar('S_high','Trackbar window',0,255,nothing)
cv2.createTrackbar('V_high','Trackbar window',0,255,nothing)
cv2.createTrackbar('H_low','Trackbar window',0,255,nothing)
cv2.createTrackbar('S_low','Trackbar window',0,255,nothing)
cv2.createTrackbar('V_low','Trackbar window',0,255,nothing)

#Setting the "high" trackbars to max values (255)
cv2.setTrackbarPos('H_high','Trackbar window', 255)
cv2.setTrackbarPos('S_high','Trackbar window', 255)
cv2.setTrackbarPos('V_high','Trackbar window', 255)

while(1):
    _, frame = capture.read()
    cv2.imshow('Trackbar window', np.zeros((1,512,3), np.uint8))
    
    _f = cv2.medianBlur(frame, 15)
    _f = cv2.cvtColor(_f, cv2.COLOR_BGR2HSV) #To HSV

    # get current positions of four trackbars 
    #These are HSV values
    h_low = cv2.getTrackbarPos('H_low','Trackbar window')
    s_low = cv2.getTrackbarPos('S_low','Trackbar window')
    v_low = cv2.getTrackbarPos('V_low','Trackbar window')
    h_high = cv2.getTrackbarPos('H_high','Trackbar window')
    s_high = cv2.getTrackbarPos('S_high','Trackbar window')
    v_high = cv2.getTrackbarPos('V_high','Trackbar window')

    # define range of color in HSV
    lower_bound = np.array([h_low,s_low,v_low])
    upper_bound = np.array([h_high,s_high,v_high])
    
    
    mask = cv2.inRange(_f, lower_bound, upper_bound)
    frame = cv2.bitwise_and(frame, frame, mask = mask) #Comment this line if you won't show the frame later

    #Comment the one you won't need
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)


    k = cv2.waitKey(1) & 0xFF
    if k == 27: #press escape to exit
        break

    
capture.release()   #Release the camera
cv2.destroyAllWindows() #Close all windows