<div align="center"><img src="../../other/img/logo.png" width="600" alt=" logo"></div>

2023WRO Future Engineers Shinan Fire On All Cylinders  
====
# <div align="center">Motor</div> 
While the vehicle is in motion, the Jetson Nano sends speed information via I2C to the motor control board to control the rear DC motor. Simultaneously, the Raspberry Pi sends messages using the PWM controller to the servo motor of the front steering mechanism, allowing the vehicle to freely steer and move forward.

### Front Steering Mechanism by Servo Motor
- To select a servo motor among commonly available options in the market, considering factors such as weight, rotation angle, and torque, we have identified two suitable servo motors: MG90S and SG90.
- The main difference between MG90S and SG90 lies in their front gears. The former has metal gears, while the latter has plastic gears. Since continuous rotation is often required, we opted for the MG90S due to its durability and resistance to damage.

#### Servo Motor
<div align="center">
<table>
<tr align="center">
<th rowspan="2" >Model</th>
<th>MG90S</th>
<th>SG90</th>
</tr>
<tr align="center">
<td><img src="./img/MG90S.png" width = "150" height = "" alt="MG90S" align=center /></td>
<td> <img src="./img/SG90.png" width = "150" height = "" alt="SG90" align=center /></td>
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

### PWM Controler

- Since the PWM signals from the Jetson Nano are not easily controlled, we require an external board to manage servo motors. We've chosen the PCA9685 16-channel 20-bit PWM driver as our PWM control board. This choice was motivated by the presence of pins on the board, enabling the adjustment of angles through rewiring if needed. This aligns well with our goal of centralizing controllers onto the circuit board. The advantage of this board lies in its utilization of the I2C protocol for controlling PWM signals, thereby not utilizing additional GPIO pins.
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

### Rear-Drive DC Motor
- When selecting a DC motor among commonly available options in the market, considering factors such as weight, rotational speed, and torque, we have identified the following four suitable DC motors。
- Among them, the three types of motors, JGA25, have different model numbers but share a similar physical appearance, and their differences are as follows.
- After conducting experimental research, we found that choosing the high-speed 1630rpm JGA-370 motor resulted in lower torque, making it difficult for the vehicle to move effectively. On the other hand, opting for the high-torque JGA-371 motor led to an excessively low rotational speed, which did not meet the requirements for the vehicle's operation.
- Therefore, based on these findings, we ultimately selected the 620rpm JGA-370 motor as the rear-wheel drive DC motor for the vehicle. This choice strikes a balance between rotational speed and torque, providing the necessary performance for the vehicle's propulsion.

#### DC Motor
<div align="center"><table><tr align="center">
<th rowspan="2" >Model</th>
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
<td >speed</td>
<td >1360rpm/m</td>
<td >620rpm/m</td>
<td >294rpm/m</td>
<td >220rpm/m</td>
</tr>
<tr align="center"><td>torque</td><td>4.27kg.cm</td><td>9.15kg.cm</td><td>5.2kg.cm</td><td>1.15kgcm</td></tr><tr align="center">
<td>power</td><td>5.4W</td><td>5.4W</td><td>4.2W</td><td>0.33W</td>
</tr>
</table>
</div>

### Motor Controller

- Since we cannot directly use 5V to control the DC motor, as it would result in insufficient voltage to drive it, we need to use a motor control board. This type of board can achieve a 5V control over a 12V voltage output, allowing us to control the direction and speed of the DC motor.

- There are two options available: the DC Motor Driver HAT (V1.0) and the L298N. Although the HAT is relatively larger, it can be directly mounted on the Jetson Nano, avoiding the issue of occupying space on the circuit board. Additionally, it does not consume the 5V and GND pins. Therefore, we chose the DC Motor Driver HAT (V1.0).

#### Motor Controller
<div align="center">
<table>
<tr align="center" >
<th>DC Motor Driver HAT(V1.0)</th>
<th>L298N</th>
</tr>
<tr align="center">
<td> <img src="./img/Motor_driver.png" width = "250"  alt="l293d" align=center /></td>
<td ><img src="./img/L298N.png" width = "250"  alt="l298n" align=center /></td>
</tr>
</tr>
</table>
</div>

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
