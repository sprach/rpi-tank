#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time, sys, signal

# GPIO 신호 On/Off
GPIO_ON = GPIO.HIGH
GPIO_OFF = GPIO.LOW

# GPIO 핀 번호
PIN_ULTRASONIC_TRIG = 19
PIN_ULTRASONIC_ECHO = 26

# 거리 Timeout
MAX_DISTANCE_CM = 300
MAX_DURATION_TIMEOUT = MAX_DISTANCE_CM * 2 * 29.1   # 17,460us = 300cm

# <CTR>+<C>
def signal_handler(signal, frame):
    print("Quit the app.")
    GPIO.cleanup()
    sys.exit(0)

# cm 환산
def distance_in_cm(duration):
    # 물체에 소리가 도착한 후에 되돌아오는 시간 계산
    # 1. 인식하기까지의 시간 계산
    #    - tm1 = 0.01 / 340 = 0.000029412초 (29.412us)
    # 2. 되돌아 오는 시간 = tm1 x 왕복
    #    - tm2 = tm1 x 2 = 0.000058824초 (58.824us)
    # 3. duration은 왕복 시간
    #    그러므로 인식까지의 시간을 2로 나눔
    return duration / 2 / 29.412    # 29.1 로 나누는 경우가 있는데???

# 거리 표시
def print_distance(distance):
    msg = 'Distance: '
    if distance == 0:
        msg += 'out of range'
    else:
        msg += str(distance) + 'cm'
    
    print(msg)

# main

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_ULTRASONIC_TRIG, GPIO.OUT)
GPIO.setup(PIN_ULTRASONIC_ECHO, GPIO.IN)

print('Press <CTR>+<C> key to exit')

# 키보드 인터럽트
signal.signal(signal.SIGINT, signal_handler)

# 초음파 센서 동작전 잠시 대기
GPIO.output(PIN_ULTRASONIC_TRIG, GPIO_OFF)
time.sleep(1)

# Start
while True:
    is_ok = True
    GPIO.output(PIN_ULTRASONIC_TRIG, GPIO_OFF)
    time.sleep(0.1)

    # 트리거를 10us동안 High후 Low
    GPIO.output(PIN_ULTRASONIC_TRIG, GPIO_ON)
    time.sleep(0.00001)
    GPIO.output(PIN_ULTRASONIC_TRIG, GPIO_OFF)

    # ECHO로 값이 들어올 때까지 기다림
    timeout = time.time()
    start_tm = time.time()

    while GPIO.input(PIN_ULTRASONIC_ECHO) == 0:
        start_tm = time.time()
        # 확인 필요함!
        if ((start_tm - timeout) * 1000000) >= MAX_DURATION_TIMEOUT:
            is_ok = False
            break

    if not is_ok:
        continue
    
    # ECHO가 종료될 때까지 대기
    timeout = time.time()
    end_tm = start_tm

    while GPIO.input(PIN_ULTRASONIC_ECHO) == 1:
        end_tm = time.time()
        # 확인 필요함!
        if ((end_tm - timeout) * 1000000) >= MAX_DURATION_TIMEOUT:
            print_distance(0)   # error
            is_ok = False
            break

    if not is_ok:
        continue

    # 신호 소요 시간
    signal_duration = (end_tm - start_tm) * 1000000

    # 소요 시간을 cm로 환산
    distance = distance_in_cm(signal_duration)

    #
    print_distance(round(distance, 2))
