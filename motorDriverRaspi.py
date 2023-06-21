import rclpy
from std_msgs.msg import String

def cb(msg):
   print(f'I heard:"{msg.data}"')

rclpy.init()
node = rclpy.create_node('motorDriver')
sub = node.create_subscription(String, 'motion',cb,10)
rclpy.spin(node)


