2023WRO Future Engineers Shinan Fire On All Cylinders  
=====
# <div align="center">Work Diary </div> 

## 2023/03/19 ~ 2023/03/26  
**member:** ZHAO,ZHEN-BO  
**content:**  

At the beginning, since we were unsure of how to start building and making the vehicle, we referenced the Donkey Car official website. Therefore, the construction of the vehicle will be based on modifications of the vehicle design from the official website.

由於一開始我們還不知道如何開始建構及製作，因此我們參考了Donkey Car 官網，因此車輛的製作會基於官網的車輛來改造。

<div align="center">
<table>
<tr align="center"><th><a href="https://www.donkeycar.com/">Donkey Car 官網</a></th>
<th><a href="http://docs.donkeycar.com/">Donkey Car 技術文件</a></th>
</tr>
<tr align="center">
<td> <img src="./img/3/donkeycar.png" width = "300"  alt="樹梅派" align=center /></td>
<td><img src="./img/3/donkeycar_doc.png" width = "300"  alt="jeston nano" align=center /></td>
</tr>
</table>
</div>


<div align="center" width=100%>
<img src="./img/3/Daily.jpg" width="300" alt="Daily" >
</div>


## 2023/03/27 ~ 2023/04/02
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN  
**content:** 
- To ensure the smooth progression of the competition, our team carefully planned the completion timeline for each stage of the competition activities.
- After reading the rules, We started to choose the controller. After watching the previous competitions, we found that most of them are raspberry pi but there are also jeston nano, so I decided to choose one of these two. In the end, I chose raspberry pi 4B because of its smaller size and cheaper price than jeston nano. 

- 為確保競賽活動順利進行，我們小組進行了競賽活動各階段工作完成時間的細心規劃。，如下圖。
- 在閱讀完規則後，開始挑選控制器，因為看過歷屆的比賽，發現大多都是 raspberry pi ，但也有 jeston nano ，因此決定在這兩種裡挑一種，最後選擇了 raspberry pi 4B ，因為體積比較小而且價格也比 jeston nano 便宜。

  __競賽活動各階段工作完成時間規劃表(甘特圖)__ 
<div align="center" >
  <img src="../img/Gantt_Chart.png" width = "600" height = "" alt="甘特圖" align=center />
</div>

### Vehicle Computing Controller(車輛運算控制器)
<div align="center" >
<table >
<tr align="center">
<th>Raspberry pi 4 B 8G</th>
<th>Jeston Nano </th>
<tr align="center">
<td>
<img src="./img/3/raspberry_pi_4.png" width = "300"  alt="樹梅派" /></td>
<td>
<img src="./img/3/jeston_nano.png" width = "300"  alt="jeston nano"/></td>
</tr>
</table>
</div>



## 2023/04/03 ~ 2023/04/09  
**member:** ZHAO,ZHEN-BO  
**content:**  

- While waiting for the Raspberry Pi to initialize and libraries to be installed, we selected the motor for propulsion, with two options: JGA25-370 and JGA16-050. The former boasts higher torque, capable of moving heavier objects, while the latter is smaller and lighter, albeit with relatively lower torque. Considering the potential weight of the robot, we opted for the higher torque of the JGA25-370.
- Among the JGA25-370 options, there are several variations currently available within the club.
- During the testing of motor operation, a simple application of positive and negative voltage did not provide effective control over the JGA25-370's performance or speed adjustment. As a result, a motor controller is needed to regulate the speed of the DC geared motor. Two options were considered: the L293D chip and the L298N module. To minimize weight, we chose the compact L293D chip. Its small size allows us to accommodate more sensors, thereby saving space, reducing weight, and enhancing the robot's maneuverability.


- 在等待初始化樹梅派及安裝函式庫時，挑選作為動力的馬達，有兩種，分別是 JGA25-370 和 JGA16-050，前者的優點是扭力大，可以帶動較重的物體，後者的優點是體積小，重量也比較輕，但是扭力相對較小，由於考慮到機體可能會比較重，所以選了扭力較大的 JGA25-370 
- 而 JGA25-370 有許多種不同的分支，下面幾顆是目前社團擁有的
- 在測試馬達的作動方式時，單純的提供正負極並沒有辦法很好的控制JGA25-370的作動，無法調節速度，因此還需要馬達控制器來調節直流減速馬達的速度，有兩種選擇：L293D晶片和L298N模組。為了減輕重量，我們選擇了體積較小的L293D晶片。它的小巧尺寸使我們能夠安裝更多的感應器，進而節省空間、減輕重量，並增加機器人的機動性。


#### DC Motor(直流馬達)
<div align="center"><table><tr align="center">
<th rowspan="2">Model(型號)</th>
<th>JGA25 370</th>
<th>JGA25 370</th>
<th>JGA25 371</th>
<th>JGA16-050</th>
</tr>
<tr  align="center">

