from gpiozero import LED
from time import sleep

LED_R = LED(24)
LED_G = LED(25)
LED_B = LED(4)

def all_led_off():
    LED_R.off()
    LED_G.off()
    LED_B.off()
    
def led_red_on():
    LED_R.on()
    LED_G.off()
    LED_B.off()

def led_green_on():
    LED_R.off()
    LED_G.on()
    LED_B.off()

def led_blue_on():
    LED_R.off()
    LED_G.off()
    LED_B.on()

# main
all_led_off()

try:
    while True:
        led_red_on()
        sleep(1)
        led_green_on()
        sleep(1)
        led_blue_on()

except KeyboardInterrupt:
        all_led_off()
