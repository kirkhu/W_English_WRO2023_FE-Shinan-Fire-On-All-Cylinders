<div align=center> <img src="../../../other/img/logo.png" width=300 alt=" logo"> </div>

## <div align="center">Steering Overview</div> 

 ### Wall Steering
  - While the vehicle is moving, it reads whether one side of the LiDAR walls is more than 100 cm away. If the right LiDAR reads a distance exceeding 100 cm, it indicates clockwise motion; otherwise, it is counterclockwise, and the vehicle performs a steering maneuver.
  - After determining the travel direction, read the distance between the LiDAR and the wall ahead. When the distance between the LiDAR and the wall is less than 55 cm, execute the turning action.
  - program code:
        ```
        if get_left_dis > 100:
            reverse = False
        else:
            reverse = True
        if get_mid_dis > 55:
            servo.angle(-40)
        ```

        |LiDAR Readings|
        |:---:|
        |<div align="center"> <img src="./img/read_lidar.png" width="300" alt="Detecting_nearby_obstacles"></div>|

### Obstacle Avoidance
 - While the vehicle is in motion, the camera lens transmits the video to the controller (Raspberry Pi), which performs calculations to obtain the X and Y coordinates and area of the objects in the image.
 - We will complete the avoidance of traffic signs through the following steps:  
   1. Use the Y coordinates to determine which block has a larger Y coordinate, indicating that it is closer.  
   2. Determine the color of the closer traffic sign and obtain its X coordinate.  
   3. Subtract the desired avoidance coordinate from the X coordinate of the closer  traffic sign and then multiply it by the avoidance coefficient to calculate the error value.  
   4. Set the steering angle of the servo motor to turn in the direction of the error value, completing the avoidance of the traffic sign.

  |Recognize Obstacles that are Closer in Distance|XY Coordinates of Obstacles|
  |:---:|:---:|
  |<div align="center"> <img src="./img/Detecting_nearby_obstacles.png" width="400" alt="Detecting_nearby_obstacles"></div>|<div align="center"> <img src="./img/Obstacle_XY_coordinates.png" width="250" alt="Obstacle_XY_coordinates"></div>|

  

 ### Slalom Steering

  - We will use the color sensor to detect the number of times the line is crossed and determine if it has exceeded the set count.
  - If the specified count is not reached, the system will continuously record the color of the nearest traffic sign until the number of line crossings is greater than or equal to the set count. At that point, it will stop recording colors.
  - After recording the color of the nearest traffic sign, the program will determine if the color is red. If the sign color is red, the system will set the servo motor angle for a right turn and continue turning until the vehicle is facing the specified direction. If the nearest traffic sign color is not red, the vehicle will continue moving forward.  
    
    |Display the Number of Lines and the Color of the Nearest Traffic Sign|
    |:---:|
    |<div align="center"> <img src="./img/detect_last_obstacle.png" width="300" alt="Obstacle_XY_coordinates"></div>|

# <div align="center">![HOME](../../../other/img/Home.png)[Return Home](../../)</div>  


