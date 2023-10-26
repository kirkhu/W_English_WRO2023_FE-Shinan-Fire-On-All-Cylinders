<div align="center"><img src="../../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Obstacle Challenge Code Overview</div>
 - In the competition, vehicle control involves complex operations such as image recognition, color identification, distance detection, motor rotation, and vehicle steering. All of these are implemented using the __Python__ programming language.
 - Through the built-in SSH or VNC functionality in Mobaxterm or using RealVNC, we can easily connect to the Raspberry Pi, access its editor interface, carry out programming tasks, and perform real-time execution tests.
 - The libraries introduced in this competition program are as follows.
 
```
   #Import the required modules
   import pigpio       #Raspberry Pi I/O Control Function Library
   import time         #Time Module
   import smbus        #I2C Manage  Module
   import struct       #Binary Data Packing and Unpacking Modul
   import os           #System Information Reading Module 
   import math         #Mathematical Calculation Module
   import cv2          #OpenCV  Module
   import threading    #Multithread Management  Module
   import pickle       #Serialization/Deserialization Modul
   import rospy        #ROS Python Commands Module
   import numpy as np  #Multidimensional Arrays and Matrix Operations Module
   import signal       #Exception Handling Module
   from sensor_msgs.msg import LaserScan  #ROS Data Structure Definitions
```
<div align="center">
</div>
 <table>
 <tr align="center">
 <th> Edit python of  Mobaxterm_SSH  
 </th>
 <th> Edit python of  Mobaxterm_VNC
 </th>
 <th>Edit python of RealVNC
 </th>
 </tr>
 <tr align="center" > 
 <td><img src="../img/Mobaxterm_SSH_python.png" width="300" alt="Mobaxterm_SSH_python"> </td>
 <td><img src="../img/Mobaxterm_VNC_python.png" width="300" alt="Mobaxterm_VNC_python"> </td>
 <td><img src="../img/realVNC_python.png" width="300" alt="realVNC_python"> </td>
 </tr>
 </table>
 </div>
 
 - ### Introduction to the Required Module Programs in the Operating Software:
   - #### Field Environment Value Recording Configuration Workflow
     ![Field Environment Value Recording Configuration Workflow](../../System_Platform_Software/img/setup_recode_obstacle.png)
     - #### [line_color_write.py](./line_color_write.py)
       - The main functionality of the "line_color_write.py" program is to read the color values of white areas, orange lines, and blue lines, and save these values to a file named "color_sensor.p". Additionally, the program stores this file in the "save_file" directory.       
       
     - #### [HSV_Detect.py](./HSV_Detect.py)
       - The main purpose of the 'HSV_Detect.py' program is to adjust HSV range values for color filtering. Users can configure the HSV range values for green and red and save these settings in files named 'HSV_Green.p' and 'HSV_Red.p,' which are stored in the 'save_file' folder.

     - #### [save_file](./save_file)
       - The function of the 'save_file' folder is to store color values related to the white area of the field, orange lines, and blue lines.
       - These numerical data are used for image processing, image recognition, and determining whether the next turn is reached or whether to walk forward or backward.

      
    - #### Obstacle Challenge Flow Chart
      ![flowchart_obstacle](../img/flowchart_obstacle.png)  
      - #### [vehicle_function.py](./vehicle_function.py)
        - "vehicle_function.py," which is the program library used in this competition, provides custom functions for vehicle movement, image recognition, color recognition, and controlling servo motors. These custom functions simplify complex procedures into subroutines for ease of debugging.
  
      - #### [Obstacle_Challenge.py](./Obstacle_Challenge.py)  
        - "Obstacle_Challenge.py" is the main program responsible for controlling the self-driving car. It reads the values detected by the color sensor, LIDAR sensor, and image recognition technology to drive the car's motors and achieve the goal of avoiding obstacles and completing specific tasks.

- ### Obstacle Challenge Program Operation Flowchart Description
  - After the vehicle starts, the program reads values from the LiDAR, color sensor, and captures images from the camera. Once the button is pressed, the program sets the DC motor speed to 60% and the vehicle continues moving forward. It keeps moving forward until the color sensor detects a line, at which point it initiates a turn. The program then checks whether it has completed 12 turns; if it has, the program ends. If not, it continues repeating the cycle of moving forward, avoiding obstacles, and turning when a wall is detected.   
     [Wall-Steering@Steering_overview](../../Image_Processing_and_Steering/Steering_overview#wall-steering)  
    - During the course of driving, the images captured by the camera undergo processing to obtain the X and Y coordinates, as well as the area of objects within the frame.  
   [Image_Processing](../../Image_Processing_and_Steering/Image_Processing/)     
  - Subsequently, by subtracting the X-coordinate of the nearer traffic sign from the X-coordinate of our intended target to avoid, we calculate an error value. Finally, we set this error value as the angle for the servo motor to turn, completing the avoidance maneuver around the traffic sign.  
    [obstacle-avoidance@Steering_overview](../../Image_Processing_and_Steering/Steering_overview#obstacle-avoidance)  
  - When the vehicle is in its second lap and encounters a green traffic signal at the end, it continues to proceed according to the regulations.
  - When the vehicle is in its second lap and encounters a red traffic signal at the end, it will turn around in the starting area, and then follow the regulations, completing 12 wall-turns before ending the program.  
  [slalom-steering@Steering_overview](../../Image_Processing_and_Steering/Steering_overview#slalom-steering)
  - __Subroutine Description:__   

    __1. Determining Vehicle Turn Direction Based on Blue and Orange Lines Subroutine：__    
    While the vehicle is in motion, if the color sensor detects a value lower than that of white (35), it indicates the presence of a blue line (15) or an orange line (27). Subsequently, the program calculates the midpoint value between the two lines as (15+27)/2 to determine the color of the line. If the value is lower than 21, it signifies the detection of a blue line, and the turning direction is set to counterclockwise. If the value is higher than 21, it signifies the detection of an orange line, and the turning direction is set to clockwise.
    
    __2. Vehicle Lane Centering Subroutine：__    
   While driving, it continuously checks whether the value read by the color sensor is greater than that of white (35). If it is, the vehicle continues moving forward. It also checks for the presence of obstacles in front. If an obstacle is detected, it performs the action to avoid the obstacle. If no obstacle is detected, it proceeds to center the Lidar. Lidar centering involves calculating the values on the left and right sides, subtracting the right value from the left value, and passing it to the servo motor to control the direction.

    __3. Vehicle Avoiding Obstacles Subroutine:__  
    It determines which has a larger area, the red block or the green block. If the red block is larger, it controls the servo motor to steer to the right and avoid the red block. If the green block is larger, it controls the servo motor to steer to the left and avoid the green block.
    
    __4. Vehicle Turning Subroutine：__ Continue turning until the specified angle is reached.
    
# <div align="center">![HOME](../../../other/img/Home.png)[Return Home](../../../)</div>  
