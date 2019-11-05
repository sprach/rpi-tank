# Logitech C270
  1. guvcview webcam viewer 설치
     <pre><code>$ sudo apt-get install guvcview</code></pre>
  2. 퍼미션 설정 및 드라이버 활성화
     <pre><code>$ sudo usermod -a -G video pi
	 $ sudo modprobe uvcvideo</code></pre>
  3. Reboot
     <pre><code>$ sudo reboot</code></pre>
  4. Web 작동시 고려 사항
     1. WebCam을 파워온시 연결해 놓은 경우
	    - 별도의 작업 필요하지 않음
     2. 라즈베리파이 전원을 On 시킨 이후에 WebCam을 연결한 경우에는 아래 스크립트를 먼저 실행해 주어야 한다.
	    <pre><code>$ sudo rmmod uvcvideo
		sudo modprobe uvcvideo</code></pre>
