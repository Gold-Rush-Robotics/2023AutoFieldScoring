#!/usr/bin/python3


from typing import List
import rclpy
from rclpy.node import Node
from rclpy.context import Context
from rclpy.parameter import Parameter

from std_msgs.msg import Bool


class Field(Node):
    def __init__(self) -> None:
        super().__init__("grr_field")
        self.publisher = self.create_publisher(Bool, "end_button", 10)
        self.subscription = self.create_subscription(Bool, "start", self.start, 10)
    
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
