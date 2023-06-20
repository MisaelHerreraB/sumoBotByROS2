from time import sleep
import rclpy
from std_msgs.msg import String

rclpy.init()
node = rclpy.create_node('enemyFinder')
pub = node.create_publisher(String, 'enemyLocation',10)
msg = String()
i=0
while rclpy.ok():
   msg.data = f'Hello World:{i}'
   i+=1
   print(f'Publishing:"{msg.data}"')
   pub.publish(msg)
   sleep(0.5)