<td><img src="./img/4/JGA25-370_1360RPM.JPG" width = "150" alt="JGA25-370_1360RPM" /></td>
<td><img src="./img/4/JGA25-370_620RPM.JPG" width = "150" alt="JGA25-370_620RPM" /></td>
<td><img src="./img/4/JGA25-371_1_34.JPG" width = "100" alt="JGA25-371M" /></td>
<td ><img src="./img/5/JGA16-050.png" width = "150" alt="JGA16-050" /></td>
</tr>
<tr align="center">
<td >speed(轉速)</td>
<td >1360rpm/m</td>
<td >620rpm/m</td>
<td >294rpm/m</td>
<td >220rpm/m</td>
</tr>
<tr align="center">
<td>torque(力距)</td>
<td>4.27kg.cm</td>
<td>9.15kg.cm</td>
<td>5.2kg.cm</td><td>1.15kgcm</td>
</tr><tr align="center">
<td>power(功率)</td><td>5.4W</td><td>5.4W</td><td>4.2W</td><td>0.33W</td>
</tr>
</table>
</div>



## 2023/04/10 ~ 2023/04/16  
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei
**content:**  

- Due to the continuous movement of the vehicle, the power source needs to be changed to a battery. Considering that the motors require a 12V voltage to operate, we need to choose a battery with a voltage of 12V and a current of 3V. There are two options: lithium-ion batteries (18650) and lithium polymer batteries (3S). However, the 18650 battery is heavier and takes up more space, so we opted for the lithium polymer battery.
- However, the maximum voltage supported by the Raspberry Pi is only 5.2V. Therefore, we need to use a step-down module to reduce the voltage to prevent damage to the Raspberry Pi. We initially considered using the LM2596 DC-DC adjustable step-down module, as it has a numerical display to show the current output voltage. However, its maximum current capacity is only 3A. Therefore, we chose a constant voltage and constant current step-down power supply module that can handle up to 5A. Though it lacks a numerical display, we will install a low voltage alarm to detect the battery voltage and ensure its safety.

- 由於車輛需要不斷的移動，因此需要將電力來源改成電池。考慮到馬達需要12V的電壓才能使用，我們選擇了電壓為12V、電流為3A的電池。有兩種選擇：鋰離子電池(18650)和鋰聚合電池(3S)。然而，由於18650電池重量較重且佔據空間較大，因此我們選擇了鋰聚合電池。
- 但是樹梅派最大電壓只能到5.2V，因此我們需要使用降壓板來將電壓降低，以避免樹梅派受損。最初我們打算使用LM2596 DC-DC可調降壓模組，因為它有數值顯示，可以顯示目前輸出電壓的大小。然而，它的最大電流只能接受3A，因此我們選擇了一個能夠支援最大5A電流的恆壓恆流降壓電源模組。儘管沒有數值顯示，我們將安裝一個能夠偵測電池電壓的低電壓警報器，以確定目前電池的電壓是否正常。

####  Batteries(電池)
<div align="center" width=100%>
<table >
<tr>
  <th> 18650 lithium batteries(18650充電電池) </th> <th>Li-Polymer 3S Battery (鋰聚合物電池 3S)
  </th>
</tr>
<tr>
  <td>
  <img src="./img/4/18650.jpeg" width = "300"  alt="18650" /> </td>
  <td>
  <img src="./img/4/lipo_battery.png" width = "300" alt="lipo_battery"  />
  </td>
</tr>
</table>
</div>


#### Step-Down Module(降壓模組)
<div align="center" width=100%>
<table >
<tr align="center">
  <th> LM2596 DC-DC可調降壓模組 </th> 
  <th>5A恆壓恆流降壓電源模組 </th>
</tr>
<tr align="center">
  <td>  <img src="./img/4/LM25.jpeg" width = "250" height = "" alt="MG90S"/>  </td>
  <td><img src="./img/4/ADIO-DC36V5A.png" width = "300" height = "" alt="MG90S"/> 
  </td>
  </tr>
</table>
</div>

#### Low Voltage Alarm(低電壓警報器)
<div align="center" width=100%>
<table >
<tr align="center">
  <th> 低電壓警報器</th> 
</tr>
<tr align="center">
  <td>  <img src="./img/4/low_voltage_alarm.png" width = "150" alt="low_voltage_alarm"/>  </td>

  </tr>
</table>
</div>


## 2023/04/17 ~ 2023/04/23
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**  

 - The next step is the steering motor. After searching the information on the Internet, I found that MG90S and SG90 are commonly used. The difference between MG90S and SG90 is that the front gear is metal, and the latter is plastic. Because we often need to rotate all the time, we choose MG90S, which is not easy to damage  

- 接下來是操控馬達。在網上搜尋資料後，我發現MG90S和SG90是常見的選擇。MG90S和SG90之間的差異在於前齒輪，前者是金屬的，後者則是塑料的。由於我們常常需要持續旋轉，我們選擇了MG90S，因為它不容易損壞。 

#### Servo Motor(伺服馬達)
<div align="center">
<table>
<tr align="center">
<th rowspan="2">Model(型號)</th>
<th> MG90S</th>
<th >SG90</th>
</tr>
<tr align="center">
<td><img src="./img/4/MG90S.png" width = "150" height = "" alt="MG90S" align=center /></td>
<td > <img src="./img/4/SG90.png" width = "150" height = "" alt="SG90" align=center /></td>
</tr>
<tr align="center">
<td>rotation angle</td>
<td>90° MAX</td>
<td>0~90°/180° MAX</td>
</tr>
<tr align="center">
<td>torque</td>
<td>2.0kg/cm</td>
<td>1.4 kg/cm</td>
</tr>
<tr align="center">
<td>speed</td>
<td>0.11s</td>
<td>0.1S</td>
</tr>
</table>
</div>

