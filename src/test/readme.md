# 작동하는 것
  1. gyro
     * 정상인지 아닌지 애매하므로 더 테스트가 필요함
     * RTIMULib는 제대로 동작하지 않음
  2. keyboard: OK
  3. Led: Ok
  4. Motor: Ok
  5. sound
     1. Piezo: Ok
     2. Buzzer: Ok
     
# 작동 안하는 것
  > Analog 관련은 대부분 안됨
    > MCP3008의 Pin 11(DIn), Pin 12(DOut)이 라즈베리파이의 GPIO와 거꾸로 연결되었음
    > 이것도 아닌 듯!!!
  1. psd(GP 2Y0A21) 적외선
  2. JoyStick
  3. UltraSonic
  4. 온습도
     * Data가 제대로 안 올라옴
