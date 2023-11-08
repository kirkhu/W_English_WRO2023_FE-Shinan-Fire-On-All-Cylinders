# -*- coding: UTF-8 -*-
#Import the required modules(匯入所需的模組)
from vehicle_function import*

#opencv_detect.get_program_fps()  Obtaining Image Recognition FPS(取得影像辨識FPS)
#opencv_detect.get_keyboard()     Get keyboard input(取得鍵盤的按鍵)
#opencv_detect.get_green_x()      Get the X coordinate of the green block(取得綠色積木X座標)
#opencv_detect.get_green_y        Get the Y coordinate of the green block(取得綠色積木Y座標)
#opencv_detect.get_green_area()   Obtain the area size of the green block(取得綠色積木面積大小)
#opencv_detect.get_red_x()        Get the X coordinate of the red block(取得紅色積木X座標)
#opencv_detect.get_red_y          Get the Y coordinate of the red block(取得紅色積木Y座標)
#opencv_detect.get_red_area()     Obtain the area size of the red block(取得紅色積木面積大小)

#Controlling LED using methods and properties defined in the LED_control class(使用LED_control類別內部定義的方法和屬性，控制LED)
LED = LED_control()

#Reading button using methods and properties defined in the button_control class(使用button_control類別內部定義的方法和屬性，讀取按鈕)
button = button_control()

#Controlling DC motor using methods and properties defined in the dc_motor class(使用dc_motor類別內部定義的方法和屬性，控制直流馬達)
motor = dc_motor()

#Controlling servo motor using methods and properties defined in the servo_motor class(使用servo_motor類別內部定義的方法和屬性，控制伺服馬達)
servo = servo_motor()

#Reading a color sensor using methods and properties defined in the TCS34725 class(使用TCS34725類別內部定義的方法和屬性，讀取顏色感測器)
color_sensor = TCS34725()

#Using methods and properties defined in the tools class(使用tools類別內部定義的方法和屬性)
mapping = tools()

#全域變數定義(不更動)
RADIAN_TO_DEGREES = 180000/3141.59
lidar_data = 0
lidar_run = False
thread_run = True
thread_DC = True
green_lower = 0
green_upper = 0
red_lower = 0
red_upper = 0
line_middle = 0
turn_left_dis = -1
turn_right_dis = -1
servo_control_angle = 0
record_block = 'None'
direction = 'None'
return_block_color = 'None'
start_pleace = 0

#參數調整(調整參數)
dodgeblock_kp = 0.18
center_kp = 0.8
max_power = 60
min_power = 55

def handler(signum, frame):
    exit(0)

#Activate the LiDAR(啟動lidar)
def lidar_callback(data):
    global lidar_data, lidar_run
    lidar_data = data
    lidar_run = True

#Read LiDAR distances from the left, right, and front(讀取光達左測、右測、前方距離)
def lidar_get_distance(set):
    lens = int((lidar_data.angle_max - lidar_data.angle_min) / lidar_data.angle_increment) - 15
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
        if ranges < 100:
            if abs(angle + i) < 5:
                #Lidar front distance value(光達前方數值)
                mid = ranges
            if abs(angle - 90 + i) < 5:
                #LiDAR left-side value(光達左邊數值)
                left = ranges
            if abs(angle + 90 + i) < 5:
                #LiDAR right-side value(光達右邊數值)
                right = ranges
    return int(left), int(mid), int(right) ,i

#Read values of the blue line and orange line(讀取藍線與橘線數值)
def line_color_read():
    global line_middle, color_direction_middle, white_color
    with open('/home/pi/Desktop/final/save_file/color_sensor.p', mode='rb') as f:
        file = pickle.load(f)
    blue_color = file['Blue']
    orange_color = file['Orange']
    white_color = file['white']
    color_direction_middle = (blue_color + orange_color) / 2 
    line_middle = (white_color + orange_color) / 2
    print('\norange:' + str(orange_color))
    print('blue:' + str(blue_color))
    print('white:' + str(white_color))
    print('\ndirection_middle:', color_direction_middle)
    print('line middle:', line_middle)
    
#Read obstacle HSV values(讀取障礙物HSV數值)
def block_color_read():
    global green_lower, green_upper, red_lower, red_upper
    with open('save_file/HSV_Green.p', mode='rb') as f:
        file = pickle.load(f)
    g_lower = file['Lower']
    g_upper = file['Upper']
    print('\nGreen_Lower:' + str(g_lower))
    print('Green_Upper:' + str(g_upper))
    with open('save_file/HSV_Red.p', mode='rb') as f:
        file = pickle.load(f)
    r_lower = file['Lower']
    r_upper = file['Upper']
    print('\nRed_Lower:' + str(r_lower))
    print('Red_Upper:' + str(r_upper) + '\n')
    
    red_lower = np.array(r_lower, np.uint8) 
    red_upper = np.array(r_upper, np.uint8)
    green_lower = np.array(g_lower, np.uint8)
    green_upper = np.array(g_upper, np.uint8)

