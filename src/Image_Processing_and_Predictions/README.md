<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Image Processing and Predictions</div> 

 - ### Image Processing  
    - When processing images, it is necessary to convert them to different color spaces for more efficient handling of specific tasks.  
    - We use the cv2.cvtColor function to convert the original RGB image to the HSV (Hue, Saturation, Value) color space.  
    - After the image is converted, we use the cv2.inRange function, where we set six HSV values: redMax, redMin, greenMin, greenMax, blueMin, and blueMax, to define the color ranges. The cv2.inRange function compares each pixel value in the HSV image with the specified HSV ranges. If the pixel value falls within this range, it will be retained; otherwise, it will be filtered out. This process allows us to obtain a filtered image.  

<div align="center">

|Adjusting the HSV Range Values for Red Color|Adjusting the HSV Range Values for Green Color|
|:----:|:----:|
|<img src="./img/red_HSV_value_range.png" width = "350" height = "" alt="red_HSV_value_range" align=center />|<img src="./img/green_HSV_value_range.png" width = "350" height = "" alt="green_HSV_value_range" align=center />|

|Obstacle Detection in Images|
|:----:|
|<img src="./img/Obstacle_detection.png" alt="Obstacle_detection" align=center />|
</div>


 - ### Image Predictions
    All image filtering functions can be found in the [vehicle_function.py](../Programming/Obstacle_Challenge/vehicle_function.py) file.

### Traffic Sign Avoidance  
- Using the filtered red and green color images, we obtain the X and Y coordinates, as well as the area of objects in the image. We determine which color (red or green) is closer based on the Y coordinate.  
- Then, we calculate the error value by subtracting the X coordinate of the closer traffic sign from the desired X coordinate where we want to avoid. Finally, we set this error value as the angle for the servo motor to turn, completing the avoidance maneuver around the traffic sign.  

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