## 2023/04/24 ~ 2023/04/30
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- When the vehicle is uncertain about the distance ahead, it cannot turn in time when encountering a wall. Therefore, ultrasonic sensors have been added to enable the vehicle to turn before colliding with the wall. 
- Based on the experiments conducted, it has been found that ultrasonic sensors can only detect obstacles in front of the vehicle. Additionally, they are less effective in detecting distances while the vehicle is swaying from side to side. Therefore, it has been decided to adopt a 360-degree LiDAR sensor for detecting distances in front of, as well as to the left and right sides of the vehicle.

- 車輛在不知道前方距離時，無法在遇到牆壁及時轉彎，因此加上了超音波，這樣就可以在撞到牆之前轉彎。 
- 經實驗得知，超音波只能偵測前方障礙物距離，且在車輛左右晃動下，不容易偵測距離，因此改採用可以360度偵測的光達感測器，來當車輛的前方、左右邊的距離。

#### Distance Sensor(距離感測器 )
<div align="center" width=100%>
<table >
<tr align="center">
  <th >ultrasound (超音波)</th> 
  <th>ydlidar x2(光達)</th>
</tr>
<tr>
  <td>  <img src="./img/4/ultrasound.png" width = "300"  alt="ultrasound" align=center />  </td>
  <td><img src="./img/4/Lidar_X2.jpg" width = "300"  alt="ydlidar x2" align=center />
  </td>
  </tr>
</table>
</div>




## 2023/05/01~ 2023/05/07  
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**  
- To begin assembling the machine, I used LEGO parts from the club to build the base. I attached the motors, Raspberry Pi, and other components onto the chassis and made the machine functional.
After the vehicle becomes operational, additional sensors are added to allow the vehicle to sense its surroundings and respond accordingly based on the mission requirements.
- While moving the robot, I noticed that using LEGO blocks for construction resulted in slower and sometimes stuck movements. Therefore, I switched to using a laser cutter to cut wooden boards. With the use of wooden boards, the overall weight of the robot decreased, leading to increased speed and improved energy efficiency. Additionally, I can adjust the size and position of the wooden components based on specific requirements. Unlike LEGO blocks, which come pre-built and often require continuous modifications to fit the robot's needs, wooden boards offer more flexibility and can be custom-designed using Onshape.


- 首先，我們需要組裝機器，所以我利用社團的樂高零件先組裝底座，並將馬達和樹梅派等裝上車，讓車輛能夠行駛。
隨後，在車輛可以行駛之後，我們進一步添加其他感測器，讓車輛能夠感測場地環境，並根據任務需求做出相應的反應。
- 在進行測試時，我們發現使用樂高積木的移動速度不快，而且轉彎時重量過重，無法順利轉彎。因此，我們改用雷切機切割木板，使車輛的重量減輕，速度也相應提高，同時還節省了電力。使用木板的好處是可以根據需要自行調整尺寸和位置，而不像樂高需要不斷改裝以適應各種情況。這可以通過 Onshape 等工具進行自由繪畫和調整。

<div align="center" width=100%>
<table >
<tr align="center">
  <th>木板  </th>
  <th>onshape 網站  </th>
  </tr>
<tr align="center">
  <td><img src="./img/5/wood.jpg" width = "300"  alt="wood" align=center />  </td>
  <td><img src="./img/5/onshape.png" width = "300"  alt="onshape" align=center />
  </td>
  </tr>
</table>
</div>


## 2023/05/08 ~ 2023/05/14  
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- Although it is possible to move straight and turn using the ultrasonic sensor, there is a risk of scraping against walls and getting stuck at corners. Therefore, we replaced the ultrasonic sensor with a lidar, which can detect the surroundings and maintain the robot in the center of the road. With the lidar, it can also detect turns ahead.  
- However, during the actual testing of the YDLIDAR X4 and DLIDAR X2, we also encountered the issue of missing angles (as shown in the attached image). Therefore, in this competition, we decided to use the D100 sensor for vehicle detection and measuring the distance to the side walls. The results obtained from the D100 sensor met our expectations and requirements.

- 雖然可以直行和利用超音波轉彎，但是有可能轉彎時擦到牆壁，然後卡牆邊無法繼續運行，之後我們將超音波改成了光達，光達可以偵測四周，因此可以維持在道路中央，還可以偵測前方轉彎。
- 然而我們在實測光達時也發現了ydlidar x4、dlidar x2 所遇之缺角問題(如附圖所示)因此，在本次競賽中，我們決定採用D100感測器來進行車輛偵測場邊牆距離，並且使用的結果符合預期的需求。

<div align="center" width=100%>
<table >
<tr align="center" >
  <th>ydlidar x4</th> 
  <th>ydlidar x2</th>
  <th>lidar 100</th>
</tr>
<tr align="center">
  <td><img src="./img/7/Lidar_X4.jpg" width = "300"  alt="ydlidar x4" align=center />  </td>
  <td><img src="./img/4/Lidar_X2.jpg" width = "300" height = "" alt="ydlidar x2" align=center />  </td>
  <td><img src="./img/7/Lidar-D100.png" width = "300"  alt="ydlidar x4" align=center /> </td>
