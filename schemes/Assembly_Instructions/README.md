<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>


# <div align="center">Hardware Assembly Instructions.</div>

- ## Components's Position 
<img src="./img/introduct_new.png" alt="Components's Position (硬體結構配置)width=400" > 

- ## System Operation Process 
![image](./img/System_operation_process.png)

- The battery outputs 12V of power to the motor controller (L293D) and voltage regulator, which then controls the current to 5V before supplying power to the Raspberry Pi and various sensors.

- The LiDAR sensor uses TTL to USB conversion and transmits data to the Raspberry Pi via the ROS system from the front, right, and left sensors.

- The camera (Sony IMX219) transmits images to the Raspberry Pi, which then utilizes OPENCV for image recognition.

- The button is used to start the program, and the Raspberry Pi determines if it has been pressed based on the presence or absence of current through the button.

- The servo motor (MG90S) is used for controlling the direction of movement, and it utilizes PWM signals to control the rotation angle.

- The motor controller (L293D) is employed to control the forward and reverse motion of the DC motors, using PWM signals to adjust the current output to the motors.


- ## Mechanical Structure 
<div align="center">
<table>
  <tr>
      <th>Inner Structure Top View of the Overall Apparatus</th>
      <th>Middle Layer Structure Top View</th>
      <th>Top View of Vehicle Chassis</th>
      <th>Bottom View of Vehicle Chassis</th>
  </tr>
  <tr align="center">
     <td>  <img src="./img/up.png"  width = "400" alt="All vehicle up view" > </td><td><img src="./img/Middle_Layer_Top_View.png" width = "400" alt="Midium vehicle uo view" ></td><td><img src="./img/down_layer_top_view.jpg" width="400" alt="Top view of the vehicle chassis." ></td>
     <td><img src="./img/down.png" width="400" alt="Bottom view of the vehicle chassis." ></td>
  </tr>
</table>
</div>

- ### Circuit Board 
<div align="center">
<table>
  <tr align="center">
      <th> Circuit Board of Top View </th>
      <th> Circuit Board of Rear View </th>
  </tr>
  <tr align="center">
     <td> <img src="./img/circuit_up.jpg" width="300" alt="circuit_up.jpg"> </td>
     <td> <img src="./img/circuit_lower.jpg" width="300" alt="circuit_up.jpg"> </td>
  </tr>
</table>
</div>

- ## Overview of Important Parts List
### Raspberry Pi 4B 8G
<table border=0 width=100% >
  <tr>
    <td >

__Specification:__ 
- With the Advanced RISC Machine(ARM) produced by Broadcom Corporation 
- the total memory capacity of it has 1、2、4 or 8 Giga bytes.
- The TransFlash card of it serves as the system’s main storage media.
- equipped the USB interface device and the output of High Definition Multimedia Interface, it can adapt with several types of operating systems.  

__Usage:__ 
- Collects photos from the lens and carries out the image identifying, controls the vehicle to move ,and ,last but not least, used to write the program.  
 </td>
    <td >
<img src="./img/raspberry_pi_4.png" width = "400" height = "" alt=" Raspberry Pi 4B 8G (樹梅派4B 8G )" align=center />   
    </td>
  </tr>
</table>


### JGA25-370 DC reduction motor
<table border=0 width=100% >
  <tr>
    <td > 

__Specifications:__  
- No-load Speed: 640 rpm/m  
- Reduction Ratio: 1:34  
- Operating Voltage: 6 - 12V  

__Usage:__
- Driving the car's rear wheels to control the vehicle's forward and backward movements.  
 </td>
    <td >
<img src="./img/Motor.png" width = "250" height = "" alt="GA25-370 DC reduction motor 直流減速馬達" align=center />   
    </td>
  </tr>
</table>


### MG90S servo motor
<table border=0 width=100% >
  <tr>
    <td>  

__Specifications:__ 
- Controllable Rotation Angle: 90°  
- Maximum Torque: 2.0 kg/cm (at 4.8V)  
- Fastest Rotation Speed: 0.11 seconds (at 4.8V)  
- Operating Voltage: 4.8V - 7.2V  

__Usage:__
- Control the steering mechanism to make the vehicle turn.  
 </td>
    <td>
