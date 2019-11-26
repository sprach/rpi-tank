# Raspbian Update and Upgrade
  * Upgrade시 소요시간이 제법 길기 때문에 교육시에는 실행하지 말 것
    <pre><code>$ sudo apt-get update
    $ sudo apt-get upgrade</code></pre>

# 라즈베리파이 한글 폰트 설치
  1. 라즈베리파이에서 한글 보기용 폰트 설치
     <pre><code>sudo apt-get install fonts-unfonts-core fonts-nanum fonts-nanum-extra</code></pre>

# 개발 및 종속 파일 설치
  ## 개발 종속 파일 설치
  1. Python files
     <pre><code>$ sudo apt-get install -y python3-dev python3-pillow python3-virtualenv python3-numpy python3-picamera python3-pandas python3-rpi.gpio</code></pre>
  
  2. Dependency files
     <pre><code>$ sudo apt-get install -y git build-essential i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-dev</code></pre>
   
  3. OpenCV files
     <pre><code>$ sudo apt-get install -y libilmbase-dev libopenexr-dev libgstreamer1.0-dev libjasper-dev libwebp-dev libatlas-base-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test</code></pre>
   
  4. Setup Virtual Env
     <pre><code>$ python3 -m virtualenv -p python3 env --system-site-packages</code></pre>

     * .bashrc 파일의 맨 끝에 'source env/bin/activate'가 없을 때 아래와 같이 적용
       <pre><code>$ echo "source ./env/bin/activate" &gt;&gt ~/.bashrc
       $ source ~/.bashrc</code></pre>

  ## GPIO 라이브러리 설치
  <pre><code>sudo apt-get install rpi.gpio rpi.gpio-common</code></pre>
  
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
