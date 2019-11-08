# 자이로 및 가속도 센서
  * https://kingtidesailing.blogspot.com/2016/02/how-to-setup-mpu-9250-on-raspberry-pi_25.html

## 센서 설정

  1. i2c 활성화
     <pre><code>$ sudo raspi-config
     <b><i><u>5 Interfacing Options</u></i></b> &gt; <b><i><u>P5 I2C</u></i></b> &gt; <b><i><u>Yes</u></i></b> &gt; <b><i><u>Ok</u></i></b> &gt; <b><i><u>Finish</u></i></b></code></pre>
     > 필요시 재부팅

  2. 다운로드와 설치
     1. i2c
        <pre><code>$ sudo apt-get install i2c-tools
        $ sudo i2cdetect -y 1
        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
        00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
        10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- -- 
        70: -- -- -- -- -- -- -- --
        </code></pre>
        > <b><i><u>68</u></i></b>은 센서의 기본 주소이다.

     2. cmake
        <pre><code>$ sudo apt-get install cmake
        ...
        계속 하시겠습니까? [Y/n] &lt;Enter&gt;
        ...
        $ </code></pre>
    
     3. 개발용 python
        <pre><code>$ sudo apt-get install python-dev</code></pre>
    
     4. Ellipsoid Fit Calibration
        <pre><code>$ sudo apt-get install octave
        ...
        계속 하시겠습니까? [Y/n] &lt;Enter&gt;
        ...
        $ </code></pre>
    
     5. RTIMULib library
        <pre><code>$ cd ~
        $ mkdir kts
        $ cd kts
        $ git clone https://github.com/richards-tech/RTIMULib2.git
        $ cd RTIMULib2/Linux/RTIMULibCal
        $ make -j4
        $ sudo make install
        $ cd ~
        $ ln -s ~/kts/RTIMULib2/RTEllipsoidFit ~/kts/RTEllipsoidFit
        $ cd ~/kts/RTEllipsoidFit
        $ </code></pre>
    
     6. 설정
        1. /etc/modules 에 아래 내용 추가 (없을 경우에 한함)
           <pre><code><b><i><u>i2c-dev
           i2c-bcm2708</u></i></b></code></pre>
     
        2. /etc/udev/rules.d/90-i2c.rules 에 아래 내용 추가
           <pre><code><b><i><u>KERNEL=="i2c-[0-7]",MODE="0666"</u></i></b></code></pre>

        3. /boot/config.txt 에 아래 내용 추가
           <pre><code><b><i><u>dtparam=i2c1_baudrate=400000</u></i></b></code></pre>
        
        4. 재부팅
           <pre><code>$ sudo reboot</code></pre>

  3. Calibrating the MPU-9250
     1. RTIMULibCal 실행
        <pre><code>$ cd ~/kts/RTEllipsoidFit
        $ RTIMULibCal</code></pre>
        1. 'm' 키를 누른후 값이 안정되면 's' 키를 누른다.
        2. 'e' 키를 눌러서 타원체를 교정한다. 많은 숫자가 몇 분에 걸쳐서 표시되다가 자동으로 중단된다.
        3. 'a' 키를 눌러서 가속도계를 교정한다.
           1. (*중요*)... 내용 확인 필요함!!!
           2. x 축 센서 가속도계 보정, 'e'를 눌러 활성화, 'd'를 눌러 비활성화
           3. 'x'를 눌러서 종료

      2. 'RTIMULib.ini' 파일을 작업 디렉토리에 복사해야 한다.

## 테스트
