<div align=center> <img src="../../other/img/logo.png" width=300> </div>

2023WRO Future Engineers Fire On All Cylinders  
=====
## <div align="center">Software Platform Construction</div>
 
- ### Green Recording of Venue Environmental Value Configuration
![images](./img/setup_recode.png)  
#### [ColorDetect.py](../Programming/Open_Challenge/line_color_write.py)
- Open ColorDetect.py to start recording the values of white, orange, and blue colors, and save the values to the color_sensor.p file.
- Press the button to start recording the blue line. Move the color sensor back and forth over the white area of the field to record the minimum value of that area. Press the button again to stop recording and save the value of the white area to the color_sensor.p file.
- After finishing recording the white zone, press the button again to start recording the orange line. Place the color sensor on the orange line and move it back and forth on the track to record the minimum value of the orange line. Press the button again to stop recording the orange line, and save the recorded orange line value to the "color_sensor.p" file.
- After ending the recording of the orange line, press the button again to start recording the blue line. Place the color sensor on the blue line of the field and move it back and forth to record the minimum value of the blue line. Press the button again to end the recording of the blue line and save the value of the blue line to the "color_sensor.p" file.


<div align="center">

|Record the color values of the venue|
|:---:|
|<img src="./img/detect_color.png" width="200" alt="detect_color">|
</div>

#### [HSV_Detect.py](../Programming/Obstacle_Challenge/HSV_Test.py)
- After opening HSV_Detect.py, the following functions will be displayed corresponding to the keyboard number keys 1 to 5:  
1: Display the previously recorded green threshold values.  
2: Display the previously recorded red threshold values.  
3: Restore the currently adjusted threshold values to their default values.  
4: Record the adjusted green threshold values to the HSV_Green.p file.  
5: Record the adjusted red threshold values to the HSV_Red.p file.
- When adjusting the block threshold, we will place a block both at a distant and close distance to ensure that the adjusted threshold can recognize blocks at any distance. After the adjustment, press the number keys 4 or 5 to record the threshold into the HSV_Green.p or HSV_Red.p file.
- After adjusting the settings, you can press the number keys 1 and 2 to display the previous recorded thresholds for readjustment.

<div align="center">
 
|Adjust the green color threshold|Adjust the red color threshold|Display Button Functionality|
|:---:|:---:|:---:|
|<div align="center"> <img src="./img/Adjust_the_green_color_threshold.png" width="250" alt="Adjust_the_green_color_threshold"></div>|<div align="center"> <img src="./img/Adjust_the_red_color_threshold.png" width="250" alt="Adjust_the_red_color_threshold"></div>|<div align="center"> <img src="./img/Display_Button_Functionality.png" width="250" alt="Display_Button_Functionality"></div>|
</div>

- ### Programming Language
   - Python is a high-level, general-purpose, interpreted programming language created by Guido van Rossum in 1991. It is designed to be concise, readable, and comes with a rich standard library, allowing developers to write code quickly and efficiently.
  standard library, enabling developers to write code quickly and efficiently. 
   - Python is widely used in web development, scientific computing, data analysis, artificial intelligence, machine learning, and various other fields. It features dynamic typing, automatic garbage collection, and supports multiple platforms.
   - With an active community, Python has a plethora of third-party libraries and tools, making development even more convenient. Python has become a popular choice for both beginners and experienced developers.  

  __Therefore, we choose Python as the programming language for the development of the self-driving vehicle.__


### ${{\color{red} Introduction to  Mobaxterm}} $  
  - MobaXterm is a feature-rich cross-platform remote computing management tool. 
  - It integrates various network tools such as X11 server, remote computing, SSH, VNC, and more, providing an intuitive user interface for easy connection to remote servers in Windows environments.
  - MobaXterm also supports simultaneous management of multiple sessions, allowing users to switch and operate different remote connections effortlessly. This tool is highly valuable for system administrators, network engineers, and developers.

  __Therefore, we have chosen MobaXterm as the remote control tool for the Raspberry Pi in the self-driving vehicle.__  

- Software link：[Mobaxterm](https://mobaxterm.mobatek.net/) 
  

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
