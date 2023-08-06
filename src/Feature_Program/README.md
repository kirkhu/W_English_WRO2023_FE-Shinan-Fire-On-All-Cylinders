![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
## <div align="center">Feture Program </div>

- The most distinctive aspect of our program lies in the image recognition segment. Here is the excerpt of the program content  
([A snippet of code fromvehicle_function.py](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/src/Programming/Obstacle_Challenge/vehicle_function.py))
- 在我們的程式中，最有特色的莫過於是閃避積木的地方，以下是程式內容  
  ([vehicle_function.py 的片段程式](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/src/Programming/Obstacle_Challenge/vehicle_function.py))


- Identify obstacle coordinates and calculate the center point of the obstacle(辨識障礙物座標並計算出障礙物中心點)

        ```
        def color_detect(self,raw_img, hsv_img, lower, upper):
            mask = cv2.inRange(hsv_img, lower, upper)  
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            find_x = -1
            find_y = -1
            max_y = 0
            find_area = 0
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                x, y, w, h = cv2.boundingRect(contour)
                x = int(x + w / 2)
                y = int(y + h / 2)
                if y > max_y and area > block_detect_min_area:
                    find_area = area
                    max_y = y
                    find_x = x
                    find_y = y
            return raw_img, find_x, find_y, find_area
        ```


# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  