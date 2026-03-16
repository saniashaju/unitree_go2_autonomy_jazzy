import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from unitree_api.msg import Request
import json

class Bridge(Node):
    def __init__(self):
        super().__init__('cmd_vel_to_unitree')
        self.pub = self.create_publisher(Request, '/api/sport/request', 10)
        self.sub = self.create_subscription(Twist, '/cmd_vel', self.callback, 10)
        print("Bridge is LIVE. Waiting for keyboard keys...")

    def callback(self, msg):
        req = Request()
        req.header.identity.id = 1
        req.header.identity.api_id = 1008 # Move API ID
        data = {"x": msg.linear.x, "y": msg.linear.y, "z": msg.angular.z}
        req.parameter = json.dumps(data)
        self.pub.publish(req)

def main():
    rclpy.init()
    rclpy.spin(Bridge())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
