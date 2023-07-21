Engineering materials
====

This repository contains engineering materials of a self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2022.
* [2022美國第二名的GitHub參考](https://github.com/definitely-nobody-is-here/SPARK_Future-Engineers_2022?fbclid=IwAR00_3dfM16glfze2lCYE--QD1HyJoParn6c9IV0YEm_ZA2aLQ1S2wIMOSM_aem_AbD82MjkT8YgQMrDoxd_dTQKZyMoBclmGeazY_IAPRwTwzgrg0K8dnOkb8TkuzYEPvc).
* [Future-Engineers國際規則](https://wro-association.org/competition/2023-season/)
* [Future-Engineers馬達配置規定](https://www.era.org.tw/main/wp-content/uploads/2023/06/Future-Engineers%E9%A6%AC%E9%81%94%E9%85%8D%E7%BD%AE%E8%A6%8F%E5%AE%9A.pdf)
* [WRO-2023-未來工程師_混齡（全國賽版本）_繁中0627_V1](https://www.era.org.tw/main/wp-content/uploads/2023/06/WRO-2023-%E6%9C%AA%E4%BE%86%E5%B7%A5%E7%A8%8B%E5%B8%AB_%E6%B7%B7%E9%BD%A1%EF%BC%88%E5%85%A8%E5%9C%8B%E8%B3%BD%E7%89%88%E6%9C%AC%EF%BC%89_%E7%B9%81%E4%B8%AD0627_V1.pdf)
* [歡迎使用 Markdown線上編輯器 MdEditor](https://www.mdeditor.tw/)
* [使用VSCODE 編輯 MarkDown   Markdown All in One  v3.5.1 ](https://ithelp.ithome.com.tw/articles/10225442)
* [官方教程](https://markdown.com.cn/basic-syntax/headings.html)
 
* [Video to markdown!](https://video-to-markdown.marcomontalbano.com/)  
  只需要粘贴Youtube视频地址，就可以生成markdown文本，封面图带上了播放按钮。比如下面的视频  
* 使用VScode 上傳檔案到GITHUB方式
  - 下載 VScode 並安裝 
  - 下載 Git  並安裝
  - 執行 Git bash 
    > git config --global user.name "您的姓名"  
    > git config --global user.email "您的Email"   
  - 執行 VScode 點 複製Git存放庫
  - 選擇本地電腦資料夾位置
  - 編輯後存檔、打說明、提交、同步變更
* 圖片改大小
   > "<img src="./t-photos/team_photo.jpg" width = "300" height = "300" alt="圖體照" align=center />"
## Content
- ### ${{\color{red} Hardware Overview }} $ 
  - [Parts List](#parts-list)
  - Lidar of Introduction
  - Assembly Instructions & Diagrams
  - Robot's Photos
- ### ${{\color{red} Software Overview }} $ 
  - [Operating System](#operating-system)
  - ROS of Introduction
  - Programming Language
  - IO
  - Image Processing and Predictions
    - Image Preprocessing
    - Wall Steering
    - Pillar Steering
    - Final Steering
  - PARK Control Panel
- ### Team Photos
  **Team Photo**  
  <img src="./t-photos/team_photo.jpg"/>  

  
  **A Funny Photo**  
  <img src="./t-photos/funny_photo.jpg"/>  
- ### Demonstration Video
- ### LiPo Battery Safety Notice

> * t-photos包含 2 張團隊照片（一張是官方照片，一張是所有團隊成員的搞笑照片）
> * v-photos包含 6 張車輛照片（從各個側面、從頂部和底部）
> * video包含 video.md 文件，其中包含指向存在駕駛演示的視頻的鏈接
> * schemes包含一張或多張 JPEG、PNG 或 PDF 形式的機電組件示意圖，說明車輛中使用的所有元件（電子元件和電機）以及它們如何相互連接。
> * src包含所有被編程參加比賽的組件的控制軟件代碼
> * models用於 3D 打印機、激光切割機和 CNC 機器生產車輛元件所使用的模型的文件。如果沒有任何內容可添加到此位置，則可以刪除該目錄。
> * other用於其他文件，可用於了解如何為比賽準備車輛。它可能包括如何連接到 SBC/SBM 並向其中上傳文件、數據集、硬件規格、通信協議描述等的文檔。如果沒有任何內容可添加到此位置，則可以刪除該目錄。

 ## ${{\color{red} The Hardware }}$ 
   ### 。Parts List
   ### 。Lidar of Introduction
   - 介紹光達  
     D100 開發者套裝是以光達 LiDAR LD14為核心再搭配相關零配件組合而成。  
     使用三角測距技術，可以偵測周圍360度，最大偵測距離是8公尺，2300次偵測頻率  
   - 比較超音波與光達的異差  
     超音波只能偵測單方向，但是光達可以偵測四周，所以能偵測兩旁的牆壁，減少擦牆的機率  
   - 說明不同品牌光達遇到的問題  
     D100體積小，但是偵測頻率是2300，相比 ydlidar 的 x2 的 3000HZ 和 x4 的 5000HZ，頻率更小，因此反應會慢一點  
     <small>網址來源:[飆機器人](https://shop.playrobot.com/products/lidar-d100-ld14)</small>
   ### Assembly Instructions & Diagrams
   ### Robot's Photos   
|        |        |  
| :----: | :----: |  
|  左視圖 | 右視圖 |
| <img src="./v-photos/Left_view.png" alt="Image"> | <img src="./v-photos/Right_view.png" alt="Image"> |
|  前視圖  |  後視圖   |    
| <img src="./v-photos/front_view.png" alt="Image"> | <img src="./v-photos/rear_view.png" alt="Image"> | 
|  上視圖  |  下視圖   |   
| <img src="./v-photos/top_view.png" alt="Image"> | <img src="./v-photos/bottom-view.png" alt="Image"> |   

 ## ${{\color{red} The Softwarehe }} $ 
   ### 。Operating System  
   #### System Platform Software Installation Process Diagram.
   ![images](src/software_setup.png)  
   安裝 pi os時，選擇安裝Legacy    
   安裝完之後打開終端機輸入  
   > sudo raspi-config  
   
   選擇Interface Options之後打開Camera、SSH和VNC然後退出    

   之後安裝opencv，在裝之前要先確認setuptools和wheel的版本支援安裝的opencv  

   然後安裝ROS系統，先設定資料庫，再來建立工作環境，之後安裝依賴項目，最後在建置catkin的工作環境  

   再來是安裝光達的驅動程式，首先先取得Lidar安裝包，再來設定USB接口權限，之後安裝依賴項目，然後編譯，最後加入環境變數

   ### 。Programming Language
   我們選了 python 用於我們的程式開發上  
   ![image](/src/python.png)  
   <small>圖片來源:[medium](https://allaboutdataanalysis.medium.com/%E5%AD%B8python%E5%B8%B8%E9%80%9B%E7%9A%8410%E5%80%8B%E7%B6%B2%E7%AB%99-%E9%80%99%E6%AC%A1%E5%85%A8%E9%83%BD%E5%91%8A%E8%A8%B4%E4%BD%A0-eb2656ee0b22)</small>
   
   Python是一种高级、通用的编程语言。它的设计理念强调代码的可读性，使用了显著缩进。Python是动态类型且具有自動的記憶體管理機制功能。  
   支持多种编程范式，包括结构化（特别是特別程序化）、面向对象和函数式编程。由于其全面的标准库，它通常被描述为一个 “batteries included” 的語言。  
   <small>來源網址:[維基百科](https://zh.wikipedia.org/zh-tw/Python)</small>
   ### 。IO
   ### 。Image Processing and Predictions
   ####  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Image Preprocessing
   ####  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wall Steering
   ####  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pillar Steering
   ####  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Final Steering
   ####  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PARK Control Panel
          可複製程式用法
    
> _這部分必須由參與者填寫有關代碼的技術說明：代碼由哪些模塊組成，它們與車輛的機電組件有何關係，以及構建/編譯/上傳代碼到車輛的過程是什麼控制器。_

## How to prepare the repo based on the template

_Remove this section before the first commit to the repository_

1. Clone this repo by using the `git clone` functionality.
2. Remove `.git` directory
3. [Initialize a new public repository on GitHub](https://github.com/new) by following instructions from "create a new repository on the command line" section (appeared after pressing "Create repository" button).
新增文章內容
