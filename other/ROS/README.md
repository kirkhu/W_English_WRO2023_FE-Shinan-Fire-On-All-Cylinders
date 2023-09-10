 <div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>
 
 2023WRO Future Engineers Shinan Fire On All Cylinders  
=====
# <div align="center">Introduction to ROS</div> 
- ROS (Robot Operating System) is an open-source framework designed to facilitate the development of robot applications. It provides a collection of software libraries and tools that enable seamless communication and collaboration between different components of a robotic system.

- With a flexible and distributed architecture, ROS allows developers to build complex robot applications by creating modular and reusable software components known as nodes. These nodes can communicate with each other by passing messages, enabling easy integration of various functionalities.

- One of the key advantages of ROS is its extensive library of pre-existing packages, which cover a wide range of robotic tasks, such as mapping, localization, navigation, perception, and more. This vast ecosystem of packages makes ROS a popular choice for researchers, developers, and robotic enthusiasts worldwide.

- ROS supports multiple programming languages, including C++, Python, and others, catering to developers with diverse language preferences. Furthermore, it is platform-independent, allowing users to deploy ROS-based applications on different operating systems.

- Whether in research, industrial automation, autonomous vehicles, or other robotic applications, ROS has proven to be a powerful and versatile tool for creating sophisticated robotic systems and applications.


## Installation Steps  
__Step1. setup ROS Database__
```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python3-rosdep python3-rosinstall-generator python3-vcstool build-essential
$ sudo rosdep init
$ rosdep update
```
__Step2. install ROS__
- __2.1 Create a working environment__
```
$ cd
$ mkdir ~/ros_catkin_ws
$ cd ~/ros_catkin_ws
$ pip3 install importlib-metadata
$ rosinstall_generator desktop --rosdistro noetic --deps --tar > noetic-desktop.rosinstall
$ mkdir ./src
$ vcs import --input noetic-desktop.rosinstall ./src
```
- __2.2 Install dependencies__
```
$ rosdep install --from-paths ./src --ignore-packages-from-source --rosdistro noetic -y
```
- __2.3 Create catkin working environment__
```
$ sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3 --install-space /opt/ros/noetic
$ source /opt/ros/noetic/setup.bash
$ echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
```
<small>Date sourse:<br>[ithelp](https://ithelp.ithome.com.tw/articles/10200551)  
[wikipedia](https://zh.wikipedia.org/zh-tw/%E6%A9%9F%E5%99%A8%E4%BA%BA%E4%BD%9C%E6%A5%AD%E7%B3%BB%E7%B5%B1)  
[Mechanical-Engineering-Magazine Issue 412](https://docs.google.com/document/d/1M4JN4CFelSwmJmYl0W2PQt0lKBieaWgcDpVNfjTycGE/edit?pli=1)</small>  

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
