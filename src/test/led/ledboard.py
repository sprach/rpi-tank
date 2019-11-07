from gpiozero import LEDBoard
from time import sleep

# Red, Green, Blue
LEDS = LEDBoard(24, 25, 4)

def all_led_off():
    for led in LEDS:
        led.off()

def led_on(pos):
    for i in range(0, len(LEDS)):
        if pos == i: LEDS[i].on()
        else: LEDS[i].off()

def led_red_on():
    led_on(0)

def led_green_on():
    led_on(1)

def led_blue_on():
    led_on(2)

# main
all_led_off()

try:
    while True:
        led_red_on()
        sleep(1)
        led_green_on()
        sleep(1)
        led_blue_on()
        sleep(1)

except KeyboardInterrupt:
        all_led_off()
