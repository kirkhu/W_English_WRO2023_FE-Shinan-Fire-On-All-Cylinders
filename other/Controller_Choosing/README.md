<div align=center><img src="../img/logo.png" width=300></div>

# <div align="center">Controller Selection </div> 

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
<td>40P</td>
<td>40P</td>
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
<td>Expensive</td>
<td>Cheap</td>  
</tr>
</table>
</div>

- At the beginning of the competition, we chose the Raspberry Pi, which is more affordable and has AI image recognition capabilities, as the controller for our self-driving car. However, we found that the Raspberry Pi controller had insufficient image recognition performance.   
- Therefore, after the national competition in Taiwan, we attempted to switch to the Jetson Nano as the controller for our self-driving car, as it offered significantly faster image recognition processing.  
- However, after actual experiments, although the image recognition speed is very fast, the speed of reading the color sensor is very slow, which leads to the inability to make timely judgments and make correct operations, which delays the turning of the vehicle and makes the vehicle unable to drive correctly. This may be a problem of our insufficient technical capabilities.
- To ensure it wouldn't affect upcoming competitions, we reverted to using the Raspberry Pi as the controller. Although its image recognition speed is slower, it allows the vehicle to operate reliably. Additionally, we are implementing other solutions to address the Raspberry Pi's limitations in image recognition performance.  

- __In conclusion, we have chosen to use the Raspberry Pi as the controller for our self-driving car in this competition.__
# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
