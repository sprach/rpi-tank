# MicroSD 사전 설정
  > HDMI와 같이 디스플레이를 연결할 수 없을 때의 작업
  1. ssh 사용을 위한 빈 'ssh' 파일 복사 또는 만들어 넣기
  2. WiFi 접속을 위한 'wpa_supplicant.conf' 파일 복사해 넣기
     <pre><code>country=GB
     ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
     update_config=1

     network={
       ssid="&lt;ssid-name&gt;"
       psk="&lt;password&gt;"
     }</code></pre>
  3. USB Serial 접속을 위한 Serial 활성화 Key 삽입
     <pre><code>...
     enable_uart=1</code></pre>

# Raspbian Update and Upgrade
  * Upgrade시 소요시간이 제법 길기 때문에 교육시에는 실행하지 말 것
    <pre><code>$ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo rpi-update -y</code></pre>

# 라즈베리파이 한글 폰트 설치
  1. 라즈베리파이에서 한글 보기용 폰트 설치
     <pre><code>sudo apt-get install fonts-unfonts-core fonts-nanum fonts-nanum-extra</code></pre>

# 라즈베리파이 원격접속 설정
  > Windows 원격데스크톱용
  1. 기존 VNC Server 제거
     <pre><code>$ sudo apt-get purge realvnc-vnc-server</code></pre>
  2. 새 VNC Server 설치
     <pre><code>$ sudo apt-get install tightvncserver</code></pre>
  3. XRDP 설치
     <pre><code>$ sudo apt-get install xrdp</code></pre>
  4. Windows 원격데스크톱으로 라즈베리파이에 연결
