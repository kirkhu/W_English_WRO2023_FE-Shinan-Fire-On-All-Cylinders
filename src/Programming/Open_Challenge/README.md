![LOGO](../../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
# <div align="center">Open Challenge Code Introduce</div> 
## save_file
The function of the "save_file" folder is to store the HSV range values for the green and red colors from HSV_Test, along with the color values of the white region, orange lines, and blue lines.

save_file這個資料夾的功能是儲存HSV_Test綠色和紅色的HSV範圍值與白色區域、橘色線條和藍色線條的顏色數值。
## [HSV_Test.py](./HSV_Test.py)
The function of the program "HSV_Test" is to adjust the HSV range values for color filtering. It allows you to set the range values for green and red colors and save them to "save_file".

HSV_Test這個程式個功能是用來調整HSV範圍值進行顏色篩選，可設定綠色和紅色範圍值並並保存到save_file。
## [line_color_write.py](./line_color_write.py)
The program "HSV_Test" is designed to read the color values of the white areas, orange lines, and blue lines. After reading these color values, it saves them to "save_file".

HSV_Test這個程式個功能是用來讀取白色區域、橘色線條和藍色線條的顏色數值並保存到save_file。
## [vehicle_function.py](./vehicle_function.py)
This code is used to control a vehicle using a Raspberry Pi along with various sensors and devices to perform functions such as vehicle movement, image recognition, color detection, and controlling servo motors.

這段程式是用來控制車輛的程式，使用樹莓派(Raspberry Pi)搭配各種感測器和裝置，進行車輛移動、影像辨識、顏色辨識、操控伺服馬達等功能。

## [Open_Challenge.py](./Open_Challenge.py)
This program enables the vehicle to navigate intelligently based on sensor data and make appropriate actions in different situations, achieving more complex autonomous control capabilities.

這個程式使車輛能夠根據感測器的數據進行智能導航，並能夠在不同情況下做出適當的行動，實現了較為複雜的自主控制功能。

## 圖像預測
所有圖像過濾可以在[vehicle_function.py](./Obstacle_Challenge/vehicle_function.py)中找到。
### 圖像處理
處理圖像時，需要將其轉換到不同的色彩空間，以便更有效地進行特定任務。我們使用cv2.cvtColor函數將原始的RGB圖像轉換為HSV（色調、飽和度、明度）色彩空間。轉換圖像後使用cv2.inRange函數，我們會設定六個HSV值，即redMax、redMin、greenMin、greenMax、blueMin和blueMax，設定顏色範圍。cv2.inRange函數比較HSV圖像中的每個像素值與指定的HSV範圍，如果像素值在這個範圍內，則將保留這個像素，否則將其過濾掉。這樣我們就可以得到一個經過過濾的圖像。

### 交通標誌閃避
使用過濾後的紅色綠色圖像，獲得圖像在畫面中的X、Y座標與面積。我們會利用Y座標判斷是哪一個顏色較近，再使用較近的交通標誌X座標減去我們所想要閃避到的座標計算出誤差值，將誤差值設定成伺服馬達轉向角度完成交通標誌閃避。

# <div align="center">![HOME](../../../other/img/Home.png)[Return Home](../../../)</div>  
