<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">Work Diary </div> 
  Here is the record of the process for own design and manufacturing of vehicle and components, with off the shelf electrical components, such as motors and sensors.  
## 2023/03/19 ~ 2023/03/26  
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

At the outset, due to our uncertainty about how to initiate the process of constructing and assembling the vehicle, we turned to the official Donkey Car website for guidance. Consequently, the construction of the vehicle will be based on modifications to the vehicle design provided on the official website.

<div align="center">
<table>
<tr align="center">
<th><a href="https://www.donkeycar.com/">Donkey Car official website</a></th>
<th><a href="http://docs.donkeycar.com/">Donkey Car technical documentation</a></th>
</tr>
<tr align="center">
<td><img src="./img/3/donkeycar.png" width = "300"  alt="樹梅派" align=center /></td>
<td><img src="./img/3/donkeycar_doc.png" width = "300"  alt="jeston nano" align=center /></td>
</tr>
</table>
</div>
<div align="center" width=100%>
<img src="./img/3/Daily.jpg" width="300" alt="Daily" >
</div>

## 2023/03/27 ~ 2023/04/02
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  
- To ensure the smooth progression of the competition, our team carefully planned the completion timeline for each stage of the competition activities.
- After reading the rules, we began the process of selecting our controller. Upon reviewing previous competitions, we observed that the majority of participants used either Raspberry Pi or Jetson Nano as their controllers. Based on this information, I had to decide between these two options. Ultimately, I opted for the Raspberry Pi 4B due to its smaller size and more affordable price compared to the Jetson Nano.

  __Competition Activity Stages Work Completion Timeline Schedule(Gantt Chart)__ 
<div align="center" >
  <img src="../img/Gantt_Chart.png" width = "600"   alt="甘特圖" align=center />
</div>

### Vehicle Computing Controller
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
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

- As we waited for the Raspberry Pi to initialize and the required libraries to be installed, we proceeded to choose the motor for propulsion. We had two options: the JGA25-370 and the JGA16-050. The JGA25-370 offers higher torque, making it suitable for moving heavier objects. On the other hand, the JGA16-050 is smaller and lighter but comes with relatively lower torque. Taking into account the anticipated weight of the robot, we decided to go with the higher torque of the JGA25-370 motor.
- Among the JGA25-370 options, there are several variations currently available within the club.
- While testing the motor's operation, we found that a simple application of positive and negative voltage did not offer effective control over the performance or speed adjustment of the JGA25-370 motor. Consequently, a motor controller was necessary to regulate the speed of the DC geared motor. We considered two options: the L293D chip and the L298N module. In order to keep the weight minimal, we opted for the compact L293D chip. Its small size enables us to integrate more sensors, ultimately saving space, reducing weight, and improving the robot's maneuverability.

#### DC Motor
<div align="center"><table><tr align="center">
<th rowspan="2">Model(model number)</th>
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
<td >speed</td>
<td >1360rpm/m</td>
<td >620rpm/m</td>
<td >294rpm/m</td>
<td >220rpm/m</td>
</tr>
<tr align="center">
<td>torque</td>
<td>4.27kg.cm</td>
<td>9.15kg.cm</td>
<td>5.2kg.cm</td><td>1.15kgcm</td>
</tr><tr align="center">
<td>power</td><td>5.4W</td><td>5.4W</td><td>4.2W</td><td>0.33W</td>
</tr>
</table>
</div>



## 2023/04/10 ~ 2023/04/16  
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

- Given the vehicle's continuous movement, a switch to battery power is necessary. Considering the motors' requirement of a 12V voltage for operation, selecting a battery with 12V voltage and 3V current is essential. Two alternatives are available: lithium-ion batteries (18650) and lithium polymer batteries (3S). However, the 18650 battery is bulkier and heavier, leading us to choose the lithium polymer battery for its space-saving and lightweight advantages.
- However, the maximum voltage supported by the Raspberry Pi is only 5.2V. Therefore, we need to use a voltage regulator module to reduce the voltage and prevent any potential damage to the Raspberry Pi. In our initial considerations, the LM2596 DC-DC adjustable voltage regulator module seemed promising due to its numerical display feature that indicates the current output voltage. Nonetheless, it's worth noting that this module has a maximum current capacity of only 3A. Considering our requirements, we decided to opt for a constant voltage and constant current step-down power supply module, capable of handling up to 5A. While this alternative lacks a numerical display, we have plans to integrate a low voltage alarm system to monitor the battery voltage closely and ensure its safety.
####  Batteries
<div align="center" width=100%>
<table >
<tr>
  <th> 18650 lithium batteries </th> <th>Li-Polymer 3S Battery 
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


