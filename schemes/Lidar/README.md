<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">Lidar Selection</div> 
- Lidar, also known as Light Detection and Ranging, is a technology that uses laser pulses to measure distances and create maps. Lidar systems typically consist of lasers, receivers, computing devices, and navigation systems.

    __Working Principle:__
  - Emitting laser pulses: Lidar emits very short laser pulses through a laser. These pulses propagate at extremely high speeds and then return after reflection.  
  - Receiving reflected signals: The receiver of the Lidar records the time it takes for the laser pulses to return and measures the intensity of the light pulses. The time and intensity information of the reflections can be used to calculate the distance and characteristics of objects from the Lidar.  
  - Data processing: The computing device of the Lidar processes the received reflection data and calculates the position, shape, and movement of objects based on the measured time and the speed of light.

  __Applications:__  
  - Lidar has widespread applications in various fields, including but not limited to:  
    - Autonomous vehicles
    - Environmental sensing
    - Drones and aviation
    - Environmental monitoring
    - Military applications  
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
- The difference between ultrasonic sensors and Lidar is as follows:

  Ultrasonic sensors can only detect in one direction, typically limited to the front, and are mainly used for distance measurement and obstacle detection. In contrast, Lidar provides 360-degree panoramic coverage, enabling simultaneous sensing of the surroundings. It is utilized for high-precision environmental perception and map creation, reducing collision risks. Lidar finds extensive applications in autonomous driving, environmental modeling, and more. It surpasses ultrasonic sensors in providing comprehensive environmental information, making it superior for robot navigation.

- Issues encountered with different brands of Lidar:  
One problem with the D100 Lidar is its detection frequency, which is 2300 Hz, compared to the YDLidar X2 with 3000 Hz and X4 with 5000 Hz. The lower frequency results in a slower response time.  

__Due to unfamiliarity with the usage of ydlidar x4 and ydlidar x2, there were issues with detecting obstacles, leading to missing angles. Therefore, in this competition, we decided to utilize the D100 sensor for vehicle detection and measuring the distance to the arena walls. The results obtained using this sensor met our expectations.__

- #### The types of LiDAR used in the actual testing.
<div align="center">
    
|  Lidar D100    |  Ydlidar x4  |   Ydlidar x2    |      
| :----: | :----: | :----:|
|<img src="./img/Lidar-D100.png" width = "250" height = "" alt="lidar D100  " align=center />|<img src="./img/Lidar_X2.jpg" width = "250" height = "" alt=" ydlidar x4" align=center />|<img src="./img/Lidar_X4.jpg" width = "250" height = "" alt="ydlidar x2" align=center />|
</div> 

- #### The issues encountered with missing angles during the actual testing of ydlidar x4 and ydlidar x2 LiDAR.<br>

<div align="center">
 <table>
    <tr align="center">
    <th> Lidar D100</th>
    <th colspan="2">Ydlidar X4 X2</th>
    </tr>
    <tr align="center">
    <td><img src="./img/D100.png" width = "400" height = "" alt="D100"  /></td>
    <td><img src="./img/Lidar_X2_X4_error1.jpg" width = "400" height = "" alt="ydlidar x4 X2偵測缺角"  /></td>
    <td><img src="./img/Lidar_X2_X4_error.jpg" width = "400" height = "" alt="ydlidar x4 X2偵測缺角" /></td>
    </tr>
</table>  
 
</div> 

## Lidar Dudging Process


The lidar and the program start simultaneously. The lidar sends values for the front, right, and left directions to the Raspberry Pi through the ROS system. The Raspberry Pi calculates the difference between the right and left values to determine the machine's current direction. Then, it adjusts the servo motor to bring the machine back to the center position.
<div align=center><img src="./img/Lidar.png"></div>
# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
