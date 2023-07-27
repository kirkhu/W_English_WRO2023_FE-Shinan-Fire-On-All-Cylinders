![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
# <div align="center">Assembly_Instructions(硬體組裝說明)</div>

## Components's Position (硬體結構配置)
<img src="./img/introduct.png" alt="介紹圖">  

## System operation process(系統運作流程)
![image](./img/System_operation_process.png)  

|        |        |        |  
| :----: | :----: | :----: |  
|  |  |  |
| <img src="./img/up.jpg"  width = "600" alt="Image" > | <img src="./img/inside.jpg" width = "600" alt="Image" > | <img src="./img/up_view.png" width="600" alt="Image" > |  
|        |        |        |  
| :----: | :----: | :----: |  
| <img src="./img/circuit_up.jpg"  width = "600" alt="Image" > | <img src="./img/circuit_lower.jpg" width = "600" alt="Image" > |

## Part list  


### Raspberry Pi 4B(8G)  
Specification:  
With the Advanced RISC Machine(ARM) produced by Broadcom Corporation , the total memory capacity of it has 1、2、4 or 8 Giga bytes.The TransFlash card of it serves as the system’s main storage media. equipped the USB interface device and the output of High Definition Multimedia Interface, it can adapt with several types of operating systems.  

Usage:  
Collects photos from the lens and carries out the image identifying, controls the vehicle to move ,and ,last but not least, used to write the program.  
<img src="./img/raspberry_pi_4.png" width = "150" height = "" alt="樹梅派" align=center />  



### GA25-370 DC reduction motor  
Specifications:  
No-load Speed: 126 rpm/m  
Reduction Ratio: 1:34  
Operating Voltage: 3 - 12V  

Usage:  
Driving the car's rear wheels to control the vehicle's forward and backward movements.  
<img src="./img/Motor.png" width = "150" height = "" alt="馬達圖" align=center />  

### MG90S servo motor  
Specifications:  
Controllable Rotation Angle: 90°  
Maximum Torque: 2.0 kg/cm (at 4.8V)  
Fastest Rotation Speed: 0.11 seconds (at 4.8V)  
Operating Voltage: 4.8V - 7.2V  

Usage:  
Control the steering mechanism to make the vehicle turn.  
<img src="./img/MG90S.png" width = "200" height = "" alt="伺服馬達" align=center />   

### L293d motor controler  
Specifications:  
Wide power supply voltage range: 4.5V to 36V  
Output current per channel: 0.6mA per channel  
Peak output current: 1.2A  

Usage:  
Control the rotation direction of GA25-371 DC reduction motor.  
<img src="./img/l293d.png" width = "200" height = "" alt="顏色感測器" align=center />   

### Lipo 3S Battery(鋰電池 3S)
Specifications:  
Maximum Current: 45.5A  
Net Weight: Approximately 107g  
Rated Voltage: 11.1V  

Usage:  
Supplying power to Raspberry Pi and other electronic components.  
<img src="./img/lipo_battery.png" width = "300" height = "" alt="電池" align=center />   

### Button( B3F-4055 微動輕觸開關)
Specifications:  
Operating Voltage: 3.3V - 5.0V  
Number of Pins: 3  
Output Signal: Digital  

Usage:  
Send an activation signal before initiating the program.  
<img src="./img/button.png" width = "200" height = "" alt="按鈕" align=center />   

### Xl4015 5A DC/DC Switching power adapter  
Specifications:  
Input Voltage: 4.0V - 38.0V  
Output Voltage: 1.25V - 36.0V  
Operating Frequency: 180Hz  

Usage:  
Stabilizing the power supplied by lithium batteries.  
<img src="./img/ADIO-DC36V5A.png" width = "250" height = "" alt="降壓板" align=center />   

### TCS34725  RGB color sensor  
Specifications:  
Operating Voltage: 3.3V - 5.0V  
Interface: I2C interface  

Usage:  
Line recognition and counting the current number of revolutions.  
<img src="./img/TCS34725.png" width = "150" height = "" alt="顏色感測器" align=center />   

### Raspberry Pi Camera V2  
Specifications:  
Viewing Angle: 160 degrees  
Interface: CSI (Camera Serial Interface)  

Usage:  
Collecting images for image recognition.  
<img src="./img/raspi_camera_V2.png" width = "175" height = "" alt="相機" align=center />   

### D100 LiDAR(D100 光達)
Specification 規格:  

The D100 Developer Kit is built around the LiDAR LD14 core, complemented with various related accessories. 
- It utilizes triangulation technology for straightforward 360-degree full scanning, with a maximum range of 8 meters.
- The detection frequency is 2300 Hz, and the physical dimensions of the device are 96.3 x 59.8 x 38.8 mm.

D100 開發者套裝是以光達 LiDAR LD14為核心再搭配相關零配件組合而成。  
- 採用三角測距技術，簡易360度全掃描
- 最大測距為8公尺。  
- 偵測頻率 2300 HZ，外觀尺寸 96.3*59.8*38.8 mm  

Usage:

Used for detecting front-facing walls and keeping the machine centered in the lane.  
用於偵測前方牆壁及使機器維持在車道中央  
<img src="./img/Lidar-D100.png" width = "175" height = "" alt="光達" align=center />  

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
