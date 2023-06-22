import rclpy
from std_msgs.msg import String
from RPi import GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

def adelante():
   GPIO.output(3, GPIO.HIGH)
   GPIO.output(5, GPIO.LOW)
   GPIO.output(7, GPIO.HIGH)
   GPIO.output(8, GPIO.LOW)

def back():
   GPIO.output(3, GPIO.LOW)
   GPIO.output(5, GPIO.HIGH)
   GPIO.output(7, GPIO.LOW)
   GPIO.output(8, GPIO.HIGH)

def izS():
   GPIO.output(3, GPIO.LOW)
   GPIO.output(5, GPIO.LOW)
   GPIO.output(7, GPIO.HIGH)
   GPIO.output(8, GPIO.LOW)

def izF():
   GPIO.output(3, GPIO.LOW)
   GPIO.output(5, GPIO.HIGH)
   GPIO.output(7, GPIO.HIGH)
   GPIO.output(8, GPIO.LOW)

def deF():
   GPIO.output(3, GPIO.HIGH)
   GPIO.output(5, GPIO.LOW)
   GPIO.output(7, GPIO.LOW)
   GPIO.output(8, GPIO.HIGH)

def deS():
   GPIO.output(3, GPIO.HIGH)
   GPIO.output(5, GPIO.LOW)
   GPIO.output(7, GPIO.LOW)
   GPIO.output(8, GPIO.LOW)

def stop():
   GPIO.output(3, GPIO.LOW)
   GPIO.output(5, GPIO.LOW)
   GPIO.output(7, GPIO.LOW)
   GPIO.output(8, GPIO.LOW)

def cb(msg):
   if msg.data=="adelante":
      adelante()
   elif msg.data=="back":
      back()
      time.sleep(1.2)
   elif msg.data=="izS":
      izS()
   elif msg.data=="izF":
      izF()
   elif msg.data=="deF":
      deF()
   elif msg.data=="deS":
      deS()
   elif msg.data=="stop":
      stop()
   print(f'I heard:"{msg.data}"')

rclpy.init()
node = rclpy.create_node('motorDriver')
sub = node.create_subscription(String, 'motion',cb,10)
rclpy.spin(node)


