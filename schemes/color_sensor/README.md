<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">Color Sensor Introduction</div> 
 __Color Sensor-TCS34725__
<div align="center">
<table>
<tr>  
<td>
 <li>In the competition, vehicles need to demonstrate more functionalities than just turning. To achieve clockwise and counterclockwise turns, we must equip the vehicle with a color sensor to detect the colors of the lines on the ground and make appropriate judgments accordingly. Therefore, we must be particularly cautious in selecting the color sensor. </li>
 <li>The TCS34725 color sensor can count laps by detecting the blue and orange lines on the track.</li> 
 <li>The TCS34725 color sensor has been chosen because it meets all the requirements of this competition. Firstly, it possesses outstanding sensing capabilities, allowing it to quickly and accurately identify the colors of the ground lines. Secondly, the sensor is thin and compact, enabling it to be placed close to the ground without interfering with the vehicle's movements.</li> 
 <li>The high precision of this sensor ensures that the vehicle can accurately recognize the colors of the ground lines and execute clockwise or counterclockwise turns as needed.  </li>
</td>
 <td width=250 ><img src="./img/TCS34725.png" alt="TCS34725" width="250" /> 
</td>
</tr>
</table> 
</div>
  
In summary, the TCS34725 color sensor is a sensor perfectly suited for the requirements of this competition. Its slim design and highly accurate color recognition capabilities enable the vehicle to adapt flexibly to changes in ground lines, achieving both clockwise and counterclockwise turns. This significantly enhances the performance of the vehicle in the competition.

We encountered a bottleneck when using the color sensor to detect lines because we was unsure how to write a Python program to detect the values of blue and orange lines. 
  With the guidance of my teacher, We successfully completed it.  
- __The partial code is as follows:__

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

#### Algorithm for Detecting Blue and Orange Lines Using a Color Sensor
1. After the program is started, it will first read the three original values of the field lines: blue (blue_color = 15), orange (orange_color = 27), and white (white_color = 35).
2. Then, the light sensor will read the current color value of the field and record it in the variable color_value. If the detected color value is greater than white (35), the vehicle can move forward directly. Otherwise, it indicates that it may be one of the blue (15) or orange (27) lines.
3. Next, the program will add the color values of blue (15) and orange (27) and then divide them by 2 to obtain the middle value of the color value.
4. Finally, the program will use the value of color_value to determine which line it is. If color_value is lower than the middle value, it indicates that it is a blue line (15); if color_value is higher than the middle value, it indicates that it is an orange line (27). When the blue and orange lines are known first, the vehicle can be determined to go clockwise or counterclockwise.
  <div align=center><img src="./img/color_sensor.png"></div>

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  