#### Voltage Regulator Module
<div align="center" width=100%>
<table >
<tr align="center">
  <th> LM2596 DC-DC Adjustable Buck Converter Module </th> 
  <th>5A Constant Voltage and Constant Current Buck Converter Module </th>
</tr>
<tr align="center">
  <td>  <img src="./img/4/LM25.jpeg" width = "250"   alt="MG90S"/>  </td>
  <td><img src="./img/4/ADIO-DC36V5A.png" width = "300"   alt="MG90S"/> 
  </td>
  </tr>
</table>
</div>

#### Low Voltage Alarm
<div align="center" width=100%>
<table >
<tr align="center">
  <th> Low Voltage Alarm</th> 
</tr>
<tr align="center">
  <td><img src="./img/4/low_voltage_alarm.png" width = "150" alt="low_voltage_alarm"/></td>

  </tr>
</table>
</div>


## 2023/04/17 ~ 2023/04/23
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**    

- The next step is to choose the controlling motor. After searching for information online, we discovered that MG90S and SG90 are the most common options. The difference between MG90S and SG90 lies in the front gear, with the former being made of metal and the latter being made of plastic. Due to our frequent need for continuous rotation, we have selected the MG90S, as it is less prone to damage.


#### Servo Motor
<div align="center">
<table>
<tr align="center">
<th rowspan="2">Model(model number)</th>
<th> MG90S</th>
<th >SG90</th>
</tr>
<tr align="center">
<td><img src="./img/4/MG90S.png" width = "150"   alt="MG90S" align=center /></td>
<td><img src="./img/4/SG90.png" width = "150"   alt="SG90" align=center /></td>
</tr>
<tr align="center">
<td>Rotation angle</td>
<td>90° MAX</td>
<td>0~90°/180° MAX</td>
</tr>
<tr align="center">
<td>Torque</td>
<td>2.0kg/cm</td>
<td>1.4 kg/cm</td>
</tr>
<tr align="center">
<td>Speed</td>
<td>0.11s</td>
<td>0.1S</td>
</tr>
</table>
</div>

## 2023/04/24 ~ 2023/04/30
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

- When the vehicle is uncertain about the distance ahead, it may fail to turn in time when it encounters a wall. To address this issue, ultrasonic sensors have been incorporated to allow the vehicle to initiate a turn before coming into contact with the wall.
- Based on the conducted experiments, it has been determined that ultrasonic sensors are only capable of detecting obstacles directly in front of the vehicle. Moreover, their effectiveness diminishes when the vehicle sways from side to side. Therefore, the decision has been made to implement a 360-degree LiDAR sensor. This sensor will not only detect distances in front of the vehicle but also on its left and right sides.

#### Distance Sensor
<div align="center" width=100%>
<table>
<tr align="center">
  <th>Ultrasound </th> 
  <th>Ydlidar x2</th>
</tr>
<tr>
  <td><img src="./img/4/ultrasound.png" width = "300"  alt="ultrasound" align=center /></td>
  <td><img src="./img/4/Lidar_X2.jpg" width = "300"  alt="ydlidar x2" align=center />
  </td>
  </tr>
</table>
</div>


## 2023/05/01~ 2023/05/07  
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  
- We began assembling the machine by using LEGO parts from the club to build the base. We then attached the motors, Raspberry Pi, and other components onto the chassis, making the machine functional.

   After the vehicle becomes operational, we further add additional sensors to enable the vehicle to sense its surroundings and respond accordingly based on mission requirements
