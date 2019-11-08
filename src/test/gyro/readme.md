# 자이로 및 가속도 센서
  * https://kingtidesailing.blogspot.com/2016/02/how-to-setup-mpu-9250-on-raspberry-pi_25.html

  1. i2c 활성화
     <pre><code>$ sudo raspi-config
     5 Interfacing Options &gt; P5 I2C &gt; Yes &gt; Ok &gt; Finish</code></pre>
     ^ 필요시 재부팅

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
        ^ <b><i><u>68</u></i></b>은 센서의 기본 주소이다.

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