</tr>
</table>
</div>

<div align="center" width=100%>
<table >
<tr align="center">
  <th colspan="2">ydlidar x4、X2 距離呈像</th> 
  <th >lidar 100 距離呈像</th>
</tr>
<tr align="center">
  <td>  <img src="./img/7/Lidar_X2_X4_error1.jpg" width = "400" height = "" alt="偵測缺角" align=center />  </td>
  <td><img src="./img/7/Lidar_X2_X4_error.jpg" width = "400" height = "" alt="偵測缺角" align=center />  </td>
  <td> <img src="./img/7/d100.png" width = "400" height = "" alt="D100" align=center />  
  </td>
  </tr>
</table>
</div>


## 2023/05/15 ~ 2023/05/21  
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**  
- TCS34725 color sensor 
  - In the competition, vehicles need to demonstrate more functionalities than just turning. To achieve clockwise and counterclockwise turns, we must equip the vehicle with a color sensor to detect the colors of the lines on the ground and make appropriate judgments accordingly. Therefore, we must be particularly cautious in selecting the color sensor.
  - The TCS34725 color sensor has been chosen because it meets all the requirements of this competition. Firstly, it possesses outstanding sensing capabilities, allowing it to quickly and accurately identify the colors of the ground lines.Secondly, the sensor is thin and compact, enabling it to be placed close to the ground without interfering with the vehicle's movements.
  - The high precision of this sensor ensures that the vehicle can accurately recognize the colors of the ground lines and execute clockwise or counterclockwise turns as needed. 
  
   This is a crucial factor in the vehicle's excellent performance and victory in the competition.In conclusion, the TCS34725 color sensor is a perfect fit for the requirements of this competition.Its slim design and highly accurate color recognition capabilities enable the vehicle to adapt flexibly to changes in ground lines, achieve clockwise and counterclockwise turns, and enhance its performance in the competition. 
  
   I encountered a bottleneck when using the color sensor to detect lines because I was unsure how to write a Python program to detect the values of blue and orange lines. 
  With the guidance of my teacher, I successfully completed it. The partial code is as follows:

- During the implementation testing, it was discovered that we originally used a USB 180-degree adapter (as shown in the lower left image), but it was prone to colliding with obstacles, particularly building blocks. As a result, we made a change and switched to using a USB 3.0 90-degree adapter for the connection. This modification makes it less likely to accidentally hit obstacles when trying to avoid them.

- TCS34725 顏色感測器 
  - 車輛在競賽中需要展現更多功能，而僅僅懂得轉彎是不夠的。為了實現順時針和逆時針的轉彎，我們必須裝備車輛以感測地上線的顏色，並相應地做出適當的判斷。因此，我們在挑選顏色感測器時，要特別謹慎。
  - TCS34725 顏色感測器被選中是因為它滿足了此次競賽的所有要求。首先，它具有出色的感測功能，可以快速而準確地辨識地面線條的顏色。其次，這款感測器相當薄且小巧，這意味著它可以輕鬆貼近地面，不會對車輛的運行造成任何干擾。
  - 該感測器的高度精確度確保了車輛可以準確識別地面線條的顏色，並且根據需要執行順時針或逆時針的轉彎動作。這是車輛在競賽中表現出色並獲得優勝的關鍵因素之一。
  
   綜上所述，TCS34725 顏色感測器是一款完美符合本次競賽要求的感測器。它的薄型設計和高度精確的顏色識別功能使車輛能夠靈活適應地面線條的變化，實現順時針和逆時針的轉彎，從而提升了車輛在競賽中的表現。

   在使用顏色感測器偵測線時遇到瓶頸，因為不知道如何使用python撰寫程式來偵測藍、橘線的數值，經過老師指導，成功完成，片段程式如下。
- 在實作測試時發現，本來我們是使用usb 180度轉接頭(如左下圖)，但容易撞到積木，因此我們改成使用 usb3.0 90 度轉接頭來連接，就不容易避開障礙物時碰到障礙物。
 

<div align="center" width=100%>
<table >
<tr align="center">
  <th>Snippet of Code</th> 
  <th>Function</th>
</tr>
<tr align="center">
  <td><img src="./img/5/TCS34725_code.png" alt="TCS34725" width=500/ > </td>
  <td><img src="./img/5/TCS34725_code_class.png" alt="TCS34725" width=500 />
  </td>  
  </tr>
</table>
</div>

<div align="center" width=100%>
<table >
<tr align="center">
  <th>USB Horizontal 180°</th> 
  <th>USB Vertical 90°</th>
</tr>
<tr align="center">
  <td align="center"><img src="./img/5/180.jpg" alt="USB180" width=400/></td> 
  <td align="center"><img src="./img/5/90.jpg" alt="USB90" width=400/></td>
</tr>
</table>
</div>

<div align="center" width=100%>
<table >
<tr align="center">
  <th >Event Photo</th> 
  <th >Event Photo</th> 
</tr>
<tr>
  <td align="center"><img src="./img/4/site.jpg" width=300 alt="site" /</td> 
  <td align="center"><img src="./img/4/work_photo_2_1_0417.jpg" width=300 alt="work_photo_2_1_0417" /></td>
</tr>
</table>
</div>

## 2023/05/22 ~ 2023/05/28  
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**  