<img src="./img/MG90S.png" width = "200" height = "" alt="MG90S servo motor伺服馬達" align=center />  
    </td>
  </tr>
</table>

   

### L293d motor controler 
<table border=0 width=100% >
  <tr>
    <td>  

__Specifications:__ 
- Wide power supply voltage range: 4.5V to 36V  
- Output current per channel: 0.6mA per channel  
- Peak output current: 1.2A  

__Usage:__  
- Control the rotation direction of JGA25-371 DC reduction motor.  
 </td>
    <td>
<img src="./img/l293d.png" width = "200" height = "" alt="L293d motor controler" align=center />  
    </td>
  </tr>
</table>
  

### Li-Polymer 3S Battery 
<table border=0 width=100% >
  <tr>
    <td> 

__Specifications:__
- Maximum Current: 45.5A  
- Net Weight: Approximately 107g  
- Rated Voltage: 11.1V  

__Usage:__  
- Supplying power to Raspberry Pi and other electronic components.  
 </td>
    <td>
<img src="./img/lipo_battery.png" width = "400" height = "" alt="Li-Polymer 3S Battery(鋰聚合物電池 3S)" align=center />  
    </td>
  </tr>
</table>


### Button B3F-4055 
#### English
<table border=0 width=100% >
  <tr>
    <td>

__Specifications:__ 
- Operating Voltage: 3.3V - 5.0V  
- Number of Pins: 3  
- Output Signal: Digital  

__Usage:__
- Send an activation signal before initiating the program.  
 </td>
    <td>
<img src="./img/button.png" width = "200" height = "" alt="Button( B3F-4055 微動輕觸開關)" align=center />   
    </td>
  </tr>
</table>


### High Current 5A Constant Voltage Constant Current Buck Power Supply Module  
<table border=0 width=100% >
  <tr>
    <td> 

__Specifications:__ 
- Input Voltage: 4.0V - 38.0V  
- Output Voltage: 1.25V - 36.0V  
- Operating Frequency: 180Hz  

__Usage:__  
- Stabilizing the power supplied by lithium batteries.  
 </td>
    <td>
<img src="./img/ADIO-DC36V5A.png" width = "300" height = "" alt="High Current 5A Constant Voltage Constant Current Buck Power Supply Module(大電流5A恆壓恆流降壓電源模組)" align=center />   
    </td>
  </tr>
</table>

  

### TCS34725 RGB color sensor
#### English
<table border=0 width=100% >
  <tr>
    <td > 

__Specifications:__  

- Operating Voltage: 3.3V - 5.0V  
- Interface: I2C interface  

__Usage:__  
- Line color recognition 
- counting the current number of revolutions.  
 </td>
    <td>
<img src="./img/TCS34725.png" width = "200" height = "" alt="TCS34725  RGB color sensor顏色感測器" align=center />   
    </td>
  </tr>
</table>


### SNOY IMX 219 Lens module   
<table border=0 width="100%" >
  <tr>
    <td> 

__Specifications:__ 
- Viewing Angle: 160 degrees  
- Interface: CSI (Camera Serial Interface)  

__Usage:__  
- Collecting images for image recognition. 
  </td>
    <td >
<img src="./img/raspi_camera_V2.png" width = "200" height = "" alt="SNOY IMX 219 Lens module(SNOY IMX 219鏡頭模組) " align=center />    
    </td>
  </tr>
</table>


### D100 LiDAR 
#### English
<table border=0 width=100% >
  <tr>
    <td> 

__Specifications:__  
The D100 Developer Kit is built around the LiDAR LD14 core, complemented with various related accessories. 
- It utilizes triangulation technology for straightforward 360-degree full scanning, with a maximum range of 8 meters.
- The detection frequency is 2300 Hz, and the physical dimensions of the device are 96.3 x 59.8 x 38.8 mm.

__Usage:__  
- Used for detecting front, left, and right walls and keeping the machine centered in the lane. 
  </td>
    <td>
<img src="./img/Lidar-D100.png" width = "400" height = "" alt="D100 LiDAR(D100 光達)" align=center />      
    </td>
  </tr>
</table>



# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
