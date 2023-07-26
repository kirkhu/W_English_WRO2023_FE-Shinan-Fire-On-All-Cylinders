import pigpio
import time
import smbus
import struct
import os
import math
import cv2
import threading
import numpy as np
'''
import rospy
from sensor_msgs.msg import LaserScan
'''
    
#==========各裝置腳位設定==========
Red_LED_pin = 27   #紅色LED腳位編號
Green_LED_pin = 22 #綠色LED腳位編號
Motor_IN1_pin = 6  #直流馬達IN1腳位編號
Motor_IN2_pin = 13 #直流馬達IN2腳位編號
Motor_PWM_pin = 19 #直流馬達PWM腳位編號
Button_pin = 5    #按鈕腳位編號
Servo_pin = 26     #伺服馬達(轉向舵)腳位編號

#==========車輛參數設定==========
servo_offset = 8                            #伺服馬達(轉向舵)置中微調
reverse = False                        #直流馬達前進後退反向設定
servo_range = 30                       #伺服馬達(轉向舵)轉彎極限角度
block_detect_min_area = 500           #積木影像辨識最小容許面積大小
image_black_area = 280                 #影像畫面黑色遮罩範圍(數字越大遮罩範圍越大)
red_line_xy = [[420, 0], [0, 480]]    #紅色線會製作標示設定，[上點, 下點]
green_line_xy = [[210, 0], [640, 480]] #綠色線會製作標示設定，[上點, 下點]
camera_BRIGHTNESS = 55                 #影像畫面亮度調整(數字越大畫面越亮)
#================================
RADIAN_TO_DEGREES = 360/(math.pi *2)
pi = pigpio.pi()

def mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def constrain(x, out_min, out_max):
    return out_min if x < out_min else out_max if x > out_max else x
# Get I2C bus
bus = smbus.SMBus(1)

# I2C Address of the device
TCS34725_DEFAULT_ADDRESS = 0x29

# TCS34725 Register Set
TCS34725_COMMAND_BIT = 0x80
TCS34725_REG_ENABLE = 0x00 # Enables states and interrupts
TCS34725_REG_ATIME = 0x01 # RGBC integration time
TCS34725_REG_WTIME = 0x03 # Wait time
TCS34725_REG_CONFIG = 0x0D # Configuration register
TCS34725_REG_CONTROL = 0x0F # Control register
TCS34725_REG_CDATAL = 0x14 # Clear/IR channel low data register
TCS34725_REG_CDATAH = 0x15 # Clear/IR channel high data register
TCS34725_REG_RDATAL = 0x16 # Red ADC low data register
TCS34725_REG_RDATAH = 0x17 # Red ADC high data register
TCS34725_REG_GDATAL = 0x18 # Green ADC low data register
TCS34725_REG_GDATAH = 0x19 # Green ADC high data register
TCS34725_REG_BDATAL = 0x1A # Blue ADC low data register
TCS34725_REG_BDATAH = 0x1B # Blue ADC high data register

# TCS34725 Enable Register Configuration
TCS34725_REG_ENABLE_SAI = 0x40 # Sleep After Interrupt
TCS34725_REG_ENABLE_AIEN = 0x10 # ALS Interrupt Enable
TCS34725_REG_ENABLE_WEN = 0x08 # Wait Enable
TCS34725_REG_ENABLE_AEN = 0x02 # ADC Enable
TCS34725_REG_ENABLE_PON = 0x01 # Power ON

# TCS34725 Time Register Configuration
TCS34725_REG_ATIME_2_4 = 0xFF # Atime = 2.4 ms, Cycles = 1
TCS34725_REG_ATIME_24 = 0xF6 # Atime = 24 ms, Cycles = 10
TCS34725_REG_ATIME_101 = 0xDB # Atime = 101 ms, Cycles = 42
TCS34725_REG_ATIME_154 = 0xC0 # Atime = 154 ms, Cycles = 64
TCS34725_REG_ATIME_700 = 0x00 # Atime = 700 ms, Cycles = 256
TCS34725_REG_WTIME_2_4 = 0xFF # Wtime = 2.4 ms
TCS34725_REG_WTIME_204 = 0xAB # Wtime = 204 ms
TCS34725_REG_WTIME_614 = 0x00 # Wtime = 614 ms

