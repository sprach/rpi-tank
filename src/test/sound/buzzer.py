import RPi.GPIO as GPIO
from time import sleep

#
PIN_BUZZER = 27

# Disable GPIO warnings
GPIO.setwarnings(False)

# Select GPIO mode
GPIO.setmode(GPIO.BCM)

# Set buzzer
GPIO.setup(PIN_BUZZER, GPIO.OUT)

# Run
try:
    while True:
        GPIO.output(PIN_BUZZER, GPIO.HIGH)
        print("Beep")
        sleep(0.5)

        GPIO.output(PIN_BUZZER, GPIO.LOW)
        print("No beep")
        sleep(0.5)

except KeyboardInterrupt:
    GPIO.output(PIN_BUZZER, GPIO.LOW)
    GPIO.cleanup()
