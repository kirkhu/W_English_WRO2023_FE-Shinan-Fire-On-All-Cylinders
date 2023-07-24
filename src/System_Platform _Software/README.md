![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
=====
# <div align="center">Software Platform (軟體平台)</div> 
- ### System Platform Software Installation Process Diagram.
![images](./img/software_setup.png) 
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


- ### Vs Code Introduce
  # <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
