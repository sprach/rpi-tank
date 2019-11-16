# 적외선 거리측정 (PDS)
  1. Sharp 2Y0A21
     * 참조 사이트
       * [Infrared Distance Measurement with the Raspberry Pi (Sharp GP2Y0A02YK0F)](https://tutorials-raspberrypi.com/infrared-distance-measurement-with-the-raspberry-pi-sharp-gp2y0a02yk0f/)
       * [블로그: 적외선 거리측정센서 (sharp 2Y0A21)사용 예제](https://m.blog.naver.com/PostView.nhn?blogId=boilmint7&logNo=220927816896&proxyReferer=https%3A%2F%2Fwww.google.com%2F)
	   * [PDF: Datasheet GP2Y0A02YK0F](https://global.sharp/products/device/lineup/data/pdf/datasheet/gp2y0a21yk_e.pdf)
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
