#!/usr/bin/python3


# -- SRV imports
from grr_field_interfaces.srv import Thruster

# -- Import
import cv2 
import numpy as np 
import math
import rclpy
from rclpy.node import Node
  



# -- Thruster Service Node
class ThrusterCount(Node):
    def __init__(self):
        super().__init__('ThrusterCount')
        self.srv = self.create_service(Thruster, 'Counting_Thrusters', self.Thruster_count_callback)

    def Thruster_count_callback(self, response):
        cam = cv2.VideoCapture(1)

        check, frame = cam.read()

        # number of tanks scored
        scored = 3


        # Read image. 
        img = frame
        
        # Convert to grayscale. 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        
        # Blur using 3 * 3 kernel. 
        gray_blurred = cv2.blur(gray, (3, 3)) 
        
        # Apply Hough transform on the blurred image. 
        detected_circles = cv2.HoughCircles(gray_blurred,  
                        cv2.HOUGH_GRADIENT, 1, 20, param1 = 40, 
                    param2 = 25, minRadius = 1, maxRadius = 15) 
        
        # Draw circles that are detected. 
        if detected_circles is not None: 
        
            # Convert the circle parameters a, b and r to integers. 
            detected_circles = np.uint16(np.around(detected_circles)) 
        
            for pt in detected_circles[0, :]: 
                

                scored-=1

                a, b, r = pt[0], pt[1], pt[2] 
            
                # Draw the circumference of the circle. 
                cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
        
                # Draw a small circle (of radius 1) to show the center. 
                cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 

                cropped_image = img[b-int(r*(math.sqrt(2))/2):b+int(r*(math.sqrt(2))/2), a-int(r*(math.sqrt(2))/2):a+int(r*(math.sqrt(2))/2)]

                mean = cv2.mean(cropped_image)

                # if circle is too bright (false positive) add point back
                if mean[2]>110:
                    scored+=1
                
                
                ##cv2.waitKey(0) 

        response.fuel_tanks_placed = scored
        return response
    
def main():
    rclpy.init()

    ThrusterCount = ThrusterCount()

    rclpy.spin(ThrusterCount)

    rclpy.shutdown()

if __name__ == '__main__':
    main()