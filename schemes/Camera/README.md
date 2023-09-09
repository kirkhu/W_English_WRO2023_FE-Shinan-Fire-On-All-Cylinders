<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

2023WRO Future Engineers Shinan Fire On All Cylinders  
====
# <div align="center">Camera</div> 
- In order to enable the vehicle to avoid obstacles accurately, we need to install a camera module on the vehicle. Since we are using a Raspberry Pi as the controller, we need to find a compatible camera module for it. To do this, we referred to the camera module used by the American team in last year's competition and compared it with other camera modules in the same series. Here is the product information:

1. IMX 219-160 Camera for Jetson Nano(sensor: Sony IMX219)
2. raspberry pi camera Module V2(sensor: Sony IMX219)
3. raspberry pi camera Module V3(sensor: Sony IMX708)

- When selecting an appropriate camera, we went through a careful consideration and comparison process. We noticed that Module Rev 1.3 and V3 cameras are not compatible with the Jetson Nano, which posed a limitation in our selection process. After thoroughly researching multiple camera options, we ultimately decided to use IMX 219 Camera  as our chosen camera for image recognition.

#### Camera Module
<div align="center">
<table>
<tr align="center" >
<th rowspan="2">Model</th> 
<th >IMX 219-160 Camera for Jeston Nano</th>
<th >raspberry pi camera Module V2</th>
<th >raspberry pi camera Module V3</thd>
</tr>
<tr align="center">

<td><img src="./img/v1_width-angle.jpg" width=150 alt="V1"  /></td>
<td><img src="./img/V2.jpeg" width=200 alt="V2" ></td>
<td><img src="./img/V3.jpeg" width=200 alt="V3" /></td>
</tr>
<tr align="center">
<td>sensor</td>
<td>Sony IMX 219</td>
<td>Sony IMX 219</td>
<td>Sony IMX 708</td>
</tr>
<tr align="center">
<td>sensor resolution</td>
<td>3280 * 2464 pix</td>
<td>3280 * 2464 pix</td>
<td>4608 * 2592 pix</td>
</tr>
<tr align="center">
<td>FPS</td>
<td>90p MAX</td>
<td>90p MAX</td>
<td>120p MAX</td>
</tr>
</table>
</div>


- When purchasing this camera, it comes with a built-in wide-angle lens function, with a viewing angle of 160 degrees, which can better help us recognize building blocks.

#### wide-angle lens
<div align="center">
<table>
<tr align="center">
<th>With the wide-angle lens</th>
</tr>
<tr align="center">
<td><img src="./img/v1_width-angle.jpg" width=200 alt="site" >
</td>
</tr>
<tr align="center">
<td> <img src="./img/160angle.png" width=200 alt="site" ></td>
</tr>
</table>
</div>


- In the Jetson Nano program, it is possible to configure the resolution of the camera module. We conducted experiments with the following common resolutions.

1. 1080x640 FPS 30p
2. 640x320 FPS 60p
3. 320x240 FPS 90p
- In our experiments, we found that when the camera module's resolution was set to 1080x640, the high-resolution image processing demands led to a significant amount of time being spent on block recognition, resulting in a decrease in computational efficiency. On the other hand, when the resolution was set to 320x240, the computational efficiency was extremely high, but the low resolution hindered the proper recognition of the blocks. However, when we set the resolution to 640x320, we observed that the program could successfully recognize the blocks without compromising computational efficiency, thus avoiding collisions with the blocks. Therefore, we ultimately decided to set the camera module's resolution to 640x320.

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  

