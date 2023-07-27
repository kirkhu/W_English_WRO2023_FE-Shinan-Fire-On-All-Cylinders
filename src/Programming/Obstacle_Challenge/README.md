![LOGO](../../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
# <div align="center">Obstacle Challenge Code Introduc</div>
## save_file(./save_file)
- The function of the save_file folder is to store the HSV range values for green and red colors from HSV_Test, along with color values related to white areas, orange lines, and blue lines.
- These data values will be used as the basis for image processing, image recognition, and determining whether to approach the next curve or proceed with straight or reverse movement decisions.

- save_file 資料夾的功能是用於儲存HSV_Test中綠色和紅色的HSV範圍值，以及與白色區域、橘色線條和藍色線條相關的顏色數值。  
- 這些數值資料將用於圖像處理、影像辨識及判斷是否到逹下一個彎道或順逆行走的判斷依據。

## [HSV_Test.py](./HSV_Test.py)
- The purpose of the HSV_Test program is to adjust the HSV range values for color filtering. It allows the user to set the HSV range values for green and red colors and save them to the save_file.

- HSV_Test.py 這個程式主要功能在於調整HSV範圍值，以進行顏色篩選的工作。使用者可以設定綠色和紅色的HSV範圍值，並將這些設定數值保存到名為    並存入到"save_file"的資料夾中。

## [line_color_write.py](./line_color_write.py)
- The main functionality of the "line_color_write.py" program is to read the color values of white areas, orange lines, and blue lines, and save these values to a file named "color_sensor.p". Additionally, the program stores this file in the "save_file" directory.

- line_color_write.py 這個程式主要功能是用來讀取白色區域、橘色線條和藍色線條的顏色數值保存到名為color_sensor.p檔案並存入到"save_file"的資料夾中。

## [vehicle_function.py](./vehicle_function.py)
This code is used to control a vehicle using a Raspberry Pi along with various sensors and devices to perform functions such as vehicle movement, image recognition, color detection, and controlling servo motors.

這段程式是用來控制車輛的自行定義函式，使用樹莓派(Raspberry Pi)搭配各種感測器和裝置，進行車輛移動、影像辨識、顏色辨識、操控伺服馬達等功能。
## [Obstacle_Challenge.py](./Obstacle_Challenge.py)
This piece of code is a Python program designed to control a vehicle. It utilizes several modules and sensors to perform various tasks, including image recognition, obstacle avoidance, and servo motor control, among other functions.

這段程式碼是一個用於控制車輛的Python程式，它使用了多個模組和感測器來執行各種任務，包括影像辨識、閃避障礙物、操控伺服馬達等功能。


## Image Predictions 圖像預測
所有圖像過濾可以在[vehicle_function.py](./Obstacle_Challenge/vehicle_function.py)中找到。
### Image processing 圖像處理
When processing images, it is necessary to convert them to different color spaces for more efficient handling of specific tasks. We use the cv2.cvtColor function to convert the original RGB image to the HSV (Hue, Saturation, Value) color space. After the image is converted, we use the cv2.inRange function, where we set six HSV values: redMax, redMin, greenMin, greenMax, blueMin, and blueMax, to define the color ranges. The cv2.inRange function compares each pixel value in the HSV image with the specified HSV ranges. If the pixel value falls within this range, it will be retained; otherwise, it will be filtered out. This process allows us to obtain a filtered image.

處理圖像時，需要將其轉換到不同的色彩空間，以便更有效地進行特定任務。我們使用cv2.cvtColor函數將原始的RGB圖像轉換為HSV（色調、飽和度、明度）色彩空間。轉換圖像後使用cv2.inRange函數，我們會設定六個HSV值，即redMax、redMin、greenMin、greenMax、blueMin和blueMax，設定顏色範圍。cv2.inRange函數比較HSV圖像中的每個像素值與指定的HSV範圍，如果像素值在這個範圍內，則將保留這個像素，否則將其過濾掉。這樣我們就可以得到一個經過過濾的圖像。

### Traffic sign avoidance 交通標誌閃避
Using the filtered red and green color images, we obtain the X and Y coordinates, as well as the area of objects in the image. We determine which color (red or green) is closer based on the Y coordinate. Then, we calculate the error value by subtracting the X coordinate of the closer traffic sign from the desired X coordinate where we want to avoid. Finally, we set this error value as the angle for the servo motor to turn, completing the avoidance maneuver around the traffic sign.

使用過濾後的紅色綠色圖像，獲得圖像在畫面中的X、Y座標與面積。我們會利用Y座標判斷是哪一個顏色較近，再使用較近的交通標誌X座標減去我們所想要閃避到的座標計算出誤差值，將誤差值設定成伺服馬達轉向角度完成交通標誌閃避。

### 

# <div align="center">![HOME](../../../other/img/Home.png)[Return Home](../../../)</div>  