# TCS34725 Gain Configuration
TCS34725_REG_CONTROL_AGAIN_1 = 0x00 # 1x Gain
TCS34725_REG_CONTROL_AGAIN_4 = 0x01 # 4x Gain
TCS34725_REG_CONTROL_AGAIN_16 = 0x02 # 16x Gain
TCS34725_REG_CONTROL_AGAIN_60 = 0x03 # 60x Gain

class opencv_recognition():
    def __init__(self, red_upper, red_lower, green_upper, green_lower):
        self.imcap = cv2.VideoCapture(0)
        if not self.imcap.isOpened():
            print("Cannot open camera")
            exit()
        self.imcap.set(cv2.CAP_PROP_BRIGHTNESS, camera_BRIGHTNESS)
        self.thread = False
        self.hsv_red_upper = red_upper
        self.hsv_red_lower = red_lower
        self.hsv_green_upper = green_upper
        self.hsv_green_lower = green_lower
        self.green_x = -1
        self.green_y = -1
        self.green_area = -1
        self.red_x = -1
        self.red_y = -1
        self.red_area = -1
        self.green_node_x = -1
        self.red_node_x = -1
        self.key = 0
        self.program_fps = -1
        self.raw_image = np.zeros((480, 640, 3), np.uint8)
        self.draw_red_line_xy = red_line_xy
        self.draw_green_line_xy = green_line_xy
        self.red_line_m = (self.draw_red_line_xy[1][1] - self.draw_red_line_xy[0][1]) / (self.draw_red_line_xy[1][0] - self.draw_red_line_xy[0][0])
        self.green_line_m = (self.draw_green_line_xy[1][1] - self.draw_green_line_xy[0][1]) / (self.draw_green_line_xy[1][0] - self.draw_green_line_xy[0][0])
        self.color_read_thread = threading.Thread(target = self.color_recognition)
        self.camera_stream_thread = threading.Thread(target = self.camera_stream)

    def start(self):
        self.thread = True
        self.color_read_thread.start()
        self.camera_stream_thread.start()

    def draw_line(self, input_img):
        cv2.line(input_img, (self.draw_red_line_xy[0][0],self.draw_red_line_xy[0][1]), (self.draw_red_line_xy[1][0],self.draw_red_line_xy[1][1]), (0, 0, 255), 2)
        cv2.line(input_img, (self.draw_green_line_xy[0][0],self.draw_green_line_xy[0][1]), (self.draw_green_line_xy[1][0],self.draw_green_line_xy[1][1]), (0, 255, 0), 2)
        return input_img

    def get_intersection(self, img, m, down_x, down_y, y, color):
        if y == -1:
            return img, -1
        else:
            x0 = int((y-down_y+m*down_x)/m)
            cv2.circle(img, (x0, y), 5, color, -1)
            return img, x0

    def camera_stream(self):
        while self.thread:
            _, self.raw_image = self.imcap.read()
            self.key = cv2.waitKey(15)

    def color_recognition(self):
        while self.thread:
            reset = time.time()
            img = self.raw_image.copy()
            img[0:image_black_area, 0:640] = [0, 0, 0]
            img[380:480, 0:640] = [0, 0, 0]
            hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            detect_image, self.green_x, self.green_y, self.green_area = self.color_detect(img, hsv_image, self.hsv_green_upper, self.hsv_green_lower)
            detect_image, self.green_node_x = self.get_intersection(detect_image, self.green_line_m, self.draw_green_line_xy[1][0], self.draw_green_line_xy[1][1], self.green_y, (0, 255, 0))
            detect_image, self.red_x, self.red_y, self.red_area = self.color_detect(img, hsv_image, self.hsv_red_upper, self.hsv_red_lower)
            detect_image, self.red_node_x = self.get_intersection(detect_image, self.red_line_m, self.draw_red_line_xy[1][0], self.draw_red_line_xy[1][1], self.red_y, (0, 0, 255))
            result_img = self.draw_line(img)
            cv2.imshow('show', result_img)
            self.program_fps = time.time() - reset
        cv2.destroyAllWindows()
        
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
        cv2.circle(raw_img, (find_x, find_y), 5, (255, 255, 255), -1)
        return raw_img, find_x, find_y, find_area
    
    def get_program_fps(self):
        return int(1 / self.program_fps)
    
    def get_keyboard(self):
        return self.key
    
    def get_green_node_x(self):
        return self.green_node_x

    def get_red_node_x(self):
        return self.red_node_x

    def get_green_x(self):
        return self.green_x
    
    def get_green_y(self):
        return self.green_y
    
    def get_green_area(self):
        return self.green_area
    
    def get_red_x(self):
        return self.red_x
    
    def get_red_y(self):
        return self.red_y
    
    def get_red_area(self):
        return self.red_area

    def shutdown(self):
        self.thread = False
        self.color_read_thread.join()
        self.camera_stream_thread.join()
        self.imcap.release()

