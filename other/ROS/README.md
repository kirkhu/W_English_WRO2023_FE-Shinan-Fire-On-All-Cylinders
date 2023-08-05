![LOGO](../img/logo.png) 2023WRO Future Engineers Fire On All Cylinders  
=====
# <div align="center">Introduction to ROS(ROS系統介紹)</div> 
## English Introduction
- ROS (Robot Operating System) is an open-source framework designed to facilitate the development of robot applications. It provides a collection of software libraries and tools that enable seamless communication and collaboration between different components of a robotic system.

- With a flexible and distributed architecture, ROS allows developers to build complex robot applications by creating modular and reusable software components known as nodes. These nodes can communicate with each other by passing messages, enabling easy integration of various functionalities.

- One of the key advantages of ROS is its extensive library of pre-existing packages, which cover a wide range of robotic tasks, such as mapping, localization, navigation, perception, and more. This vast ecosystem of packages makes ROS a popular choice for researchers, developers, and robotic enthusiasts worldwide.

- ROS supports multiple programming languages, including C++, Python, and others, catering to developers with diverse language preferences. Furthermore, it is platform-independent, allowing users to deploy ROS-based applications on different operating systems.

- Whether in research, industrial automation, autonomous vehicles, or other robotic applications, ROS has proven to be a powerful and versatile tool for creating sophisticated robotic systems and applications.

## 中文介紹（Chinese Introduction）：

- ROS（Robot Operating System）是一個開源框架，旨在促進機器人應用的開發。它提供了一系列軟體庫和工具，實現機器人系統中不同組件之間的無縫通信和協作。  
- ROS具有靈活和分佈式的架構，允許開發者通過創建稱為節點的模塊化和可重用的軟體組件來構建複雜的機器人應用。這些節點可以通過傳遞消息相互通信，實現各種功能的輕鬆集成。  
- ROS的一個主要優點是其龐大的預先存在的軟體包庫，涵蓋了廣泛的機器人任務，如建圖、定位、導航、感知等。這個龐大的軟體生態系統使得ROS成為全球研究人員、開發者和機器人愛好者的熱門選擇。  
- ROS支持多種編程語言，包括C++、Python等，滿足擁有不同語言偏好的開發者。此外，ROS是跨平台的，允許用戶在不同的操作系統上部署基於ROS的應用。  
- 不論是在研究、工業自動化、自動駕駛車輛還是其他機器人應用領域，ROS都已被證明是一個強大且多功能的工具，用於創建複雜的機器人系統和應用。  

## Installation Steps  
__Step1. setup ROS Database(建立ROS資料庫)__
```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python3-rosdep python3-rosinstall-generator python3-vcstool build-essential
$ sudo rosdep init
$ rosdep update
```
__Step2. install ROS(安裝ROS系統)__
- __2.1 Create a working environment(建立工作環境)__
```
$ cd
$ mkdir ~/ros_catkin_ws
$ cd ~/ros_catkin_ws
$ pip3 install importlib-metadata
$ rosinstall_generator desktop --rosdistro noetic --deps --tar > noetic-desktop.rosinstall
$ mkdir ./src
$ vcs import --input noetic-desktop.rosinstall ./src
```
- __2.2 Install dependencies(安裝依賴項)__
```
$ rosdep install --from-paths ./src --ignore-packages-from-source --rosdistro noetic -y
```
- __2.3 Create catkin working environment(建立 catkin 工作環境)__
```
$ sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3 --install-space /opt/ros/noetic
$ source /opt/ros/noetic/setup.bash
$ echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
```
<small>資料來源:[it邦邦忙](https://ithelp.ithome.com.tw/articles/10200551)  
資料來源:[維基百科](https://zh.wikipedia.org/zh-tw/%E6%A9%9F%E5%99%A8%E4%BA%BA%E4%BD%9C%E6%A5%AD%E7%B3%BB%E7%B5%B1)  
資料來源:[機械工業雜誌 412期](https://docs.google.com/document/d/1M4JN4CFelSwmJmYl0W2PQt0lKBieaWgcDpVNfjTycGE/edit?pli=1)</small>  

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
