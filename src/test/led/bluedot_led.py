from bluedot import BlueDot
from gpiozero import LEDBoard

# Red, Green, Blue
LEDS = LEDBoard(24, 25, 4)

# https://bluedot.readthedocs.io/en/latest/index.html
bd = BlueDot()

while True:
    bd.wait_for_press()
    LEDS.on()
    bd.wait_for_release()
    LEDS.off()