class TCS34725():
    def __init__(self):
        self.enable_selection()
        self.time_selection()
        self.gain_selection()

    def enable_selection(self):
        """Select the ENABLE register configuration from the given provided values"""
        ENABLE_CONFIGURATION = (TCS34725_REG_ENABLE_AEN | TCS34725_REG_ENABLE_PON)
        bus.write_byte_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_ENABLE | TCS34725_COMMAND_BIT, ENABLE_CONFIGURATION)

    def time_selection(self):
        """Select the ATIME register configuration from the given provided values"""
        bus.write_byte_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_ATIME | TCS34725_COMMAND_BIT, TCS34725_REG_ATIME_2_4)

        """Select the WTIME register configuration from the given provided values"""
        bus.write_byte_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_WTIME | TCS34725_COMMAND_BIT, TCS34725_REG_WTIME_2_4)

    def gain_selection(self):
        """Select the gain register configuration from the given provided values"""
        bus.write_byte_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_CONTROL | TCS34725_COMMAND_BIT, TCS34725_REG_CONTROL_AGAIN_1)

    def readluminance(self):
        """Read data back from TCS34725_REG_CDATAL(0x94), 8 bytes, with TCS34725_COMMAND_BIT, (0x80)
        cData LSB, cData MSB, Red LSB, Red MSB, Green LSB, Green MSB, Blue LSB, Blue MSB"""
        data = bus.read_i2c_block_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_CDATAL | TCS34725_COMMAND_BIT, 8)

        # Convert the data
        cData = data[1] * 256 + data[0]
        red = data[3] * 256 + data[2]
        green = data[5] * 256 + data[4]
        blue = data[7] * 256 + data[6]

# Calculate luminance
        luminance = (-0.32466 * red) + (1.57837 * green) + (-0.73191 * blue)

        return {'c' : cData, 'r' : red, 'g' : green, 'b' : blue, 'l' : luminance}

class button_control():
    def __init__(self):
        pi.set_mode(Button_pin, pigpio.INPUT)
        pi.set_pull_up_down(Button_pin, pigpio.PUD_UP)

    def raw_value(self):
        return pi.read(Button_pin)
    
    def wait_press(self):
        state = 1
        while state == 1:
            state = pi.read(Button_pin)

    def wait_press_release(self):
        button_state = 1
        while button_state == 1:
            button_state = pi.read(Button_pin)
        button_state = 0
        while button_state == 0:
            button_state = pi.read(Button_pin)

    def wait_release(self):
        state = 0
        while state == 0:
            state = pi.read(Button_pin)

class LED_control():
    def __init__(self):
        pi.set_mode(Red_LED_pin, pigpio.OUTPUT)
        pi.set_mode(Green_LED_pin, pigpio.OUTPUT)

    def green_on(self):
        pi.write(Green_LED_pin, pigpio.HIGH)

    def green_off(self):
        pi.write(Green_LED_pin, pigpio.LOW)

    def red_on(self):
        pi.write(Red_LED_pin, pigpio.HIGH)

    def red_off(self):
        pi.write(Red_LED_pin, pigpio.LOW)

