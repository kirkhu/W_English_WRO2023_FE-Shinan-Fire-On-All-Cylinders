![LOGO](../../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
## <div align="center">Open Challenge Code overview(資格賽程式概述)</div> 
- In the competition, the control of the vehicle's movement encompasses a series of actions, including image recognition, color identification, distance detection, motor rotation, and vehicle steering, among other intricate maneuvers. All of these precise and versatile controls are implemented using the __Python__ programming language.
- Through the built-in SSH or VNC functionalities of the Mobaxterm tool or RealVNC, we can easily establish connections to the Raspberry Pi, access its editor interface, initiate programming tasks, and perform real-time execution testing.

- 在競賽活動中，車輛行進的控制涵蓋了一系列的動作，包括影像辨識、顏色判別、距離偵測、馬達轉動以及車輛轉向等複雜操作。而所有這些精密而多變的操控，皆透過 __Python__ 程式語言來實現。
- 透過Mobaxterm工具內建的SSH或VNC功能或RealVNC，我們能夠輕鬆地連線到樹莓派，進入其編輯器界面，開展程式撰寫的工作並即時進行執行測試。


 <div align="center">
 <table>
 <tr align="center" > 
 <td><img src="../img/Mobaxterm_SSH_python.png" width="300" alt="Mobaxterm_SSH_python"> </td>
 <td><img src="../img/Mobaxterm_VNC_python.png" width="300" alt="Mobaxterm_VNC_python"> </td>
 <td><img src="../img/realVNC_python.png" width="300" alt="realVNC_python"> </td>
 </tr>
 <tr align="center">
 <td> Edit python of  Mobaxterm_SSH  
 </td>
 <td> Edit python of  Mobaxterm_VNC
 </td>
 <td>Edit python of RealVNC
 </td>
 </tr>
 </table>
 </div>

### [save_file](./save_file)
- The function of the save_file folder is to store the HSV range values for green and red colors from HSV_Test, along with color values related to white areas, orange lines, and blue lines.
- These data values will be used as the basis for image processing, image recognition, and determining whether to approach the next curve or proceed with straight or reverse movement decisions.

- save_file 資料夾的功能是用於儲存HSV_Test中綠色和紅色的HSV範圍值，以及與白色區域、橘色線條和藍色線條相關的顏色數值。  
- 這些數值資料將用於圖像處理、影像辨識及判斷是否到逹下一個彎道或順逆行走的判斷依據。

### [HSV_Test.py](./HSV_Test.py)
- The main functionality of "HSV_Test.py" is to adjust HSV range values for color filtering. Users can set the HSV range values specifically for green and red colors and record these settings in files named "HSV_Green.p" and "HSV_Red.p". Furthermore, the program stores these files in the "save_file" directory.

- HSV_Test.py 這個程式主要功能在於調整HSV範圍值，以進行顏色篩選的工作。使用者可以設定綠色和紅色的HSV範圍值，並將這些設定數值紀錄到名為HSV_Green.p與HSV_Red.p檔案並存入到"save_file"的資料夾中。

### [line_color_write.py](./line_color_write.py)
- The main functionality of the "line_color_write.py" program is to read the color values of white areas, orange lines, and blue lines, and save these values to a file named "color_sensor.p". Additionally, the program stores this file in the "save_file" directory.

- "line_color_write.py" 這個程式主要功能是用來讀取白色區域、橘色線條和藍色線條的顏色數值保存到名為color_sensor.p檔案並存入到"save_file"的資料夾中。

### Flowchart for the Configuration of Green Recording of Venue Environmental Value(場地環境值記綠設定流程圖)
 ![場地環境值記綠設定流程圖](../../System_Platform%20_Software/img/setup_recode.png)  

## [vehicle_function.py](./vehicle_function.py)
- "vehicle_function.py" is a library primarily designed to provide a variety of custom functions for controlling a vehicle. It utilizes a Raspberry Pi along with various sensors and devices to implement functions such as vehicle movement, image recognition, color identification, and servo motor control.

- "vehicle_function.py"，它是一個函式庫，這個程式主要是為了提供控制車輛的各式自定義函式。它使用樹莓派(Raspberry Pi)搭配各種感測器和裝置，實現車輛移動、影像辨識、顏色辨識和操控伺服馬達等函式。  

### [Open_Challenge.py](./Open_Challenge.py)
- The main functionality of "Open_Challenge.py" is to control a vehicle. It combines data from color sensors and LIDAR sensors to drive the vehicle's motors and perform steering maneuvers. Its objective is to enable the vehicle to accurately complete three laps around the designated course in both clockwise and counterclockwise directions, accomplishing a specific task goal.

- "Open_Challenge.py"這段程式碼的主要功能是控制車輛。它結合了顏色感測器和光達感測器所偵測的數值，來驅動車輛的馬達並進行轉向。其目的在於使車輛能夠準確地順逆時針繞場地三圈，完成特定的任務目標。

### Open Challenge Flow Chart(資格賽程式流程)

![flowchart_open](../img/flowchart_open.png)


# <div align="center">![HOME](../../../other/img/Home.png)[Return Home](../../../)</div>  
