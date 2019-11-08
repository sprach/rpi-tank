# 적외선 거리측정 (PDS)
  1. Sharp 2Y0A21
     * 참조 사이트
       * https://tutorials-raspberrypi.com/infrared-distance-measurement-with-the-raspberry-pi-sharp-gp2y0a02yk0f/
       * https://m.blog.naver.com/PostView.nhn?blogId=boilmint7&logNo=220927816896&proxyReferer=https%3A%2F%2Fwww.google.com%2F
  2. 사전 작업
     1. SPI 활성화
        <pre><code>$ sudo raspi-config
        Menu &gt; 5 Interfacing Options &gt; P4 SPI &gt; Yes &gt; Ok &gt; Finish</code></pre>
     2. /etc/modules 의 마지막 라인에 'spi-bcm2807' 추가
        <pre><code>$ sudo vi /etc/modules
        spi-bcm2807</code></pre>
     3. spidev 라이브러리 설치
        <pre><code>$ sudo apt-get install git python3-dev
        $ git clone git://github.com/doceme/py-spidev
        $ cd py-spidev
        $ sudo python3 setup.py install</code></pre>
