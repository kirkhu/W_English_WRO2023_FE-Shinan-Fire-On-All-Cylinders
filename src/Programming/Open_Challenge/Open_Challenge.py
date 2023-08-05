#Import the required modules(匯入所需的模組)
from sys import breakpointhook
from vehicle_function import*
import time
import pickle
import threading
import math
import numpy as np
import rospy
from sensor_msgs.msg import LaserScan
import signal

#Control the LED using the methods and attributes defined within the LED_control class(使用LED_control類別內部定義的方法和屬性，控制LED)
LED = LED_control()

#Utilize the methods and properties defined within the button_control class to read the button(使用button_control類別內部定義的方法和屬性，讀取按鈕)
button = button_control()

#Using methods and attributes defined within the dc_motor class to control a DC motor(使用dc_motor類別內部定義的方法和屬性，控制直流馬達)
motor = dc_motor()

#Utilize the methods and attributes defined within the servo_motor class to control the servo motor(使用servo_motor類別內部定義的方法和屬性，控制伺服馬達)
servo = servo_motor()

#Utilize the methods and attributes defined within the TCS34725 class to read the color sensor(使用TCS34725類別內部定義的方法和屬性，讀取顏色感測器)
color_sensor = TCS34725()

thread_run = True
color = 0
k = 0
line_middle = 0
color_direction_middle = 0
white_color = 0
record_box = ''
RADIAN_TO_DEGREES = 180000/3141.59
lidar_data = 0
lidar_run = False

#Activate the LiDAR(啟動lidar)
def lidar_callback(data):
    global lidar_data, lidar_run
    lidar_data = data
    lidar_run = True

#Read LiDAR distances from the left, right, and front(讀取光達左測、右測、前方距離)
def lidar_get_distance(set):
    lens = int((lidar_data.angle_max - lidar_data.angle_min) / lidar_data.angle_increment) - 1
    mid = -1
    left = -1
    right = -1
    for i in range(lens):
        angle_error = int((lidar_data.angle_min + i * lidar_data.angle_increment) * RADIAN_TO_DEGREES) + 180
        if angle_error >= 0:
            angle = angle_error % 360 - 180
        else:
            angle = 359 - (-1 - angle_error) % 360 - 180
        ranges = lidar_data.ranges[i] * 100
        if not math.isnan(ranges):
            if abs(angle + value) < 5:
            #Lidar front distance value(光達前方數值)
                mid = int(ranges)
            if abs(angle - 90 + value) < 5:
            #LiDAR left-side value(光達左邊數值)
                left = int(ranges)
            if abs(angle + 90 + value) < 5:
            #LiDAR right-side value(光達右邊數值)
                right = int(ranges)
        if mid > 0 and left > 0 and right > 0:
            break
    return left, mid, right, value
    
#Lidar Road Centering(光達道路置中)
def center_control(set):
    left, mid, right = lidar_get_distance(set)
    if left > 0 and right > 0 and left < 100 and right < 100:
      center_error = (right - left) / 1.8
    elif right < 0 or right > 120:
        center_error = 48 - left
    else:
        center_error = right - 48
    servo.angle(center_error * 2 )
    return left, mid, right
    
#Detect whether there are walls on both sides(判斷兩側是否有牆壁)
def to_no_well(set):
    left_dis = 0
    right_dis = 0
    mid_dis = 0
    while left_dis < 150 and right_dis < 150:
        left_dis, mid_dis, right_dis = center_control(set)
    return mid_dis, left_dis
    
def to_well(set, set_time):
    left_dis = 0
    right_dis = 0
    reset = time.time()
    while time.time() - reset < set_time:
        if left_dis > 150 or right_dis > 150:
            reset = time.time()
        left_dis, mid_dis, right_dis = center_control(set)
        
