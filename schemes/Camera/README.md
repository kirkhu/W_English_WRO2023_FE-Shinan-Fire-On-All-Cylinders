![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
# <div align="center">Camera(攝影鏡頭)</div> 
- In order to enable the vehicle to avoid obstacles accurately, we need to install a camera module on the vehicle. Since we are using a Raspberry Pi as the controller, we need to find a compatible camera module for it. To do this, we referred to the camera module used by the American team in last year's competition and compared it with other camera modules in the same series. Here is the product information:
- 為了讓車輛能夠正確地閃避積木，我們需要在車輛上安裝一個鏡頭模組。由於我們使用的控制器是 Raspberry Pi，因此我們需要尋找與其相容的鏡頭模組。為此，我們參考了去年美國隊伍使用的鏡頭模組，並尋找了同一系列的鏡頭模組進行比較。以下是產品資訊：

1. raspberry pi camera Rev 1.3(傳感器:OmniVision OV5647)
2. raspberry pi camera Module V2(傳感器:Sony IMX219)
3. raspberry pi camera Module V3(傳感器:Sony IMX708)

- Considering that V3 is not compatible with our existing Raspberry Pi operating system, we decided not to use that version. Additionally, the detection rate of version 1.3 is only 30p, whereas the V2 version can reach a maximum of 90p. Therefore, we ultimately chose the Raspberry Pi Camera Module V2 for our project. Through experimentation, we found that the V2 version has the best recognition performance.
- 考慮到V3與我們現有的Raspberry Pi作業系統不相容，我們決定不使用該版本。而1.3版本的偵測率僅為30p，相比之下，V2版本的偵測率最高達到90p。因此，我們最終選擇了Raspberry Pi相機模組V2作為我們的選擇。經過實驗，我們發現V2版本具有最佳的辨識效果。

#### Camera Module(攝影模組)
<div align="center">
<table>
<tr align="center" >
<th rowspan="2">Model(型號)</th> 
<th >raspberry pi camera Rev 1.3</th>
<th >raspberry pi camera Module V2</th>
<th >raspberry pi camera Module V3</thd>
</tr>
<tr>

<td align="center"><img src="./img/V12.jpeg" width=200 alt="V1"  /></td>
<td align="center"><img src="./img/V2.jpeg" width=200 alt="V2" ></td>
<td align="center"><img src="./img/V3.jpeg" width=200 alt="V3" /></td>
</tr>
<td align="center">sensor</td>
<td align="center">Omnivision OV547</td>
<td align="center">Sony IMX 219</td>
<td align="center">Sony IMX 708</td>
</tr>
<td align="center">sensor resolution</td>
<td align="center">2592 * 1944 pix</td>
<td align="center">3280 * 2464 pix</td>
<td align="center">4608 * 2592 pix</td>
</tr>
<td align="center">FPS幀率</td>
<td align="center">30p MAX</td>
<td align="center">90p MAX</td>
<td align="center">120p MAX</td>
</tr>
</table>
</div>



- During subsequent testing, we found that the vehicle was unable to anticipate the position of the next block while avoiding obstacles. This posed a challenge for the vehicle's obstacle avoidance strategy. As a result, we decided to modify the original camera and convert it into a wide-angle lens. Compared to the original 72-degree field of view, the wide-angle lens provides a 160-degree field of view, allowing us to anticipate the position of the next block in advance. This improvement has enhanced the vehicle's obstacle avoidance effectiveness.
- 在之後的測試中，我們發現當車輛閃避積木時無法預先得知下一個積木的位置，這對於車輛的避障策略造成了困擾。因此，我們決定將原本的鏡頭進行改裝，將其轉換成廣角鏡頭。相較於原本的72度視野範圍，廣角鏡頭提供了160度的視野範圍，能夠讓我們提前預測下一個積木的位置，從而改善車輛的避障效果。

#### wide-angle lens(廣角鏡)
<div align="center">
<table>
<tr>
<th align="center"> Without the wide-angle lens(未加廣角鏡)</th> 
<th align="center">With the wide-angle lens 巳加廣角鏡</th>
</tr>
<tr>
<td align="center"><img src="./img/V2.jpeg" width=200 alt="site" ></td>
<td align="center"><img src="./img/V2_wide_angle.jpeg" width=200 alt="site" >
</td>
</tr>
<td align="center"><img src="./img/72angle.png" width=200 alt="site" ></td>
<td align="center"> <img src="./img/160angle.png" width=200 alt="site" ></td>
</tr>
</table>
</div>


- In the Raspberry Pi program, it is possible to configure the resolution of the camera module. We conducted experiments with the following common resolutions.
- 在raspberry pi的程式中可以設定鏡頭模組的解析度，我們將實驗以下常見的解析度

1. 1080x640 幀率30p
2. 640x320 幀率60p
3. 320x240 幀率90p
- In our experiments, we found that when the camera module's resolution was set to 1080x640, the high-resolution image processing demands led to a significant amount of time being spent on block recognition, resulting in a decrease in computational efficiency. On the other hand, when the resolution was set to 320x240, the computational efficiency was extremely high, but the low resolution hindered the proper recognition of the blocks. However, when we set the resolution to 640x320, we observed that the program could successfully recognize the blocks without compromising computational efficiency, thus avoiding collisions with the blocks. Therefore, we ultimately decided to set the camera module's resolution to 640x320.
- 在我們的實驗發現，當相機模組的解析度設定為1080x640時，由於高解析度的影像處理需求，程式需要花費大量的時間來辨識積木，這導致了程式的運算效率降低。另一方面，當解析度設定為320x240時，雖然運算效率極高，但由於解析度過低，導致無法正常辨識積木。然而，當解析度設定為640x320時，我們觀察到可以正常辨識積木，而且運算效率也不會太慢，避免了車輛撞上積木的問題。因此，我們最終選擇將相機模組的解析度設定為640x320。- 
# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  