- During testing, we discovered that the vehicle's movement speed using LEGO bricks was not fast, and its weight caused difficulties during turns. Consequently, we opted to use a laser cutting machine to cut wooden boards for the chassis, reducing the vehicle's weight, increasing its speed, and conserving power. Additionally, the use of wooden boards offers the advantage of adjusting dimensions and positions as needed. This adjustment is facilitated through tools like Onshape, allowing for flexible design and modifications without the need for constant adaptations like those required with LEGO in various scenarios."

<div align="center" width=100%>
<table>
<tr align="center">
  <th>Wooden boards</th>
  <th>Onshape web page</th>
  </tr>
<tr align="center">
  <td><img src="./img/5/wood.jpg" width = "300"  alt="wood" align=center />  </td>
  <td><img src="./img/5/onshape.png" width = "300"  alt="onshape" align=center />
  </td>
  </tr>
</table>
</div>


## 2023/05/08 ~ 2023/05/14  
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

- While it's feasible to move in a straight line and execute turns using the ultrasonic sensor, there's a risk of scraping against walls and encountering difficulties at corners. To address this, we substituted the ultrasonic sensor with a lidar, capable of detecting surroundings and maintaining the robot's position at the center of the path. Additionally, the lidar facilitates the identification of upcoming turns.
- Nevertheless, during actual testing of the YDLIDAR X4 and DLIDAR X2, we encountered a problem with missing angles (as depicted in the attached image). Therefore, for this competition, we opted to employ the D100 sensor for vehicle detection and measuring distances to side walls. The results yielded by the D100 sensor aligned with our expectations and requirements.

<div align="center" width=100%>
<table>
<tr align="center" >
  <th>Ydlidar x4</th> 
  <th>Ydlidar x2</th>
  <th>Lidar 100</th>
</tr>
<tr align="center">
  <td><img src="./img/7/Lidar_X4.jpg" width = "300" alt="Ydlidar x4" align=center /></td>
  <td><img src="./img/4/Lidar_X2.jpg" width = "300"  alt="Ydlidar x2" align=center /></td>
  <td><img src="./img/7/Lidar-D100.png" width = "300" alt="Ydlidar x4" align=center /></td>
</tr>
</table>
</div>

<div align="center" width=100%>
<table>
<tr align="center">
  <th colspan="2">Ydlidar x4、X2 distance imaging</th> 
  <th>Lidar 100 distance imaging</th>
</tr>
<tr align="center">
  <td><img src="./img/7/Lidar_X2_X4_error1.jpg" width = "400" alt="偵測缺角" align=center /></td>
  <td><img src="./img/7/Lidar_X2_X4_error.jpg" width = "400" alt="偵測缺角" align=center /></td>
  <td> <img src="./img/7/d100.png" width = "400" alt="D100" align=center />  
  </td>
  </tr>
</table>
</div>


## 2023/05/15 ~ 2023/05/21  
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  
- TCS34725 color sensor 
  - In the competition, vehicles need to showcase more functionalities than just being able to turn. Merely knowing how to turn is insufficient. To achieve clockwise and counterclockwise turns, we must enable the vehicle to sense the color of lines on the ground and make appropriate judgments accordingly. Therefore, when selecting color sensors, we need to exercise special caution.
  - The TCS34725 color sensor has been chosen because it fulfills all the requirements of this competition. Firstly, it boasts exceptional sensing capabilities, enabling it to swiftly and accurately identify the colors of the ground lines. Secondly, the sensor is slim and compact, allowing it to be positioned near the ground without disrupting the vehicle's movements.
  - The high precision of this sensor ensures that the vehicle can accurately detect the colors of the ground lines and perform clockwise or counterclockwise turns as required. This is a crucial factor in the vehicle's excellent performance and its victory in the competition.

     In conclusion, the TCS34725 color sensor is a perfect fit for the requirements of this competition. Its slim design and highly accurate color recognition capabilities enable the vehicle to adapt flexibly to changes in ground lines, achieve clockwise and counterclockwise turns, and enhance its performance in the competition.

     I encountered a bottleneck when using the color sensor to detect lines because I was unsure how to write a Python program to detect the values of blue and orange lines. With the guidance of my teacher, I successfully overcame this challenge. The partial code is as follows:
- Additionally, during the implementation testing, we discovered that the original use of a USB 180-degree adapter (as shown in the lower left image) was prone to colliding with obstacles, particularly building blocks. As a result, we made a change and switched to using a USB 3.0 90-degree adapter for the connection. This modification reduces the likelihood of accidentally hitting obstacles while attempting to avoid them.


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
  <td align="center"><img src="./img/4/site.jpg" width=300 alt="site" /></td> 
  <td align="center"><img src="./img/4/work_photo_2_1_0417.jpg" width=300 alt="work_photo_2_1_0417" /></td>
</tr>
</table>
</div>

## 2023/05/22 ~ 2023/05/28  
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

- In order to enable the vehicle to avoid obstacles accurately, we need to install a camera module on the vehicle. Since we are using a Raspberry Pi as the controller, we need to find a compatible camera module for it. To do this, we referred to the camera module used by the American team in last year's competition and compared it with other camera modules in the same series. Here is the product information:

1. raspberry pi camera Rev 1.3(Sensor:OmniVision OV5647)
2. raspberry pi camera Module V2(Sensor:Sony IMX219)
3. raspberry pi camera Module V3(Sensor:Sony IMX708)

- Considering that V3 is not compatible with our existing Raspberry Pi operating system, we decided not to use that version. Additionally, the detection rate of version 1.3 is only 30p, whereas the V2 version can reach a maximum of 90p. Therefore, we ultimately chose the Raspberry Pi Camera Module V2 for our project. Through experimentation, we found that the V2 version has the best recognition performance.


#### Camera Module
<div align="center">
<table>
<tr  align="center">
<th rowspan="2">Model(model number)</td> 
<th>Raspberry pi camera Rev 1.3</th>
<th >Raspberry pi camera Module V2</th>
<th >Raspberry pi camera Module V3</th>
</tr>
<tr  align="center">
<td ><img src="./img/5/V1.jpeg" width=200 alt="V1"  /></td>
<td ><img src="./img/5/V2.jpeg" width=200 alt="V2" ></td>
<td ><img src="./img/5/V3.jpeg" width=200 alt="V3" /></td>
</tr>
<tr  align="center">
<td>Sensor</td>
<td>Omnivision OV547</td>
<td >Sony IMX 219</td>
<td>Sony IMX 708</td>
</tr>
<tr  align="center">
<td>Sensor resolution</td>
<td >2592 * 1944 pix</td>
<td>3280 * 2464 pix</td>
<td>4608 * 2592 pix</td>
</tr>
<tr  align="center">  
<td>FPS Frame rate</td>
<td>60p MAX</td>
<td>90p MAX</td>
<td>120p MAX</td>
</tr>
</table>
</div>

During subsequent testing, we discovered that the vehicle was unable to predict the position of the next block while avoiding obstacles. This posed a challenge to the vehicle's obstacle avoidance strategy. Consequently, we decided to modify the original camera by converting it into a wide-angle lens. In comparison to the original 72-degree field of view, the wide-angle lens offers a 160-degree field of view, enabling us to anticipate the next block's position in advance. This enhancement has significantly improved the vehicle's obstacle avoidance effectiveness.

#### Wide-angle lens
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
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

- By using VS Code along with Git to edit our technical documentation, we can effectively manage potential conflicts and improve collaboration. The advantages of this approach include easy version control, immediate notifications to editors when conflicts arise due to simultaneous edits, and the ability for editors who upload data later to merge conflicts by comparing the data. This way, we can ensure a smoother and more efficient process when working on the technical documentation.

