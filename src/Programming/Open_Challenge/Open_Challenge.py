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

#opencv_detect.get_program_fps()  ¨ú±o¼v¹³¿ëÃÑFPS
#opencv_detect.get_keyboard()     ¨ú±oÁä½Lªº«öÁä
#opencv_detect.get_green_node_x() ¨ú±oºñ¦â¿n¤ì»P±×½u¤§¥æÂIX(¨S¿ëÃÑ¨ì¥Ø¼Ð¼Æ­È¬°-1)
#opencv_detect.get_red_node_x()   ¨ú±o¬õ¦â¿n¤ì»P±×½u¤§¥æÂIX(¨S¿ëÃÑ¨ì¥Ø¼Ð¼Æ­È¬°-1)
#opencv_detect.get_green_x()      ¨ú±oºñ¦â¿n¤ìX®y¼Ð(¨S¿ëÃÑ¨ì¥Ø¼Ð¼Æ­È¬°-1)
#opencv_detect.get_green_y        ¨ú±oºñ¦â¿n¤ìY®y¼Ð(¨S¿ëÃÑ¨ì¥Ø¼Ð¼Æ­È¬°-1)
#opencv_detect.get_green_area()   ¨ú±oºñ¦â¿n¤ì­±¿n¤j¤p(¨S¿ëÃÑ¨ì¥Ø¼Ð¼Æ­È¬°0)
#opencv_detect.get_red_x()        ¨ú±o¬õ¦â¿n¤ìX®y¼Ð(¨S¿ëÃÑ¨ì¥Ø¼Ð¼Æ­È¬°-1)
#opencv_detect.get_red_y          ¨ú±o¬õ¦â¿n¤ìY®y¼Ð(¨S¿ëÃÑ¨ì¥Ø¼Ð¼Æ­È¬°-1)
#opencv_detect.get_red_area()     ¨ú±o¬õ¦â¿n¤ì­±¿n¤j¤p(¨S¿ëÃÑ¨ì¥Ø¼Ð¼Æ­È¬°0)

LED = LED_control()
button = button_control()
motor = dc_motor()
servo = servo_motor()
gyro_sensor = BNO055()
color_sensor = TCS34725()
mapping = tools()

thread_run = True
color = 0
k = 0
line_middle = 0
color_direction_middle = 0
white_color = 0
turn_direction = [0, -90, -180, -270]
pluse_turn = -90
Final_Direction = -270
gyro_value = 180
gyro = 0
record_box = ''
RADIAN_TO_DEGREES = 180000/3141.59
lidar_data = 0
lidar_run = False

def lidar_callback(data):
    global lidar_data, lidar_run
    lidar_data = data
    lidar_run = True

def lidar_get_distance(set_gyro):
    lens = int((lidar_data.angle_max - lidar_data.angle_min) / lidar_data.angle_increment) - 1
    mid = -1
    left = -1
    right = -1
    gyro_value = gyro_relative(set_gyro)
    for i in range(lens):
        angle_error = int((lidar_data.angle_min + i * lidar_data.angle_increment) * RADIAN_TO_DEGREES) + 180
        if angle_error >= 0:
            angle = angle_error % 360 - 180
        else:
            angle = 359 - (-1 - angle_error) % 360 - 180
        ranges = lidar_data.ranges[i] * 100
        if not math.isnan(ranges):
            if abs(angle + gyro_value) < 5:
                mid = int(ranges)
            if abs(angle - 90 + gyro_value) < 5:
                left = int(ranges)
            if abs(angle + 90 + gyro_value) < 5:
                right = int(ranges)
        if mid > 0 and left > 0 and right > 0:
            break
    return left, mid, right, gyro_value

def gyro_read():
    global gyro
    while thread_run:
        gyro = gyro_sensor.raw()
        time.sleep(0.01)

def gyro_relative(value):
    error = value - gyro + 180
    if error >= 0:
        result = (error % 360) - 180
    else:
        result = 359 - ((-1 - error) % 360) - 180
    return result

