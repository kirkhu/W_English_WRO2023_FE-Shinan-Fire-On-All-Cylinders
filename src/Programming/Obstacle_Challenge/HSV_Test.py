#Import the required modules(匯入所需的模組)
import cv2
import time
import pickle
import numpy as np

set_light = 60

def undistort(img, cal_dir='/home/pi/Desktop/opencv_detect/image/cal_pickle.p'):
    with open(cal_dir, mode='rb') as f: 
        file = pickle.load(f) 
    mtx = file['mtx'] 
    dist = file['dist'] 
    dst = cv2.undistort(img, mtx, dist, None, mtx) 
    return dst

#Display all functions of the numeric keypad(顯示數字鍵所有功能)
def print_mes():
    print('---------------')
    print('1, set Green')
    print('2, set Red')
    print('3, HSV value reset.')
    print('4, Write green.')
    print('5, Write red.')
    print('---------------')
    
def nothing(x):
    pass

img2 = np.zeros((300,512,3), np.uint8)
img = np.uint8(np.clip((cv2.add(1*img2,30)),0,255))
img1 = np.uint8(np.clip((cv2.add(1.5*img2,100)),0,255))
img2 = np.hstack((img2,img1,img))
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H_low','image',0,255,nothing)
cv2.createTrackbar('H_high','image',255,255,nothing)
cv2.createTrackbar('S_low','image',0,255,nothing)
cv2.createTrackbar('S_high','image',255,255,nothing)
cv2.createTrackbar('V_low','image',0,255,nothing)
cv2.createTrackbar('V_high','image',255,255,nothing)

imcap = cv2.VideoCapture(0)
imcap.set(3, 480) # set width as 640 480
imcap.set(4, 360) # set height as 480 360
imcap.set(cv2.CAP_PROP_FPS, 40)
imcap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
imcap.set(cv2.CAP_PROP_BRIGHTNESS, set_light)
imcap.set(cv2.CAP_PROP_CONTRAST, 10)
imcap.set(cv2.CAP_PROP_EXPOSURE, 0)
kernal = np.ones((4,4), np.uint8)

print_mes()

while(1):
    H_high = cv2.getTrackbarPos('H_high','image')
    H_low = cv2.getTrackbarPos('H_low','image')
    S_high = cv2.getTrackbarPos('S_high','image')
    S_low = cv2.getTrackbarPos('S_low','image')
    V_high = cv2.getTrackbarPos('V_high','image')
    V_low = cv2.getTrackbarPos('V_low','image')
    success, img = imcap.read()
    img[0:190, 0:480] = [0, 0, 0]
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hls_low = np.array([H_low, S_low, V_low])
    hls_high = np.array([H_high, S_high, V_high])
    
    mask = cv2.inRange(hls, hls_low, hls_high)
#     mask = cv2.dilate(mask,kernal,iterations=1)
    res = cv2.bitwise_and(img, img, mask=mask)
    
    cv2.imshow('image',res)
    
    k = cv2.waitKey(25) & 0xFF

    #Display HSV_Green values(顯示HSV_Red數值)
    if k == ord('1'):
        with open('save_file/HSV_Green.p', mode='rb') as f:
            file = pickle.load(f)
        Green_Lower = file['Lower']
        Green_Upper = file['Upper']
        
        cv2.setTrackbarPos('H_high','image', Green_Upper[0])
        cv2.setTrackbarPos('H_low','image', Green_Lower[0])
        cv2.setTrackbarPos('S_high','image', Green_Upper[1])
        cv2.setTrackbarPos('S_low','image', Green_Lower[1])
        cv2.setTrackbarPos('V_high','image', Green_Upper[2])
        cv2.setTrackbarPos('V_low','image', Green_Lower[2])
        print('Green_set')
        print_mes()

    #Display HSV_Red values(顯示HSV_Red數值)
    if k == ord('2'):
        with open('save_file/HSV_Red.p', mode='rb') as f:
            file = pickle.load(f)
        Red_Lower = file['Lower']
        Red_Upper = file['Upper']
        cv2.setTrackbarPos('H_high','image', Red_Upper[0])
        cv2.setTrackbarPos('H_low','image', Red_Lower[0])
        cv2.setTrackbarPos('S_high','image', Red_Upper[1])
        cv2.setTrackbarPos('S_low','image', Red_Lower[1])
        cv2.setTrackbarPos('V_high','image', Red_Upper[2])
        cv2.setTrackbarPos('V_low','image', Red_Lower[2])
        print('Red_set')
        print_mes()

    #Restore HSV values to default(將HSV數值恢復為預設)
    if k == ord('3'):
        cv2.setTrackbarPos('H_high','image', 255)
        cv2.setTrackbarPos('H_low','image', 0)
        cv2.setTrackbarPos('S_high','image', 255)
        cv2.setTrackbarPos('S_low','image', 0)
        cv2.setTrackbarPos('V_high','image', 255)
        cv2.setTrackbarPos('V_low','image', 0)
        print('Reset')
        print_mes()
        
    #Record green HSV values(紀錄綠色HSV數值)
    if k == ord('4'):
        print('====Green HSV====')
        hsv_value = {}
        hsv_value['Lower'] = [H_low, S_low, V_low]
        hsv_value['Upper'] = [H_high, S_high, V_high]
        print('lower:' + str(hsv_value['Lower']))
        print('upper:' + str(hsv_value['Upper']))
        print('Write Finish')
        pickle.dump(hsv_value, open('save_file/HSV_Green.p', 'wb') )
        print_mes()

    #Record red HSV values(紀錄紅色HSV數值)
    if k == ord('5'):
        print('====Red HSV====')
        hsv_value = {}
        hsv_value['Lower'] = [H_low, S_low, V_low]
        hsv_value['Upper'] = [H_high, S_high, V_high]
        print('lower:' + str(hsv_value['Lower']))
        print('upper:' + str(hsv_value['Upper']))
        print('Write Finish')
        pickle.dump(hsv_value, open('save_file/HSV_Red.p', 'wb') )
        print_mes()
    if k == 27:
        break
imcap.release()
cv2.destroyAllWindows()
