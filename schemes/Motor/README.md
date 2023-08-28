2023WRO Future Engineers Shinan Fire On All Cylinders  
====
# <div align="center">Motor</div> 
While the vehicle is moving, the Jetson Nano sends speed information to the motor control board, which then transmits it to the L293D motor driver to control the rear-wheel drive DC motors. Simultaneously, the Raspberry Pi sends messages through a PWM controller to the servo motor of the front steering mechanism, allowing the vehicle to maneuver and steer freely while moving forward.

車輛行走時，Jetson Nano將轉速訊息藉由 __馬達控制板__ 傳送給 __L293D 馬達控制器__，以控制 __後驅直流馬達__。同時，樹莓派也將訊息利用 __PWM控制器__ 傳送給 __前轉向機構的伺服馬達__，使車輛能夠自由轉向前進。

### Front Steering Mechanism by Servo Motor(前轉向機構伺服馬達)
#### 英文
- To select a servo motor among commonly available options in the market, considering factors such as weight, rotation angle, and torque, we have identified two suitable servo motors: MG90S and SG90.
- The main difference between MG90S and SG90 lies in their front gears. The former has metal gears, while the latter has plastic gears. Since continuous rotation is often required, we opted for the MG90S due to its durability and resistance to damage.

#### 中文

- 在選擇伺服馬達以市售常見伺服馬達為目標，並考慮其重量、轉向角度、轉矩等因素，找到MG90S和SG90這二種符合條件之伺服馬達。
- MG90S和SG90之間的差異在於前齒輪，前者是金屬的，後者則是塑料的。由於我們常常需要持續旋轉，我們選擇了MG90S，因為它不容易損壞。 
#### Servo Motor(伺服馬達)
<div align="center">
<table>
<tr align="center">
<th rowspan="2" >Model(型號)</th>
<th>MG90S</th>
<th>SG90</th>
</tr>
<tr align="center">
<td><img src="./img/MG90S.png" width = "150" height = "" alt="MG90S" align=center /></td>
<td> <img src="./img/SG90.png" width = "150" height = "" alt="SG90" align=center /></td>
</tr>
<tr align="center">
<td>rotation angle(轉動角度)</td>
<td>90° MAX</td>
<td>0~90°/180° MAX</td>
</tr>
<tr align="center">
<td>torque(轉矩)</td>
<td>2.0kg/cm</td>
<td>1.4 kg/cm</td>
</tr>
<tr align="center">
<td>speed(轉速)</td>
<td>0.11s</td>
<td>0.1S</td>
</tr>
</table>
</div>

### PWM Controler(PWM控制版)
#### 英文
- Due to the somewhat challenging nature of controlling PWM signals with Jetson Nano directly, we have opted for an external board to manage the servo motors. We chose the PCA9685 16-channel 20bit PWM driver as the PWM control board, mainly because it features pins that allow for angle adjustments through re-soldering if needed. This aligns well with our requirement of integrating controllers onto the circuit board.

#### 中文

- 由於 Jetson Nano 的 PWM 訊號並不是這麼的好控制，因此我們需要外接板子來控制伺服馬達，诶們選擇了 PCA9685 16-channel 20bit PWM driver 作為 PWM 控制版，因為上面裝有引腳，並且如果引腳需要修改角度還可以重新焊接，很符合我們將控制器都裝於電路板的需求。
#### PWM Controler
<div align="center">
<table>
<tr align="center">
<th>PCA9685 16-channel 20bit PWM driver</th>
</tr>
<tr align="center">
<td><img src="./img/pmw_driver.png" width = "400" height = "" alt="MG90S" align=center /></td>
</tr>
</table>
</div>

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

#### DC Motor(直流馬達)
<div align="center"><table><tr align="center">
<th rowspan="2" >Model(型號)</th>
<th >JGA25 370</th>
<th >JGA25 370</th>
<th >JGA25 371</th>
<th >JGA16-050</th>
</tr>
<tr align="center">
<td ><img src="./img/JGA25-370_1360RPM.JPG" width = "150" alt="JGA25-370_1360RPM" /></td>
<td ><img src="./img/JGA25-370_620RPM.JPG" width = "150" alt="JGA25-370_620RPM" /></td>
<td ><img src="./img/JGA25-371_1_34.JPG" width = "100" alt="JGA25-371M" /></td>
<td ><img src="./img/JGA16-050.png" width = "150" alt="JGA16-050" /></td>
</tr>
<tr align="center">
<td >speed(轉速)</td>
<td >1360rpm/m</td>
<td >620rpm/m</td>
<td >294rpm/m</td>
<td >220rpm/m</td>
</tr>
<tr align="center"><td>torque(力距)</td><td>4.27kg.cm</td><td>9.15kg.cm</td><td>5.2kg.cm</td><td>1.15kgcm</td></tr><tr align="center">
<td>power(功率)</td><td>5.4W</td><td>5.4W</td><td>4.2W</td><td>0.33W</td>
</tr>
</table>
</div>

### Motor Controller(馬達控制器)
#### 英文
- When testing the operation of the motor, simply providing power does not effectively control the movement of the GA25-370 motor, making it impossible to adjust the speed. Therefore, we need to install a motor controller to regulate the speed of the DC gear motor. Currently, there are two options available in the market: the L293D chip and the L298N module. To reduce weight, we chose the smaller L293D chip. Its compact size allows us to install more sensors, thereby saving space, reducing weight, and increasing the maneuverability of the vehicle.
#### 中文
- 由於我們無法直接的使用5V來控制直流馬達，那樣會導致電壓不足無法驅動，因此我們需要用到馬達控制板，這種板子可以達到使用5V來控制12V的電壓輸出，這樣就能控制直流馬達的正反轉以及速度
- 有 DC Motor Driver HAT(V1.0) 和 L298N 兩個選擇，雖然 HAT 比較大片，但可以直接裝在Jetson Nano 上，所以不會有佔據電路板空間的問題，而且還不會占用5V和GND的腳位，因此我們選擇DC Motor Driver HAT(V1.0)

#### Motor Controller(馬達控制器)
<div align="center">
<table>
<tr align="center" >
<th>DC Motor Driver HAT(V1.0)(馬達控制版)</th>
<th>L298N(馬達控制器)</th>
</tr>
<tr align="center">
<td> <img src="./img/Motor_driver.png" width = "300"  alt="l293d" align=center /></td>
<td ><img src="./img/L298N.png" width = "300"  alt="l298n" align=center /></td>
</tr>
</tr>
</table>
</div>

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
