# Raspbian Update and Upgrade
  * Upgrade시 소요시간이 제법 길기 때문에 교육시에는 실행하지 말 것
  <pre><code>$ sudo apt-get update
$ sudo apt-get upgrade</code></pre>

# 라즈베리파이 한글 폰트 설치
  1. 라즈베리파이에서 한글 보기용 폰트 설치
     <pre><code>sudo apt-get install fonts-unfonts-core fonts-nanum fonts-nanum-extra</code></pre>

# 개발 및 종속 파일 설치
  ## 개발용 Python 설치
  <pre><code>sudo apt-get install python3-dev python3-pillow -y</code></pre>
   
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