class dc_motor():
    def __init__(self):
        pi.set_mode(Motor_IN1_pin, pigpio.OUTPUT)
        pi.set_mode(Motor_IN2_pin, pigpio.OUTPUT)
        pi.set_mode(Motor_PWM_pin, pigpio.OUTPUT)
    def power(self, power):
        if power == 0:
            pi.write(Motor_IN1_pin, pigpio.LOW)
            pi.write(Motor_IN2_pin, pigpio.LOW)
            pi.set_PWM_dutycycle(Motor_PWM_pin, 0)
        elif power > 0:
            if reverse == True:
                pi.write(Motor_IN1_pin, pigpio.LOW)
                pi.write(Motor_IN2_pin, pigpio.HIGH)
            else:
                pi.write(Motor_IN1_pin, pigpio.HIGH)
                pi.write(Motor_IN2_pin, pigpio.LOW)
            pi.set_PWM_dutycycle(Motor_PWM_pin, constrain(mapping(power, 0, 100, 0, 255), 0, 255))
        else:
            if reverse == True:
                pi.write(Motor_IN1_pin, pigpio.HIGH)
                pi.write(Motor_IN2_pin, pigpio.LOW)
            else:
                pi.write(Motor_IN1_pin, pigpio.LOW)
                pi.write(Motor_IN2_pin, pigpio.HIGH)
            value = mapping(abs(power), 0, 100, 0, 255)
            pi.set_PWM_dutycycle(Motor_PWM_pin, constrain(mapping(abs(power), 0, 100, 0, 255), 0, 255))

class servo_motor():
    def __init__(self):
        pi.set_mode(Servo_pin, pigpio.OUTPUT)
    def angle(self, turn_angle):
        turn_angle = constrain(turn_angle, -servo_range, servo_range ) * -1
        self.servoangle = turn_angle + 90 + servo_offset
        duty = constrain(mapping(self.servoangle, 0, 180, 500, 2500), 500, 2500)
        pi.set_servo_pulsewidth(Servo_pin, duty)

class ultrasonic_sensor:
   def __init__(self):
      self._ping = False
      self._high = None
      self._time = None
      self._triggered = False
      self._trig_mode = pi.get_mode(trigger_pin)
      self._echo_mode = pi.get_mode(echo_pin)
      pi.set_mode(trigger_pin, pigpio.OUTPUT)
      pi.set_mode(echo_pin, pigpio.INPUT)
      self._cb = pi.callback(trigger_pin, pigpio.EITHER_EDGE, self._cbf)
      self._cb = pi.callback(echo_pin, pigpio.EITHER_EDGE, self._cbf)
      self._inited = True

   def _cbf(self, gpio, level, tick):
      if gpio == trigger_pin:
         if level == 0: # trigger sent
            self._triggered = True
            self._high = None
      else:
         if self._triggered:
            if level == 1:
               self._high = tick
            else:
               if self._high is not None:
                  self._time = tick - self._high
                  self._high = None
                  self._ping = True
   def read(self):
      if self._inited:
         self._ping = False
         pi.gpio_trigger(trigger_pin)
         start = time.time()
         while not self._ping:
            if (time.time()-start) > 5.0:
               return 20000
            time.sleep(0.001)
         return self._time/58.2
      else:
         return None
   def cancel(self):
      if self._inited:
         self._inited = False
         self._cb.cancel()
         pi.set_mode(trigger_pin, self._trig_mode)
         pi.set_mode(echo_pin, self._echo_mode)

