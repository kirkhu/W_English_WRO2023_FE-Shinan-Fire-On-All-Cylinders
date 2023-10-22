<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">Color Sensor Introduction</div> 
- __TCS34725 Color Sensor__
<div align="center">
<table>
<tr>  
<td>
 1.In the competition, vehicles need to demonstrate more functionalities than just turning. To achieve clockwise and counterclockwise turns, we must equip the vehicle with a color sensor to detect the colors of the lines on the ground and make appropriate judgments accordingly. Therefore, we must be particularly cautious in selecting the color sensor.
 2.The TCS34725 color sensor has been chosen because it meets all the requirements of this competition. Firstly, it possesses outstanding sensing capabilities, allowing it to quickly and accurately identify the colors of the ground lines. Secondly, the sensor is thin and compact, enabling it to be placed close to the ground without interfering with the vehicle's movements.
 3.The high precision of this sensor ensures that the vehicle can accurately recognize the colors of the ground lines and execute clockwise or counterclockwise turns as needed.  
</td>
 <td width=250 ><img src="./img/TCS34725.png" alt="TCS34725" width="250" /> 
</td>
</tr>
</table> 
</div>
  
This is a crucial factor in the vehicle's excellent performance and victory in the competition.In conclusion, the TCS34725 color sensor is a perfect fit for the requirements of this competition.Its slim design and highly accurate color recognition capabilities enable the vehicle to adapt flexibly to changes in ground lines, achieve clockwise and counterclockwise turns, and enhance its performance in the competition.  

We encountered a bottleneck when using the color sensor to detect lines because we was unsure how to write a Python program to detect the values of blue and orange lines. 
  With the guidance of my teacher, We successfully completed it. The partial code is as follows:

<div align="center" width=100%>
<table >
<tr align="center">
  <th>Snippet of Code</th> 
  <th>Function</th>
</tr>
<tr>
  <td><img src="./img/TCS34725_code.png" alt="TCS34725" width=500/ > </td>
  <td><img src="./img/TCS34725_code_class.png" alt="TCS34725" width=500 />
  </td>  
  </tr>
</table>
</div>

## Color Sensor Judging Process  
  1.After the program is initiated, it activates the color sensor to continuously detect the color values on the ground.   
  2.If the detected color value is lower than that of white, it indicates that it's one of the lines, either blue or orange.  
  3.At this point, comparing the color value to the midpoint between the blue and orange line values determines which line it is.  
  4.If the value is lower than the midpoint, it's the blue line, and if it's higher, it's the orange line.
  <div align=center><img src="./img/color_sensor.png"></div>

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  

