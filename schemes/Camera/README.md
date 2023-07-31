![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
# <div align="center">Camera(攝影鏡頭)</div> 
為了能夠讓機器閃避積木，因此我們需要在車輛上加裝鏡頭，由於我們使用的控制器是raspberry pi，因此我們需要找與其相符的鏡頭，因此我們找到了三種鏡頭

1. raspberry pi camera Rev 1.3(傳感器:OmniVision OV5647)
2. raspberry pi camera Module V2(傳感器:Sony IMX219)
3. raspberry pi camera Module V3(傳感器:Sony IMX708)

由於V3與我們raspberry pi的作業系統不符，因此不採用，而1.3的偵率只有30p，而V2最高達到90p，因此最後我們選擇了raspberry pi camera Module V2。

| <img src="./img/V1.jpeg" width=200 alt="site"  /> | <img src="./img/V2.jpeg" width=200 alt="site" > | <img src="./img/V3.jpeg" width=200 alt="site" /> |
| :---: | :---: | :---: |
| raspberry pi camera Rev 1.3 | raspberry pi camera Module V2 | raspberry pi camera Module V3 |

在之後測試時，發現當汽車閃避積木時無法預判下一個積木的位置，因此我們將原本的鏡頭改裝成廣角，相比原本的72度的視野範圍，廣角的160度範圍大，能夠提前預判下一積木的位置

| 原本的 | 加裝廣角後 |
| :---: | :---: |
|<img src="./img/V2.jpeg" width=200 alt="site" >|<img src="./img/V2_wide_angle.jpeg" width=200 alt="site" >|
| <img src="./img/72angle.png" width=200 alt="site" > | <img src="./img/160angle.png" width=200 alt="site" > |

raspberry pi camera Module V2 可以選擇三種解析度

  1. 1080x640 幀率30p
  2. 640x320 幀率60p
  3. 320x240 幀率90p

當解析度為1080x640時，由於解析度高，因此程式需要耗費大量的時間去辨識積木，會降低程式的運算效率，而當解析度為320x240時，雖然預算效率極高，但是由於解析度過低，因而無法正常辨識積木，然而當解析度為640x320時，可以正常辨識積木，而且運算效率也不會太慢導致撞上積木

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  

