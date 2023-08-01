![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
# <div align="center">Motor</div> 
## Front Steering Mechanism Driven by Servo Motor(前轉向機構驅動伺服馬達)
-在選擇伺服馬達以市售常見直流馬逹為目標，並考慮其重量、轉向角度、轉矩等因素，找到以下二種符合條件之直流馬達。


## Rear-Drive DC Motor(後驅直流馬達)
- 在選擇直流馬達時以市售常見直流馬逹為目標，並考慮其重量、轉速、轉矩等因素，找到以下三種符合條件之直流馬達。
- 這三種馬達雖型號不相同，但外型相同，其差異如下表。

| 型號 |JGA25 370 |JGA25 370|JGA25 371|
|:---:|:---:|:---:|:---:|
|轉速|136rpm/m|620rpm/m|294rpm/m|
|扭距||||
|功率||||

## 馬達驅動器


Motor(速度、扭距、功率)
GA25-370 DC reduction motor
servo motor


- When selecting the motor, we considered the weight of the vehicle and the need for a motor with greater torque. There were two options available: the JGA16-050, which is lighter and smaller in size, and the GA25-370, which is larger, heavier, but provides stronger torque.
- 在選擇馬達時，考慮到車輛的重量，我們需要具有較大扭力的直流減速馬達。有兩種可供選擇，一種是較輕、體積較小的JGA16-050，另一種是體積較大、重量較重但扭力更強的GA25-370。


||  <img src="./img/JGA16-050.png" width = "150" height = "" alt="little motor" align=center /> | <img src="./img/Motor.png" width = "150" height = "" alt="motor" align=center /> |
| :---: | :---: |:---:|
| 名稱: | JGA16-050 | GA25-370 |
| 空載轉速(rpm): | 340±10% | 310±12% |
| 負載扭矩(kg.cm): | 0.65 | 1.5 |
| 負載功率(w): | 0.54 | 0.75 |

- After comparing the two, we found that their speeds were similar, but the GA25-370 had significantly higher torque and load capacity than the JGA16-050. Considering the vehicle's substantial weight, we needed a motor with ample torque, so we chose the GA25-370 as the driving motor.
- 經過比較，我們發現兩者在速度上差異不大，但扭力和負載功率方面GA25-370明顯優於JGA16-050。考慮到機器的重量較大，需要馬達具有足夠的扭力，因此我們選擇了GA25-370作為驅動馬達。






- 在等待初始化樹梅派及安裝函式庫時，挑選作為動力的馬達，有兩種，分別是 GA25-370 和 JGA16-050，前者的優點是扭力大，可以帶動較重的物體，後者的優點是體積小，重量也比較輕，但是扭力相對較小，由於考慮到機體可能會比較重，所以選了扭力較大的 GA25-370   
- 在測試馬達的作動方式時，單純的提供正負極並沒有辦法很好的控制GA25-370的作動，無法調節速度，因此還需要馬達控制器來調節直流減速馬達的速度，有兩種選擇：L293D晶片和L298N模組。為了減輕重量，我們選擇了體積較小的L293D晶片。它的小巧尺寸使我們能夠安裝更多的感應器，進而節省空間、減輕重量，並增加機器人的機動性。


| GA25-370 | JGA16-050 |
| :---: | :---: |
|  <img src="./img/3/Motor.png" width = "150" height = "" alt="motor" align=center /> | <img src="./img/3/JGA16-050.png" width = "150" height = "" alt="little motor" align=center /> |

| L293D | L298N |
| :---: | :---: |
|  <img src="./img/4/l293d.png" width = "150" height = "" alt="l293d" align=center /> | <img src="./img/4/L298N.png" width = "150" height = "" alt="l298n" align=center /> |
# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