def center_control(set_gyro):
    left, mid, right, gyro = lidar_get_distance(set_gyro)
    if left > 0 and right > 0 and left < 100 and right < 100:
        center_error = (right - left) / 1.8
    elif right < 0 or right > 120:
        center_error = 48 - left
    else:
        center_error = right - 48
    servo.angle(center_error * 2 + gyro * 1.4)
    return left, mid, right

def to_no_well(set_gyro):
    left_dis = 0
    right_dis = 0
    mid_dis = 0
    while left_dis < 150 and right_dis < 150:
        left_dis, mid_dis, right_dis = center_control(set_gyro)
    return mid_dis, left_dis

def to_well(set_gyro, set_time):
    left_dis = 0
    right_dis = 0
    reset = time.time()
    while time.time() - reset < set_time:
        if left_dis > 150 or right_dis > 150:
            reset = time.time()
        left_dis, mid_dis, right_dis = center_control(set_gyro)

def turn_gyro(set_gyro):
    gyro_value = 100
    while abs(gyro_value) > 20:
        gyro_value = gyro_relative(set_gyro)
        servo.angle(gyro_value * 1.4)
        print(gyro_value)

def to_mid_wall(set_gyro, set_mid_dis):
    left_dis = 0
    right_dis = 0
    mid_dis = 999
    while mid_dis > set_mid_dis:
        left_dis, mid_dis, left_dis = center_control(set_gyro)

def gyro_time(set_gyro, set_time):
    reset = time.time()
    while time.time() - reset < set_time:
        left_dis, mid_dis, left_dis = center_control(set_gyro)

def handler(signum, frame):
    exit(0)

#=====================main=====================
#=============ªûÁ³»öªì©l¤Æ=============
try:
    if gyro_sensor.begin() is not True:
        print("Error initializing device")
        exit()
    time.sleep(1)
    gyro_sensor.setExternalCrystalUse(True)

    #=============©w¸q¦h°õ¦æ§Ç=============
    gyro_read_thread = threading.Thread(target = gyro_read)

    gyro_read_thread.start()
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
        left, mid, right, gyro = lidar_get_distance(0)
        print('left:', left, ' mid:', mid, ' right:', right)
    print('start run')
    motor.power(50)
    #=============¶}©l=============
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
        gyro_value = 100
        while abs(gyro_value) > 20:
            gyro_value = gyro_relative(turn_direction[(count_1+1)%4])
            servo.angle(gyro_value*0.4)
    else:
        gyro_value = 100
        while abs(gyro_value) > 20:
            gyro_value = gyro_relative(turn_direction[(count_1+1)%4])
            servo.angle(gyro_value * 1.1)
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
                    gyro_value = 100
                    while abs(gyro_value) > 20:
                        gyro_value = gyro_relative(turn_direction[(count_1+1)%4])
                        servo.angle(gyro_value*0.3)
                else:
                    gyro_value = 100
                    while abs(gyro_value) > 20:
                        gyro_value = gyro_relative(turn_direction[(count_1+1)%4])
                        servo.angle(gyro_value * 1.1)
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
                    gyro_value = 100
                    while abs(gyro_value) > 20:
                        gyro_value = gyro_relative(turn_direction[(count_1+1)%4])
                        servo.angle(gyro_value*0.4)
                else:
                    gyro_value = 100
                    while abs(gyro_value) > 20:
                        gyro_value = gyro_relative(turn_direction[(count_1+1)%4])
                        servo.angle(gyro_value * 1.1)
                    reset = time.time()
                    while time.time() - reset < 0.7:
                        servo.angle(0)
                reset = time.time()
                while time.time() - reset < 2:
                    get_left_dis, get_mid_dis, get_right_dis = center_control(turn_direction[(count_1+1)%4])
                print('count:', (count_1+1)%4)
                count_1+=1
    

    #=============µ²§ô=============
finally:
    stop_time = time.time()
    while time.time() - stop_time < 1.5:
        motor.power(-20)
    print('\nshutdown')
    motor.power(0)
    servo.angle(0)
    thread_run = False
    gyro_read_thread.join()
