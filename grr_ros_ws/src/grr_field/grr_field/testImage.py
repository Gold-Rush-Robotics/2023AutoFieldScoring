from typing import List
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter
from cv_bridge import CvBridge
import rclpy
import cv2


from grr_field_interfaces import ImageRequest

class Viewer(Node):
    def __init__(self) -> None:
        super().__init__("viewer")
        self.cli = self.create_client(ImageRequest, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = ImageRequest.Request()
        self.bridge = CvBridge()
    
    def getCVImage(self, camNum:int):
        self.req.cam = camNum
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
       
        return  self.bridge.imgmsg_to_cv2(self.future.result(), "passthrough")
    
def main():
    rclpy.init()
    viewer = Viewer()
    while True:
        img = viewer.getCVImage(0)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    
    


