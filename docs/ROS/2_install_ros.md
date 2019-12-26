# ROS Home
  > http://ros.org
  
# Install ROS Melodic on Raspberry Pi 3/4 with Raspbian
  1. Ref.
     1. [ROS](http://wiki.ros.org/melodic/Installation/Source) : http://wiki.ros.org/melodic/Installation/Source
     2. [Hackster.IO](https://www.hackster.io/dmitrywat/ros-melodic-on-raspberry-pi-4-debian-buster-rplidar-a1m8-0d63d1) : https://www.hackster.io/dmitrywat/ros-melodic-on-raspberry-pi-4-debian-buster-rplidar-a1m8-0d63d1
     3. [Kyubot Blog](https://kyubot.tistory.com/130) : https://kyubot.tistory.com/130
     4. [Install ROS Melodic on Raspberry Pi 3 with Ubuntu Mate](https://roboticsbackend.com/install-ros-on-raspberry-pi-3/) : https://roboticsbackend.com/install-ros-on-raspberry-pi-3/
  
  2. ROS Melodic 설치
     1. 종속성 설치와 패키지 다운로드
        * 레포지토리를 설정하고 필요한 종속성 설치 (candi #1)
          <pre><code>$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' 
          $ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
          $ sudo apt-get update
          $ sudo apt-get install -y python-empy python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential cmake
          $ sudo pip install --upgrade setuptools</code></pre>

        * sources.list 설정 (candi #2)
          <pre><code>$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'</code></pre>
        
        * Key 설정
          <pre><code>$ wget http://packages.ros.org/ros.key -O - | sudo apt-key add -</code></pre>

        * Update
          <pre><code>$ sudo apt-get update</code></pre>

        * Raspberry Pi 패키지 설치
          <pre><code>$ sudo apt-get install -y build-essential cmake dirmngr zlib1g-dev minizip</code></pre>

        * 파이썬 &amp; ROS 개발 패키지 설치
          <pre><code>$ sudo apt-get install -y python-empy python-rosdep python-rosinstall-generator python-wstool python-rosinstall
          $ sudo pip install --upgrade setuptools</code></pre>

        * rosdep를 초기화하고 업데이트
          <pre><code>$ sudo rosdep init  
          $ rosdep update</code></pre>

        * ROS 빌드를 위한 전용 catkin 작업 공간을 만들고 디렉토리 이동
          <pre><code>$ mkdir ~/ros_catkin_ws  
          $ cd ~/ros_catkin_ws</code></pre>

        * ROS-Comm (Bare Bones) 또는 Desktop Install 설치
          > ROS-Comm: Headless(KVM이 없는 디바이스)로 설치 (rviz 미포함)<br/>
          > Desktop Install: GUI 툴 포함 설치(rqt, rviz, robot-generic libraries)
          <pre><code># Desktop 설치
          $ rosinstall_generator desktop --rosdistro melodic --deps --wet-only --tar > melodic-desktop-wet.rosinstall
          $ wstool init -j8 src melodic-desktop-wet.rosinstall</code></pre>
          > <i>watool init</i>가 실패하거나 중단된 경우 다음을 실행하여 다운로드를 재개할 수 있다.
          <pre><code>$ wstool update -j4 -t src</code></pre>

        * Dependency packages 설치 확인
          <pre><code>$ rosdep install --from-paths src --ignore-src --rosdistro melodic -y</code></pre>

     2. 이슈 수정
        * collada_urdf 종속 문제를 해결하기 위해 호환 가능 버전인 Assimp 설치
          * (Not used) [Manual Build Assimp](https://github.com/assimp/assimp/blob/master/Build.md) : https://github.com/assimp/assimp/blob/master/Build.md
          > Assimp: Open Asset Import Library
          <pre><code>$ mkdir -p ~/ros_catkin_ws/external_src
          $ cd ~/ros_catkin_ws/external_src
          $ wget http://sourceforge.net/projects/assimp/files/assimp-3.1/assimp-3.1.1_no_test_models.zip/download -O assimp-3.1.1_no_test_models.zip
          $ unzip assimp-3.1.1_no_test_models.zip
          $ cd assimp-3.1.1
          $ cmake .
          $ make
          $ sudo make install</code></pre>
          > ↑ <i>sudo make install</i> 진행시 Warning이 엄청 나옴

        * rvix용 OGRE 설치
          <pre><code>$ sudo apt-get install -y libogre-1.9-dev</code></pre>

        * (Skip) libboost 이슈 수정 (Skip)
          * https://stackoverflow.com/questions/53266574/installing-ros-melodic-on-ubuntu-18-10/53382269#53382269
          > boost 최신 버전은 정수 인수만 허용하지만 ROS의 actionlib 패키지에서 부동소수점 사용하므로 수동으로 해당 소스를 찾아 수정해야 함<br/>
          > <b>실제 각 소스는 int64_t로 캐스팅되거나 int형으로 수정되어 있으므로 해당 소스 찾기는 건너뛰어도 됨</b>

          * 오류 소스 찾기
            <pre><code>$ cd ~
            $ find -type f -print0 | xargs -0 grep 'boost::posix_time::milliseconds' | cut -d: -f1 | sort -u</code></pre>

          * 찾은 파일
            > <i>vi</i> 사용시 ':set number'로 소스 앞에 라인 번호를 볼 수 있음<br/>
            <pre><code>./src/actionlib/CHANGELOG.rst
            ./src/actionlib/include/actionlib/client/simple_action_client.h
            ./src/actionlib/include/actionlib/destruction_guard.h
            ./src/actionlib/include/actionlib/server/simple_action_server_imp.h
            ./src/actionlib/src/connection_monitor.cpp
            ./src/actionlib/test/destruction_guard_test.cpp
            ./src/bond_core/bondcpp/src/bond.cpp
            ./src/ros_comm/roscpp/include/ros/timer_manager.h
            ./src/ros/roslib/test/utest.cpp</code></pre>

          * 수정 예시 #1
            <pre><code>boost::posix_time::milliseconds(loop_duration.toSec() * <i>1000.0f</i>));
            → boost::posix_time::milliseconds(<i>int(loop_duration.toSec() * 1000.0f)</i>));</code></pre>

          * 수정 예시 #2
            <pre><code>boost::posix_time::milliseconds(<i>1000.0f</i>)
            → boost::posix_time::milliseconds(<i>1000</i>)</code></pre>

     3. rosdep 도구로 나머지 종속성 설치
               <pre><code>$ rosdep install --from-paths src --ignore-src --rosdistro melodic -y</code></pre>

  3. ROS 빌드
     * CPU 발열 대비를 하지 않을 경우 빌드중 라즈베리파이가 다운될 수도 있음

     1. Swap 공간 확보
        > Desktop 버전 설치시 컴파일이 멈추는 경우가 종종 발생한다.<br/>
        > 이 때에는 사용 가능한 Swap 공간 영역을 늘여야 한다.<br/>
        > 100MB인 기본값을 2,048MB로 늘려서 빌드를 하고, 끝나면 원상복구를 해 놓아야 한다.
        <pre><code>$ sudo vi /etc/dphys-swapfile
        ...
        # CONF_SWAPSIZE=100
        CONF_SWAPSIZE=2048
        &lt;ESC&gt;:wq!
        $ sudo /etc/init.d/dphys-swapfile stop
        $ sudo /etc/init.d/dphys-swapfile start</code></pre>

     2. catkin 패키지 빌드
        * 컴파일 과정은 <b>약 3시간</b>(Raspberry Pi 3 기준) 이상 소요
        <pre><code>$ cd ~/ros_catkin_ws
        $ sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/melodic -j2</code></pre>

        * Error
          <pre><code>
          ==> Processing catkin package: 'rviz'
          ==> Building with env: '/opt/ros/melodic/env.sh'
          Makefile exists, skipping explicit cmake invocation...
          ==> make cmake_check_build_system in '/home/pi/ros_catkin_ws/build_isolated/rviz'
          ==> make -j2 in '/home/pi/ros_catkin_ws/build_isolated/rviz'
          [  0%] Automatic MOC for target interactive_marker_test
          [  0%] Automatic MOC for target rviz
          [  0%] Built target interactive_marker_test_autogen
          [  1%] Automatic MOC for target connect_test
          [  1%] Built target rviz_autogen
          ...
          [ 57%] Automatic MOC for target two_render_widgets
          [ 57%] Built target two_render_widgets_autogen
          [ 57%] Compiling generated code for rviz_sip Python bindings...
          make[3]: warning: jobserver unavailable: using -j1.  Add '+' to parent make rule.
          make[3]: *** No targets.  Stop.
          make[2]: *** [src/python_bindings/sip/CMakeFiles/librviz_sip.dir/build.make:61: /home/pi/ros_catkin_ws/devel_isolated/rviz/lib/python2.7/dist-packages/rviz/librviz_sip.so] Error 2
          make[1]: *** [CMakeFiles/Makefile2:5125: src/python_bindings/sip/CMakeFiles/librviz_sip.dir/all] Error 2
          make[1]: *** Waiting for unfinished jobs....
          [ 57%] Built target rviz_default_plugin_autogen
          make: *** [Makefile:141: all] Error 2
          <== Failed to process package 'rviz':
            Command '['/opt/ros/melodic/env.sh', 'make', '-j2']' returned non-zero exit status 2

          Reproduce this error by running:
          ==> cd /home/pi/ros_catkin_ws/build_isolated/rviz && /opt/ros/melodic/env.sh make -j2

          Command failed, exiting.</code></pre>

        * 옵션 <i>-j2</i>를 <i>-j1</i>로 변경하여 빌드
        <pre><code>$ sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/melodic -j1</code></pre>

     3. Swap 공간 복구
        <pre><code>$ sudo vi /etc/dphys-swapfile
        ...
        CONF_SWAPSIZE=100
        # CONF_SWAPSIZE=2048
        &lt;ESC&gt;:wq!
        $ sudo /etc/init.d/dphys-swapfile stop
        $ sudo /etc/init.d/dphys-swapfile start</code></pre>

  4. 설치 소싱
     <pre><code>$ cd ~
     $ cp .bashrc .bashrc.bak
     $ echo "source /opt/ros/melodic/setup.bash" &gt;&gt; ~/.bashrc</code></pre>

  5. roscore 실행으로 체크
