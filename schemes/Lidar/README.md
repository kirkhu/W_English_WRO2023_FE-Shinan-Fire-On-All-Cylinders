![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
=====
# <div align="center">Lidar introduce(光達介紹)</div> 
## English
- Lidar, also known as Light Detection and Ranging, is a technology that uses laser pulses to measure distances and create maps. Lidar systems typically consist of lasers, receivers, computing devices, and navigation systems.

    __Working principle:__
  - Emitting laser pulses: Lidar emits very short laser pulses through a laser. These pulses propagate at extremely high speeds and then return after reflection.  
  - Receiving reflected signals: The receiver of the Lidar records the time it takes for the laser pulses to return and measures the intensity of the light pulses. The time and intensity information of the reflections can be used to calculate the distance and characteristics of objects from the Lidar.  
  - Data processing: The computing device of the Lidar processes the received reflection data and calculates the position, shape, and movement of objects based on the measured time and the speed of light.

  __Applications:__  
- Lidar has widespread applications in various fields, including but not limited to:  
  - Autonomous vehicles: Lidar is widely used in autonomous vehicles to help them perceive their surroundings, detect obstacles, and other vehicles.  
  - Environmental sensing: Lidar is used to create 3D maps and models for urban planning, land surveying, and building modeling.  
  - Drones and aviation: Lidar is employed in unmanned aerial vehicles (drones) and aviation for tasks such as terrain mapping and surface feature detection.  
  - Environmental monitoring: Lidar is used for environmental monitoring, such as atmospheric pollution monitoring and climate research.  
  - Military applications: Lidar finds applications in the military sector, such as target identification, ranging, and terrain reconnaissance.  

Due to its ability to provide high-precision and high-resolution data, Lidar is widely adopted in many fields, and its applications continue to expand with technological advancements.  
<br>
The Lidar D100 Developer Kit is composed of the Lidar LD14 as its core, accompanied by a combination of related accessories.
<br>
This system adopts triangulation-based distance measurement technology and utilizes high-performance photosensitive CCD (Charge-Coupled Device) that complies with FDA Class human eye safety standards.  

- Specifications
  - Detection Range: 360 degrees
  - Detection Distance: 0.15 ~ 8 meters
  - Angular Resolution: 1 degree
  - Detection Frequency: 2300 Hz
  - Scanning Frequency: 6 Hz
  - Dimensions: Approximately 96.3 * 59.8 * 38.8 mm
- The difference between ultrasonic sensors and Lidar:  
Ultrasonic sensors can only detect in one direction, limited to the front, used for distance measurement and obstacle detection. Lidar, on the other hand, provides a 360-degree panoramic coverage, enabling simultaneous sensing of surroundings, used for high-precision environmental perception and map creation, reducing collision risks. It is widely applied in autonomous driving, environmental modeling, etc. Lidar surpasses ultrasonic sensors in providing comprehensive environmental information, making it superior in robot navigation.  

- Issues encountered with different brands of Lidar:  
One problem with the D100 Lidar is its detection frequency, which is 2300 Hz, compared to the YDLidar X2 with 3000 Hz and X4 with 5000 Hz. The lower frequency results in a slower response time.  

__Due to unfamiliarity with the usage of ydlidar x4 and ydlidar x2, there were issues with detecting obstacles, leading to missing angles. Therefore, in this competition, we decided to utilize the D100 sensor for vehicle detection and measuring the distance to the arena walls. The results obtained using this sensor met our expectations.__

## 中文
- Lidar
光達，也被稱為激光雷達（Lidar，Light Detection and Ranging的縮寫），是一種使用激光脈衝來測量距離和創建地圖的技術。激光雷達系統通常由激光器、接收器、計算設備和導航系統組成。

    工作原理：  
    - 發射激光脈衝：激光雷達通過激光器發射非常短的激光脈衝。這些脈衝會以極高的速度傳播，然後反射回來。  
    - 接收反射信號：激光雷達的接收器會記錄激光脈衝反射回來所需的時間，並測量光脈衝的強度。反射的時間和強度信息可以用來計算物體與激光雷達的距離和特徵。  
    - 數據處理：激光雷達的計算設備會處理接收到的反射數據，並根據測量的時間和光的速度計算出物體的位置、形狀和運動。       
    應用領域：
    - 激光雷達在多個領域都有廣泛的應用，包括但不限於：  
      - 自動駕駛汽車：激光雷達被廣泛用於自動駕駛汽車中，幫助車輛感知周圍環境，檢測障礙物和其他車輛。  
      - 環境感知：激光雷達可用於創建三維地圖和模型，用於城市規劃、土地測量、建築物模型等。  
      - 無人機和航空：激光雷達被用於無人機和航空領域，用於地形測繪、地表特徵檢測等任務。  
      - 環境監測：激光雷達可用於環境監測，如大氣污染監測、氣候研究等。  
      - 軍事應用：激光雷達在軍事領域也有應用，例如用於目標識別、測距和地形探測。  
     由於激光雷達能夠提供高精度、高分辨率的數據，因此在許多領域都被廣泛採用，而隨著技術的發展，其應用領域還在不斷擴展。

     Lidar D100 開發者套裝是以光達 LiDAR LD14為核心再搭配相關零配件組合而成。  
採用三角測距技術、高性能感光CCD
符合FDA Class 人眼安全等級

- 規格:  
    - 偵測範圍: 360度  
    - 偵測距離: 0.15 ~ 8 m  
    - 角度分辨率: 1 度  
    - 偵測頻率: 2300 HZ  
    - 掃描頻率: 6 HZ  
    - 尺寸: 約96.3* 59.8*38.8 mm  

- 超音波與光達之異差  
超音波感測器只能單向偵測，限於前方，用於距離測量與障礙物檢測。光達則具備360度全方位覆蓋範圍，可同時感測四周，用於高精度環境感知和地圖製作，減少碰撞風險，並廣泛應用於自動駕駛、環境建模等領域。光達優於超音波在提供完整環境資訊方面，使其在機器人導航中更為優勢。

- 不同品牌光達遇到的問題  
    D100偵測頻率是2300，相比 ydlidar x2 的 3000HZ 和 x4 的 5000HZ，頻率更小，因此反應會慢一點。  

__由於對ydlidar x4和ydlidar x2的使用不熟悉，導致在偵測障礙物時出現了缺角問題。因此，在本次競賽中，我們決定採用D100感測器來進行車輛偵測場邊牆距離，並且使用的結果符合預期的需求。__

- #### The types of LiDAR used in the actual testing.(實測之光達種類)
|  lidar D100    |  ydlidar x4  |   ydlidar x2    |      
| :----: | :----: | :----:|
|<img src="../Assembly_Instructions/img/Lidar-D100.png" width = "250" height = "" alt="lidar D100  " align=center />|<img src="./img/Lidar_X2.jpg" width = "250" height = "" alt=" ydlidar x4" align=center />|<img src="./img/Lidar_X4.jpg" width = "250" height = "" alt="ydlidar x2" align=center />|

- #### The issues encountered with missing angles during the actual testing of ydlidar x4 and ydlidar x2 LiDAR.<br>(實測光達ydlidar x4、dlidar x2 所遇之缺角問題)

<div align="center">
<img src="./img/Lidar_X2_X4_error1.jpg" width = "400" height = "" alt="偵測缺角" align=center /> <img src="./img/Lidar_X2_X4_error.jpg" width = "400" height = "" alt="偵測缺角" align=center />|

</div> 

<small>資料來源:[飆機器人](https://shop.playrobot.com/products/lidar-d100-ld14)</small>



# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
