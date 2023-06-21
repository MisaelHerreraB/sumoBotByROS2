from time import sleep
import rclpy
from std_msgs.msg import String
from pymata4 import pymata4

board = pymata4.Pymata4()
board.set_sampling_interval(100)
board.set_pin_mode_analog_input(0, callback=None, differential=1)
board.set_pin_mode_analog_input(1, callback=None, differential=1)
board.set_pin_mode_analog_input(2, callback=None, differential=1)
board.set_pin_mode_analog_input(3, callback=None, differential=1)
board.set_pin_mode_analog_input(4, callback=None, differential=1)
board.set_pin_mode_analog_input(5, callback=None, differential=1)

rclpy.init()
node = rclpy.create_node('enemyFinder')
pub = node.create_publisher(String, 'enemyLocation',10)
msg = String()

while rclpy.ok():
   value1=0
   value2=0
   value3=0
   value4=0
   value5=0
   value6=0
   v1 = board.analog_read(0)
   v2 = board.analog_read(1)
   v3 = board.analog_read(2)
   v4 = board.analog_read(3)
   v5 = board.analog_read(4)
   v6 = board.analog_read(5)
   value1= lambda v1: 1 if v1 >= 300 else 0
   value2= lambda v2: 1 if v2 >= 300 else 0
   value3= lambda v3: 1 if v3 >= 300 else 0
   value4= lambda v4: 1 if v4 >= 300 else 0
   value5= lambda v5: 1 if v5 >= 500 else 0
   value6= lambda v6: 1 if v6 >= 500 else 0   
   msg.data = f'{value1}{value2}{value3}{value4}{value5}{value6}'
   print(f'Publishing:"{msg.data}"')
   pub.publish(msg)

