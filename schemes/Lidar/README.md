<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center"> Lidar Selection </div> 
- ### Lidar Introduction
   - Lidar, also known as Light Detection and Ranging, is a technology that uses laser pulses to measure distances and create maps. Lidar systems typically consist of a laser, a receiver, computing equipment, and a navigation system.  
   - Lidar is widely used in various fields, including applications such as autonomous vehicles, environmental monitoring, drones, and aviation.  
   - Therefore, in this competition, we have chosen __Lidar__ as the sensor for detecting the distance between the vehicle and the walls.

- ### Comparison between Ultrasonic and Lidar  
  - Ultrasonic sensors can only detect in one direction, typically limited to the front, and are used for distance measurement and obstacle detection. Lidar, on the other hand, offers 360-degree coverage, allowing simultaneous sensing in all directions. It is used for high-precision environmental awareness, map creation, collision risk reduction, and finds extensive applications in areas such as autonomous driving and environmental modeling. Lidar excels over ultrasonic sensors in providing comprehensive environmental information, making it more advantageous in robot navigation. 

- ### Comparison of Different Lidars
  - We compared commonly available and cost-effective Lidar models in the market, including D100, YDLIDAR X2, and YDLIDAR X4, with the expectation of finding the best Lidar to be used as the sensor for this competition.  
  - The D100 has a detection frequency of 2300Hz, which is lower compared to the 3000Hz of YDLIDAR X2 and the 5000Hz of X4, making its response slightly slower.  
  - Due to unfamiliarity with the use of YDLIDAR X4 and YDLIDAR X2, we encountered issues with missing angles in obstacle detection. Therefore, for this competition, we decided to use the __D100__ sensor for detecting the distance of the vehicle from the field's edge walls.
 
   - #### Performance Testing of Low-Cost LiDARs Commonly Available in the Market
    
      |  Lidar D100    |  Ydlidar x4  |   Ydlidar x2    |      
      | :----: | :----: | :----:|
      |<img src="./img/Lidar-D100.png" width = "250"  alt="lidar D100  " align=center />|<img src="./img/Lidar_X2.jpg" width = "250" alt=" ydlidar x4" align=center />|<img src="./img/Lidar_X4.jpg" width = "250" alt="ydlidar x2" align=center />|


   - #### Missing Point Problems of LiDARs ydlidar x4, ydlidar x2, and D100

      <div align="center">
      <table>
         <tr >
         <th> Lidar D100</th>
         <th colspan="2"  >Ydlidar X4 X2</th>
         </tr>
         <tr >
         <td><img src="./img/D100.png" width = "400"  /></td>
         <td><img src="./img/Lidar_X2_X4_error1.jpg" width = "400"  /></td>
         <td><img src="./img/Lidar_X2_X4_error.jpg" width = "400" /></td>
         </tr>
      </table>   
      </div> 

- ### LiDAR-Controlled Steering Detection Process

   - This is the workflow for using Lidar in this competition.
   - When the LiDAR and program are started, the LiDAR will use the ROS system to detect the distance between the vehicle and the walls in front, right, and left sides. The distance data will be transmitted to the Raspberry Pi controller for computation and judgment. The controller will then determine which side the vehicle is leaning towards. It will also transmit the steering value to the front steering servo motor to control the vehicle's travel and steering.  

   <img src="./img/Lidar.png">  

   - ####  Using LIDAR to Center on the Road
      - Using LIDAR to measure the distances between the object's right and left sides and the walls, we can calculate the error values for both sides.  
      - By multiplying these error values with coefficients, we can obtain the angle to center the servo motor on the road.  
         
         |LIDAR Detects Surrounding Walls|LIDAR Readings|
         |:---:|:---:|
         |<img src="./img/LIDAR_Detecting_Walls.png" width = "350" alt="LIDAR_Detecting_Walls" align=center />|<img src="./img/LIDAR_readings.png" width = "300" alt="LIDAR_readings" align=center />|

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
