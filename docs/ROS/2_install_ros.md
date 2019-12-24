# ROS Home
  ^ http://ros.org
  
# Install ROS Melodic on Raspberry Pi 3
  1. Ref.
     1. http://wiki.ros.org/melodic/Installation/Source
     2. https://www.hackster.io/dmitrywat/ros-melodic-on-raspberry-pi-4-debian-buster-rplidar-a1m8-0d63d1
  
  2. Install ROS Melodic
     1. Install Dependencies and Download the Packages
        <pre><code>$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' 
        $ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
        $ sudo 
        </code></pre>