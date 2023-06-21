from time import sleep
import rclpy
from std_msgs.msg import String
from pymata4 import pymata4

board = pymata4.Pymata4()
board.set_sampling_interval(200)
board.set_pin_mode_analog_input(0, callback=None, differential=1)
board.set_pin_mode_analog_input(1, callback=None, differential=1)
board.set_pin_mode_analog_input(2, callback=None, differential=1)
board.set_pin_mode_analog_input(3, callback=None, differential=1)
board.set_pin_mode_analog_input(4, callback=None, differential=1)
board.set_pin_mode_analog_input(5, callback=None, differential=1)

rclpy.init()
node = rclpy.create_node('sensorsDriver')
pub = node.create_publisher(String, 'sensors',10)
msg = String()

while rclpy.ok():
   value1=0
   value2=0
   value3=0
   value4=0
   value5=0
   value6=0
   v1 = board.analog_read(0)[0]
   v2 = board.analog_read(1)[0]
   v3 = board.analog_read(2)[0]
   v4 = board.analog_read(3)[0]
   v5 = board.analog_read(4)[0]
   v6 = board.analog_read(5)[0]
   if (v1 >= 300):
      value1=1
   else:
      value1=0
   if (v2 >= 300):
      value2=1
   else:
      value2=0
   if (v3 >= 500):
      value3=1
   else:
      value3=0
   if (v4 >= 500):
      value4=1
   else:
      value4=0
   if (v5 >= 300):
      value5=1
   else:
      value5=0
   if (v6 >= 300):
      value6=1
   else:
      value6=0 
   msg.data = f'{value6}{value2}{value1}{value5}-{value4}{value3}'
   print(f'Publishing:"{msg.data}"')
   pub.publish(msg)

