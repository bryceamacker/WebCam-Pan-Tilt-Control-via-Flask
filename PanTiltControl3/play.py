import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH)

pan = GPIO.PWM(12, 50)
tilt = GPIO.PWM(16, 50)

pan.start(7.5)
tilt.start(7.5)
counter = 0
try:
    while counter < 10:
        GPIO.output(7, GPIO.LOW)
        pan.ChangeDutyCycle(7.5)  # turn towards 90 degree
        tilt.ChangeDutyCycle(7.5)  # turn towards 90 degree
        time.sleep(1) # sleep 1 second
        pan.ChangeDutyCycle(12.5) # turn towards 180 degree
        tilt.ChangeDutyCycle(12.5) # turn towards 180 degree
        time.sleep(1) # sleep 1 second
        counter += 1
except KeyboardInterrupt:
    pan.stop()
    tilt.stop()
    GPIO.output(7, GPIO.HIGH)
    GPIO.cleanup()

 0   45   90    135   180
2.5   5   7.5   10    12.5

