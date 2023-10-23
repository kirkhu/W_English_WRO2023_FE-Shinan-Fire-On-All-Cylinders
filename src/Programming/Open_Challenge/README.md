<div align=center> <img src="../../../other/img/logo.png" width = 300 alt=" logo"> </div>

## <div align="center">Open Challenge Code Overview</div> 
- In the competition, the control of the vehicle's movement encompasses a series of actions, including image recognition, color identification, distance detection, motor rotation, and vehicle steering, among other intricate maneuvers. All of these precise and versatile controls are implemented using the __Python__ programming language.
- Through the built-in SSH or VNC functionalities of the Mobaxterm tool or RealVNC, we can easily establish connections to the Raspberry Pi, access its editor interface, initiate programming tasks, and perform real-time execution testing.
- Modules required for the operation of the program :

<div align="center">
<img src="../img/modles_NO_C.png" width="300" alt="Mobaxterm_SSH_python">
</div>

 <div align="center">
 <table>
 <tr align="center">
 <th> Edit python of  Mobaxterm_SSH  
 </th>
 <th> Edit python of  Mobaxterm_VNC
 </th>
 <th>Edit python of RealVNC
 </th>
 <tr align="center" > 
 <td><img src="../img/Mobaxterm_SSH_python.png" width="300" alt="Mobaxterm_SSH_python"> </td>
 <td><img src="../img/Mobaxterm_VNC_python.png" width="300" alt="Mobaxterm_VNC_python"> </td>
 <td><img src="../img/realVNC_python.png" width="300" alt="realVNC_python"> </td>
 </tr>

 </tr>
 </table>
 </div>

### [save_file](./save_file)
- The function of the "save_file" folder is to store color values related to the white area, orange lines, and blue lines.
- These data values will be used as the basis for image processing, image recognition, and determining whether to approach the next curve or proceed with straight or reverse movement decisions.



### [line_color_write.py](./line_color_write.py)
- The main functionality of the "line_color_write.py" program is to read the color values of white areas, orange lines, and blue lines, and save these values to a file named "color_sensor.p". Additionally, the program stores this file in the "save_file" directory.



### Flowchart for the Configuration of Green Recording of Venue Environmental Value
 ![Flowchart for the Configuration of Green Recording of Venue Environmental Value](../../System_Platform_Software/img/setup_recode.png)  

## [vehicle_function.py](./vehicle_function.py)
- "vehicle_function.py" is a library primarily designed to provide a variety of custom functions for controlling a vehicle. It utilizes a Raspberry Pi along with various sensors and devices to implement functions such as vehicle movement, image recognition, color identification, and servo motor control.



### [Open_Challenge.py](./Open_Challenge.py)
- The main functionality of "Open_Challenge.py" is to control a vehicle. It combines data from color sensors and LIDAR sensors to drive the vehicle's motors and perform steering maneuvers. Its objective is to enable the vehicle to accurately complete three laps around the designated course in both clockwise and counterclockwise directions, accomplishing a specific task goal.



### Open Challenge Flow Chart

<div align=center><img src="../img/open_challange_img.jpg"></div>


The LiDAR is initiated along with the program and the program continuously reads LiDAR data. When the program starts, it doesn't begin immediately; it goes through an initialization process. This involves setting the DC motor speed to 0, the servo motor angle to 0, and the default turning direction to counterclockwise.

Upon pressing the button, the program sets the DC motor speed to 90% and checks if the lap count is 0 and the LiDAR's right side distance is greater than 120. If this condition is met, it changes the turning direction to clockwise; otherwise, it proceeds. When the front distance is less than 60, the vehicle initiates a turn.

The program continually checks if it has completed three laps. If not, it detects if the current lap is finished. If it's not, it identifies whether this is the second lap. If it is, it checks if the front distance is greater than 60. If so, it proceeds straight until it's less than 60, then initiates a turning action, following which it goes straight for a certain distance to prevent LiDAR misreadings.

Other actions explained:
1. Continue straight until a certain time elapses: The program constantly reads the current time (referring to the program's execution time). If it exceeds a specified time, it checks if the LiDAR's left and right distances are both greater than 0 and less than 100. If within this range, it calculates the difference between the right and left values and adjusts the servo motor to center the vehicle. If not, it checks if the right-side distance falls between 0 and 120. If yes, it processes the left value; otherwise, it processes the right value. Finally, it outputs the value to the servo motor for centering.
2. Turning action: When the vehicle reaches a turning point, it executes a turn based on the specified turning angle until it completes the turn.
3. Continue straight until a front wall is detected: This action continuously checks if the front distance is less than 65 while proceeding straight. During this process, it also maintains road centering until a wall is detected, at which point it initiates a turn.


# <div align="center">![HOME](../../../other/img/Home.png)[Return Home](../../../)</div>  
