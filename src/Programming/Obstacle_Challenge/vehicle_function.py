import pigpio
import time
import smbus
import struct
import os
import math
import cv2
import threading
import numpy as np

Red_LED_pin = 27   
Green_LED_pin = 22
Motor_IN1_pin = 6  
Motor_IN2_pin = 13 
Motor_PWM_pin = 19
Button_pin = 5    
Servo_pin = 26    

servo_offset = 15                      
reverse = False                        
servo_range = 30                       
block_detect_min_area = 100            
image_black_area = 310                 
image_black_area_down = 400
red_line_xy = [[460, 0], [70, 480]]    
green_line_xy = [[180, 0], [570, 480]] 
camera_BRIGHTNESS = 55                 
RADIAN_TO_DEGREES = 360/(math.pi *2)
pi = pigpio.pi()

def mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def constrain(x, out_min, out_max):
    return out_min if x < out_min else out_max if x > out_max else x
bus = smbus.SMBus(1)

TCS34725_DEFAULT_ADDRESS = 0x29

TCS34725_COMMAND_BIT = 0x80
TCS34725_REG_ENABLE = 0x00 
TCS34725_REG_ATIME = 0x01 
TCS34725_REG_WTIME = 0x03 
TCS34725_REG_CONFIG = 0x0D 
TCS34725_REG_CONTROL = 0x0F 
TCS34725_REG_CDATAL = 0x14 
TCS34725_REG_CDATAH = 0x15 
TCS34725_REG_RDATAL = 0x16 
TCS34725_REG_RDATAH = 0x17 
TCS34725_REG_GDATAL = 0x18 
TCS34725_REG_GDATAH = 0x19 
TCS34725_REG_BDATAL = 0x1A 
TCS34725_REG_BDATAH = 0x1B

TCS34725_REG_ENABLE_SAI = 0x40 
TCS34725_REG_ENABLE_AIEN = 0x10 
TCS34725_REG_ENABLE_WEN = 0x08 
TCS34725_REG_ENABLE_AEN = 0x02
TCS34725_REG_ENABLE_PON = 0x01

TCS34725_REG_ATIME_2_4 = 0xFF 
TCS34725_REG_ATIME_24 = 0xF6 
TCS34725_REG_ATIME_101 = 0xDB 
TCS34725_REG_ATIME_154 = 0xC0 
TCS34725_REG_ATIME_700 = 0x00 
TCS34725_REG_WTIME_2_4 = 0xFF 
TCS34725_REG_WTIME_204 = 0xAB 
TCS34725_REG_WTIME_614 = 0x00 

TCS34725_REG_CONTROL_AGAIN_1 = 0x00 
TCS34725_REG_CONTROL_AGAIN_4 = 0x01 
TCS34725_REG_CONTROL_AGAIN_16 = 0x02 
TCS34725_REG_CONTROL_AGAIN_60 = 0x03 

    def start(self):
        self.thread = True
        self.color_read_thread.start()
        self.camera_stream_thread.start()


    def camera_stream(self):
        while self.thread:
            _, self.raw_image = self.imcap.read()
            self.key = cv2.waitKey(15)
        
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
        ENABLE_CONFIGURATION = (TCS34725_REG_ENABLE_AEN | TCS34725_REG_ENABLE_PON)
        bus.write_byte_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_ENABLE | TCS34725_COMMAND_BIT, ENABLE_CONFIGURATION)

    def time_selection(self):
        bus.write_byte_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_ATIME | TCS34725_COMMAND_BIT, TCS34725_REG_ATIME_2_4)

        bus.write_byte_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_WTIME | TCS34725_COMMAND_BIT, TCS34725_REG_WTIME_2_4)

    def gain_selection(self):
        bus.write_byte_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_CONTROL | TCS34725_COMMAND_BIT, TCS34725_REG_CONTROL_AGAIN_1)

    def readluminance(self):        
        data = bus.read_i2c_block_data(TCS34725_DEFAULT_ADDRESS, TCS34725_REG_CDATAL | TCS34725_COMMAND_BIT, 8)

        cData = data[1] * 256 + data[0]
        red = data[3] * 256 + data[2]
        green = data[5] * 256 + data[4]
        blue = data[7] * 256 + data[6]

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
		self.setMode(mode)
		time.sleep(0.02)
		return True

	def raw(self):
		return self.getVector(self.VECTOR_EULER)[0]

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
    print("error")