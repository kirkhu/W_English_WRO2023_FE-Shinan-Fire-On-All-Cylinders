import time
import pickle
from vehicle_function import*
import time

LED = LED_control()
button = button_control()
motor = dc_motor()
servo = servo_motor()
gyro_sensor = BNO055()
color_sensor = TCS34725()
mapping = tools()

white_color = -1
orange_color = -1
blue_color = -1

def white_area_read():
    global white_color
    print('=======white area=======')
    print('wait button')
    button.wait_press_release()
    print('start white area\n')
    state = 1
    low_color = 100
    while state == 1:
        state = button.raw_value()
        color = color_sensor.readluminance()['c']
        if color < low_color:
            low_color = color
            print('  white:' + str(low_color))
        time.sleep(0.01)
    button.wait_release()
    white_color = low_color

def orange_line_read():
    print('\n=======orange line=======')
    print('wait button')
    button.wait_press_release()
    print('start orange line\n')
    state = 1
    low_color = 100
    while state == 1:
        state = button.raw_value()
        color = color_sensor.readluminance()['c']
        if color < low_color:
            low_color = color
            print('  Orange:' + str(low_color))
        time.sleep(0.01)
    button.wait_release()
    orange_color = low_color

def blue_line_read():
    print('\n=======blue line=======')
    print('wait button')
    button.wait_press_release()
    print('start blue line\n')
    state = 1
    low_color = 100
    while state == 1:
        state = button.raw_value()
        color = color_sensor.readluminance()['c']
        if color < low_color:
            low_color = color
            print('  Blue:' + str(low_color))
        time.sleep(0.01)
    button.wait_release()
    blue_color = low_color


def file_write():
    print('\n=======file write down=======')
    print('Orange:' + str(orange_color))
    print('Blue:' + str(blue_color))
    print('white:' + str(white_color))
    value = {}
    value['Blue'] = blue_color
    value['Orange'] = orange_color
    value['white'] = white_color
    print('Write Finish')
    pickle.dump(value, open('save_file/color_sensor.p', 'wb') )

white_area_read()
orange_line_read()
blue_line_read()