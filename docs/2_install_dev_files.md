# 개발 도구
  ## 개발 관련 파일 설치
  1. 개발 관련 파일
     <pre><code>$ sudo apt-get install -y cmake git</code></pre>

  2. Python files
     <pre><code>$ sudo apt-get install -y python3-dev python3-pillow python3-virtualenv python3-numpy python3-picamera python3-pandas python3-rpi.gpio</code></pre>

  3. Dependency files
     <pre><code>$ sudo apt-get install -y build-essential i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-dev</code></pre>

  4. OpenCV files
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