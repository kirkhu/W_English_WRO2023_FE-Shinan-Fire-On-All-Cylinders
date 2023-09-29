<div align=center><img src="../img/logo.png" width=300></div>

2023WRO Future Engineers Shinan Fire On All Cylinders  
====
# <div align="center">Controller Selection </div> 

- We have two controller options, Jetson Nano and Raspberry Pi. There are significant differences between these two controllers, including factors such as size, Gflops (floating-point operations per second), CPU configuration, and more. Here is a comparison of the specifications for both:

<div align=center>
<table>
<tr>
<th rowspan="2">Picture</th>
<th>Nvidia Jetson Nano</th>
<th>Raspberry Pi 4B</th>
</tr><tr>
<td><img src="./img/jeston_nano.png" width=200></td>
<td><img src="./img/raspberry_pi_4.png" width=200></td>
</tr><tr>
<th>Number of Pins</th>
<td>40P</td>
<td>40P</td>
</tr><tr>
<th>CPU</th>
<td>Quad-core ARM® Cortex®-A57 MPCore processor</td>
<td>1.5GHz 64-bit Quad-core ARM Cortex-A72 CPU</td>
</tr><tr>
<th>GPU</th>
<td>NVIDIA Maxwell™ architecture with 128 NVIDIA CUDA® cores</td>
<td>Broadcom VideoCore VI<br> H.265 (4kp60 decode)<br> H264 (1080p60 decode, 1080p30 encode) OpenGL ES 3.1<br> Vulkan 1.0</td>
</tr><tr>
<th>Storage Space </th>
<td>4 GB 64-bit LPDDR4</td>
<td>8GB LPDDR4-3200 SDRAM</td>
</tr><tr>
<th>Built-in Bluetooth and wireless WiFi connectivity</th>
<td>Requires external Bluetooth and wireless WiFi connectivity</td>
<td>Built-in</td>
</tr><tr>
<th>Gflops</th>
<td>472</td>
<td>13.5</td>
</tr>
</table>
</div>

- After the national competition, we attempted to switch to the budget-efficient Jetson Nano. While it provided extremely fast image recognition, the reading speed of the color sensor was significantly slower. This might have been due to the heavy workload on image recognition or possibly because the I2C was also being used by the PWM controller and the DC motor controller, causing delays in color sensor readings. As a result, the vehicle often couldn't turn accurately. Consequently, we reverted to using the Raspberry Pi as the main controller. Although the image recognition speed is slower, it allows the vehicle to operate smoothly.

__Therefore, we ultimately chose to use a Raspberry Pi as our primary controller.__

- Introduction to Two Types of Controllers can be viewed at the following link. 
[Jetson Nano](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/tree/main/other/Jetson%20Nano)

[Raspberry Pi 4B](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/tree/main/other/Raspberry_Pi)



# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 