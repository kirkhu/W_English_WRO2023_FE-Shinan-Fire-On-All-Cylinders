<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">Color Sensor Introduction</div> 
 __Color Sensor-TCS34725__
<div align="center">
<table>
<tr>  
<td>
<ul>
  <li>The TCS34725 color sensor has been chosen because it meets all the requirements of this competition. Firstly, it possesses outstanding sensing capabilities, allowing it to quickly and accurately identify the colors of the ground lines. Secondly, the sensor is thin and compact, enabling it to be placed close to the ground without interfering with the vehicle's movements.</li>
  <li>The TCS34725 color sensor has two primary functions on the vehicle:</li>
  <ol>
  <li>It can count laps around the track by detecting the blue and orange lines on the field.</li>
  <li>By detecting the sequence of blue and orange lines through the color sensor, it can determine whether the vehicle is currently moving in a clockwise or counterclockwise direction. This information is used by the program to calculate the number of clockwise and counterclockwise turns, ensuring that the vehicle can smoothly return to the starting area after completing 3 laps.</li>
  </ol>
</ul>
</td>
 <td width=250 ><img src="./img/TCS34725.png" alt="TCS34725" width="250" /> 
</td>
</tr>
</table> 
</div>
  
We encountered a bottleneck when using the color sensor to detect lines because we was unsure how to write a Python program to detect the values of blue and orange lines. 
        
With the guidance of my teacher, We successfully completed it.  
 __The partial code is as follows:__
#### Function
```
class TCS34725():
    def __init__(self):
        self.enable_selection()
        self.time_selection()
        self.gain_selection()
    def enable_selection(self):
        """Select the ENABLE register configuration from the given provided values"""
        ENABLE_CONFIGURATION = (TCS34725_REG_ENABLE_AEN | TCS34725_REG_ENABLE_PON)
        bus.write_byte_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_ENABLE | TCS34725_COMMAND_BIT, ENABLE_CONFIGURATION)
    def time_selection(self):
        """Select the ATIME register configuration from the given provided values"""
        bus.write_byte_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_ATIME | TCS34725_COMMAND_BIT, TCS34725_REG_ATIME_2_4)
        """Select the WTIME register configuration from the given provided values"""
        bus.write_byte_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_WTIME | TCS34725_COMMAND_BIT, TCS34725_REG_WTIME_2_4)
    def gain_selection(self):
        """Select the gain register configuration from the given provided values"""
        bus.write_byte_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_CONTROL | TCS34725_COMMAND_BIT, TCS34725_REG_CONTROL_AGAIN_1)
    def readluminance(self):
        """Read data back from TCS34725_REG_CDATAL(0x94), 8 bytes, with TCS34725_COMMAND_BIT, (0x80)
        cData LSB, cData MSB, Red LSB, Red MSB, Green LSB, Green MSB, Blue LSB, Blue MSB"""
        data = bus.read_i2c_block_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_CDATAL | TCS34725_COMMAND_BIT, 8 )        
  //# Convert the data
        cData = data[1] * 256 + data[0]
        red = data[3] * 256 + data[2]
        green = data[5] * 256 + data[4]
        blue = data[7] * 256 + data[6]        
  //# Calculate luminance
        luminance = (-0.32466 * red) + (1.57837 * green) + (-0.73191 * blue)
        return {'c' : cData, 'r' : red, 'g' : green, 'b' : blue, 'l' : luminance}
``` 
#### Snippet of Code  
```
data = bus.read_i2c_block_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_CDATAL | TCS34725_COMMAND_BIT, 8 )        
        # Convert the data
        cData = data[1] * 256 + data[0]
        red = data[3] * 256 + data[2]
        green = data[5] * 256 + data[4]
        blue = data[7] * 256 + data[6]        
# Calculate luminance
        luminance = (-0.32466 * red) + (1.57837 * green) + (-0.73191 * blue)
        return {'c' : cData, 'r' : red, 'g' : green, 'b' : blue, 'l' : luminance}
```
![image](https://github.com/kirkhu/WRO2023_FE-Shinan-Fire-On-All-Cylinders/assets/128333488/3e4aaa24-69fc-4b84-90dd-42c91de13b7b)


- #### Algorithm for Detecting Blue and Orange Lines Using a Color Sensor
  1. After the program is started, it will first read the three original values of the field lines: blue (blue_color = 15), orange (orange_color = 27), and white (white_color = 35).
  2. Then, the light sensor will read the current color value of the field and record it in the variable color_value. If the detected color value is greater than white (35), the vehicle can move forward directly. Otherwise, it indicates that it may be one of the blue (15) or orange (27) lines.
  3. Next, the program will add the color values of blue (15) and orange (27) and then divide them by 2 to obtain the middle value of the color value.
  4. Finally, the program will use the value of color_value to determine which line it is. If color_value is lower than the middle value, it indicates that it is a blue line (15); if color_value is higher than the middle value, it indicates that it is an orange line (27). When the blue and orange lines are known first, the vehicle can be determined to go clockwise or counterclockwise.
  <div align=center><img src="./img/color_sensor.png"></div>

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  

