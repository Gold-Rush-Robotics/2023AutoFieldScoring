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
        self.cli = self.create_client(ImageRequest, 'getCam')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = ImageRequest.Request()
        self.bridge = CvBridge()

    def getCVImage(self, camNum:int):
        self.req.cam = camNum
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.bridge.imgmsg_to_cv2(self.future.result().frame, "passthrough")
    

def main():
    rclpy.init()
    counter = cubeCounter()
    img0 = counter.getCVImage(0)
    img1 = counter.getCVImage(1)

    cv.imshow("cam1", img0)
    cv.imshow("cam2", img1)