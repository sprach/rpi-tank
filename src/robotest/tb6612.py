# Import required modules
import time
import RPi.GPIO as GPIO

# PIN_STBY = ??
# Motor A
PIN_PWMA = 12
PIN_AIN1 = 20
PIN_AIN2 = 16
# Motor B
PIN_PWMB = 13
PIN_BIN1 = 5
PIN_BIN2 = 6

# Declare the GPIO settings
GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
#GPIO.setup(PIN_STBY, GPIO.OUT) # Connected to STBY
# Motor A
GPIO.setup(PIN_PWMA, GPIO.OUT) # Connected to PWMA
GPIO.setup(PIN_AIN1, GPIO.OUT) # Connected to AIN2
GPIO.setup(PIN_AIN2, GPIO.OUT) # Connected to AIN1
# Motor B
GPIO.setup(PIN_PWMB, GPIO.OUT) # Connected to PWMB
GPIO.setup(PIN_BIN1, GPIO.OUT) # Connected to BIN1
GPIO.setup(PIN_BIN2, GPIO.OUT) # Connected to BIN2

#
print('Ready...')
GPIO.output(PIN_PWMA, GPIO.LOW) # Set PWMA
GPIO.output(PIN_AIN1, GPIO.LOW) # Set AIN1
GPIO.output(PIN_AIN2, GPIO.LOW) # Set AIN2
GPIO.output(PIN_PWMB, GPIO.LOW) # Set PWMB
GPIO.output(PIN_BIN1, GPIO.LOW) # Set BIN1
GPIO.output(PIN_BIN2, GPIO.LOW) # Set BIN2

time.sleep(1)   # 1초 대기

# Drive the motor clockwise
print('Start 1')

# Motor A:
GPIO.output(PIN_AIN1, GPIO.HIGH) # Set AIN1
GPIO.output(PIN_AIN2, GPIO.LOW) # Set AIN2
# Motor B:
GPIO.output(PIN_BIN1, GPIO.HIGH) # Set BIN1
GPIO.output(PIN_BIN2, GPIO.LOW) # Set BIN2

# Set the motor speed
# Motor A:
GPIO.output(PIN_PWMA, GPIO.HIGH) # Set PWMA
# Motor B:
GPIO.output(PIN_PWMB, GPIO.HIGH) # Set PWMB

# Disable STBY (standby)
# GPIO.output(PIN_STBY, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

# Drive the motor counterclockwise
print('Start 2')

# Motor A:
GPIO.output(PIN_AIN1, GPIO.LOW) # Set AIN1
GPIO.output(PIN_AIN2, GPIO.HIGH) # Set AIN2
# Motor B:
GPIO.output(PIN_BIN1, GPIO.LOW) # Set BIN1
GPIO.output(PIN_BIN2, GPIO.HIGH) # Set BIN2

# Set the motor speed
# Motor A:
GPIO.output(PIN_PWMA, GPIO.HIGH) # Set PWMA
# Motor B:
GPIO.output(PIN_PWMB, GPIO.HIGH) # Set PWMB

# Disable STBY (standby)
#GPIO.output(PIN_STBY, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

# Reset all the GPIO pins by setting them to LOW
print('Finish')

GPIO.output(PIN_AIN1, GPIO.LOW) # Set AIN1
GPIO.output(PIN_AIN2, GPIO.LOW) # Set AIN2
GPIO.output(PIN_PWMA, GPIO.LOW) # Set PWMA
# GPIO.output(PIN_STBY, GPIO.LOW) # Set STBY
GPIO.output(PIN_BIN1, GPIO.LOW) # Set BIN1
GPIO.output(PIN_BIN2, GPIO.LOW) # Set BIN2
GPIO.output(PIN_PWMB, GPIO.LOW) # Set PWMB
#
GPIO.cleanup()