- In order to enable the vehicle to avoid obstacles accurately, we need to install a camera module on the vehicle. Since we are using a Raspberry Pi as the controller, we need to find a compatible camera module for it. To do this, we referred to the camera module used by the American team in last year's competition and compared it with other camera modules in the same series. Here is the product information:

1. raspberry pi camera Rev 1.3(Sensor:OmniVision OV5647)
2. raspberry pi camera Module V2(Sensor:Sony IMX219)
3. raspberry pi camera Module V3(Sensor:Sony IMX708)

- Considering that V3 is not compatible with our existing Raspberry Pi operating system, we decided not to use that version. Additionally, the detection rate of version 1.3 is only 30p, whereas the V2 version can reach a maximum of 90p. Therefore, we ultimately chose the Raspberry Pi Camera Module V2 for our project. Through experimentation, we found that the V2 version has the best recognition performance.

### Camera Module
#### Camera Module
<div align="center">
<table>
<tr  align="center">
<th rowspan="2">Model(型號)</td> 
<th>raspberry pi camera Rev 1.3</th>
<th >raspberry pi camera Module V2</th>
<th >raspberry pi camera Module V3</th>
</tr>
<tr  align="center">
<td ><img src="./img/5/V1.jpeg" width=200 alt="V1"  /></td>
<td ><img src="./img/5/V2.jpeg" width=200 alt="V2" ></td>
<td ><img src="./img/5/V3.jpeg" width=200 alt="V3" /></td>
</tr>
<tr  align="center">
<td>sensor</td>
<td>Omnivision OV547</td>
<td >Sony IMX 219</td>
<td>Sony IMX 708</td>
</tr>
<tr  align="center">
<td>sensor resolution</td>
<td >2592 * 1944 pix</td>
<td>3280 * 2464 pix</td>
<td>4608 * 2592 pix</td>
</tr>
<tr  align="center">  
<td>FPS Frame rate</td>
<td >30p MAX</td>
<td>90p MAX</td>
<td>120p MAX</td>
</tr>
</table>
</div>

During subsequent testing, we discovered that the vehicle was unable to predict the position of the next block while avoiding obstacles. This posed a challenge to the vehicle's obstacle avoidance strategy. Consequently, we decided to modify the original camera by converting it into a wide-angle lens. In comparison to the original 72-degree field of view, the wide-angle lens offers a 160-degree field of view, enabling us to anticipate the next block's position in advance. This enhancement has significantly improved the vehicle's obstacle avoidance effectiveness.

#### wide-angle lens
<div align="center">
<table>
<tr>
<th align="center"> Without the wide-angle lens </th> 
<th align="center">With the wide-angle lens </th>
</tr>
<tr>
<td align="center"><img src="./img/5/V2.jpeg" width=200 alt="common" ></td><td>
<img src="./img/5/V2_wide_angle.jpeg" width=200 alt="wide angle" >
</td>
</tr>
<td align="center"><img src="./img/5/72angle.png" width=200 alt="common view" ></td>
<td align="center"> <img src="./img/5/160angle.png" width=200 alt="wide angle view" ></td>
</tr>
</table>
</div>

- In the Raspberry Pi program, it is possible to configure the resolution of the camera module. We conducted experiments with the following common resolutions.

  1. 1080x640 Frame rate30p
  
  2. 640x320 Frame rate60p
 
  3. 320x240 Frame rate90p
- In our experiments, we found that when the camera module's resolution was set to 1080x640, the high-resolution image processing demands led to a significant amount of time being spent on block recognition, resulting in a decrease in computational efficiency. On the other hand, when the resolution was set to 320x240, the computational efficiency was extremely high, but the low resolution hindered the proper recognition of the blocks. However, when we set the resolution to 640x320, we observed that the program could successfully recognize the blocks without compromising computational efficiency, thus avoiding collisions with the blocks. Therefore, we ultimately decided to set the camera module's resolution to 640x320.

## 2023/05/29 ~ 2023/06/04  
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- By using VS Code along with Git to edit our technical documentation, we can effectively manage potential conflicts and improve collaboration. The advantages of this approach include easy version control, immediate notifications to editors when conflicts arise due to simultaneous edits, and the ability for editors who upload data later to merge conflicts by comparing the data. This way, we can ensure a smoother and more efficient process when working on the technical documentation.

[github Homepage : https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/tree/main](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/tree/main)

<div align="center">
<table>
<tr align="center">
<th> To edit in VS Code, just click on the source file control and then press "Copy to Repository
</th> 
<th>Entering the URL allows you to perform editing and version control in VS Code
</th>
</tr>
<tr>
<td align="center"><img src="./img/5/clone.png" width = "300" alt="clone" align=center /></td><td>
<img src="./img/5/web.png" width = "300"  alt="WEB" align=center />
</td>
</tr>
</table>
</div>