class BNO055:
	BNO055_ADDRESS_A 				= 0x28
	BNO055_ADDRESS_B 				= 0x29
	BNO055_ID 		 			= 0xA0

	# Power mode settings
	POWER_MODE_NORMAL   				= 0X00
	POWER_MODE_LOWPOWER 				= 0X01
	POWER_MODE_SUSPEND  				= 0X02

	# Operation mode settings
	OPERATION_MODE_CONFIG 				= 0X00
	OPERATION_MODE_ACCONLY 				= 0X01
	OPERATION_MODE_MAGONLY 				= 0X02
	OPERATION_MODE_GYRONLY 				= 0X03
	OPERATION_MODE_ACCMAG 				= 0X04
	OPERATION_MODE_ACCGYRO 				= 0X05
	OPERATION_MODE_MAGGYRO 				= 0X06
	OPERATION_MODE_AMG 				= 0X07
	OPERATION_MODE_IMUPLUS 				= 0X08
	OPERATION_MODE_COMPASS 				= 0X09
	OPERATION_MODE_M4G 				= 0X0A
	OPERATION_MODE_NDOF_FMC_OFF 			= 0X0B
	OPERATION_MODE_NDOF 				= 0X0C

	# Output vector type
	VECTOR_ACCELEROMETER 				= 0x08
	VECTOR_MAGNETOMETER  				= 0x0E
	VECTOR_GYROSCOPE     				= 0x14
	VECTOR_EULER         				= 0x1A
	VECTOR_LINEARACCEL   				= 0x28
	VECTOR_GRAVITY       				= 0x2E

	# REGISTER DEFINITION START
	BNO055_PAGE_ID_ADDR 				= 0X07

	BNO055_CHIP_ID_ADDR 				= 0x00
	BNO055_ACCEL_REV_ID_ADDR 			= 0x01
	BNO055_MAG_REV_ID_ADDR 				= 0x02
	BNO055_GYRO_REV_ID_ADDR 			= 0x03
	BNO055_SW_REV_ID_LSB_ADDR 			= 0x04
	BNO055_SW_REV_ID_MSB_ADDR 			= 0x05
	BNO055_BL_REV_ID_ADDR 				= 0X06

	# Accel data register 
	BNO055_ACCEL_DATA_X_LSB_ADDR 			= 0X08
	BNO055_ACCEL_DATA_X_MSB_ADDR 			= 0X09
	BNO055_ACCEL_DATA_Y_LSB_ADDR 			= 0X0A
	BNO055_ACCEL_DATA_Y_MSB_ADDR 			= 0X0B
	BNO055_ACCEL_DATA_Z_LSB_ADDR 			= 0X0C
	BNO055_ACCEL_DATA_Z_MSB_ADDR 			= 0X0D

	# Mag data register 
	BNO055_MAG_DATA_X_LSB_ADDR 			= 0X0E
	BNO055_MAG_DATA_X_MSB_ADDR 			= 0X0F
	BNO055_MAG_DATA_Y_LSB_ADDR 			= 0X10
	BNO055_MAG_DATA_Y_MSB_ADDR 			= 0X11
	BNO055_MAG_DATA_Z_LSB_ADDR 			= 0X12
	BNO055_MAG_DATA_Z_MSB_ADDR			= 0X13

	# Gyro data registers 
	BNO055_GYRO_DATA_X_LSB_ADDR 			= 0X14
	BNO055_GYRO_DATA_X_MSB_ADDR 			= 0X15
	BNO055_GYRO_DATA_Y_LSB_ADDR 			= 0X16
	BNO055_GYRO_DATA_Y_MSB_ADDR 			= 0X17
	BNO055_GYRO_DATA_Z_LSB_ADDR 			= 0X18
	BNO055_GYRO_DATA_Z_MSB_ADDR 			= 0X19
	
	# Euler data registers 
	BNO055_EULER_H_LSB_ADDR 			= 0X1A
	BNO055_EULER_H_MSB_ADDR 			= 0X1B
	BNO055_EULER_R_LSB_ADDR 			= 0X1C
	BNO055_EULER_R_MSB_ADDR 			= 0X1D
	BNO055_EULER_P_LSB_ADDR 			= 0X1E
	BNO055_EULER_P_MSB_ADDR 			= 0X1F

	# Quaternion data registers 
	BNO055_QUATERNION_DATA_W_LSB_ADDR 		= 0X20
	BNO055_QUATERNION_DATA_W_MSB_ADDR 		= 0X21
	BNO055_QUATERNION_DATA_X_LSB_ADDR 		= 0X22
	BNO055_QUATERNION_DATA_X_MSB_ADDR 		= 0X23
	BNO055_QUATERNION_DATA_Y_LSB_ADDR 		= 0X24
	BNO055_QUATERNION_DATA_Y_MSB_ADDR 		= 0X25
	BNO055_QUATERNION_DATA_Z_LSB_ADDR 		= 0X26
	BNO055_QUATERNION_DATA_Z_MSB_ADDR 		= 0X27

	# Linear acceleration data registers 
	BNO055_LINEAR_ACCEL_DATA_X_LSB_ADDR 		= 0X28
	BNO055_LINEAR_ACCEL_DATA_X_MSB_ADDR 		= 0X29
	BNO055_LINEAR_ACCEL_DATA_Y_LSB_ADDR	 	= 0X2A
	BNO055_LINEAR_ACCEL_DATA_Y_MSB_ADDR		= 0X2B
	BNO055_LINEAR_ACCEL_DATA_Z_LSB_ADDR		= 0X2C
	BNO055_LINEAR_ACCEL_DATA_Z_MSB_ADDR		= 0X2D

	# Gravity data registers 
	BNO055_GRAVITY_DATA_X_LSB_ADDR 			= 0X2E
	BNO055_GRAVITY_DATA_X_MSB_ADDR	 		= 0X2F
	BNO055_GRAVITY_DATA_Y_LSB_ADDR 			= 0X30
	BNO055_GRAVITY_DATA_Y_MSB_ADDR 			= 0X31
	BNO055_GRAVITY_DATA_Z_LSB_ADDR 			= 0X32
	BNO055_GRAVITY_DATA_Z_MSB_ADDR 			= 0X33

	# Temperature data register 
	BNO055_TEMP_ADDR 				= 0X34

	# Status registers 
	BNO055_CALIB_STAT_ADDR 				= 0X35
	BNO055_SELFTEST_RESULT_ADDR	 		= 0X36
	BNO055_INTR_STAT_ADDR 				= 0X37

	BNO055_SYS_CLK_STAT_ADDR 			= 0X38
	BNO055_SYS_STAT_ADDR 				= 0X39
	BNO055_SYS_ERR_ADDR 				= 0X3A

	# Unit selection register 
	BNO055_UNIT_SEL_ADDR 				= 0X3B
	BNO055_DATA_SELECT_ADDR 			= 0X3C

	# Mode registers 
	BNO055_OPR_MODE_ADDR 				= 0X3D
	BNO055_PWR_MODE_ADDR 				= 0X3E

	BNO055_SYS_TRIGGER_ADDR 			= 0X3F
	BNO055_TEMP_SOURCE_ADDR 			= 0X40

	# Axis remap registers 
	BNO055_AXIS_MAP_CONFIG_ADDR 			= 0X41
	BNO055_AXIS_MAP_SIGN_ADDR 			= 0X42

	# SIC registers 
	BNO055_SIC_MATRIX_0_LSB_ADDR 			= 0X43
	BNO055_SIC_MATRIX_0_MSB_ADDR 			= 0X44
	BNO055_SIC_MATRIX_1_LSB_ADDR 			= 0X45
	BNO055_SIC_MATRIX_1_MSB_ADDR 			= 0X46
	BNO055_SIC_MATRIX_2_LSB_ADDR 			= 0X47
	BNO055_SIC_MATRIX_2_MSB_ADDR 			= 0X48
	BNO055_SIC_MATRIX_3_LSB_ADDR 			= 0X49
	BNO055_SIC_MATRIX_3_MSB_ADDR 			= 0X4A
	BNO055_SIC_MATRIX_4_LSB_ADDR 			= 0X4B
	BNO055_SIC_MATRIX_4_MSB_ADDR 			= 0X4C
	BNO055_SIC_MATRIX_5_LSB_ADDR 			= 0X4D
	BNO055_SIC_MATRIX_5_MSB_ADDR 			= 0X4E
	BNO055_SIC_MATRIX_6_LSB_ADDR 			= 0X4F
	BNO055_SIC_MATRIX_6_MSB_ADDR 			= 0X50
	BNO055_SIC_MATRIX_7_LSB_ADDR 			= 0X51
	BNO055_SIC_MATRIX_7_MSB_ADDR 			= 0X52
	BNO055_SIC_MATRIX_8_LSB_ADDR 			= 0X53
	BNO055_SIC_MATRIX_8_MSB_ADDR 			= 0X54
	
	# Accelerometer Offset registers	 
	ACCEL_OFFSET_X_LSB_ADDR 			= 0X55
	ACCEL_OFFSET_X_MSB_ADDR 			= 0X56
	ACCEL_OFFSET_Y_LSB_ADDR 			= 0X57
	ACCEL_OFFSET_Y_MSB_ADDR 			= 0X58
	ACCEL_OFFSET_Z_LSB_ADDR 			= 0X59
	ACCEL_OFFSET_Z_MSB_ADDR 			= 0X5A

	# Magnetometer Offset registers 
	MAG_OFFSET_X_LSB_ADDR 				= 0X5B
	MAG_OFFSET_X_MSB_ADDR 				= 0X5C
	MAG_OFFSET_Y_LSB_ADDR 				= 0X5D
	MAG_OFFSET_Y_MSB_ADDR 				= 0X5E
	MAG_OFFSET_Z_LSB_ADDR 				= 0X5F
	MAG_OFFSET_Z_MSB_ADDR 				= 0X60

	# Gyroscope Offset registers
	GYRO_OFFSET_X_LSB_ADDR 				= 0X61
	GYRO_OFFSET_X_MSB_ADDR 				= 0X62
	GYRO_OFFSET_Y_LSB_ADDR 				= 0X63
	GYRO_OFFSET_Y_MSB_ADDR 				= 0X64
	GYRO_OFFSET_Z_LSB_ADDR 				= 0X65
	GYRO_OFFSET_Z_MSB_ADDR 				= 0X66

	# Radius registers 
	ACCEL_RADIUS_LSB_ADDR 				= 0X67
	ACCEL_RADIUS_MSB_ADDR 				= 0X68
	MAG_RADIUS_LSB_ADDR 				= 0X69
	MAG_RADIUS_MSB_ADDR 				= 0X6A

	# REGISTER DEFINITION END


	def __init__(self, sensorId=-1, address=0x28):
		self._sensorId = sensorId
		self._address = address
		self._mode = BNO055.OPERATION_MODE_NDOF


	def begin(self, mode=None):
		if mode is None: mode = BNO055.OPERATION_MODE_NDOF
		# Open I2C bus
		self._bus = smbus.SMBus(1)

		# Make sure we have the right device
		if self.readBytes(BNO055.BNO055_CHIP_ID_ADDR)[0] != BNO055.BNO055_ID:
			time.sleep(1)	# Wait for the device to boot up
			if self.readBytes(BNO055.BNO055_CHIP_ID_ADDR)[0] != BNO055.BNO055_ID:
				return False

		# Switch to config mode
		self.setMode(BNO055.OPERATION_MODE_CONFIG)

		# Trigger a reset and wait for the device to boot up again
		self.writeBytes(BNO055.BNO055_SYS_TRIGGER_ADDR, [0x20])
		time.sleep(1)
		while self.readBytes(BNO055.BNO055_CHIP_ID_ADDR)[0] != BNO055.BNO055_ID:
			time.sleep(0.01)
		time.sleep(0.05)

		# Set to normal power mode
		self.writeBytes(BNO055.BNO055_PWR_MODE_ADDR, [BNO055.POWER_MODE_NORMAL])
		time.sleep(0.01)

		self.writeBytes(BNO055.BNO055_PAGE_ID_ADDR, [0])
		self.writeBytes(BNO055.BNO055_SYS_TRIGGER_ADDR, [0])
		time.sleep(0.01)

		# Set the requested mode
		self.setMode(mode)
		time.sleep(0.02)

		return True

	def setMode(self, mode):
		self._mode = mode
		self.writeBytes(BNO055.BNO055_OPR_MODE_ADDR, [self._mode])
		time.sleep(0.03)

	def setExternalCrystalUse(self, useExternalCrystal = True):
		prevMode = self._mode
		self.setMode(BNO055.OPERATION_MODE_CONFIG)
		time.sleep(0.025)
		self.writeBytes(BNO055.BNO055_PAGE_ID_ADDR, [0])
		self.writeBytes(BNO055.BNO055_SYS_TRIGGER_ADDR, [0x80] if useExternalCrystal else [0])
		time.sleep(0.01)
		self.setMode(prevMode)
		time.sleep(0.02)

	def getSystemStatus(self):
		self.writeBytes(BNO055.BNO055_PAGE_ID_ADDR, [0])
		(sys_stat, sys_err) = self.readBytes(BNO055.BNO055_SYS_STAT_ADDR, 2)
		self_test = self.readBytes(BNO055.BNO055_SELFTEST_RESULT_ADDR)[0]
		return (sys_stat, self_test, sys_err)

	def getRevInfo(self):
		(accel_rev, mag_rev, gyro_rev) = self.readBytes(BNO055.BNO055_ACCEL_REV_ID_ADDR, 3)
		sw_rev = self.readBytes(BNO055.BNO055_SW_REV_ID_LSB_ADDR, 2)
		sw_rev = sw_rev[0] | sw_rev[1] << 8
		bl_rev = self.readBytes(BNO055.BNO055_BL_REV_ID_ADDR)[0]
		return (accel_rev, mag_rev, gyro_rev, sw_rev, bl_rev)

	def getCalibration(self):
		calData = self.readBytes(BNO055.BNO055_CALIB_STAT_ADDR)[0]
		return (calData >> 6 & 0x03, calData >> 4 & 0x03, calData >> 2 & 0x03, calData & 0x03)

	def getTemp(self):
		return self.readBytes(BNO055.BNO055_TEMP_ADDR)[0]

	def getVector(self, vectorType):
		buf = self.readBytes(vectorType, 6)
		xyz = struct.unpack('hhh', struct.pack('BBBBBB', buf[0], buf[1], buf[2], buf[3], buf[4], buf[5]))
		if vectorType == BNO055.VECTOR_MAGNETOMETER:	scalingFactor = 16.0
		elif vectorType == BNO055.VECTOR_GYROSCOPE:	scalingFactor = 900.0
		elif vectorType == BNO055.VECTOR_EULER: 		scalingFactor = 16.0
		elif vectorType == BNO055.VECTOR_GRAVITY:	scalingFactor = 100.0
		else:											scalingFactor = 1.0
		return tuple([i/scalingFactor for i in xyz])

	def getQuat(self):
		buf = self.readBytes(BNO055.BNO055_QUATERNION_DATA_W_LSB_ADDR, 8)
		wxyz = struct.unpack('hhhh', struct.pack('BBBBBBBB', buf[0], buf[1], buf[2], buf[3], buf[4], buf[5], buf[6], buf[7]))
		return tuple([i * (1.0 / (1 << 14)) for i in wxyz])

	def readBytes(self, register, numBytes=1):
		return self._bus.read_i2c_block_data(self._address, register, numBytes)

	def writeBytes(self, register, byteVals):
		return self._bus.write_i2c_block_data(self._address, register, byteVals)
	
	def relative(self, dirction):
		value = dirction - int(self.getVector(self.VECTOR_EULER)[0]) + 180
		if value >= 0:
			gyro = (value % 360) - 180
		else:
			gyro = 359 - ((-1 - value) % 360) - 180
		time.sleep(0.01)
		return gyro

	def raw(self):
		return self.getVector(self.VECTOR_EULER)[0]

