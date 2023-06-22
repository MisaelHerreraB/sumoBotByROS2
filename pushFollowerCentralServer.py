from time import sleep
import rclpy
from std_msgs.msg import String

def cb(msg):
   aux = msg.data
   val = f'izF'   
   if aux[0]=="0" and aux[1]=="1" and aux[2]=="1" and aux[3]=="0":
      val = f'adelante'
   elif aux[0]=="0" and aux[1]=="0" and aux[2]=="0" and aux[3]=="0":
      val = f'izF'
   elif aux[0]=="0" and aux[1]=="0" and aux[2]=="0" and aux[3]=="1":
      val = f'deF'
   elif aux[0]=="1" and aux[1]=="0" and aux[2]=="0" and aux[3]=="0":
      val = f'izF'
   elif aux[0]=="0" and aux[1]=="0" and aux[2]=="1" and aux[3]=="0":
      val = f'deS'
   elif aux[0]=="0" and aux[1]=="1" and aux[2]=="0" and aux[3]=="0":
      val = f'izS'
   else:
      val = f'stop'
   
   if aux[6]=="1" or aux[5]=="1":
      val = f'back'
   msg.data = val
   print(f'Publishing:"{msg.data}"')
   pub.publish(msg)
   
rclpy.init()
node = rclpy.create_node('pushFollower')
pub = node.create_publisher(String, 'motion',10)
sub = node.create_subscription(String, 'sensors',cb,10)

rclpy.spin(node)
