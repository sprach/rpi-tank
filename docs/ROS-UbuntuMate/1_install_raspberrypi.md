# Ubuntu MATE
  1. Download Steps
     1. [Raspberry Pi Download page](https://www.raspberrypi.org/downloads/) : https://www.raspberrypi.org/downloads/
     2. Third Party Operating System Images > Ubuntu MATE
     3. Supported Raspberry Pi > Download Ubuntu MATE for the Pi
     4. Choose your architecture > Raspberry Pi (experimental)
     5. Download - Which release would you like? for a Raspberry Pi ARMv8 64-bit system > 18.04.2 (Bionic)
        * 최신 버전 선택
     6. Download Links > ubuntu-mate-18.04.2-beta1-desktop-arm64+raspi3-ext4.img.xz
  2. Flashing

# Ubunte MATE 첫 설치
  1. MicroSD를 라즈페비파이 슬롯에 삽입
     * Ubuntu MATE는 첫 부팅 과정을 거치면서 환경 설정이 이루어지므로 Raspbian 같이 선(先) 작업을 진행할 수 없음
  2. 키보드, 마우스, 모니터를 반드시 연결시키고 전원 연결함
     * UART, WiFi 작업은 O/S 설치후 가능함
  3. 설치
      1. 사용할 언어: English
      2. 키보드: Korean - 103/104 Keyboards
      3. 시간대: Seoul
      4. 사용자 및 암호: pi / raspberry
         * 개발시 편의를 위한 정의이며 실 배포시에는 다르게 진행해야 함
      5. 설치 진행
  4. 자동 재부팅

# Ubunte MATE 설치후 환경 설정
  1. Raspberry Pi config
     <pre><code>$ sudo raspi-config
     [sudo] password for pi: <i>&lt;password&gt;</i></code></pre>
  2. 인터페이스 옵션 설정에서 지정된 옵션 모두 Enable 처리
     * 메뉴 이동은 커서 키 또는 &lt;Tab&gt; 키 사용함
     <pre><code>3 Interfacing Options
     P1 Camera - Enabled &gt; <i>Yes</i>
     P2 SSH - Enabled &gt; <i>Yes</i>
     P3 SPI - Enabled &gt; <i>Yes</i>
     P4 I2C - Enabled &gt; <i>Yes</i>
     p5 Serial - Enabled &gt; <i>Yes</i></code></pre>
  3. 파일시스템 확장
     <pre><code>5 Advanced Options
     A1 Expand Filesystem</code></pre>
  4. 종료 및 재부팅
     <pre><code>&lt;<i>Finish</i>&gt;
     Would you like to reboot now?
     &lt;<i>Yes</i>&gt;</code></pre>

# Update &amp; Upgrade
  <pre><code>$ sudo apt-get update
  [sudo] password for pi: <i>&lt;password&gt;
  $ sudo apt-get -y upgrade
    [sudo] password for pi: <i>&lt;password&gt;</code></pre>

# WiFi 설정
  1. GUI인 경우
     1. 우상단의 '↑↓' 아이콘 선택
     2. 연결할 AP 선택 및 SSID, PWD 입력 연결
        * 원하는 AP가 표시되지 않으면 'Enable Wi-Fi'를 선택하여 Uncheck한 뒤에 다시 Check함
  2. CUI인 경우
     <pre><code>$ sudo nmcli d wifi connect &lt;<i>SSID</i>&gt; password &lt;<i>Password</i>&gt;</code></pre>
  * WiFi 리스트 보기
    <pre><code>$ nmcli d wifi list</code></pre>
    > 빠져 나오기는 'q' 키를 누르면 됨

# Raspberry Pi의 IP 주소
  <pre><code> $ ifconfig
  [sudo] password for pi: <i>&lt;password&gt;</code></pre>

  <pre><code>eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether b8:27:eb:0a:0d:86  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

  lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

  <b><i><u>wlan0</u></i></b>: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet <b><i><u>192.168.100.80</u></i></b>  netmask 255.255.255.0  broadcast 192.168.100.255
        inet6 fe80::a1c:e5d6:efac:b041  prefixlen 64  scopeid 0x20<link>
        ether b8:27:eb:5f:58:d3  txqueuelen 1000  (Ethernet)
        RX packets 15  bytes 1648 (1.6 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 37  bytes 5409 (5.2 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0</code></pre>

# Raspbian Update and Upgrade
  * Upgrade시 소요시간이 제법 길기 때문에 교육시에는 실행하지 말 것
    <pre><code>$ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo rpi-update -y</code></pre>

# GUI에서 터미널 사용
  1. 'Menu' &gt; 'System Tools' &gt; 'MATE Terminal'

# CUI/GUI 부팅 전환
  1. GUI → CUI
     <pre><code>$ sudo graphical disable
     $ sudo shutdown -r now</code></pre>
  2. CUI → GUI
     <pre><code>$ sudo graphical ebable
     $ sudo shutdown -r now</code></pre>

# 라즈베리파이 한글 폰트 설치
  1. 라즈베리파이에서 한글 보기용 폰트 설치
     <pre><code>$ sudo apt-get install fonts-unfonts-core fonts-nanum fonts-nanum-extra</code></pre>

# 라즈베리파이 원격접속 설정
  > Windows 원격데스크톱용
  1. 기존 VNC Server 제거
     <pre><code>$ sudo apt-get purge -y realvnc-vnc-server</code></pre>
  2. 새 VNC Server 설치
     <pre><code>$ sudo apt-get install -y tightvncserver</code></pre>
  3. XRDP 설치
     <pre><code>$ sudo apt-get install -y xrdp</code></pre>
  4. Windows 원격데스크톱으로 라즈베리파이에 연결
