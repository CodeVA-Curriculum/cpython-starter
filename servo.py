# move the servo
from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

while True:
    kit.servo[0].angle = 180
    time.sleep(0.5)
    kit.servo[0].angle = 0
    time.sleep(0.5)