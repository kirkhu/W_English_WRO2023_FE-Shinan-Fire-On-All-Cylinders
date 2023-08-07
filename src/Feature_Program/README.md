![LOGO](../../other/img/logo.png)2023WRO Future Engineers Fire On All Cylinders  
====
## <div align="center">Feture Program </div>
__In our program, many repetitive sections of code have been written as subroutines to facilitate debugging and simplify program complexity. And perhaps the most distinctive feature in the program is the avoidance of code blocks resembling building blocks. Here is the excerpt of the program content__
__在我們的程式中，將許多重覆使用的程式寫成副程式，以方便除錯及簡化程式複雜性，而在程式中最有特色的莫過於是閃避積木的地方，以下是程式內容__
- ### Avoid obstacles until the field line is detected(閃避障礙物直到測到場地線)
  - This segment of the code will continuously detect if a line is detected. If detected, it will exit and perform a turn.
  - 這段程式會一直偵測是否測到線，如果測到就會跳出進行轉彎
    ```
    def dodgeblock_to_line(set):
        while color > line_middle:
            dodgeblock_control(set)
            time.sleep(0.001)
    ```   
- ### Translation in English: Avoid obstacles until the time is up(閃避障礙物直到時間到)
  - Since the camera cannot detect obstacles on the sides, turning back directly to the center of the road could lead to a collision with the obstacle. Therefore, it is necessary to continue moving forward for a certain duration until the obstacle is completely avoided.
  - 由於鏡頭辨識不到在側邊的障礙物，因此直接轉回道路中央會撞到障礙物，因此需要持續前進一段時間直到完全閃過障礙物
    ```
    def dodgeblock_to_time(set_time, set):
        set_reset = time.time()
        while time.time() - set_reset < set_time:
            dodgeblock_control(set)
            time.sleep(0.001)
    ```
- ### Detect if a turnaround is required and execute it(偵測是否需要進行迴轉並執行)
  - In the second round of the mission, if the color of the last obstacle is red, the third round requires reversing direction, while if it is green, the vehicle continues in the same direction.
  - 在任務賽的第二圈，如果最後一個障礙物的顏色是紅色，則第三圈需要反向行駛；如果是綠色，則車輛繼續保持原方向行駛。
    ```
    for count in range(2):
        # Counterclockwise direction 逆時針行駛
        if reverse == True: 
            if count == 1: 
                dodgeblock_to_line(0)
            dodgeblock_to_time(2, -90)
            dodgeblock_to_line(-90)
            dodgeblock_to_time(2, -180)
            dodgeblock_to_line(-180)
            dodgeblock_to_time(2, -270)
            # If the obstacle turns red and it is currently the second round, perform a turnaround. If it is not red or not the second round, continue driving. 
            # 若障礙物回紅色且目前是第二圈，進行迴轉，若不是紅色或不是第二圈則繼續繼續行駛
            if record_box == 'red' and count == 1:                  
                dodgeblock_to_line(-270)
                motor.power(70)
                red_turn(-90, 25, 0.3)
                motor.power(50)
                dodgeblock_to_time(1, -90)
            else: 
                dodgeblock_to_line(-270)
                dodgeblock_to_time(2, 0)
        # Clockwise direction 順時針行駛
        else: 
            if count == 1: 
                dodgeblock_to_line(0)
            dodgeblock_to_time(2.5, 90)
            dodgeblock_to_line(90)
            dodgeblock_to_time(2.5, 180)
            dodgeblock_to_line(180)
            dodgeblock_to_time(2.5, 270)
            # If the obstacle turns red and it is currently the second round, perform a turnaround. If it is not red or not the second round, continue driving. 
            # 若障礙物回紅色且目前是第二圈，進行迴轉，若不是紅色或不是第二圈則繼續繼續行駛
            if record_box == 'red' and count == 1: 
                dodgeblock_to_line(270)
                motor.power(70)
                red_turn(90, 25, 0.3)
                motor.power(50)
                dodgeblock_to_time(1, 90)
            else: 
                dodgeblock_to_line(270)
                dodgeblock_to_time(2, 0)
    ```
# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
