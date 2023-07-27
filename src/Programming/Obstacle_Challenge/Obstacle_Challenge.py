from vehicle_function import*
import time
import pickle
import threading
import math
import numpy as np
import rospy
from sensor_msgs.msg import LaserScan
import signal

LED = LED_control()
button = button_control()
motor = dc_motor()
servo = servo_motor()
gyro_sensor = BNO055()
color_sensor = TCS34725()
mapping = tools()

thread_run = True
reverse = True
color = 0
k = 0
green_lower = 0
green_upper = 0
red_lower = 0
red_upper = 0
line_middle = 0
color_direction_middle = 0
white_color = 0
Final_Direction = -270
gyro_value = 180
gyro = 0
record_box = ''
count = 0
round_count = 0
line_count = 0
RADIAN_TO_DEGREES = 180000/3141.59
lidar_data = 0
lidar_run = False
#====================================
lidar_kp = 0.8
dodgeblock_kp = 0.1
gyro_kp = 0.8

def lidar_callback(data):
    global lidar_data, lidar_run
    lidar_data = data
    lidar_run = True

def lidar_get_distance(set_gyro):
    lens = int((lidar_data.angle_max - lidar_data.angle_min) / lidar_data.angle_increment) - 15
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
        if ranges < 100:
            if abs(angle + gyro_value) < 5:
                mid = ranges
            if abs(angle - 90 + gyro_value) < 5:
                left = ranges
            if abs(angle + 90 + gyro_value) < 5:
                right = ranges
    return int(left), int(mid), int(right) ,gyro_value

def line_color_read():#Åª¨ú¦a¤WÃC¦â¼Æ­È
    global line_middle, color_direction_middle, white_color
    with open('save_file/color_sensor.p', mode='rb') as f:
        file = pickle.load(f)
    blue_color = file['Blue']
    orange_color = file['Orange']
    white_color = file['white']
    color_direction_middle = (blue_color + orange_color) / 2
    line_middle = (white_color + orange_color) / 2
    print('orange:' + str(orange_color))
    print('blue:' + str(blue_color))
    print('white:' + str(white_color))
    print('direction_middle:', color_direction_middle)
    print('line middle:', line_middle)
    print('=======================')
    
def block_color_read():#Åª¨ú¿n¤ìªºHSV¼Æ­È
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

def color_read():#Åª¨úÃC¦â·PÀ³¾¹¼Æ­È
    global color
    while thread_run:
        color = color_sensor.readluminance()['c']
        time.sleep(0.01)

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

def car_control():#Áä½L±±¨îª½¬y°¨¹F«e¶i»P°±¤î
    while thread_run:
        if opencv_detect.get_keyboard() == ord('w'):
            motor.power(50)
        elif opencv_detect.get_keyboard() == ord('s'):
            motor.power(0)
        time.sleep(0.1)

def dodgeblock_to_line(set_gyro):#°{Á×¿n¤ì¨ì°»´ú¦a¤W½u
    while color > line_middle:
        dodgeblock_control(set_gyro)
        time.sleep(0.001)

def dodgeblock_to_time(set_time, set_gyro):#°{Á×¿n¤ì¨ì®É¶¡
    set_reset = time.time()
    while time.time() - set_reset < set_time:
        dodgeblock_control(set_gyro)
        time.sleep(0.001)
        
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

def center_control(set_gyro):
    left, mid, right, gyro = lidar_get_distance(set_gyro)
    if left > 0 and right > 0:
        center_error = (right - left) / 1.8
    elif left > 0:
        center_error = 48 - left
    else:
        center_error = right - 48
    servo.angle(center_error * lidar_kp + gyro * gyro_kp)

def red_turn(set_gyro, set_gyro_range, set_gyro_time):
    while gyro_sensor.relative(set_gyro) > set_gyro_range or gyro_sensor.relative(set_gyro) < -set_gyro_range:
        servo.angle(-35)
    gyro_time = time.time()
    while time.time() - gyro_time < set_gyro_time:
        left, mid, right, gyro = lidar_get_distance(set_gyro)
        center_error = (right - left) / 1.8
        servo.angle(center_error * lidar_kp + gyro * gyro_kp)
                
def number_line():
    global line_count ,round_count
    if reverse == True:
        while thread_run:
            print("wait line")
            while color > line_middle and thread_run:
                time.sleep(0.001)
            if line_count + 1 == 4:
                line_count = 0
                round_count += 1
            else:
                line_count += 1
            print('round:', round_count, 'line:', line_count)
            time.sleep(2.3)
        print('end')
    else:
        while thread_run:
            print("wait line")
            while color > line_middle and thread_run:
                time.sleep(0.001)
            if line_count + 1 == 4:
                line_count = 0
                round_count += 1
            else:
                line_count += 1
            print('round:', round_count, 'line:', line_count)
            time.sleep(2.3)
        print('end')

