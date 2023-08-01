![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
# <div align="center">Motor(馬達)</div> 
### Front Steering Mechanism Driven by Servo Motor(前轉向機構驅動伺服馬達)
#### 英文
- To select a servo motor among commonly available options in the market, considering factors such as weight, rotation angle, and torque, we have identified two suitable servo motors: MG90S and SG90.
- The main difference between MG90S and SG90 lies in their front gears. The former has metal gears, while the latter has plastic gears. Since continuous rotation is often required, we opted for the MG90S due to its durability and resistance to damage.

#### 中文
- 在選擇伺服馬達以市售常見伺服馬達為目標，並考慮其重量、轉向角度、轉矩等因素，找到MG90S和SG90這二種符合條件之伺服馬達。
- MG90S和SG90之間的差異在於前齒輪，前者是金屬的，後者則是塑料的。由於我們常常需要持續旋轉，我們選擇了MG90S，因為它不容易損壞。 

| Model(型號)| MG90S | SG90 |
| :---: | :---: | :---: |
|  |<img src="./img/MG90S.png" width = "150" height = "" alt="MG90S" align=center /> | <img src="./img/SG90.png" width = "150" height = "" alt="SG90" align=center /> |
|
rotation angle(轉動角度)|90° MAX | 0~90°/180° MAX 
|torque(轉矩)|2.0kg/cm|1.4 kg/cm|
|speed(轉速)|0.11s|0.1S|

### Rear-Drive DC Motor(後驅直流馬達)
#### 英文
- When selecting a DC motor among commonly available options in the market, considering factors such as weight, rotational speed, and torque, we have identified the following four suitable DC motors。
- Among them, the three types of motors, JGA25, have different model numbers but share a similar physical appearance, and their differences are as follows.
- After conducting experimental research, we found that choosing the high-speed 1630rpm JGA-370 motor resulted in lower torque, making it difficult for the vehicle to move effectively. On the other hand, opting for the high-torque JGA-371 motor led to an excessively low rotational speed, which did not meet the requirements for the vehicle's operation.
- Therefore, based on these findings, we ultimately selected the 620rpm JGA-370 motor as the rear-wheel drive DC motor for the vehicle. This choice strikes a balance between rotational speed and torque, providing the necessary performance for the vehicle's propulsion.

#### 中文
- 在選擇直流馬達時以市售常見直流馬逹為目標，並考慮其重量、轉速、轉矩等因素，找到以下四種符合條件之直流馬達。
- 其中JGA25系統等三種馬達雖型號不相同，但外型相同，其差異如下。
- 經過實驗研究後，我們發現選擇轉速快的1630rpm JGA-370馬達會產生較低的扭距，使車輛行動困難。而若選擇扭距較高的JGA-371馬達，轉速則會過低，不符合車輛行駛所需。因此，我們最終選擇了轉速為620rpm的JGA-370馬達作為車輛的後驅直流馬達。

|Model(型號) |JGA25 370 |JGA25 370|JGA25 371|JGA16-050|
|:---:|:---:|:---:|:---:|:---:|
| |<img src="./img/JGA25-370_1360RPM.JPG" width = "150" alt="JGA25-370_1360RPM" /> |<img src="./img/JGA25-370_620RPM.JPG" width = "150" alt="JGA25-370_620RPM" />|<img src="./img/JGA25-371_1_34.JPG" width = "150" alt="JGA25-371M" />|<img src="./img/JGA16-050.png" width = "150" alt="JGA16-050" />|
|speed(轉速)|1360rpm/m|620rpm/m|294rpm/m|220rpm/m|
|torque(扭距)|0.35kg.cm|0.75kg.cm|5.2kg.cm|0.15kgcm|
|power(功率)|5.4W|5.4W|4.2W|0.33W|

### Motor Controller(馬達控制器)
#### 英文
- When testing the operation of the motor, simply providing power does not effectively control the movement of the GA25-370 motor, making it impossible to adjust the speed. Therefore, we need to install a motor controller to regulate the speed of the DC gear motor. Currently, there are two options available in the market: the L293D chip and the L298N module. To reduce weight, we chose the smaller L293D chip. Its compact size allows us to install more sensors, thereby saving space, reducing weight, and increasing the maneuverability of the vehicle.
#### 中文
- 在測試馬達的作動方式時，單純提供電源並無法有效地控制GA25-370馬達的運動，使得我們無法調節速度。因此，我們需要安裝馬達控制器來調節直流減速馬達的速度。目前市售有兩種選擇：L293D晶片和L298N模組。為了減輕重量，我們選擇了體積較小的L293D晶片。它的小巧尺寸讓我們能夠安裝更多的感應器，進而節省空間、減輕重量，並增加車輛的機動性。

| L293D | L298N |
| :---: | :---: |
|  <img src="./img/l293d.png" width = "150" height = "" alt="l293d" align=center /> | <img src="./img/L298N.png" width = "150" height = "" alt="l298n" align=center /> |


# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
