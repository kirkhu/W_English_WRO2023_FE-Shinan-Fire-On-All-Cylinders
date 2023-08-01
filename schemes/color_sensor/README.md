![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
# <div align="center">Color sensor(顏色感應器)</div> 

<img src="./img/TCS34725.png" alt="TCS34725" width=200 style="display: block; margin: 0 auto;" />  

## English
- TCS34725 color sensor 
  - In the competition, vehicles need to demonstrate more functionalities than just turning. To achieve clockwise and counterclockwise turns, we must equip the vehicle with a color sensor to detect the colors of the lines on the ground and make appropriate judgments accordingly. Therefore, we must be particularly cautious in selecting the color sensor.
  - The TCS34725 color sensor has been chosen because it meets all the requirements of this competition. Firstly, it possesses outstanding sensing capabilities, allowing it to quickly and accurately identify the colors of the ground lines. 
  - Secondly, the sensor is thin and compact, enabling it to be placed close to the ground without interfering with the vehicle's movements.
  - The high precision of this sensor ensures that the vehicle can accurately recognize the colors of the ground lines and execute clockwise or counterclockwise turns as needed. 
  - This is a crucial factor in the vehicle's excellent performance and victory in the competition.In conclusion, the TCS34725 color sensor is a perfect fit for the requirements of this competition. 
  - Its slim design and highly accurate color recognition capabilities enable the vehicle to adapt flexibly to changes in ground lines, achieve clockwise and counterclockwise turns, and enhance its performance in the competition. 
- I encountered a bottleneck when using the color sensor to detect lines because I was unsure how to write a Python program to detect the values of blue and orange lines. With the guidance of my teacher, I successfully completed it. The partial code is as follows:
- During the implementation testing, it was discovered that we originally used a USB 180-degree adapter (as shown in the lower left image), but it was prone to colliding with obstacles, particularly building blocks. As a result, we made a change and switched to using a USB 3.0 90-degree adapter for the connection. This modification makes it less likely to accidentally hit obstacles when trying to avoid them.

## 中文
- TCS34725 顏色感測器 
 - 車輛在競賽中需要展現更多功能，而僅僅懂得轉彎是不夠的。為了實現順時針和逆時針的轉彎，我們必須裝備車輛以感測地上線的顏色，並相應地做出適當的判斷。因此，我們在挑選顏色感測器時，要特別謹慎。
 - TCS34725 顏色感測器被選中是因為它滿足了此次競賽的所有要求。首先，它具有出色的感測功能，可以快速而準確地辨識地面線條的顏色。其次，這款感測器相當薄且小巧，這意味著它可以輕鬆貼近地面，不會對車輛的運行造成任何干擾。
 - 該感測器的高度精確度確保了車輛可以準確識別地面線條的顏色，並且根據需要執行順時針或逆時針的轉彎動作。這是車輛在競賽中表現出色並獲得優勝的關鍵因素之一。
 - 綜上所述，TCS34725 顏色感測器是一款完美符合本次競賽要求的感測器。它的薄型設計和高度精確的顏色識別功能使車輛能夠靈活適應地面線條的變化，實現順時針和逆時針的轉彎，從而提升了車輛在競賽中的表現。
- 在使用顏色感測器偵測線時遇到瓶頸，因為不知道如何使用python撰寫程式來偵測藍、橘線的數值，經過老師指導，成功完成，片段程式如下。

<div align="center" width=100%>
<table >
<tr>
  <td align="center">Snippet of Code(片段程式)</td> 
  <td align="center">Function(定義成函數)</td>
</tr>
<tr>
  <td><img src="./img/5/TCS34725_code.png" alt="TCS34725" width=500/ > </td>
  <td><img src="./img/5/TCS34725_code_class.png" alt="TCS34725" width=500 />
  </td>  
  </tr>
</table>
</div>


# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  

