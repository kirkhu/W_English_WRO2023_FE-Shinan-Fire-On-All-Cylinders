![logo](../../other/img/logo.png)2023WRO Future Engineers Shinan Fire On All Cylinders  
====
# <div align="center">Controller</div> 
在控制器上我們有兩個選擇，Jetson Nano 和 Raspberry Pi ，這兩個控制器的差別還是挺多的，不管是尺寸、Gflops(每秒浮點運算次數)、CPU配置等，以下是兩者的規格比較

We have two controller options, Jetson Nano and Raspberry Pi. There are significant differences between these two controllers, including factors such as size, Gflops (floating-point operations per second), CPU configuration, and more. Here is a comparison of the specifications for both:

<div align=center>
<table>
<tr>
<th rowspan="2">圖片</th>
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
<th>內建藍芽與無線WIFI連接</th>
<td>需外接</td>
<td>有</td>
</tr><tr>
<th>Gflops(每秒浮點運算次數)</th>
<td>472</td>
<td>13.5</td>
</tr>
</table>
</div>

After the national competition, we attempted to switch to the budget-efficient Jetson Nano. While it provided extremely fast image recognition, the reading speed of the color sensor was significantly slower. This might have been due to the heavy workload on image recognition or possibly because the I2C was also being used by the PWM controller and the DC motor controller, causing delays in color sensor readings. As a result, the vehicle often couldn't turn accurately. Consequently, we reverted to using the Raspberry Pi as the main controller. Although the image recognition speed is slower, it allows the vehicle to operate smoothly.
在全國賽比完之後，我們嘗試改用預算效率較快的Jetson Nano，雖然影像辨識速度極快，但是讀取顏色感測器的速度卻很慢，可能是效能都用在影像辨識，也有可能是因為I2C也用在PWM控制器和直流馬達控制器上，造成顏色感測器讀取延遲，常常無法正確轉彎，因此我們將主控制器改回樹梅派，雖然影像辨識速度較慢，但是可以車輛可以正常行駛。
- 因此我們最後選擇使用樹梅派作為我們的主要控制器
- Therefore, we ultimately chose to use a Raspberry Pi as our primary controller.


# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