#Read the values of the color sensor(讀取顏色感測器數值)
def color_read():
    global color
    while thread_run:
        color = color_sensor.readluminance()['c']
        time.sleep(0.01)

#=======================任務執行程序=======================

#Recognize Clockwise and Counterclockwise(辨識順逆時針)
def start_to_NoWall():
    global gyro_offset, turn_direction, reverse_direction, direction
    left_dis=50
    right_dis=50
    while left_dis < 200 and right_dis < 200:
        left_dis, right_dis, gyro_angle = dodge_control(0)
    print('left:', left_dis, ' right:', right_dis, '\n')

    #判斷順時針或逆時針
    if left_dis > right_dis:
        #逆時針
        print('turn left\n')
        direction = 'counterclockwise'
        gyro_offset = 0 #陀螺儀微調
        #正旋轉方向
        turn_direction = [-90, -180, -270, 0, 
                          -90, -180, -270, 0, 
                          -90, -180, -270
                          ]
        #反轉旋轉方向
        reverse_direction = [180, -90, 0, 90]
    else:
        #順時針
        print('turn right\n')
        direction = 'clockwise'
        gyro_offset = 0 #陀螺儀微調
        #正旋轉方向
        turn_direction = [90, 180, 270, 0,
                          90, 180, 270, 0,
                          90, 180, 270
                          ]
        #反轉旋轉方向
        reverse_direction = [180, 90, 0, -90]

#Avoid obstacles until the field line is detected(閃避障礙物直到測到場地線)
def dodge_to_line(set_gyro):
    while color > line_middle:
        left_dis, right_dis, gyro_angle = dodge_control(set_gyro)
    print(color)

#Translation in English: Avoid obstacles until the time is up(閃避障礙物直到時間到)
def dodge_to_time(set_gyro, set_time):
    reset = time.time()
    while time.time() - reset < set_time:
        left_dis, right_dis, gyro_angle = turn_dodge_control(set_gyro)
        
#Rotating motion(迴轉動作)
def reverse():
    global record_block, servo_control_angle, max_power, min_power, turn_left_dis, turn_right_dis
    while color > line_middle:
        left_dis, right_dis, gyro_angle = dodge_control(0)
    while color < line_middle:
        left_dis, right_dis, gyro_angle = dodge_control(0)
    while color > line_middle:
        left_dis, right_dis, gyro_angle = dodge_control(0)
        if opencv_detect.get_red_y() > 290:
            return_block_color = 'red'
            record_block = 'red'
        elif opencv_detect.get_green_y() > 290:
            return_block_color = 'green'
            record_block = 'green'
        else:
            return_block_color ='None'
            record_block = 'None'
    #判斷正前方有沒有積木
    if not return_block_color =='None':
        #有積木
        max_power = 60
        min_power = 55
        print('find block\n')
        #繼續閃避到接近下一個走道方向
        gyro_angle = 100
        while abs(gyro_angle) > 20:
            left_dis, right_dis, gyro_angle = dodge_control(0)
        #繼續閃避到積木消失
        while opencv_detect.get_red_y() > 0 or opencv_detect.get_green_y() > 0:
            left_dis, right_dis, gyro_angle = dodge_control(0)
        #繼續走一小段距離,必面太早轉彎撞到積木
        reset = time.time()
        while time.time() - reset < 0.8:
            left_dis, right_dis, gyro_angle = dodge_control(0)
            turn_left_dis = left_dis
            turn_right_dis = right_dis
        print('\nreturn block color:', return_block_color, '\n')
    else:
        max_power = 35
        min_power = 35
        #沒積木
        print('not find block\n')
        gyro_angle = 100
        while abs(gyro_angle) > 5:
            left_dis, right_dis, gyro_angle = dodge_control(0)
        if direction == 'clockwise':
            #順時針
            print('順時針')
            right_dis = 250
            while right_dis > 200 or right_dis < 0:
                left_dis, right_dis, mid_dis, gyro = lidar_get_distance(0)
                turn_left_dis = left_dis
                turn_right_dis = right_dis
                servo_control_angle = gyro * gyro_kp
                servo.angle(-servo_control_angle)
            reset = time.time()
            right_dis = 250
            while time.time() - reset < 0.15:
                left_dis, right_dis, mid_dis,gyro = lidar_get_distance(0)
                servo_control_angle = gyro * gyro_kp
                turn_left_dis = left_dis
                turn_right_dis = right_dis
                servo.angle(-servo_control_angle)
                if right_dis > 200 or right_dis < 0:
                    reset = time.time()
                if opencv_detect.get_red_y() > 0:
                    record_block = 'red'
                elif opencv_detect.get_green_y() > 0:
                    record_block = 'green'
                else:
                    record_block = 'None'
        else:
            #逆時針
            max_power = 35
            min_power = 35
            left_dis = 250
            while left_dis > 200 or left_dis < 0:
                left_dis, right_dis, mid_dis, gyro = lidar_get_distance(0)
                turn_left_dis = left_dis
                turn_right_dis = right_dis 
                servo_control_angle = gyro * gyro_kp
                servo.angle(-servo_control_angle)
            reset = time.time()
            left_dis = 250
            while time.time() - reset < 0.15:
                left_dis, right_dis, mid_dis, gyro = lidar_get_distance(0)
                print('left:', left_dis,'right:', right_dis)
                servo_control_angle = gyro * gyro_kp
                servo.angle(-servo_control_angle)
                turn_left_dis = left_dis
                turn_right_dis = right_dis
                if left_dis > 200 or left_dis < 0:
                    reset = time.time()
                if opencv_detect.get_red_y() > 0:
                    record_block = 'red'
                elif opencv_detect.get_green_y() > 0:
                    record_block = 'green'
                else:
                    record_block = 'None'
    #判斷當下離兩側牆壁哪邊比較遠
    if record_block == 'red':
        max_power = 80
        min_power = 60
        if turn_left_dis > turn_right_dis:
            print('左轉')
            servo_control_angle = -50
            servo.angle(50)
        else:
            print('右轉')
            servo_control_angle = 50
            servo.angle(-50)
        print('left:', turn_left_dis, 'right:', turn_right_dis)
        gyro_error = 100
        while abs(gyro_error) > 40:
            gyro_error = gyro_relative(reverse_direction[0]) 
              