def handler(signum, frame):
    exit(0)

try:
    if gyro_sensor.begin() is not True:
        print("Error initializing device")
        exit()
    time.sleep(1)
    gyro_sensor.setExternalCrystalUse(True)

    color_read_thread = threading.Thread(target = color_read)
    gyro_read_thread = threading.Thread(target = gyro_read)
    car_control_thread = threading.Thread(target = car_control)
    number_line_thread = threading.Thread(target = number_line)

    line_color_read()
    block_color_read()
    opencv_detect = opencv_recognition(red_lower, red_upper, green_lower, green_upper)#opencv¼v¹³¿ëÃÑ¥\¯à©w¸q»Pªì©l¤Æopencv¥\¯à
    opencv_detect.start()
    color_read_thread.start()
    gyro_read_thread.start()
    car_control_thread.start()
    number_line_thread.start()
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
    while button_state == 1 and not opencv_detect.get_keyboard() == ord('g') and not opencv_detect.get_keyboard() == ord('c'):
        button_state = button.raw_value()
        time.sleep(0.05)
        #center_control(0)
        left, mid, right, gyro = lidar_get_distance(0)
#         print('left:', left, ' mid:', mid, ' right:', right)
    print('start run')
    motor.power(60)

    direction_detect()
    for count in range(2):
        if reverse == True:
            if count == 1:
                dodgeblock_to_line(0)
            dodgeblock_to_time(2, -90)
            dodgeblock_to_line(-90)
            dodgeblock_to_time(2, -180)
            dodgeblock_to_line(-180)
            dodgeblock_to_time(2, -270)
            if record_box == 'red' and count == 1:
                dodgeblock_to_line(-270)
                motor.power(70)
                red_turn(-90, 25, 0.3)
                motor.power(50)
                dodgeblock_to_time(1, -90)
            else:
                dodgeblock_to_line(-270)
                dodgeblock_to_time(2, 0)
        else:
            if count == 1:
                dodgeblock_to_line(0)
            dodgeblock_to_time(2.5, 90)
            dodgeblock_to_line(90)
            dodgeblock_to_time(2.5, 180)
            dodgeblock_to_line(180)
            dodgeblock_to_time(2.5, 270)
            if record_box == 'red' and count == 1:
                dodgeblock_to_line(270)
                motor.power(70)
                red_turn(90, 25, 0.3)
                motor.power(50)
                dodgeblock_to_time(1, 90)
            else:
                dodgeblock_to_line(270)
                dodgeblock_to_time(2, 0)

    if reverse == True:
        if record_box == 'red':
            dodgeblock_to_line(-90)
            dodgeblock_to_time(2.5, 0)
            dodgeblock_to_line(0)
            dodgeblock_to_time(2.5, 90)
            dodgeblock_to_line(90)
            dodgeblock_to_time(2, 180)
        else:
            dodgeblock_to_line(0)
            dodgeblock_to_time(2.5, -90)
            dodgeblock_to_line(-90)
            dodgeblock_to_time(2.5, -180)
            dodgeblock_to_line(-180)
            dodgeblock_to_time(2.5, -270)
            dodgeblock_to_line(-270)
            dodgeblock_to_time(2, 0)
    else:
        if record_box == 'red':
            dodgeblock_to_line(90)
            dodgeblock_to_time(2.5, 0)
            dodgeblock_to_line(0)
            dodgeblock_to_time(2.5, -90)
            dodgeblock_to_line(-90)
            dodgeblock_to_time(2, -180)
        else:
            dodgeblock_to_line(0)
            dodgeblock_to_time(2.5, 90)
            dodgeblock_to_line(90)
            dodgeblock_to_time(2.5, 180)
            dodgeblock_to_line(180)
            dodgeblock_to_time(2.5, 270)
            dodgeblock_to_line(270)
            dodgeblock_to_time(2, 0)
    brakes = time.time()
    while time.time() - brakes < 1:
        motor.power(-20)
    motor.power(0)
    servo.angle(0)
    
finally:
    print('\nshutdown')
    motor.power(0)
    servo.angle(0)
    thread_run = False
    color_read_thread.join()
    car_control_thread.join()
    gyro_read_thread.join()
    number_line_thread.join()
    opencv_detect.shutdown()#opencv¼v¹³¿ëÃÑ¥\¯à°±¤î¦ê¬y