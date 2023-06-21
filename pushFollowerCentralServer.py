from time import sleep
import rclpy
from std_msgs.msg import String


def cb(msg):
   print(f'I heard:"{msg.data}"')
   msg.data = msg.data + f'+push'
   print(f'Publishing:"{msg.data}"')
   pub.publish(msg)
   
rclpy.init()
node = rclpy.create_node('pushFollower')
pub = node.create_publisher(String, 'motion',10)
sub = node.create_subscription(String, 'sensors',cb,10)

rclpy.spin(node)