#Controlling DC Motors for Vehicles(控制車輛直流馬達)
def power_control():
    global min_power, max_power
    motor.power(70)
    time.sleep(0.4)
    while thread_DC:
        power_error = tools.constrain(servo_control_angle, -50, 50)
        motor.power(tools.mapping(abs(power_error), 0, 50, min_power, max_power))
        time.sleep(0.05)
#=======================main=======================
try:
    signal.signal(signal.SIGINT, handler)
    #ROS 雷達程序啟動
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, lidar_callback)
    print('\nROS init')
    while not lidar_run:
        pass
    print('ROS connected')

    time.sleep(1)
    gyro_sensor.setExternalCrystalUse(True)

    #讀取記憶體數據
    line_color_read()
    block_color_read()

    #opencv程序啟動
    opencv_detect = opencv_recognition(red_lower, red_upper, green_lower, green_upper)
    opencv_detect.start()

    #定義平行化執行序
    color_read_thread = threading.Thread(target = color_read)
    power_thread = threading.Thread(target = power_control)
    color_read_thread.start()
    gyro_read_thread.start()

    #直流馬達初始化
    motor.power(0)

    #伺服馬達初始化
    servo.angle(30)
    time.sleep(0.5)
    servo.angle(-30)
    time.sleep(0.5)
    servo.angle(0)
    time.sleep(0.5)
    
    #開啟LED燈
    LED.green_on()
    LED.red_on()
    
    #等待按鈕啟動
    button_state = 1
    while button_state == 1 and not opencv_detect.get_keyboard() == ord('g'):
        button_state = button.raw_value()
        left, right, mid, gyro = lidar_get_distance(0)
        print('left:', left, ' right:', right, ' mid:', mid, ' gyro:', gyro)
        #print('fps:', opencv_detect.get_program_fps())
        # print('green_y:', opencv_detect.get_green_y(), 'red_y:', opencv_detect.get_red_y())
        time.sleep(0.05)
    
    power_thread.start()
    print('\n=========================\n')

    #出發直到兩側某一牆壁消失
    start_to_NoWall()
    for i in range(7):
        print('count:', i)
        dodge_to_time(turn_direction[i], 2)
        dodge_to_line(turn_direction[i])
        
    #判斷是否需要迴轉
    reverse()
    print('\nlast block color:', record_block, '\n')
    if record_block == 'red':
        max_power = 60
        min_power = 55
        dodge_to_line(reverse_direction[0])
        for i in range(3):
            print('count:', i)
            dodge_to_time(reverse_direction[i + 1], 1.8)
            dodge_to_line(reverse_direction[i + 1])
        #進入終點
        dodge_to_time(reverse_direction[0], 0.1)
        dodge_to_line(reverse_direction[0])
        dodge_to_time(reverse_direction[0], 1.3)
    else:
        #最後一顆積木偵測為綠色積木，同方向完成最後一圈
        max_power = 60
        min_power = 55
        dodge_to_line(turn_direction[3])
        for i in range(3):
            print('count:', i)
            dodge_to_time(turn_direction[i + 4], 1.8)
            dodge_to_line(turn_direction[i + 4])
        #進入終點
        dodge_to_time(0, 0.1)
        dodge_to_line(0)
        dodge_to_time(0, 1.3)
    #煞車
    thread_DC = False
    power_thread.join()
    brakes = time.time()
    while time.time() - brakes < 0.5:
        motor.power(-50)

finally:
    print('\nshutdown')
    if thread_DC:
        thread_DC = False
        power_thread.join()
    motor.power(0)
    servo.angle(0)
    LED.green_off()
    LED.red_off()
    thread_run = False
    color_read_thread.join()
    gyro_read_thread.join()
    opencv_detect.shutdown()
