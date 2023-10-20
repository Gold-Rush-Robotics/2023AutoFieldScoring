from typing import List
import rclpy
from rclpy import Node
from rclpy.context import Context
from rclpy.parameter import Parameter

from std_msgs.msg import Bool


class Field(Node):
    def __init__(self) -> None:
        super().__init__("grr_field")
        self.publisher = self.create_publisher(Bool, "end_button", 10)
        self.subscription = self.create_subscription(Bool, "start", self.start)
    
    def start(self, data:Bool) -> None:
        pass