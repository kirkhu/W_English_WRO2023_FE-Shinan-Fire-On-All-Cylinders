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
<th rowspan="2" width=300>圖片</th>
<th>Nvidia Jetson Nano</th>
<th>Raspberry Pi 4B</th>
</tr><tr>
<td><img src="./img/jeston_nano.png" width=200></td>
<td><img src="./img/raspberry_pi_4.png" width=200></td>
</tr><tr>
<th>Number of Pins 針腳數量</th>
<td>40P</td>
<td>40P</td>
</tr><tr>
<th>CPU</th>
<td>四核心 ARM® Cortex®-A57 MPCore 處理器</td>
<td>1.5GHz 64 位四核 ARM Cortex-A72 CPU</td>
</tr><tr>
<th>GPU</th>
<td>NVIDIA Maxwell™ 架構配備 128 個 NVIDIA CUDA® 核心</td>
<td>博通 VideoCore VI；H.265（4kp60 解碼）、<br>H264（1080p60 解碼、1080p30 編碼）
OpenGL ES 3.1、Vulkan 1.0</td>
</tr><tr>
<th>Storage Space 儲存空間</th>
<td>4 GB 64-bit LPDDR4</td>
<td>8GB LPDDR4-3200 SDRAM</td>
</tr><tr>
<th>Built-in Bluetooth and Wireless WiFi Connectivity內建藍芽與無線WIFI連接</th>
<td>需外接</td>
<td>有內建</td>
</tr><tr>
<th>Gflops(每秒浮點運算次數)</th>
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
