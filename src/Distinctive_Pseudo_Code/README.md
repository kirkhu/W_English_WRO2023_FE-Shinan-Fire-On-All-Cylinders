<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Distinctive Pseudo Code</div>
In our program, many repetitive sections of code have been written as subroutines to facilitate debugging and simplify program complexity. And perhaps the most distinctive feature in the program is the avoidance of code blocks resembling building blocks. Here is the excerpt of the program content.
- ### Avoid obstacles until the field line is detected
  - This segment of the code will continuously detect if a line is detected. If detected, it will exit and perform a turn.
    ```
    def dodgeblock_to_line(set):
        #Detecting whether the field line has been detected
        while color > line_middle:
            #Executing evasive maneuvers and setting the driving direction
            dodgeblock_control(set)
            #Placing a 0.001-second pause within the loop is intended to regulate the loop's execution speed, preventing an overall increase in the program's execution time
            time.sleep(0.001)
    ```   
- ###  Avoid obstacles until the Time is Up
  - Since the camera cannot detect obstacles on the sides, turning back directly to the center of the road could lead to a collision with the obstacle. Therefore, it is necessary to continue moving forward for a certain duration until the obstacle is completely avoided.
    ```
    def dodgeblock_to_time(set_time, set):
        #Start recording the stopwatch
        set_reset = time.time()
        #Subtract the current time from the recorded stopwatch time to determine if it exceeds the set time
        while time.time() - set_reset < set_time:
            #Executing evasive maneuvers and setting the direction of travel
            dodgeblock_control(set)
            #Placing a 0.001-second pause within the loop is intended to regulate the loop's execution speed, preventing an overall increase in the program's execution time
            time.sleep(0.001)
    ```
- ### Detect if a turnaround is required and execute it
  - In the second round of the mission, if the color of the last obstacle is red, the third round requires reversing direction, while if it is green, the vehicle continues in the same direction.
    ```
    #Determine whether the following program has been executed twice
    for count in range(2):
        #Determine if it's counterclockwise travel
        # Counterclockwise direction 
        if reverse == True: 
            if count == 1: 
                dodgeblock_to_line(0)
            dodgeblock_to_timhe(2, -90)
            dodgeblock_to_line(-90)
            dodgeblock_to_time(2, -180)
            dodgeblock_to_line(-180)
            dodgeblock_to_time(2, -270)
            # If the obstacle turns red and it is currently the second round, perform a turnaround. If it is not red or not the second round, continue driving. 
            if record_box == 'red' and count == 1:
                dodgeblock_to_line(-270)
                motor.power(70)
                red_turn(-90, 25, 0.3)
                motor.power(50)
                dodgeblock_to_time(1, -90)
            else: 
                dodgeblock_to_line(-270)
                dodgeblock_to_time(2, 0)
        # Clockwise direction 
        else: 
            if count == 1: 
                dodgeblock_to_line(0)
            dodgeblock_to_time(2.5, 90)
            dodgeblock_to_line(90)
            dodgeblock_to_time(2.5, 180)
            dodgeblock_to_line(180)
            dodgeblock_to_time(2.5, 270)
            # If the obstacle turns red and it is currently the second round, perform a turnaround. If it is not red or not the second round, continue driving. 
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
