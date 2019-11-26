# Raspbian Update and Upgrade
  * Upgrade시 소요시간이 제법 길기 때문에 교육시에는 실행하지 말 것
    <pre><code>$ sudo apt-get update
    $ sudo apt-get upgrade</code></pre>

# 라즈베리파이 원격접속 설정
  > Windows 원격데스크톱용
  1. 기존 VNC Server 제거
     <pre><code>$ sudo apt-get purge realvnc-vnc-server</code></pre>
  2. 새 VNC Server 설치
     <pre><code>$ sudo apt-get install tightvncserver</code></pre>
  3. XRDP 설치
     <pre><code>$ sudo apt-get install xrdp</code></pre>
  4. Windows 원격데스크톱으로 라즈베리파이에 연결

# 라즈베리파이 한글 폰트 설치
  1. 라즈베리파이에서 한글 보기용 폰트 설치
     <pre><code>sudo apt-get install fonts-unfonts-core fonts-nanum fonts-nanum-extra</code></pre>

# 개발 및 종속 파일 설치
  ## 개발 종속 파일 설치
  1. 개발 관련 파일
     <pre><code>$ sudo apt-get install -y cmake git</code></pre>
	 
  1. Python files
     <pre><code>$ sudo apt-get install -y python3-dev python3-pillow python3-virtualenv python3-numpy python3-picamera python3-pandas python3-rpi.gpio</code></pre>
  
  2. Dependency files
     <pre><code>$ sudo apt-get install -y build-essential i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-dev</code></pre>
   
  3. OpenCV files
     <pre><code>$ sudo apt-get install -y libilmbase-dev libopenexr-dev libgstreamer1.0-dev libjasper-dev libwebp-dev libatlas-base-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test</code></pre>

  ## VirtualEnv
  * Requires Pytho &gt; 3.4 and pip &gt;= 19.0
  1. Check VirtualEnv
     <pre><code>$ python3 --version
     $ pip3 --version
     $ virtualenv --version</code></pre>
  2. Install Python, the pip package manager, and VirtualEnv
     <pre><code>$ sudo apt update
     $ sudo apt install python3-dev python3-pip
     $ sudo apt install libatlas-base-dev          # required for numpy
     $ sudo pip3 install -U virtualenv             # system-wide install</code></pre>
  3. Create a virtual environment
     1. Create a new virtual environment
        <pre><code>$ virtualenv --system-site-packages -p python3 ./venv
        $ ls
        <b><i><u>Desktop    Download   ...   venv</u></i></b></code></pre>
     2. Activate the virtual environment
        <pre><code>$ source ./venv/bin/activate
        (venv) $</code></pre>
     3. Install packages within a virtual environment (Start by upgradeing pip.)
        <pre><code>(venv) $ pip3 install --upgrade pip
        (venv) $ pip3 list  # show packages installed within the virtual environment</code></pre>
     * To exit virtualenv later
       <pre><code>(venv) $ deactivate  # don't exit until you're done using TensorFlow</code></pre>

  ## TensorFlow
  > Tensorflow 설치는 VirtualEnv를 기본으로 하되, 실습에서는 시스템 설치와 가상 설치는 별도로 구분하지 않는다.
  1. Install tensorflow
     * Virtualenv install
       > <i>pip</i>를 이용할 경우 Version 2.7로 동작하여 <i>TensorFlow</i> 설치가 제대로 되지 않으므로 <i>pip3</i>로 설치해야 한다.
       <pre><code>(venv) $ sudo pip3 install --upgrade tensorflow</code></pre>
     * System install
       <pre><code>$ pip3 install --user --upgrade tensorflow   # install in $HOME</code></pre>
     > 아래와 같이 오류가 발생하는 경우 다운로드 속도의 문제일 가능성이 높으므로 다시 설치를 시도해 본다.
       <pre><code><i>THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE. If you have updated the package versions, please update the hashes. Otherwise, examine the package contents carefully; someone may have tampered with them.
          tensorflow from https://www.piwheels.org/simple/tensorflow/tensorflow-1.14.0-cp27-none-linux_armv7l.whl#sha256=dad8cc7ab0497f0c91be00d07ab64d203f166d9a436b2c9a874fe033f2ec4cd6:
                  Expected sha256 dad8cc7ab0497f0c91be00d07ab64d203f166d9a436b2c9a874fe033f2ec4cd6
                      Got        03e8ffcde09dbf7e23f57d3bd68923d8300c8188897dd02ab52ab3ebe755e417</i></code></pre>
  2. Upgrade numpy (Ver. 1.16.2 to 1.17.4)
     <pre><code>(venv) $ pip3 install --upgrade numpy</code></pre>
     > 아래와 같이 <i>numpy</i> 삭제를 할 수 없다고 나오는 것은 VirtualEnv에서 설치해서 나오는 현상으로 무시해도 된다.
       <pre><code>Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
       Collecting numpy
         Downloading https://www.piwheels.org/simple/numpy/numpy-1.17.4-cp37-cp37m-linux_armv7l.whl (10.2MB)
           |████████████████████████████████| 10.2MB 90kB/s 
       Installing collected packages: numpy
         Found existing installation: numpy 1.16.2
           <b><i>Not uninstalling numpy at /usr/lib/python3/dist-packages, outside environment /home/pi/venv
           Can't uninstall 'numpy'. No files were found to uninstall.</i></b>
       Successfully installed numpy-1.17.4</code></pre>
       
  3. Test
     * Test #1
       <pre><code>$ python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
       <b><i><u>Tensor("Sum:0", shape=(), dtype=float32)</u></i></b></code></pre>
     * Test 2
       <pre><code>$ python3
       <b><i><u>Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
       [GCC 8.2.0] on linux
       Type "help", "copyright", "credits" or "license" for more information.
       >>> </u></i></b>import tensorflow as tf
       <b><i><u>WARNING:tensorflow:From /usr/local/lib/python3.7/dist-packages/tensorflow/__init__.py:98: The name tf.AUTO_REUSE is deprecated. Please use tf.compat.v1.AUTO_REUSE instead.
       WARNING:tensorflow:From /usr/local/lib/python3.7/dist-packages/tensorflow/__init__.py:98: The name tf.AttrValue is deprecated. Please use tf.compat.v1.AttrValue instead.
       WARNING:tensorflow:From /usr/local/lib/python3.7/dist-packages/tensorflow/__init__.py:98: The name tf.COMPILER_VERSION is deprecated. Please use tf.version.COMPILER_VERSION instead.
       WARNING:tensorflow:From /usr/local/lib/python3.7/dist-packages/tensorflow/__init__.py:98: The name tf.CXX11_ABI_FLAG is deprecated. Please use tf.sysconfig.CXX11_ABI_FLAG instead.
       WARNING:tensorflow:From /usr/local/lib/python3.7/dist-packages/tensorflow/__init__.py:98: The name tf.ConditionalAccumulator is deprecated. Please use tf.compat.v1.ConditionalAccumulator instead.
       >>> </u></i></b>a = tf.constant([1.0, 2.0], name="a")
       <b><i><u>>>> </u></i></b>b = tf.constant([5.0, 6.0], name="b")
       <b><i><u>>>> </u></i></b>result = a + b
       <b><i><u>>>> </u></i></b>result
       <b><i><u>&lt;tf.Tensor 'add:0' shape=(2,) dtype=float32&gt;
       >>> </u></i></b>sess = tf.Session()
       <b><i><u>>>> </u></i></b>sess.run(result)
       <b><i><u>array([6., 8.], dtype=float32)
       >>> </u></i></b>exit()
       $</code></pre>
  * Unistall tensorflow
    <pre><code>$ sudo pip3 uninstall -y protobuf
    $ sudo pip3 uninstall -y tensorflow</code></pre>

  ## GPIO 라이브러리 설치
  <pre><code>$ sudo apt-get install rpi.gpio rpi.gpio-common</code></pre>
  
  ## gpiozero
  * gpiozero는 GPIO를 함수화시킨 라이브러리
  1. Raspbian
     <pre><code>$ sudo apt install python3-gpiozero</code></pre>
  2. Non-raspbian
     <pre><code>$ sudo pip3 install gpiozero</code></pre>

  ## BlueDot
  * 안드로이드폰에서 라즈베리파이를 조정하는 패드 역할
    * [BlotDot Site](https://bluedot.readthedocs.io/) : https://bluedot.readthedocs.io/
  1. 라즈베리파이에 파이썬 라이브러리 BlueDot 설치
     <pre><code>$ sudo pip3 install bluedot</code></pre>
  2. 안드로이드 Play 스토어에서 BlueDot 앱 설치
     * [Martin O'Hanlon](https://play.google.com/store/apps/details?id=com.stuffaboutcode.bluedot&hl=ko) : https://play.google.com/store/apps/details?id=com.stuffaboutcode.bluedot&hl=ko

# Logitech C270
  1. guvcview webcam viewer 설치
     <pre><code>$ sudo apt-get install guvcview</code></pre>
  2. 퍼미션 설정 및 드라이버 활성화
     <pre><code>$ sudo usermod -a -G video pi
     $ sudo modprobe uvcvideo</code></pre>
  3. Reboot
     <pre><code>$ sudo reboot</code></pre>
  4. WebCam 작동전 고려 사항
     1. WebCam을 파워온시 연결해 놓은 경우
        - 별도의 작업 필요하지 않음
     2. 라즈베리파이 전원을 On 시킨 이후에 WebCam을 연결한 경우에는 아래 스크립트를 먼저 실행해 주어야 한다.
        <pre><code>$ sudo rmmod uvcvideo
        $ sudo modprobe uvcvideo</code></pre>
  5. WebCam 실행
     * 라즈베리파이 아이콘 &gt; Sound &amp; Video &gt; guvcview

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
    
     3. Ellipsoid Fit Calibration
        <pre><code>$ sudo apt-get install octave
        ...
        계속 하시겠습니까? [Y/n] &lt;Enter&gt;
        ...
        $ </code></pre>
    
     4. RTIMULib library
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

# 적외선 거리측정 (PDS)
  1. Sharp 2Y0A21
     * 참조 사이트
       * [Infrared Distance Measurement with the Raspberry Pi (Sharp GP2Y0A02YK0F)](https://tutorials-raspberrypi.com/infrared-distance-measurement-with-the-raspberry-pi-sharp-gp2y0a02yk0f/)
       * [블로그: 적외선 거리측정센서 (sharp 2Y0A21)사용 예제](https://m.blog.naver.com/PostView.nhn?blogId=boilmint7&logNo=220927816896&proxyReferer=https%3A%2F%2Fwww.google.com%2F)
	   * [PDF: Datasheet GP2Y0A02YK0F](https://global.sharp/products/device/lineup/data/pdf/datasheet/gp2y0a21yk_e.pdf)
  2. 사전 작업
     1. SPI 활성화
        <pre><code>$ sudo raspi-config
        <b><i><u>Menu &gt; 5 Interfacing Options &gt; P4 SPI &gt; Yes &gt; Ok &gt; Finish</u></i></b></code></pre>
     2. /etc/modules 의 마지막 라인에 'spi-bcm2807' 추가
        <pre><code>$ sudo vi /etc/modules
        <b><i><u>spi-bcm2807</u></i></b></code></pre>
     3. spidev 라이브러리 설치
        <pre><code>$ git clone git://github.com/doceme/py-spidev
        $ cd py-spidev
        $ sudo python3 setup.py install</code></pre>

