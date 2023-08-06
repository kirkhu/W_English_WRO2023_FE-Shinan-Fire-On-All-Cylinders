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
    - To navigate around obstacles, we need to determine the position of the obstacles in the camera's field of view in order to calculate the angle the servo motor needs to turn.
    - 為了閃避障礙物，我們需要的知道障礙物在鏡頭畫面中的位置，來得知伺服馬達需要轉的角度
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
  - Since obstacles at the sides might not be detected by the camera immediately, but the vehicle hasn't completely cleared them, it's necessary to continue for a certain duration until the obstacles are fully avoided.
  - 由於障礙物在側邊時鏡頭辨識不到，但是還沒完全通過，因此需要持續一段時間直到完全閃過障礙物
    ```
    def dodgeblock_to_time(set_time, set):
    set_reset = time.time()
    while time.time() - set_reset < set_time:
        dodgeblock_control(set)
        time.sleep(0.001)
    ```

- Recognize Clockwise and Counterclockwise(辨識順逆時針)
  - The mission instructions mention that if the last obstacle of the second round is red, the third round must be driven in reverse, while if it's green, there's no need for a reverse. Therefore, the obstacle color will be continuously recorded until the second round is counted, at which point the color detection will stop. The program will then determine whether the color is red or green.
  - 任務說明有提到如果第二圈的最後一個障礙物是紅，第三圈就必須反向行駛，是綠色則不用，因此會一直紀錄障礙物顏色，直到數到第二圈就會停止讀取，透過程式判斷是紅色還是綠色
    ```
    def direction_detect():
    global reverse, line_count
    print('direction detect')
    while color > line_middle:
        dodgeblock_control(0)
    low_color = 100
    while color < line_middle:
        dodgeblock_control(0)
        if color < low_color:
            low_color = color
    line_count = 1
    if low_color < color_direction_middle:
        print('blue line')
        print('Low:', low_color)
    else:
        reverse = False
        print('orange line')
        print('Low:', low_color)
    ```

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  