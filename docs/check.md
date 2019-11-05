# 점검
  1. WebCam과 UltraSonic(hc-sr04) 사이의 간격이 좁음
  2. UltraSonic의 Vcc는 5V에 연결해야 함
     * 1차 버전은 3.3V에 연결되어 있어서 동작이 되지 않음
     * 아래 링크를 보면 ECHO에 330오옴(또는 1k오옴)을, GND쪽에는 470오옴(또는 2k오옴)의 저항을 연결해 놓았음
       ** https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
       ** https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
