<div align=center><img src="../img/logo.png" width=300></div>

# <div align="center">Controller Choosing </div> 

- Two commonly available low-cost controllers capable of handling AI image recognition are the Jetson Nano and Raspberry Pi.
- They are suitable for various applications, including programming education in the field of education, smart home devices, self-driving cars, DIY projects, and more. This compact yet powerful microcomputer has become the top choice for electronics enthusiasts, students, and professionals.  
- We will compare the controller's specifications and prices to help us choose the right controller for our self-driving car.

## Controller Comparison
Here is a specification comparison between the two:

<div align=center>
<table>
<tr>
<th rowspan="2" width=300>Photo</th>
<th>Nvidia Jetson Nano</th>
<th>Raspberry Pi 4B</th>
</tr><tr>
<td><img src="./img/jeston_nano.png" width=200></td>
<td><img src="./img/raspberry_pi_4.png" width=200></td>
</tr><tr>
<th>Number of Pins</th>
<th>40P</th>
<th>40P</th>
</tr><tr>
<th>CPU</th>
<td>Quad-core ARM® Cortex®-A57 MPCore</td>
<td>1.5GHz 64-bit Quad-core ARM Cortex-A72 CPU</td>
</tr><tr>
<th>GPU</th>
<td>NVIDIA Maxwell™ architecture with 128 NVIDIA CUDA®  cores</td>
<td>Broadcom VideoCore VI<br> H.265 (4kp60 decode)<br> H264 (1080p60 decode, 1080p30 encode) OpenGL ES 3.1<br> Vulkan 1.0</td>
</tr><tr>
<th>Storage Spac</th>
<td>4 GB 64-bit LPDDR4</td>
<td>8GB LPDDR4-3200 SDRAM</td>
</tr><tr>
<th>Built-in Bluetooth and Wireless WiFi Connectivity</th>
<td>Requires external Bluetooth and wireless WiFi connectivity</td>
<td>Built-in</td>
</tr><tr>
<th>Gflops</th>
<td>472</td>
<td>13.5</td>
</tr><tr>
<th>Price</th>
<th>Expensive</th>
<th>Cheap</th>  
</tr>
</table>
</div>

After the national competition, we attempted to switch to the budget-efficient Jetson Nano. While it provided extremely fast image recognition, the reading speed of the color sensor was significantly slower. This might have been due to the heavy workload on image recognition or possibly because the I2C was also being used by the PWM controller and the DC motor controller, causing delays in color sensor readings. As a result, the vehicle often couldn't turn accurately. Consequently, we reverted to using the Raspberry Pi as the main controller. Although the image recognition speed is slower, it allows the vehicle to operate smoothly.

__Therefore, we ultimately chose to use a Raspberry Pi as our primary controller.__


# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