## 2023/06/05 ~ 2023/06/11 
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- During the hardware design process, we encountered a few instances in which the Raspberry Pi controller or IC was damaged due to incorrect power or data cable connections. To prevent such issues, we implemented a solution that involves using male-female connectors for both power supply and data transmission. This approach ensured proper wiring and effectively mitigated the risk of the Raspberry Pi or IC becoming damaged. These design improvements have enhanced the stability of the hardware system, leading to increased overall product reliability and lifespan.
- During the hardware design process, we initially used a breadboard to connect the circuits. Unfortunately, we encountered instances of burning or poor contacts, resulting in abnormal functionality or potential issues that were challenging to detect. To improve this situation, we made the decision to switch to soldering the circuits onto a prototyping board. This change significantly reduced the risks of burning or poor contacts while ensuring stable and reliable connections. Through this improvement, we successfully enhanced the overall hardware system's reliability and ensured proper functionality.

<div align="center">
<table>
<tr  align="center">
<th> <img src="./img/6/anit_daze.png" alt="插座" width="350"></th> 
<th><img src="./img/6/anit_daze_2.jpg" alt="電木板" width="350"></th>
</tr>
</table>
</div>

## 2023/06/12 ~ 2023/06/18
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- Before dodging the blocks, we need to complete the basic task of circling the track three times. During this circling process, we noticed the possibility of the vehicle rubbing against the walls while turning. To address this, we utilize the 360-degree detection capability of LiDAR to keep the vehicle centered on the track. By subtracting the distances on the left and right sides, we obtain an error value, which is then corrected using the servo motor to ensure the vehicle continues to travel along the center of the track.

<div align="center">
<table>
<tr  align="center">
<th>The vehicle collides with the side wall.
</th> 
<th>Detecting the distance to the left and right walls.
</th>
</tr>
<tr align="center">
<td><img src="./img/5/hit_wall.jpeg" width = "300"  alt="hit wall"  /></td>
<td><img src="./img/5/LIDAR_readings.png" width = "200"  alt="Distance to wall."/></td>
</tr>
</table>
</div>


## 2023/06/19 ~ 2023/06/25   
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- The robot is now able to operate successfully. The next step involves using the camera to avoid obstacles (blocks). Next, we need to detect the distance to the obstacles (blocks) and then identify the color of the blocks. By utilizing the features of OpenCV, we can calculate the distance between the blocks and the robot for obstacle avoidance. Through the implementation of an algorithm, we can control the front wheels to steer around these obstacles.
- However, there is an issue at the corners where the robot cannot avoid obstacles in a timely manner. To address this, we need to combine the gyroscope's readings with the output values from the algorithm to successfully navigate around corners.

<div align="center">
<table>
<tr align="center">
<th> Detecting block distance
</th> 
<th> Hitting a block
</th>
</tr>
<tr align="center">
<td><img src="./img/6/sign.png" width=250 alt="block distance" ></td>
<td><img src="./img/5/hit_block.jpg" width=300 alt="hit block" >
</td>
</table>
</div>


## 2023/06/26 ~ 2023/07/02 
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- During today's testing, we discovered that the robot tends to misinterpret people wearing red or green clothing in its surroundings as obstacles. This misinterpretation leads it to avoid these individuals unnecessarily, which could potentially result in missing the opportunity to timely avoid the next block. To rectify this issue, we introduced an additional layer of black masking at the top of the camera's field of view. This measure effectively prevents the robot from detecting colors outside of the designated track area. With the implementation of this black masking, the robot will no longer register colors beyond the track area, thus minimizing the likelihood of interference.

<div align="center">
<table>
<tr align="center">
<th>Using a black mask to block colors from outside the field.
</th> 
</tr>
<tr align="center">
<td><img src="./img/6/black_hid.png" width="300" alt="cover"></td>
</table>
</div>

## 2023/07/03 ~ 2023/07/09 
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- This week, most of the programming has been completed, and we began testing the robot's success rate. We started with a speed of 50%, and due to its slower pace, the robot responded well for the most part. However, when accelerating to 70% speed, the color sensor occasionally misjudged the track's color due to its high speed. As a result, we modified the turning conditions to use the LiDAR's measurements of the left and right directions for determining the turning direction. This adjustment reduces the likelihood of turning in the wrong direction because of color misjudgment.

#### Detecting the direction of the turn
```
if get_left_dis > 100:
    reverse = False
else:
    reverse = True
if get_mid_dis > 55:
    servo.angle(-40)
```


## 2023/07/10 ~ 2023/07/16 
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- The robot is now capable of successfully avoiding obstacles and completing the third lap around the track. The next task is to detect blocks and perform a turnaround maneuver. The turnaround will be executed only if the last block of the second lap is red. Therefore, it is necessary to detect the number of laps. We will use the color sensor to count the number of times the line is crossed and determine whether the set count has been reached.

- If the specified count has not yet been achieved, the system will continue to record the color of the nearest traffic sign until the count of line crossings is greater than or equal to the set count. At this point, the color recording will cease.

- After recording the color of the nearest traffic sign, the program will determine whether the color is red. If the color is indeed red, the system will adjust the angle of the servo motor to initiate a right turn and will continue turning until the vehicle is properly aligned in the specified direction, thus executing a turnaround maneuver. If the detected color is not red, the vehicle will proceed to move forward.


<div align="center">
<table>
<tr align="center">
<th>Display the number of line crossings and the color of the nearest traffic sign.</th>
<th>Adjusting the values.
</th>
</tr>
<tr align="center">
<td><img src="./img/7/detect_last_obstacle.png" width="200" alt="print color"></td>
<td><img src="./img/7/check.jpeg" width="300" alt="check"></td>
</table>
</div>

