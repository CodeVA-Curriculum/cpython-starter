# move the motors
from adafruit_motorkit import MotorKit
import time

kit = MotorKit()

while True:
    kit.motor1.throttle = 1.0
    time.sleep(0.5)
    kit.motor1.throttle = 0.5
    time.sleep(0.5)
    kit.motor1.throttle = 0
    time.sleep(0.5)
    kit.motor1.throttle = -0.5
    kit.motor1.throttle = -1