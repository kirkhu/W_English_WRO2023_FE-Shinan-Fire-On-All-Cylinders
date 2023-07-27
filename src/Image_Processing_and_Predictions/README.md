![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
# <div align="center">Image_Processing_and_Predictions</div> 

## Image Predictions 圖像預測
所有圖像過濾可以在[vehicle_function.py](../Programming/Obstacle_Challenge/vehicle_function.py)中找到。

All image filtering functions can be found in the [vehicle_function.py](../Programming/Obstacle_Challenge/vehicle_function.py)file.

### Image processing 圖像處理
- When processing images, it is necessary to convert them to different color spaces for more efficient handling of specific tasks. We use the cv2.cvtColor function to convert the original RGB image to the HSV (Hue, Saturation, Value) color space. After the image is converted, we use the cv2.inRange function, where we set six HSV values: redMax, redMin, greenMin, greenMax, blueMin, and blueMax, to define the color ranges. The cv2.inRange function compares each pixel value in the HSV image with the specified HSV ranges. If the pixel value falls within this range, it will be retained; otherwise, it will be filtered out. This process allows us to obtain a filtered image.

- 處理圖像時，需要將其轉換到不同的色彩空間，以便更有效地進行特定任務。我們使用cv2.cvtColor函數將原始的RGB圖像轉換為HSV（色調、飽和度、明度）色彩空間。轉換圖像後使用cv2.inRange函數，我們會設定六個HSV值，即redMax、redMin、greenMin、greenMax、blueMin和blueMax，設定顏色範圍。cv2.inRange函數比較HSV圖像中的每個像素值與指定的HSV範圍，如果像素值在這個範圍內，則將保留這個像素，否則將其過濾掉。這樣我們就可以得到一個經過過濾的圖像。

|調整紅色HSV數值範圍|調整綠色HSV數值範圍|
|---|---|
|<img src="./img/red_HSV_value_range.png" width = "350" height = "" alt="red_HSV_value_range" align=center />|<img src="./img/green_HSV_value_range.png" width = "350" height = "" alt="green_HSV_value_range" align=center />|

|影像辨識障礙物|
|---|
|<img src="./img/Obstacle_detection.png" alt="Obstacle_detection" align=center />|

### Traffic sign avoidance 交通標誌閃避
- Using the filtered red and green color images, we obtain the X and Y coordinates, as well as the area of objects in the image. We determine which color (red or green) is closer based on the Y coordinate. Then, we calculate the error value by subtracting the X coordinate of the closer traffic sign from the desired X coordinate where we want to avoid. Finally, we set this error value as the angle for the servo motor to turn, completing the avoidance maneuver around the traffic sign.

- 使用過濾後的紅色綠色圖像，獲得圖像在畫面中的X、Y座標與面積。我們會利用Y座標判斷是哪一個顏色較近，再使用較近的交通標誌X座標減去我們所想要閃避到的座標計算出誤差值，將誤差值設定成伺服馬達轉向角度完成交通標誌閃避。

    - Image Preprocessing
    - Wall Steering
    - Pillar Steering
    - Final Steering
  - PARK Control Panel

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
