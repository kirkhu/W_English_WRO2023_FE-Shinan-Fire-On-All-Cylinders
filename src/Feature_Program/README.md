![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
## <div align="center">Feture Program </div>

- The most distinctive aspect of our program lies in the image recognition segment. Here is the excerpt of the program content  
([A snippet of code fromvehicle_function.py](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/src/Programming/Obstacle_Challenge/vehicle_function.py))
- 在我們的程式中，最有特色的莫過於是閃避積木的地方，以下是程式內容  
  ([vehicle_function.py 的片段程式](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/src/Programming/Obstacle_Challenge/vehicle_function.py))

- Read obstacle HSV values(讀取障礙物HSV數值)
    - To avoid obstacles, we need to accurately identify the color of the obstacles.
    - 為了閃避障礙物，我們需要清楚的辨識出障礙物的顏色
        ```
        def block_color_read():
            global green_lower, green_upper, red_lower, red_upper
            with open('save_file/HSV_Green.p', mode='rb') as f:
                file = pickle.load(f)
            g_lower = file['Lower']
            g_upper = file['Upper']
            print('Green_Lower:' + str(g_lower))
            print('Green_Upper:' + str(g_upper))
            
            with open('save_file/HSV_Red.p', mode='rb') as f:
                file = pickle.load(f)
            r_lower = file['Lower']
            r_upper = file['Upper']
            print('Red_Lower:' + str(r_lower))
            print('Red_Upper:' + str(r_upper))
            
            red_lower = np.array(r_lower, np.uint8) 
            red_upper = np.array(r_upper, np.uint8)
            green_lower = np.array(g_lower, np.uint8)
            green_upper = np.array(g_upper, np.uint8)
        ```

- Identify obstacle coordinates and calculate the center point of the obstacle(辨識障礙物座標並計算出障礙物中心點)
    - To avoid obstacles, we need to determine the position of the obstacles in the camera's field of view to calculate the required angle for steering and avoidance.
    - 為了閃避障礙物，我們需要的知道障礙物在鏡頭畫面中的位置，來得知轉彎閃避的幅度
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
- Avoid obstacles until the field line is detected(閃避障礙物直到測到場地線)
  - When detecting the line indicating a turn, it's essential to halt image recognition to prevent mistaking the line for an obstacle.
  - 當測到轉彎處的線時，需要停止影像辨識，以免將線辨識成障礙物  
    ```
    def dodgeblock_to_line(set):
        while color > line_middle:
            dodgeblock_control(set)
            time.sleep(0.001)
    ```

- Translation in English: Avoid obstacles until the time is up(閃避障礙物直到時間到)
  - Since obstacles located at the sides might not be detected by the camera's vision, directly turning back could lead to a collision with the obstacle. Therefore, it is necessary to continue moving forward for a certain duration until the obstacle is completely avoided.
  - 由於鏡頭辨識不到在側邊的障礙物，因此直接轉回來會撞到障礙物，因此需要持續前進一段時間直到完全閃過障礙物
    ```
    def dodgeblock_to_time(set_time, set):
        set_reset = time.time()
        while time.time() - set_reset < set_time:
            dodgeblock_control(set)
            time.sleep(0.001)
    ```
- Detect if a turnaround is required and execute it(偵測是否需要進行迴轉並執行)
  - 在任務賽的第二圈，若最後一個障礙物顏色為紅色，則第三圈需要反方向行駛，若為綠色同方向繼續行駛
    ```
    direction_detect()
        for count in range(2):
        #前進方向為逆時針
            if reverse == True:
                if count == 1:
                    dodgeblock_to_line(0)
                dodgeblock_to_time(2, -90)
                dodgeblock_to_line(-90)
                dodgeblock_to_time(2, -180)
                dodgeblock_to_line(-180)
                dodgeblock_to_time(2, -270)
                #若障礙物為紅色，進行迴轉
                if record_box == 'red' and count == 1:
                    dodgeblock_to_line(-270)
                    motor.power(70)
                    red_turn(-90, 25, 0.3)
                    motor.power(50)
                    dodgeblock_to_time(1, -90)
                #若為綠色則繼續逆方向行駛
                else:
                    dodgeblock_to_line(-270)
                    dodgeblock_to_time(2, 0)
            else:
            #前進方向為順時針
                if count == 1:
                    dodgeblock_to_line(0)
                dodgeblock_to_time(2.5, 90)
                dodgeblock_to_line(90)
                dodgeblock_to_time(2.5, 180)
                dodgeblock_to_line(180)
                dodgeblock_to_time(2.5, 270)
                #若為障礙物為紅色，進行迴轉
                if record_box == 'red' and count == 1:
                    dodgeblock_to_line(270)
                    motor.power(70)
                    red_turn(90, 25, 0.3)
                    motor.power(50)
                    dodgeblock_to_time(1, 90)
                #若為綠色則繼續逆方向行駛
                else:
                    dodgeblock_to_line(270)
                    dodgeblock_to_time(2, 0)
    ```

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  