class lidarSensor():
    def __init__(self, lidar_type):
        if lidar_type == 'D100':
            self.D100_initialization()
        self.Lidar_left = -1
        self.Lidar_right = -1
        self.Lidar_mid = -1
        self.gyro_angle = 0

    def D100_initialization(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("/scan", LaserScan, self.D100_lidar_callback)

    def D100_lidar_callback(self, data):
        lens = int((data.angle_max - data.angle_min) / data.angle_increment)
        for i in range(lens):
            angle_error = int((data.angle_min + i * data.angle_increment) * RADIAN_TO_DEGREES) - 360
            if angle_error >= 0:
                angle = angle_error % 360 - 180
            else:
                angle = 359 - (-1 - angle_error) % 360 - 180
            ranges = data.ranges[i] * 100
            if not math.isnan(ranges):
                if angle > -5 and angle < 5:
                    self.Lidar_mid = round(data.ranges[i] * 100)
                if angle > 85 and angle < 95:
                    self.Lidar_left = round(data.ranges[i] * 100)
                if angle > -95 and angle < -85:
                    self.Lidar_right = round(data.ranges[i] * 100)

    def get_mid(self, gyro):
        self.gyro_angle = gyro
        return self.lidar_mid
    

         

class tools():        
    def constrain(self, x, out_min, out_max):
        return out_min if x < out_min else out_max if x > out_max else x                

def Motor_test():
    Motor = dc_motor()
    Motor.power(0)
    
def Distance_test():
    distance = ultrasonic_sensor()
    reset = time.time()
    while time.time() - reset < 5:
        print(distance.read())
        time.sleep(0.1)
    distance.cancel()
    pi.stop()
    
def Servo_test():
    servo = servo_motor()
    servo.angle(30)
    time.sleep(1)
    servo.angle(-30)
    time.sleep(1)
    servo.angle(0)

def color_test():
    color = TCS34725()
    while True:
        lum = color.readluminance()['c']
        print (lum)
        
def gyro_test():
    gyro = BNO055()
    if gyro.begin() is not True:
        print("Error initializing device")
        exit()
    time.sleep(1)
    gyro.setExternalCrystalUse(True)
    while True:
        print("rel:",gyro.relavite(0))
        print("abs:",int(gyro.getVector(gyro.VECTOR_EULER)[0]))
        time.sleep(0.01)
        
def external():
    control = external_control()
    while True:
        if control.button_read() == 0:
            control.Red_ON()
            control.Green_ON()
        else:
            control.Red_OFF()
            control.Green_OFF()

def lidar_test():
    lidar = YDlidar()
    motor = dc_motor()
    while True:
        a=lidar.read(0)

if __name__ == "__main__":
    Motor_test()