## 2023/07/17 ~ 2023/07/23  
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- As the field mission has been roughly completed, we are going to start writing the technical report. Since we are not familiar with the correct technical report format, we have referred to the official website's technical report documentation and found that the report should include the following sections.

  1. modles: This folder should contain documentation related to the vehicle models, such as files for laser cutting machines and 3D printers.

  2. other: This folder is used to store data that does not belong to other categories, such as communication protocols and engineering logs.

  3. schemes: This folder is dedicated to hardware introductions, explaining the functions of electronic components and how they are connected.

  4. src: All programs should be placed in this folder.

  5. t-photos: This folder should contain team photos, including a group photo and funny pictures.

  6. v-photos: Machine photos from six different perspectives should be placed in this folder.

  7. video: Videos demonstrating the machine's operation should be placed in this folder, with each video lasting more than 30 seconds.

- When writing the technical report, we are switching between VS Code and the GitHub website. We use a desktop computer to view the GitHub web page and a laptop to edit the report in VS Code.

<div align="center">
<table>
<tr align="center">
<th>Official website's GitHub example</th> 
<th>Laptop and desktop comparison and modifications</th>
</tr>
<tr align="center">
<td><img src="./img/7/github_example.png" width="300" alt="github_example"></td>
<td><img src="./img/7/vs_code.jpeg" width="300" alt="更改文件"></td>
</table>
</div>

## 2023/07/24 ~ 2023/07/30  
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- We organized and listed the components in the parts inventory, and we uploaded them to the technical documentation.Additionally, we completed the drawing of the vehicle's introduction diagram. Throughout this process, we embarked on a learning journey, gradually familiarizing ourselves with GitHub syntax. Although we are not yet fully proficient in using GitHub, we dedicated time to researching relevant information online and steadily improving our skills. These achievements have brought valuable advancements to our report and project as a whole.
- Over the past few days, we have been continuously adjusting and fine-tuning the execution of the tasks at the venue, making constant adjustments to motor speed and various parameters, with the hope of effectively reducing the error rate. We are eager to achieve better performance and improve our overall competition results.
- During practical testing, we discovered that the vehicle was getting stuck at the junctions of the terrain due to protrusions, which was affecting its normal operation. To address this issue, we adopted a method of using a laser cutting machine to create 3mm thick spacers. These spacers were then placed under the vehicle chassis to elevate its height, enabling the vehicle to pass over the obstacles smoothly.

#### Overcoming Terrain Protrusions 

<div align="center">
<table>
<tr align="center">
<th> <img src="./img/7/Spacer1.png" alt="Spacer" width=300 /></th> 
<th><img src="./img/7/Spacer2.jpg" alt="Spacer" width=300 /></th>
<th><img src="./img/7/Spacer3.jpg" alt="Spacer"  width=300/></th>
</tr>
<tr align="center">
<td><img src="./img/7/Spacer4.jpg" alt="Spacer" width=300 /></td>
<td><img src="./img/7/Spacer5.jpg" alt="Spacer" width=300 /></td>
<td><img src="./img/7/Spacer6.jpg" alt="Spacer"  width=300/></td>
</table>
</div>

### Team Members' Practice Status

<div align="center">
<table>
<tr  align="center"> 
<th> <img src="./img/7/work_photo_2_1_0729.jpg" alt="work_photo_2_1_0729" width=300 /></th> 
<th><img src="./img/7/work_photo_2_2_0729.jpg" alt="work_photo_2_2_0729" width=300 /></th>
</tr>
<tr align="center">
<td><img src="./img/7/work_photo_1_1_0727.jpg" alt="work_photo_1_1_0727"  width=300/></td>
<td><img src="./img/7/work_photo_2_1_0727.jpg" alt="work_photo_2__0727" width=300 /></td>
</tr>
</table>
</div> 

## 2023/07/31 ~ 2023/08/06
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**  

- As the deadline for submitting the technical report is next week, we have begun revising the content of the technical documentation. We are also adjusting the website according to the official grading criteria and continuously adding to the technical report.
- Complete recording videos for each task and upload them to YouTube.


