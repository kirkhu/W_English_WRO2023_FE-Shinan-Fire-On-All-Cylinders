# Electromechanical diagrams  

## Components's Position  

![image](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/schemes/Component%20position.jpg)  
## Pin Configuration  

### Raspberry Pi 4  
Specification:  
With the Advanced RISC Machine(ARM) produced by Broadcom Corporation , the total memory capacity of it is 8 Giga bytes.The TransFlash card of it serves as the system’s main storage media. equipped the USB interface device and the output of High Definition Multimedia Interface, it can adapt with several types of operating systems.  
  
Usage:  
Collects photos from the lens and carries out the image identifying, controls the vehicle to move ,and ,last but not least, used to write the program.  
![image](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/schemes/raspberry_pi_4.jpg)  

### GA25-370 DC reduction motor  
Specifications:  
No-load Speed: 126 rpm/m  
Reduction Ratio: 1:34  
Operating Voltage: 3 - 12V  
  
Usage:  
Driving the car's rear wheels to control the vehicle's forward and backward movements.  
![image](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/schemes/Motor.png)  

### MG90S servo motor  
Specifications:  
Controllable Rotation Angle: 90°  
Maximum Torque: 2.0 kg/cm (at 4.8V)  
Fastest Rotation Speed: 0.11 seconds (at 4.8V)  
Operating Voltage: 4.8V - 7.2V  
  
Usage:  
Control the steering mechanism to make the vehicle turn.  
![image](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/schemes/MG90S.jpg)  

### L293d motor controler  
Specifications:  
Wide power supply voltage range: 4.5V to 36V  
Output current per channel: 0.6mA per channel  
Peak output current: 1.2A  
  
Usage:  
Control the rotation direction of GA25-371 DC reduction motor.  
![image](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/schemes/l293d.jpg)  

### battery Lithium Polymer  
Specifications:  
Maximum Current: 45.5A  
Net Weight: Approximately 107g  
Rated Voltage: 11.1V  
  
Usage:  
Supplying power to Raspberry Pi and other electronic components.  
![image](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/schemes/battery.png)  

### button  
Specifications:  
Operating Voltage: 3.3V - 5.0V  
Number of Pins: 3  
Output Signal: Digital  
  
Usage:  
Send an activation signal before initiating the program.  
![image](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/schemes/button.png)  

### ADIO-DC36V5A Switching power adapter  
Specifications:  
Input Voltage: 4.0V - 38.0V  
Output Voltage: 1.25V - 36.0V  
Operating Frequency: 180Hz  
  
Usage:  
Stabilizing the power supplied by lithium batteries.  
![image](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/schemes/ADIO-DC36V5A.png)  

### TCS23725 RGB color sensor  
Specifications:  
Operating Voltage: 3.3V - 5.0V  
Interface: I2C interface  
  
Usage:  
Line recognition and counting the current number of revolutions.  
![image](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/schemes/TCS34725.jpg)  

### Raspberry Pi Camera V2  
Specifications:  
Viewing Angle: 160 degrees  
Interface: CSI (Camera Serial Interface)  
  
Usage:  
Collecting images for image recognition.  
![image](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/schemes/raspi%20camera%20V2.png)  
