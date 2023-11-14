#!/usr/bin/python3


from typing import List
import rclpy
import cv2 as cv
from rclpy.node import Node
from rclpy.context import Context
from rclpy.parameter import Parameter
from std_msgs.msg import Bool, Header
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from grr_field_interfaces.srv import ImageRequest


class Field(Node):
    def __init__(self) -> None:
        super().__init__("grr_field")
        self.publisher = self.create_publisher(Bool, "end_button", 10)
        self.subscription = self.create_subscription(Bool, "start", self.start, 10)
        #for retrieving field imgs
        self.cams = [cv.VideoCapture(0), cv.VideoCapture(2)]
        self.bridge = CvBridge()
        self.getCam = self.create_service(ImageRequest, 'getCam', self.cam_callback)
        self.pub = self.create_publisher(Image, 'cam0', 10)
        self.timer = self.create_timer(0.5, self.timerCallback)
        
    def timerCallback(self):
        ret, image = self.cams[0].read()
        msg = self.bridge.cv2_to_imgmsg(image, encoding="passthrough")
        self.pub.publish(msg)
    
    def cam_callback(self, request, response):
        print("requested")
        ret, image = self.cams[request.cam].read()
        print(f"got image {ret}")
        response.frame = self.bridge.cv2_to_imgmsg(image, encoding="passthrough")
        print("passed through")
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