#Drive straight continuously, reading LiDAR values until a front wall is detected(直線行駛不斷讀取光達數值，直到測到前方牆壁)
def to_mid_wall(set, set_mid_dis):
    left_dis = 0
    right_dis = 0
    mid_dis = 999
    while mid_dis > set_mid_dis:
        left_dis, mid_dis, left_dis = center_control(set)
        
#Driving straight, continuously reading LiDAR values until the time reaches直線行駛不斷讀取光達數值，直到時間到)
def time(set, set_time):
    reset = time.time()
    while time.time() - reset < set_time:
        left_dis, mid_dis, left_dis = center_control(set)

def handler(signum, frame):
    exit(0)

#=====================main=====================
try:
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, lidar_callback)
    signal.signal(signal.SIGINT, handler)
    print('ros callback ...')
    while not lidar_run:
        pass
    print('ros running...\n')
    servo.angle(0)
    print('waitting start ...')
    button_state = 1
    while button_state == 1:
        button_state = button.raw_value()
        time.sleep(0.05)
        left, mid, right = lidar_get_distance(0)
        print('left:', left, ' mid:', mid, ' right:', right)
    print('start run')
    motor.power(50)
    #=============start=============
    #get_mid_dis, get_left_dis = to_no_well(0)
    get_left_dis=50
    get_right_dis=50
    reverse=False
    count_1=0
    while get_left_dis < 100 and get_right_dis < 100:
        get_left_dis, get_mid_dis, get_right_dis = center_control(turn_direction[0])
    if get_left_dis < get_right_dis:
        turn_direction = [0, 90, -180, -90]
        reverse=True
    if get_mid_dis > 40:
        value = 100
        while abs(value) > 20:
            servo.angle(value*0.4)
    else:
        value = 100
        while abs(value) > 20:
            servo.angle(value * 1.1)
        reset = time.time()
        while time.time() - reset < 0.7:
            servo.angle(0)
    reset = time.time()
    while time.time() - reset < 2:
        get_left_dis, get_mid_dis, get_right_dis = center_control(turn_direction[(count_1+1)%4])
    count_1 = 1
    if reverse == True:
        for a in range(3):
            while count_1 < 12:
                get_right_dis=50
                get_mid_dis=150
                while get_right_dis < 100 or get_mid_dis > 100:
                    get_left_dis, get_mid_dis, get_right_dis = center_control(turn_direction[count_1%4])  
                if get_mid_dis > 55:
                    value = 100
                    while abs(value) > 20:
                        servo.angle(value*0.3)
                else:
                    value = 100
                    while abs(value) > 20:
                        servo.angle(value * 1.1)
                    reset = time.time()
                    while time.time() - reset < 0.7:
                        servo.angle(0)
                reset = time.time()
                while time.time() - reset < 2:
                    get_left_dis, get_mid_dis, get_right_dis = center_control(turn_direction[(count_1+1)%4])
                print('count:', (count_1+1)%4)
                count_1+=1
    else:
        for a in range(3):
            while count_1 < 12:
                get_left_dis=50
                get_mid_dis=150
                while get_left_dis < 100 or get_mid_dis > 100:
                    get_left_dis, get_mid_dis, get_right_dis = center_control(turn_direction[count_1%4])
                if get_mid_dis > 55:
                    value = 100
                    while abs(value) > 20:
                        servo.angle(value*0.4)
                else:
                    value = 100
                    while abs(value) > 20:
                        servo.angle(value * 1.1)
                    reset = time.time()
                    while time.time() - reset < 0.7:
                        servo.angle(0)
                reset = time.time()
                while time.time() - reset < 2:
                    get_left_dis, get_mid_dis, get_right_dis = center_control(turn_direction[(count_1+1)%4])
                print('count:', (count_1+1)%4)
                count_1+=1
    

    #=============end=============
finally:
    stop_time = time.time()
    while time.time() - stop_time < 1.5:
        motor.power(-20)
    print('\nshutdown')
    motor.power(0)
    servo.angle(0)
    thread_run = False
