# https://www.instructables.com/id/Raspberry-Pi-Tutorial-How-to-Use-a-Buzzer/
import RPi.GPIO as GPIO
from time import sleep

# GPIO22
PIN_PIEZO = 22

# Disable GPIO warnings
GPIO.setwarnings(False)

# Select GPIO mode
GPIO.setmode(GPIO.BCM)

# Set buzzer
GPIO.setup(PIN_PIEZO, GPIO.OUT)

# Run
try:
    while True:
        GPIO.output(PIN_PIEZO, GPIO.HIGH)
        print("Beep")
        sleep(0.5)

        GPIO.output(PIN_PIEZO, GPIO.LOW)
        print("No beep")
        sleep(0.5)

except KeyboardInterrupt:
    GPIO.output(PIN_PIEZO, GPIO.LOW)
    GPIO.cleanup()
