![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
=====
# <div align="center">Software Platform (軟體平台)</div> 
- ### System Platform Software Installation Process Diagram.
![images](./img/software_setup.png)  
- 安裝 pi os時，選擇安裝Legacy    
   - 安裝完之後打開終端機輸入  
   > sudo raspi-config  
   
   - 選擇Interface Options之後打開Camera、SSH和VNC然後退出    

   - 安裝opencv 版本:4.7.0.72，在裝之前要先確認setuptools和wheel的版本支援安裝的opencv  

   - 安裝ROS系統 版本:noetic ninjemys，先設定資料庫，再來建立工作環境，之後安裝依賴項目，最後在建置catkin的工作環境  

   - 安裝光達的驅動程式，首先先取得Lidar安裝包，再來設定USB接口權限，之後安裝依賴項目，然後編譯，最後加入環境變數


    ### 。Programming Language
   我們選了 python 用於我們的程式開發上  
   ![image](./src/img/python.png)  
   <small>圖片來源:[medium](https://allaboutdataanalysis.medium.com/%E5%AD%B8python%E5%B8%B8%E9%80%9B%E7%9A%8410%E5%80%8B%E7%B6%B2%E7%AB%99-%E9%80%99%E6%AC%A1%E5%85%A8%E9%83%BD%E5%91%8A%E8%A8%B4%E4%BD%A0-eb2656ee0b22)</small>
   
   Python是一种高级、通用的编程语言。它的设计理念强调代码的可读性，使用了显著缩进。Python是动态类型且具有自動的記憶體管理機制功能。  
   支持多种编程范式，包括结构化（特别是特別程序化）、面向对象和函数式编程。由于其全面的标准库，它通常被描述为一个 “batteries included” 的語言。  
   
   <small>來源網址:[維基百科](https://zh.wikipedia.org/zh-tw/Python)</small>

  # <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
