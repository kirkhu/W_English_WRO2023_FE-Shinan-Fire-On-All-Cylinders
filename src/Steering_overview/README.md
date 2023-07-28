![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
# <div align="center">Steering overview 轉向概述</div> 

## ydlidar Steering
- 進行牆壁轉向。首先讀取光達兩側其中一邊是否有>100公分，如果右邊光達讀取到的距離是超過100公分代表是順時針行駛，否則是逆時針行駛。
- 判斷完行駛方向後，會讀取光達前方距離牆壁幾公分，當光達與牆壁距離小於55公分，會執行轉彎動作。
- 程式:  
```
if get_left_dis > 100:
    reverse = False
else:
    reverse = True
if get_mid_dis > 55:
    servo.angle(-40)
```


## Pillar Steering
- 使用過濾後的紅色綠色圖像，獲得圖像在畫面中的X、Y座標與面積。  
- 我們將透過以下步驟來完成交通標誌的閃避：  
  1.用Y座標判斷哪一個積木的Y座標較大，Y座標較大的代表距離較近。  
  2.判斷較近的的交通標誌顏色，並取得其X座標。  
  3.將較近的交通標誌的X座標減去我們所欲閃避的座標再乘上閃避係數計算出誤差值。  
  4.設定伺服馬達轉向角度，使其轉向誤差值的方向，完成交通標誌閃避。
  |辨識距離較近的障礙物|障礙物的XY座標|
  |:---:|:---:|
  |<div align="center"> <img src="./img/Detecting_nearby_obstacles.png" width="400" alt="Detecting_nearby_obstacles"></div>|<div align="center"> <img src="./img/Obstacle_XY_coordinates.png" width="250" alt="Obstacle_XY_coordinates"></div>|

  

## slalom Steering
- 我們會使用顏色感測器來偵測經過的線條次數，並判斷是否超過了設定的次數。
- 如果未達到指定次數，系統將會持續紀錄距離最近的交通標誌顏色，直到經過的線條次數大於或等於設定次數，此時將不再紀錄顏色。
- 紀錄完最近的交通標誌顏色後，程式將判斷最近的交通標誌顏色是否為紅色。若標誌顏色為紅色，系統將設定伺服馬達角度為右轉角度，持續轉動直到車輛轉向指定的方向。若最近的交通標誌顏色不是紅色，則車輛會繼續向前行駛。

|顯示線條次數與最近的交通標誌顏色|
|:---:|
|<div align="center"> <img src="./img/detect_last_obstacle.png" width="300" alt="Obstacle_XY_coordinates"></div>|

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  


