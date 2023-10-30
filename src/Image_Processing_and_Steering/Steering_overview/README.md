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

<div align=center>

  |Recognize Obstacles that are Closer in Distance|XY Coordinates of Obstacles|
  |:---:|:---:|
  |<div align="center"> <img src="./img/Detecting_nearby_obstacles.png" width="400" alt="Detecting_nearby_obstacles"></div>|<div align="center"> <img src="./img/Obstacle_XY_coordinates.png" width="250" alt="Obstacle_XY_coordinates"></div>|

</div>  


 ### Slalom Steering

  - We will use a color sensor to count the number of times the track lines are passed, to determine if it has entered the last area of the second lap.
  - Therefore, if the count reaches 7 times, it means that the car has entered the last area of the second lap.
  - If the car reaches the last area of the second lap, the system will use the camera to continuously record the color of the nearest traffic sign until the car leaves the area. At this point, the traffic sign color will no longer be recorded.
  - If the color of the last traffic sign in the last area of the second lap is green, the car will continue to go straight. If the color of the sign is red, the car will turn around in the next area (starting area).

 <div align="center">

|Display the number of lines and the color of the nearest traffic sign|Camera detects the color of the nearest traffic sign|
|:---:|:---:
|<div align="center"> <img src="./img/detect_last_obstacle.png" width="300" alt="detect_last_obstacle"></div>|<div align="center"> <img src="./img/camera_detects_color.png" width="300" alt="camera_detects_color"></div>|

</div>

# <div align="center">![HOME](../../../other/img/Home.png)[Return Home](../../../)</div>  


