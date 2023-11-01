#Import the required modules(匯入所需的模組)
import pigpio       #Raspberry Pi I/O Control Function Library
import time         #Time Module時間模組
import smbus        #I2C Manage
import struct       #Binary Data Packing and Unpacking Module二進位數據打包、解包的模組
import os           #System Information Reading Module 讀系統資訊
import math         #Mathematical Calculation Module 數學運算
import cv2          #OpenCV  Module 影像處理
import threading    #Multithread Management  Module 多執行緒管理
import pickle       #Serialization/Deserialization Module 序列化/反序列化模組
import rospy        #ROS Python Commands Module ROS的Python指令
import numpy as np  #Multidimensional Arrays and Matrix Operations Module 多維陣列與矩陣運算
import signal       #Exception Handling Module 異常事件處理模組
from sensor_msgs.msg import LaserScan  #ROS Data Structure Definitions ROS定義資料結構

#==========Pin configuration(腳位設定)==========
Red_LED_pin = 27   
Green_LED_pin = 22
Motor_IN1_pin = 6  
Motor_IN2_pin = 13 
Motor_PWM_pin = 19
Button_pin = 5    
Servo_pin = 26    
#==========Parameter Settings(參數設定)==========
servo_offset = 15                      
reverse = False 

# Servo Motor Angle Limitation(伺服馬達角度限制) 
servo_range = 30                  
block_detect_min_area = 100

#Black mask area at the top of the image screen(影像畫面上方黑色遮罩範圍)
image_black_area = 310

#Black mask area at the bottom of the image frame(影像畫面下方黑色遮罩範圍)
image_black_area_down = 400 

#Adjusting Image Brightness(影像畫面亮度調整)
camera_BRIGHTNESS = 55   
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

#Executing threads for task scheduling(執行緒進行執行排程)
    def start(self):
        self.thread = True
        self.color_read_thread.start()
        self.camera_stream_thread.start()
	    
#Capture images(擷取影像)
    def camera_stream(self):
        while self.thread:
            _, self.raw_image = self.imcap.read()
            self.key = cv2.waitKey(15)

#Identify obstacle coordinates and calculate the center point of the obstacle(辨識障礙物座標並計算出障礙物中心點)        
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

#Calculate Program FPS(計算程式運算速度)
    def get_program_fps(self):
        return int(1 / self.program_fps)

#Read keyboard keys(讀取鍵盤按鍵)
    def get_keyboard(self):
        return self.key
#Return the variable green_x to allow external code to access this value(將變數green_x回傳，讓外部程式碼可以獲取該值)
    def get_green_x(self):
        return self.green_x

#Return the variable green_y to allow external code to access this value(將變數green_y回傳，讓外部程式碼可以獲取該值)
    def get_green_y(self):
        return self.green_y

#Return the variable green_area to allow external code to access this value(將變數green_area回傳，讓外部程式碼可以獲取該值)
    def get_green_area(self):
        return self.green_area

#Return the variable red_x to allow external code to access this value(將變數red_x回傳，讓外部程式碼可以獲取該值)
    def get_red_x(self):
        return self.red_x

#Return the variable red_y to allow external code to access this value(將變數red_y回傳，讓外部程式碼可以獲取該值)
    def get_red_y(self):
        return self.red_y
	    
#Return the variable red_area to allow external code to access this value(將變數red_area回傳，讓外部程式碼可以獲取該值)
    def get_red_area(self):
        return self.red_area

#Terminating a thread(將執行緒終止)
    def shutdown(self):
        self.thread = False
        self.color_read_thread.join()
        self.camera_stream_thread.join()
        self.imcap.release()

#Define a class for a color sensor(定義顏色感測器的類別)
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

#Define a class for buttons(定義按鈕的類別)
class button_control():
    def __init__(self):
        pi.set_mode(Button_pin, pigpio.INPUT)
        pi.set_pull_up_down(Button_pin, pigpio.PUD_UP)

#Read button(讀取按鈕)
    def raw_value(self):
        return pi.read(Button_pin)

#Wait for the button until it's pressed(等待按鈕直到按下)	
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

#Define a class for LEDs(定義LED的類別)
class LED_control():
    def __init__(self):
        pi.set_mode(Red_LED_pin, pigpio.OUTPUT)
        pi.set_mode(Green_LED_pin, pigpio.OUTPUT)

#Turn on the green LED(打開綠色LED)
    def green_on(self):
        pi.write(Green_LED_pin, pigpio.HIGH)

#Turn off the green LED(關閉綠色LED)
    def green_off(self):
        pi.write(Green_LED_pin, pigpio.LOW)

#Turn on the red LED(打開紅色LED)
    def red_on(self):
        pi.write(Red_LED_pin, pigpio.HIGH)

#Turn off the red LED(關閉紅色LED)
    def red_off(self):
        pi.write(Red_LED_pin, pigpio.LOW)

#Define a class for DC motors(定義直流馬達的類別)
class dc_motor():
    def __init__(self):
        pi.set_mode(Motor_IN1_pin, pigpio.OUTPUT)
        pi.set_mode(Motor_IN2_pin, pigpio.OUTPUT)
        pi.set_mode(Motor_PWM_pin, pigpio.OUTPUT)

#Configure DC motor output(設定直流馬達輸出)    
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

#Define a class for servo motors(定義伺服馬達的類別)
class servo_motor():

#Configure servo motor GPIO angle position(設定伺服馬達GPIO角位)
    def __init__(self):
        pi.set_mode(Servo_pin, pigpio.OUTPUT)

#Set servo motor angle(設定伺服馬達角度)	
    def angle(self, turn_angle):
        turn_angle = constrain(turn_angle, -servo_range, servo_range ) * -1
        self.servoangle = turn_angle + 90 + servo_offset
        duty = constrain(mapping(self.servoangle, 0, 180, 500, 2500), 500, 2500)
        pi.set_servo_pulsewidth(Servo_pin, duty)

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
		self.setMode(mode)
		time.sleep(0.02)
		return True

	def raw(self):
		return self.getVector(self.VECTOR_EULER)[0]
		
#Define a class for LiDAR(定義光達的類別)
class lidarSensor():
    def __init__(self, lidar_type):
        if lidar_type == 'D100':
            self.D100_initialization()
        self.Lidar_left = -1
        self.Lidar_right = -1
        self.Lidar_mid = -1

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
         
class tools():        
    def constrain(self, x, out_min, out_max):
        return out_min if x < out_min else out_max if x > out_max else x                

if __name__ == "__main__":
    print("error")
