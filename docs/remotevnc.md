# 라즈베리파이 원격접속 설정
  > Windows 원격데스크톱용
  1. 기존 VNC Server 제거
     <pre><code>$ sudo apt-get purge realvnc-vnc-server</code></pre>
  2. 새 VNC Server 설치
     <pre><code>$ sudo apt-get install tightvncserver</code></pre>
  3. XRDP 설치
     <pre><code>$ sudo apt-get install xrdp</code></pre>
  4. Windows 원격데스크톱으로 라즈베리파이에 연결
