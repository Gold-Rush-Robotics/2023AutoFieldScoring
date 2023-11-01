#!/usr/bin/python3


from typing import List
import rclpy
from rclpy.node import Node
from rclpy.context import Context
from rclpy.parameter import Parameter

from std_msgs.msg import Bool, Header
from sensor_msgs.msg import Image

from cv_bridge import CvBridge

from grr_field_interfaces.srv import ImageRequest

import cv2


class Field(Node):
    def __init__(self) -> None:
        super().__init__("grr_field")
        self.publisher = self.create_publisher(Bool, "end_button", 10)
        self.subscription = self.create_subscription(Bool, "start", self.start, 10)
        self.cams = [cv2.VideoCapture(0), cv2.VideoCapture(1)]
        self.bridge = CvBridge()
    
    def cam_callback(self, request, response):
        ret, image = self.cams[request.cam].read()
        response.frame = self.bridge.cv2_to_imgmsg(image)
        return response
    
    def start(self, data:Bool) -> None:
        self.get_logger().info(f"Got a message on start saying {data}")
    
    
def main():
    rclpy.init()
    field = Field()

    rclpy.spin(field)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    field.destroy_node()
    rclpy.shutdown()
