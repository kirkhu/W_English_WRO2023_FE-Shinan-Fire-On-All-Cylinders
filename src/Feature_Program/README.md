![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
## <div align="center">Feture Program </div>

- The most distinctive aspect of our program lies in the image recognition segment. Here is the excerpt of the program content  
([A snippet of code fromvehicle_function.py](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/src/Programming/Obstacle_Challenge/vehicle_function.py))
- 在我們的程式中，最有特色的莫過於是影像辨識的地方，以下是程式內容  
  ([vehicle_function.py 的片段程式](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/blob/main/src/Programming/Obstacle_Challenge/vehicle_function.py))

- Set up the Black mask area(設定遮罩)
    - Black mask area at the top of the image screen
    - 影像畫面上方黑色遮罩範圍  
        ```
        image_black_area = 310
        ```
    - Black mask area at the bottom of the image frame
    - 影像畫面下方黑色遮罩範圍
        ```
        image_black_area_down = 400 
        ```
- Adjusting Image Brightness(影像畫面亮度調整)
    - During the obstacle avoidance process, the environment plays a crucial role, and we cannot control the brightness of the surroundings. Therefore, we need to adjust our settings based on the current environmental conditions.
    - 在閃避積木時，環境很重要，我們無法決定環境的亮度，因此要根據當下環境自行調整  
        ```
        camera_BRIGHTNESS = 55   
        ```

- Capture images(擷取影像)
    - Capturing Camera Feed
    - 讀取鏡頭畫面
        ```
        def camera_stream(self):
            while self.thread:
                _, self.raw_image = self.imcap.read()
                self.key = cv2.waitKey(15)
        ```

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

- Read keyboard keys(讀取鍵盤按鍵)
    - This utilizes the waitKey function from OpenCV to read the keyboard inputs pressed on the computer.
    - 這是利用OPENCV的 waitKey 功能來讀取電腦鍵盤所按下的按鍵
    ```
    def get_keyboard(self):
        return self.key
    ```

- Return obstacle (block) values(回傳障礙物(積木)數值)
    - Return the variable green_x to allow external code to access this value
    - 將變數green_x回傳，讓外部程式碼可以獲取該值
    ```
    def get_green_x(self):
        return self.green_x
    ```
    - Return the variable green_y to allow external code to access this value
    - 將變數green_y回傳，讓外部程式碼可以獲取該值
    ```
    def get_green_y(self):
        return self.green_y
    ```
    - Return the variable green_area to allow external code to access this value
    - 將變數green_area回傳，讓外部程式碼可以獲取該值
    ```
    def get_green_area(self):
        return self.green_area
    ```
    - Return the variable red_x to allow external code to access this value
    - 將變數red_x回傳，讓外部程式碼可以獲取該值
    ```
    def get_red_x(self):
        return self.red_x
    ```
    - Return the variable red_y to allow external code to access this value
    - 將變數red_y回傳，讓外部程式碼可以獲取該值
    ```
    def get_red_y(self):
        return self.red_y
    ```
    - Return the variable red_area to allow external code to access this value
    - 將變數red_area回傳，讓外部程式碼可以獲取該值
    ```
    def get_red_area(self):
        return self.red_area
    ```

- Terminating a thread(終止執行緒)
    - This is at the end of the program, and releasing memory is necessary to prevent continuous execution from causing insufficient memory on the Raspberry Pi, rendering it unusable.
    -  這是在程式的最後，結束時需要釋放出記憶體，否則不斷重複執行會使樹梅派記憶體不足，無法繼續使用

    ```
    def shutdown(self):
        self.thread = False
        self.color_read_thread.join()
        self.camera_stream_thread.join()
        self.imcap.release()
    ```

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  