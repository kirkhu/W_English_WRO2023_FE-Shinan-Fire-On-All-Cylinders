2023WRO Future Engineers Shinan Fire On All Cylinders  
====
# <div align="center">Hardware Assembly Instructions.</div>

- ## Components's Position 

- ## System Operation Process 


- ## Mechanical Structure 

- ### Circuit Board 


- ## Overview of Important Parts List. 
### NVIDIA Jeston Nano  
<table border=0 width=100% >
  <tr>
    <td >

__Specification:__ 
- It is equipped with a quad-core ARM Cortex-A57 CPU and a 128-core Maxwell GPU. 
- the total memory capacity of it has 4 Giga bytes,It operating system is 64-bit.
- The TransFlash card of it serves as the system’s main storage media.
- Equipped the USB interface device and the output of High Definition Multimedia Interface, it can adapt with several types of operating systems.  

__Usage:__ 
- Collects photos from the lens and carries out the image identifying, controls the vehicle to move ,and used to write the program.  
 </td>
    <td >
<img src="./img/jeston_nano.png" width = "400" height = "" alt="Jeston nano" align=center />   
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
 

### Button 
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
