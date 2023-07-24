![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
=====
# <div align="center">Software Platform (軟體平台)</div> 
- ### System Platform Software Installation Process Diagram.
![images](./img/software_setup.png) 
 - [Raspberry Pi Introduce](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/other/Raspberry_Pi/README.md)
 - 安裝PI OS時，選擇安裝Raspberry Pi OS (Legacy)  
   - Software link：[On Shope](https://www.onshape.com/en/) 
   - 安裝完之後，請更新作業系統，以確保的軟體的相容性

   > $ sudo apt-get update  

   > $ sudo apt-get upgrade   

 - 選擇Interface Options之後打開Camera、SSH和VNC然後退出  
 - 安裝opencv版本:4.7.0.72，在裝之前要先確認setuptools和wheel的版本支援安裝的opencv  
 - 安裝ROS系統版本:noetic ninjemys，先設定資料庫，再來建立工作環境，之後安裝依賴項目，最後在建置catkin的工作環境  
 - 安裝PIGPIO Library，以利控制顔色感測器，讀取場地顏色值
 - 安裝Dlidar光達的驅動程式，首先先取得Lidar安裝包，再來設定USB接口權限，之後安裝依賴項目，然後編譯，最後加入環境變數

- ### Seutp Recode (紀錄場地值)
![images](./img/setup_recode.png)  
- ### Programming Language
  ### English
   - Python is a high-level, general-purpose, interpreted programming language created by Guido van Rossum in 1991. It is designed to be concise, readable, and comes with a rich 
  standard library, enabling developers to write code quickly and efficiently. 
   - Python is widely used in web development, scientific computing, data analysis, artificial intelligence, machine learning, and various other fields. It features dynamic typing, automatic garbage collection, and supports multiple platforms.
   - With an active community, Python has a plethora of third-party libraries and tools, making development even more convenient. Python has become a popular choice for both beginners and experienced developers.  

  __Therefore, we choose Python as the programming language for the development of the self-driving vehicle.__

  ### 中文
   - Python是一種高階、通用、直譯式程式語言，由Guido van Rossum於1991年創建。它設計簡潔、易讀且具有豐富的標準函式庫，使開發者能夠快速有效地撰寫程式碼。
   - Python被廣泛應用於Web開發、科學計算、數據分析、人工智慧、機器學習等領域。它具有動態類型、自動垃圾回收等特性，並支援多種平台。
   - Python社群活躍，有大量的第三方庫和工具，使得開發更加便捷，Python成為初學者和專業開發者的熱門選擇。

   __因此，我們選用python 作為自駕車輛的程式開發語言。__ 

- ### Mobaxterm Introduce
  ### English：
  - MobaXterm is a feature-rich cross-platform remote computing management tool. 
  - It integrates various network tools such as X11 server, remote computing, SSH, VNC, and more, providing an intuitive user interface for easy connection to remote servers in Windows environments.
  - MobaXterm also supports simultaneous management of multiple sessions, allowing users to switch and operate different remote connections effortlessly. This tool is highly valuable for system administrators, network engineers, and developers.

  __Therefore, we have chosen MobaXterm as the remote control tool for the Raspberry Pi in the self-driving vehicle.__

  ### 中文：
  - MobaXterm是一款功能豐富的跨平台遠端計算機管理工具。
  - 它整合了X11伺服器、遠端運算、SSH、VNC等多種網路工具，並提供一個直觀的用戶界面，方便用戶在Windows環境下連接到遠端伺服器。
  - MobaXterm還支援多個會話的同時管理，讓用戶輕鬆切換和操作不同的遠端連接。這款工具對於系統管理員、網路工程師和開發人員來說是一個極具價值的工具。

   __因此，我們選用Mobaxterm作為自駕車輛中Raspberry Pi的遠端控制工具。__  

- Software link：[Mobaxterm](https://mobaxterm.mobatek.net/) 


- ### Visal Studio Code Introduce
  ### English：
  - Visual Studio Code (often referred to as VS Code) is a free, open-source, and cross-platform code editor developed by Microsoft. It supports multiple programming languages and offers a rich set of extensions to cater to individual needs.
  - VS Code features an intuitive user interface and powerful code editing capabilities, including intelligent code completion, code navigation, debugging, and version control. It is widely embraced by developers and has become the preferred editing tool for many software development projects.

  __Therefore, we have chosen VS Code as the programming tool for the self-driving vehicle.__

  ### 中文：
  - Visual Studio Code（簡稱VS Code）是一款由Microsoft開發的免費、開源且跨平台的程式碼編輯器。它支援多種程式語言，並擁有豐富的擴充功能，讓使用者可以個性化配置以滿足不同需求。
  - VS Code擁有直覺的用戶界面和強大的代碼編輯功能，如智慧程式碼完成、程式碼導航、除錯和版本控制等。它廣受開發人員歡迎，成為許多軟體開發項目的首選編輯工具。
   
   __因此，我們選用VS Code作為自駕車輛的程式撰寫工具。__  

- Software link：[Raspberry Pi OS](https://code.visualstudio.com/) 

  # <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
