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

#Utilize the methods and attributes defined within the 'Tools' class(使用tools類別內部定義的方法和屬性)
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

def line_color_read():#Read values of the blue line and orange line(讀取藍線與橘線數值)
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

#Read obstacle HSV values(讀取障礙物HSV數值)
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

#Read the values of the color sensor(讀取顏色感測器數值)
def color_read():
    global color
    while thread_run:
        color = color_sensor.readluminance()['c']
        time.sleep(0.01)

#Controlling DC Motors for Vehicles Using a Keyboard(使用鍵盤控制車輛直流馬達)
def car_control():
    while thread_run:
        if opencv_detect.get_keyboard() == ord('w'):
            motor.power(50)
        elif opencv_detect.get_keyboard() == ord('s'):
            motor.power(0)
        time.sleep(0.1)

#Avoid obstacles until the field line is detected(閃避障礙物直到測到場地線)
def dodgeblock_to_line(set):
    while color > line_middle:
        dodgeblock_control(set)
        time.sleep(0.001)

#Translation in English: Avoid obstacles until the time is up(閃避障礙物直到時間到)
def dodgeblock_to_time(set_time, set):
    set_reset = time.time()
    while time.time() - set_reset < set_time:
        dodgeblock_control(set)
        time.sleep(0.001)

#Recognize Clockwise and Counterclockwise(辨識順逆時針)
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

#Lidar Road Centering(光達道路置中)
def center_control(set):
    left, mid, right = lidar_get_distance(set)
    if left > 0 and right > 0:
        center_error = (right - left) / 1.8
    elif left > 0:
        center_error = 48 - left
    else:
        center_error = right - 48
    servo.angle(center_error * lidar_kp)

#Rotating motion(迴轉動作)
def red_turn(set, set_range, set_time):
    while range_y > set_range:
        servo.angle(-35)
    time = time.time()
    while time.time() - time < set_time:
        left, mid, right= lidar_get_distance(set)
        center_error = (right - left) / 1.8
        servo.angle(center_error * lidar_kp)
        
#Record the number of passes through the venue's finish line(紀錄經過場地線次數)                
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

#==========main==============
try:
    color_read_thread = threading.Thread(target = color_read)
    car_control_thread = threading.Thread(target = car_control)
    number_line_thread = threading.Thread(target = number_line)

    line_color_read()
    block_color_read()
    opencv_detect = opencv_recognition(red_lower, red_upper, green_lower, green_upper)#opencv¼v¹³¿ëÃÑ¥\¯à©w¸q»Pªì©l¤Æopencv¥\¯à
    opencv_detect.start()
    color_read_thread.start()
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
        left, mid, right = lidar_get_distance(0)
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
    number_line_thread.join()
    opencv_detect.shutdown()#Close OpenCV window(opencv關閉視窗)