[github Homepage ](https://github.com/kirkhu/WRO2023_FE-Shinan-Fire-On-All-Cylinders/tree/main)

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
<img src="./img/5/web.png" width = "300" alt="WEB" align=center />
</td>
</tr>
</table>
</div>


## 2023/06/05 ~ 2023/06/11 
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

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
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

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
<td><img src="./img/5/hit_wall.jpeg" width = "300" alt="hit wall"  /></td>
<td><img src="./img/5/LIDAR_readings.png" width = "200" alt="Distance to wall."/></td>
</tr>
</table>
</div>


## 2023/06/19 ~ 2023/06/25   
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

- The vehicle is now able to operate successfully. The next step involves using the camera to avoid obstacles (blocks). Next, we need to detect the distance to the obstacles (blocks) and then identify the color of the blocks. By utilizing the features of OpenCV, we can calculate the distance between the blocks and the vehicle for obstacle avoidance. Through the implementation of an algorithm, we can control the front wheels to steer around these obstacles.
- However, there is an issue at the corners where the vehicle cannot avoid obstacles in a timely manner. To address this, we need to combine the gyroscope's readings with the output values from the algorithm to successfully navigate around corners.

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
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

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
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

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
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

- The vehicle is now capable of successfully avoiding obstacles and completing the third lap around the track. The next task is to detect blocks and perform a turnaround maneuver. The turnaround will be executed only if the last block of the second lap is red. Therefore, it is necessary to detect the number of laps. We will use the color sensor to count the number of times the line is crossed and determine whether the set count has been reached.

- If the specified count has not yet been achieved, the system will continue to record the color of the nearest traffic sign until the count of line crossings is greater than or equal to the set count. At this point, the color recording will cease.

- After recording the color of the nearest traffic sign, the program will determine whether the color is red. If the color is indeed red, the system will adjust the angle of the servo motor to initiate a right turn and will continue turning until the vehicle is properly aligned in the specified direction, thus executing a turnaround maneuver. If the detected color is not red, the vehicle will proceed to move forward.


<div align="center">
<table>
<tr align="center">
<th>Display the number of line crossings and <br>the color of the nearest traffic sign.</th>
<th>Adjusting the values.
</th>
</tr>
<tr align="center">
<td><img src="./img/7/detect_last_obstacle.png" width="200" alt="print color"></td>
<td><img src="./img/7/check.jpeg" width="300" alt="check"></td>
</table>
</div>

## 2023/07/17 ~ 2023/07/23  
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

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
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

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
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**   

- As the deadline for submitting the technical report is next week, we have begun revising the content of the technical documentation. We are also adjusting the website according to the official grading criteria and continuously adding to the technical report.
- Complete recording videos for each task and upload them to YouTube.


<table>
<tr align="center">
<th> Old directory </th>
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
<th>Report writing</th> 
<th>Mechanism adjustment</th>
<th>Report writing</th>
<th>Field mission practice</th>
</tr>
<tr align="center">
<td><img src="./img/8/work_photo_1_0805.jpg" width="500" alt="work_daily"></td>
<td><img src="./img/8/work_photo_2_0805.jpg" width="500" alt="work_daily"></td>
<td><img src="./img/8/work_photo_3_0805.jpg" width="500" alt="work_daily"></td>
<td><img src="./img/8/work_photo_4_0805.jpg" width="500" alt="work_daily"></td>
</table>
</div>

## 2023/08/07 ~ 2023/08/13
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

- This week, with our machine now adjusted to smoothly complete the mission race on the field, we have begun filming an introductory video for the race. In the video, we will showcase the actions our vehicle performs during the mission race, providing explanations through subtitles synchronized with the video.


<div align="center">
<table>
<tr align="center">
<th>Modifying code and testing vehicles</th>
<th>Currently editing videos</th>
</tr><tr align="center">
<td><img src="./img/8/work_photo_1_0813.jpg" width="300" alt="work_daily"></td>
<td><img src="./img/8/813.jpg" width="300" alt="work_daily"></td>
</tr><tr align="center">
</table>

<table>
<th>Mission race introduction video</th>
</tr>
<td>

[![video](https://i.ytimg.com/vi/EAkR-t_6i7g/maxresdefault.jpg)](https://youtu.be/EAkR-t_6i7g "video")</td>
</table>
</div>



## 2023/08/14 ~ 2023/08/20
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

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
<th>Field layout</th>
<th>Record sheet</th> 
</tr>
<tr align="center">
<td><img src="./img/8/block.png" width="400" alt="work_daily"></td>
<td><img src="./img/8/grade.png" width="500" alt="work_daily"></td>
</table>
</div>
<div align="center">
<table>
<tr align="center">
<th>Competition photos</th>
<th>Award-winning photo</th> 
</tr>
<tr align="center">
<td><img src="./img/8/0819_1.jpg" width="600" alt="contest"></td>
<td><img src="./img/8/0819_2.jpg" width="600" alt="award-winning photo"></td>
</table>
</div>

## 2023/08/21 ~ 2023/08/27
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

- As we have confirmed our participation in the international competition, we are undergoing significant modifications to our vehicle. Moreover, this redesign will allow us to incorporate threaded components for added stability. Additionally, we are upgrading the controller from Raspberry Pi 4B to the higher computing power provided by the Jetson Nano microcomputer. The Jetson Nano supports programming in Python, thus most of our existing code does not need significant modifications. However, one notable difference with the Jetson Nano is that the generation of PWM signals requires an external board for implementation.

- After switching to Jetson Nano, we encountered issues with the Camera V2. After some investigation, we discovered that V2 and V3 cameras are designed for use with Raspberry Pi. So, we decided to switch to the IMX 219-160 camera, which is compatible with Jetson Nano. This camera comes with a wide-angle lens, eliminating the need for modifications.

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

<div align=center>
<table>
<tr align=center>
<th>160 width-angle</th>
</tr><tr>
<td><img src="../../schemes/Camera/img/v1_width-angle.jpg" width="200" alt="work_daily"></td>
</tr>
</table>
</div>

<small>Data source:</small>  
<small>[Taiwansersor](https://www.taiwansensor.com.tw/product/nvidia-jetson-nano-developer-kit-%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E9%96%8B%E7%99%BC%E5%A5%97%E4%BB%B6-ai-%E9%96%8B%E7%99%BC%E5%A5%97%E4%BB%B6/)</small>  
<small>[University of Maine System](https://web.eece.maine.edu/~vweaver/group/green_machines.html)</small>


## 2023/08/28 ~ 2023/09/03
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  
Today, we started learning how to use the stereolithography 3D printer and how to maintain it after printing. Our senior demonstrated the process to us. Here are the maintenance steps:

1. After printing is complete, the finished product will be stuck to the build plate.
2. Remove the build plate and wipe off the resin, being careful not to touch the finished product.
3. Rinse off easily removable supports with water.
4. Spray alcohol onto the finished product, making sure to reach every corner.
5. Wipe the finished product to remove excess resin.
6. Carefully detach the finished product using tools.
7. Use a knife to scrape away any remaining support material on the finished product.
8. Rinse off any fine residue with water.
9. Wipe the build plate clean of resin, and it's ready for the next print.

<div align="center">
<table>
<tr align="center">
<td><img src="./img/9/0901-1.jpg" width="200" alt="work_daily"></td>
<td><img src="./img/9/0901-3.jpg" width="100" alt="work_daily"></td> 
<td><img src="./img/9/0901-4.jpg" width="200" alt="work_daily"></td>
</tr>
<tr align="center">
<td><img src="./img/9/0901-5.jpg" width="200" alt="work_daily"></td>
<td><img src="./img/9/0901-7.jpg" width="200" alt="work_daily"></td>
<td><img src="./img/9/0901-6.jpg" width="200" alt="work_daily"></td>
</tr>
<tr>
<td><img src="./img/9/0901-9.jpg" width="200" alt="work_daily"></td>
<td><img src="./img/9/0901-12.jpg" width="200" alt="work_daily"></td>
<td><img src="./img/9/0901-8.jpg" width="200" alt="work_daily"></td>
</tr>
</table>
</div>

## 2023/09/04 ~ 2023/09/10
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

- Today, we utilized a stereolithography 3D printer to produce the fixtures for our front steering mechanism, allowing us to optimize the space utilization of the steering mechanism. We chose stereolithography due to its advantages, such as a smooth surface finish, high precision, and easy maintenance. However, it's worth noting that this method tends to have longer print times. Consequently, we exclusively used it for components that needed to be printed separately, like the Ackermann steering mechanism and the bearing mounting bracket. This approach not only saved printing time but also ensured high precision in the components.

- This week, our club acquired a stacked 3D printer, which means we can now start working on vehicle integration. One of the advantages of using a 3D printer is that we can create threads, which allows for more secure fastening of screws. With vehicle integration, we can reduce the overall size, making the machine more lightweight.

- Earlier, we had multiple failed attempts at printing, and we discovered that it was because we weren't using supports. Since the printer works by stacking layers on top of each other, any overhanging parts without support would collapse. When we removed the finished prints, they would often break. After realizing that the infill density was too low, resulting in fragile prints, we increased the density, which helped us successfully complete the prints.

- When assembling the vehicle, we found that the photopolymer parts remained soft and were prone to deformation. Therefore, we used ultraviolet (UV) light for secondary curing to make the parts less susceptible to deformation.


<div align="center">
<table>
<tr align="center">
<th>Maintenance of Photocuring 3D Printer</th>
<th colspan="3">Finished Product Photos</th> 
</tr>
<tr align="center">
<td><img src="./img/9/using_3D_printer.jpg" width="200" alt="work_daily"></td>
<td><img src="./img/9/photoprinting.jpg" width="200" alt="work_daily"></td>
<td><img src="./img/9/turn_mashine-1.jpg" width="300" alt="work_daily"></td>
<td><img src="./img/9/turn_mashine-2.jpg" width="300" alt="work_daily"></td>
</tr>
</table>
</div>

<div align=center>
<table>
<tr align=center>
<th>3D Printer</th>
<th>3D Printer working</th>
</tr><tr align=center>
<td><img src="./img/9/all_3Dprinter.jpg" alt="3D printer" width=200 /></td>
<td><img src="./img/9/3D_working.jpg" alt="3D printer" width=200 /></td>
</tr>
</table>
</div>

#### 3D printed product
<div align="center">
<table>
<tr  align="center"> 
<td><img src="./img/8/3D_2.png" alt="work_photo_2_1_0729" width=300 /></td> 
<td><img src="./img/8/3D_1.png" alt="work_photo_2_2_0729" width=250 /></td>
</tr>
</table>
</div>

<div align=center>
<table>
<tr>
<th>Secondary curing</th>
</tr><tr>
<td><img src="../../models/Vehicle_2D_3D/img/curing_again.jpg" width=300 alt="light_again"></td>
</tr>
</table>
</div>

## 2023/09/11 ~ 2023/09/17
**Member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**Content:**

This week, we started modifying the program. Due to the differences in the Raspberry Pi and Jetson Nano environments, even though both use Python, we had to make significant changes to the program. With the modifications to the vehicle and the circuitry, there were many areas in the code that required adjustments. We faced several challenges during the qualifying rounds, such as the LiDAR not detecting obstacles properly, the battery slipping can get stuck in the tire, and the light sensor being too sensitive, among other issues.

While the 3D-printed chassis offered advantages such as size reduction and greater flexibility, it was not sturdy enough and prone to breaking. Therefore, we ultimately decided to use a laser cutting machine to cut wooden boards for the chassis.


During vehicle testing, we discovered that the Jetson Nano's reading speed for the color sensor was extremely slow, leading to difficulties in the vehicle's turning accuracy. When we switched back to the Raspberry Pi, the reading speed returned to normal. Later, we realized that while the Jetson Nano has extremely fast image recognition capabilities, it consumes a significant amount of processing power for this task. Additionally, the I2C interface is used not only for the color sensor but also for the motor controller and PWM controller, which contributed to the decision to switch the main controller back to the Raspberry Pi 4B.

<div align="center">
<table>
<tr  align="center"> 
<td><img src="./img/9/0918.jpg" alt="work_photo_2_2_0729" width=300 /></td>
<td><img src="./img/9/0918-1.jpg" alt="work_photo_2_1_0729" width=300 /></td> 
</tr>
</table>
</div>

<div align="center">
<table>
<tr  align="center"> 
<td><img src="./img/9/car_wood_up.jpg" alt="work_photo_2_2_0729" width=300 /></td>
<td><img src="./img/9/car_wood_down.jpg" alt="work_photo_2_1_0729" width=300 /></td> 
</tr>
</table>
</div>


## 2023/09/18 ~ 2023/09/24
**Member:**  ZHAO,ZHEN-BO、LIN,JHONG-BIN、HU,YUN-RUEI  
**Content:**  

This week, we have completed assembling the machine and started practicing. Since there haven't been many changes to the program, the most challenging part is the turning at the starting area. We have set up a practice mode specifically for practicing turns. There are a total of 32 combinations, divided into clockwise and counterclockwise turns. The red pieces are placed in slots 1 and 2, and they alternate with green pieces in slots 3 to 6. This is to test if there are any collisions with the blocks or if the machine passes through them from the wrong direction during the turns. Each combination will be tested three times. The diagram and practice conditions are as follows:

<div align="center">
<table>
<tr>
<th>Record Sheet(Success Count / Practice Count)<br> </th>
<th>Clockwise Diagram (Black Arrow indicates the direction of movement) <br></th>
<th>Counterclockwise Diagram (Black Arrow indicates the direction of movement)<br></th>
</tr>
<tr  align="center"> 
<td><img src="./img/9/point.png" alt="work_photo_2_2_0729" width=600 /></td>
<td><img src="./img/9/2.png" alt="work_photo_2_1_0729" width=250 /></td> 
<td><img src="./img/9/1.png" alt="work_photo_2_1_0729" width=250 /></td> 
</tr>
</table>
</div>


## 2023/09/25 ~ 2023/10/01
**Member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**Content:**

In the testing process, we encountered a fracture on the chassis, which was found to be due to the servo motor's shaft not being centered, resulting in a shorter gap on one side when drilling holes in the base plate. This lack of stability caused the fracture. Therefore, we made adjustments to ensure that both sides have the same gap, increasing the chassis's overall rigidity.

<div align=center>
<table>
<tr>
<th>Original </th>
<th>Improved version </th>
</tr><tr align=center>
<td><img src="./img/9/4.png" width=230></td>
<td><img src="./img/9/5.png"width=200></td>
</tr>
</table>
</div>

## 2023/10/02 ~ 2023/10/08
**Member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**Content:**

This week, our vehicle often had trouble making proper turns, and we later discovered that it was due to detecting the green blocks of the next section. This resulted in the last block being recorded as green, preventing it from making the turn. Afterward, we utilized the Y-axis to determine whether to record the blocks. Since our camera's coordinate system has (0,0) at the top-left corner, a higher Y-axis value indicates closer proximity. Thus, the condition for deciding whether to record the block is whether the block's Y-axis is greater than the set value. If this condition is met, we record the block's color; if not, we don't record it.

When the program is initiated, because the button is located on the circuit board and positioned beneath the camera, pressing the button without promptly retracting the hand could potentially interfere with the machine's operation. To address this issue, we have positioned the button on an extended wooden board, ensuring that even if the hand is not retracted in time, it will not disrupt the functioning of the vehicle.

<div align=center>
<table>
<tr align=center><th>Diagram</th>
<th>Original</th>
<th>Revised</th>
</tr>
<tr align=center><td><img src="./img/10/camera_screen.png" width=300></td>
<td><img src="./img/10/old_vehicle-removebg-preview.png" width=300></td>
<td><img src="./img/10/up.png" width=300></td>
</tr>
</table>
</div>

## 2023/10/09 ~ 2023/10/15
**Member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**Content:**

This week, the hardware of the machine has been completed. Next, it's all about continuous practice, program modifications, and report writing. The report has numerous issues with both text and formatting, making it challenging to clearly distinguish the content to be expressed. Therefore, we are using an indented format to differentiate. When there are sub-items under a main item, the sub-items are indented by one level, which allows for a clear distinction of the content of different items.

## 2023/10/16 ~ 2023/10/22
**Member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**Content:**

This week, we started making final adjustments. With only two weeks left before the competition, we started to speed up our work and began to write paper materials. We used PowerPoint to create them because PowerPoint allows for free layout, so we could fit all the necessary data into them. Although there was a lot of data, it could be well-organized through layout and would not be cluttered.

<div align="center">
<img src="./img/10/10-16.png" width=300>
</div>

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 

