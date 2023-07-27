![LOGO](../../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
# <div align="center">Obstacle Challenge Code overview(任務賽程式概述)</div>
## [save_file](./save_file)
- The function of the save_file folder is to store the HSV range values for green and red colors from HSV_Test, along with color values related to white areas, orange lines, and blue lines.
- These data values will be used as the basis for image processing, image recognition, and determining whether to approach the next curve or proceed with straight or reverse movement decisions.

- save_file 資料夾的功能是用於儲存HSV_Test中綠色和紅色的HSV範圍值，以及與白色區域、橘色線條和藍色線條相關的顏色數值。  
- 這些數值資料將用於圖像處理、影像辨識及判斷是否到逹下一個彎道或順逆行走的判斷依據。

## [HSV_Test.py](./HSV_Test.py)
- The main functionality of "HSV_Test.py" is to adjust HSV range values for color filtering. Users can set the HSV range values specifically for green and red colors and record these settings in files named "HSV_Green.p" and "HSV_Red.p". Furthermore, the program stores these files in the "save_file" directory.

- HSV_Test.py 這個程式主要功能在於調整HSV範圍值，以進行顏色篩選的工作。使用者可以設定綠色和紅色的HSV範圍值，並將這些設定數值紀錄到名為HSV_Green.p與HSV_Red.p檔案並存入到"save_file"的資料夾中。

## [line_color_write.py](./line_color_write.py)
- The main functionality of the "line_color_write.py" program is to read the color values of white areas, orange lines, and blue lines, and save these values to a file named "color_sensor.p". Additionally, the program stores this file in the "save_file" directory.

- "line_color_write.py" 這個程式主要功能是用來讀取白色區域、橘色線條和藍色線條的顏色數值保存到名為color_sensor.p檔案並存入到"save_file"的資料夾中。

## [vehicle_function.py](./vehicle_function.py)
- "vehicle_function.py" is a library primarily designed to provide a variety of custom functions for controlling a vehicle. It utilizes a Raspberry Pi along with various sensors and devices to implement functions such as vehicle movement, image recognition, color identification, and servo motor control.

- "vehicle_function.py"，它是一個函式庫，這個程式主要是為了提供控制車輛的各式自定義函式。它使用樹莓派(Raspberry Pi)搭配各種感測器和裝置，實現車輛移動、影像辨識、顏色辨識和操控伺服馬達等函式。  

## [Obstacle_Challenge.py](./Obstacle_Challenge.py)
- The main purpose of "Obstacle_Challenge.py" is to control a vehicle. It combines data from color sensors, LIDAR sensors, and image recognition techniques to drive the vehicle's motors, enabling it to navigate and avoid obstacles, accomplishing specific mission objectives.

- "Obstacle_Challenge.py"這段程式碼的主要功能是控制車輛。它結合了顏色感測器、光達感測器和影像辨識技術所偵測的數值，來驅動車輛的馬達，以達成車輛避開障礙物並完成特定任務的目標。


# <div align="center">![HOME](../../../other/img/Home.png)[Return Home](../../../)</div>  