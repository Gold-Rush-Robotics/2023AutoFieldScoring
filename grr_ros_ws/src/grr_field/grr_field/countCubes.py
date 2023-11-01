import rclpy
import sys
import cv2 as cv

from rclpy.node import Node
from grr_field_interfaces.srv import ImageRequest
from cv_bridge import CvBridge

class cubeCounter(Node):

    def __init__(self):
        super().__init__("cubeCounter")
        #roi coordinates
        self.blue0 = (50, 20, 408, 290)
        self.blue1 = (405, 170, 124, 162)
        self.red = (475, 27, 129, 131)
        #for reading field imgs
        self.cam1Clt = self.create_client(ImageRequest, 'cam1')
        self.cam2Clt = self.create_client(ImageRequest, 'cam2')
        #check services are available and send requests
        while not self.cam1Clt.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req1 = ImageRequest.Request()
        
        while not self.cam2Clt.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req2 = ImageRequest.Request()

    def requestCam1(self):
        self.future1 = self.cam1Clt.call_async(self.req1)
        rclpy.spin_until_future_complete(self, self.future1)
        return self.future1.result()
    
    def requestCam2(self):
        self.future2 = self.cam2Clt.call_async(self.req2)
        rclpy.spin_until_future_complete(self, self.future2)
        return self.future2.result()


def main():
    rclpy.init()
    counter = cubeCounter()
    bridge = CvBridge()
    cam = cv.VideoCapture(0)
    cvImg1 = bridge.imgmsg_to_cv2(counter.requestCam1, encoding="passthrough")
    cvImg2 = bridge.imgmsg_to_cv2(counter.requestCam2, encoding="passthrough")

  
    cv.imshow("cam1", cvImg1)
    cv.imshow("cam2", cvImg2)