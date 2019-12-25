# ROS Home
  > http://ros.org
  
# Install ROS Melodic on Raspberry Pi 3
  1. Ref.
     1. http://wiki.ros.org/melodic/Installation/Source
     2. https://www.hackster.io/dmitrywat/ros-melodic-on-raspberry-pi-4-debian-buster-rplidar-a1m8-0d63d1
  
  2. Install ROS Melodic
     1. Install Dependencies and Download the Packages
        * 레포지토리를 설정하고 필요한 종속성 설치
          <pre><code>$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' 
          $ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
          $ sudo apt-get update
          $ sudo apt-get install -y python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential cmake</code></pre>

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

     2. 이슈 수정
        * collada_urdf 종속 문제를 해결하기 위해 호환 가능 버전인 Assimp 설치
          > Assimp: Open Asset Import Library
          <pre><code>$ mkdir -p ~/ros_catkin_ws/external_src
          $ cd ~/ros_catkin_ws/external_src
          $ wget http://sourceforge.net/projects/assimp/files/assimp-3.1/assimp-3.1.1_no_test_models.zip/download -O assimp-3.1.1_no_test_models.zip
          $ unzip assimp-3.1.1_no_test_models.zip
          $ cd assimp-3.1.1
          $ cmake .
          $ make
          $ sudo make install</code></pre>

        * rvix용 OGRE 설치
          <pre><code>sudo apt-get install -y libogre-1.9-dev</code></pre>

        * libboost 이슈 수정
          > https://stackoverflow.com/questions/53266574/installing-ros-melodic-on-ubuntu-18-10/53382269#53382269<br/>
          > boot 최신 버전은 정수 인수만 허용하지만 ROS의 actionlib 패키지에서 부동소수점 사용하므로 수동으로 해당 소스를 찾아 수정해야 함

          1. 해당 소스 찾기
             <pre><code>$ cd ~
             $ find -type f -print0 | xargs -0 grep 'boost::posix_time::milliseconds' | cut -d: -f1 | sort -u</code></pre>
          2. 수정 예시
             * from #1
               <pre><code>boost::posix_time::milliseconds(loop_duration.toSec() * <i>1000.0f</i>));</code></pre>
             * to #1
               <pre><code>boost::posix_time::milliseconds(<i>int(loop_duration.toSec() * 1000.0f)</i>));</code></pre>

             * from #2
               <pre><code>boost::posix_time::milliseconds(<i>1000.0f</i>)</code></pre>
             * to #2
               <pre><code>boost::posix_time::milliseconds(<i>1000</i>)</code></pre>

             * rosdep 도구로 나머지 종속성 설치
               <pre><code>$ rosdep install --from-paths src --ignore-src --rosdistro melodic -y</code></pre>

          3. 빌드 설치
             <pre><code></code></pre>