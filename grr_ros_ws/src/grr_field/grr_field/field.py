#!/usr/bin/python3


from typing import List
import rclpy
import cv2 as cv
from rclpy.node import Node
from rclpy.context import Context
from rclpy.parameter import Parameter
from std_msgs.msg import Bool, Header
from sensor_msgs.msg import Image
from grr_field_interfaces.srv import ImageRequest
from cv_bridge import CvBridge


class Field(Node):
    def __init__(self) -> None:
        super().__init__("grr_field")
        self.publisher = self.create_publisher(Bool, "end_button", 10)
        self.subscription = self.create_subscription(Bool, "start", self.start, 10)
        self.getImg = self.create_service(ImageRequest, "cam1", 10) #for reading cams
    
    def start(self, data:Bool) -> None:
        self.get_logger().info(f"Got a message on start saying {data}")
    
    def getCam1(self, req:Header, ret:Image): 
        cam = cv.videoCapture(0)
        cv_img = cam.read()
        #convert to ros img
        bridge = CvBridge()
        ret = bridge.cv2_to_imgmsg(cv_img, encoding="passthrough")
        return ret

    def getCam2(self, req:Header, ret:Image):
        cam = cv.videoCapture(1)
        cv_img = cam.read()
        #convert to ros img
        bridge = CvBridge()
        ret = bridge.cv2_to_imgmsg(cv_img, encoding="passthrough")
        return ret
    
def main():
    rclpy.init()
    field = Field()

    rclpy.spin(field)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    field.destroy_node()
    rclpy.shutdown()