<table>
<tr align="center">
<th> old directory </th>
<th> Revised Directory (Upper Section) </th>
<th> Revised Directory (Lower Section) </th>
</tr>
<tr align="center">
<td><img src="./img/8/old_content.png" alt="old_content"  width="300"/> </td>
<td> <img src="./img/8/new1_content.png" alt="new1_content"  width="300"/></td>
<td> <img src="./img/8/new2_content.png" alt="new1_content"  width="300"/></td>
</tr>
</table>

  __Open Challenge__
  - [Open Challenge full narrow speed 70%](https://youtu.be/QtpuHt05MDg)
  - [Open Challenge full anrrow speed 50%](https://youtu.be/QaYUrrdAtE8)
  - [Open Challenge half width and half narrow speed 70%](https://youtu.be/pcTpH8QgJFU)
  - [Open Challenge half width and half narrow speed 50%](https://youtu.be/7HdWxfWPfWc)
  - [Open Challenge all width speed 70%](https://youtu.be/MA1k2P87LdE)
  - [Open Challenge all Width speed 50%](https://youtu.be/OUg0x4Qdc0c)  

 __Open Challenge__
  - [Obstacle Challenge speed 50% ](https://youtu.be/Jo7555gfXG8)
  - [Obstacle Challenge speed 70% ](https://youtu.be/iCmcXbACizY)

__Team Members' Practice Status__

<div align="center">
<table>
<tr align="center">
<th>report writing</th> 
<th>mechanism adjustment</th>
<th>report writing</th>
<th>field mission practice</th>
</tr>
<tr align="center">
<td><img src="./img/8/work_photo_1_0805.jpg" width="500" alt="work_daily"></td>
<td><img src="./img/8/work_photo_2_0805.jpg" width="500" alt="work_daily"></td>
<td><img src="./img/8/work_photo_3_0805.jpg" width="500" alt="work_daily"></td>
<td><img src="./img/8/work_photo_4_0805.jpg" width="500" alt="work_daily"></td>
</table>
</div>

## 2023/08/07 ~ 2023/08/13
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- This week, with our machine now adjusted to smoothly complete the mission race on the field, we have begun filming an introductory video for the race. In the video, we will showcase the actions our vehicle performs during the mission race, providing explanations through subtitles synchronized with the video.


<div align="center">
<table>
<tr align="center">
<th>modifying code and testing vehicles</th>
<th>currently editing videos</th>
</tr><tr align="center">
<td><img src="./img/8/work_photo_1_0813.jpg" width="300" alt="work_daily"></td>
<td><img src="./img/8/813.jpg" width="300" alt="work_daily"></td>
</tr><tr align="center">
</table>

<table>
<th>mission race introduction video</th>
</tr>
<td>

[![video](https://res.cloudinary.com/marcomontalbano/image/upload/v1691907166/video_to_markdown/images/youtube--VrU3wQa6h5M-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/VrU3wQa6h5M "video")</td>
</table>
</div>



## 2023/08/14 ~ 2023/08/20
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- As the competition is scheduled for this week, we have intensified our practice efforts, trying out various scenarios and adjusting our program to adapt to a wide range of situations. Experimenting with different scenarios has the advantage of helping us anticipate challenges that our machine might face and making necessary adjustments in advance. Here's our practice approach:

- We have assigned lane labels A, B, C, and D. Each lane is divided into three sections, with placement points for blocks both on the inner and outer sides in each section. Red blocks indicating turning conditions will be placed sequentially, while the positions of other blocks will be randomized.
- The record sheet will include the following information:
  1. Completion time
  2. Number of successful attempts/number of failed attempts
We believe that this approach will assist our machine in preparing for a variety of scenarios, ensuring that we are well-prepared for the competition.

- Today is 8/19, our match day. In the first half of the qualifying round, due to our Request for Maintenance during the initial round, the score was reduced by 50%, resulting in our obtaining 15 points. In the second round, we successfully completed it and achieved a full score of 30 points, allowing us to advance to the second half of the obstacle course. During the first obstacle race, our robot hit the wall and stopped due to excessive avoidance; fortunately, after adjustments, the second attempt by our team resulted in a perfect score. This marked a successful conclusion to today's competition.


<div align="center">
<table>
<tr align="center">
<th>field layout</th>
<th>record sheet</th> 
</tr>
<tr align="center">
<td><img src="./img/8/block.png" width="400" alt="work_daily"></td>
<td><img src="./img/8/grade.png" width="500" alt="work_daily"></td>
</table>
</div>
<div align="center">
<table>
<tr align="center">
<th>competition photos</th>
<th>award-winning photo</th> 
</tr>
<tr align="center">
<td><img src="./img/8/0819_1.jpg" width="600" alt="contest"></td>
<td><img src="./img/8/0819_2.jpg" width="600" alt="award-winning photo"></td>
</table>
</div>

## 2023/08/21 ~ 2023/08/27
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

As we have confirmed our participation in the international competition, we are undergoing significant modifications to our vehicle. We are transitioning from the use of wooden boards to a 3D-printed chassis for a more integrated structure, optimizing the space available. Moreover, this redesign will allow us to incorporate threaded components for added stability. Additionally, we are upgrading the controller from Raspberry Pi 4B to the higher computing power provided by the Jetson Nano microcomputer. The Jetson Nano supports programming in Python, thus most of our existing code does not need significant modifications. However, one notable difference with the Jetson Nano is that the generation of PWM signals requires an external board for implementation.



<div align="center">
<table>
<tr align="center">
<td rowspan="2">Controller</td>
<td>Jetson Nano</td>
<td>Raspberry Pi 4B</td>
<tr align="center">
<td><img src="./img/8/jeston_nano.png" width="200" alt="work_daily"></td>
<td><img src="./img/8/raspberry_pi_4.png" width="200" alt="work_daily"></td>
</tr>
<tr align="center">
<td>Computational efficiency</td>
<td>472 GFLOPs</td>
<td>13.5 GFLOPs</td>
</table>
</div>

<small>Data source</small>  
<small>[Taiwansersor](https://www.taiwansensor.com.tw/product/nvidia-jetson-nano-developer-kit-%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E9%96%8B%E7%99%BC%E5%A5%97%E4%BB%B6-ai-%E9%96%8B%E7%99%BC%E5%A5%97%E4%BB%B6/)</small>  
<small>[University of Maine System](https://web.eece.maine.edu/~vweaver/group/green_machines.html)</small>

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
