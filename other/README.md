# Diary
## 2023/06/26  

**member:** ZHAO,ZHEN-BO  

**content:**  

After reading the rules, I started to choose the controller. After watching the previous competitions, I found that most of them are raspberry pi but there are also jeston nano, so I decided to choose one of these two. I chose raspberry pi 4 because of its smaller size and cheaper price than jeston nano.


在閱讀完規則後，開始挑選控制器，因為看過歷屆的比賽，發現大多都是 raspberry pi 但也有 jeston nano 因此決定在這兩種裡挑一種，選擇的是 raspberry pi 4 因為體積比較小而且價格也比 jeston nano 便宜 


## 2023/06/29 ~ 2023/06/31  

**member:** ZHAO,ZHEN-BO  

**content:**  

While waiting for the Raspberry Pi to be initialized and the library to be installed, there are two motors to choose as power, namely GA25-370 and JGA16-050. The former has the advantage of large torque and can drive heavy objects. The latter has the advantage of small size and light weight, but the torque is relatively small. Considering that the body may be heavier, I chose the GA25-370 with higher torque.


在等待初始化樹梅派及安裝函式庫時，挑選作為動力的馬達，有兩種，分別是 GA25-370 和 JGA16-050，前者的優點是扭力大，可以帶動較重的物體，後者的優點是體積小，重量也比較輕，但是扭力相對較小，由於考慮到機體可能會比較重，所以選了扭力較大的 GA25-370  


## 2023/07/01 ~ 2023/07/02  

**member:** ZHAO,ZHEN-BO  

**content:**  

The next step is the steering motor. After searching the information on the Internet, I found that MG90S and SG90 are commonly used. The difference between MG90S and SG90 is that the front gear is metal, and the latter is plastic. Because we often need to rotate all the time, we choose MG90S, which is not easy to damage


接下來就是轉向馬達，在網上查找資料後，發現常用的是 MG90S 跟 SG90 兩種，MG90S 跟 SG90 的差異是前著齒輪式金屬，後者是塑膠，因為我們常需要一直旋轉，因此選擇就不容易損壞的 MG90S  


## 2023/07/03 ~ 2023/07/05  

**member:** ZHAO,ZHEN-BO  

**content:**   

Then there is the controller for controlling the motor. There are L293D chips and L298N templates. In order to reduce weight, the smaller L293D chip is selected because of its smaller size, so more sensors can be installed. Reducing space can reduce weight and increase moving speed.


再來是控制馬達的控制器，有 L293D 晶片 和 L298N 模板，為了減輕重量，所以選擇較小的 L293D 晶片因為體積較小的關係，所以可以裝上更多的感應器，減少空間可以減輕重量，增加移動速度  


## 2023/07/06 ~ 2023/07/08  

**member:** ZHAO,ZHEN-BO  

**content:**  

But these are not complete, because there is no way to turn normally, so I added supersonic, so that you can turn before hitting the wall


但是這些還不完整，因為沒辦法正常的轉彎，因此我加上了超音波，這樣就可以在撞到牆之前轉彎  


## 2023/07/09 ~ 2023/07/12  

**member:** ZHAO,ZHEN-BO  

**content:**

But you can't just turn, because you need to rotate clockwise and counterclockwise, so you need a color sensor to sense the color of the ground line to judge whether it is clockwise or counterclockwise, so when choosing a color sensor, because it is to measure the line on the ground, it should be thin and close to the ground, so it can't be too large, so the TCS34725 color sensor meets my requirements.


但是不能只會轉彎，因為要順時針旋轉和逆時針旋轉，因此需要顏色感測器感測地上線的顏色來判斷是順時針和逆時針，所以在挑選顏色感測器時，因為是要測地上的線，所以要薄的，可以貼近地面的，所以也不能太大，因此 TCS34725 顏色感測器很符合我的要求 


## 2023/07/09 ~ 2023/07/12  

**member:** ZHAO,ZHEN-BO  

**content:**

Later, when I used the color sensor to detect the line, I encountered some bottlenecks, because I still don’t know how to detect the values ​​​​of the blue and orange lines, so I searched online, but there was no satisfactory result, so I asked my seniors and referred to their programs. Later, the detection was successful, and I can confirm that there is a line on the ground, but I still can’t tell whether it is blue or orange.


在之後使用顏色感測器偵測線時遇到了點瓶頸，因為我還不知道要怎麼偵測藍、橘線的數值，因此我上網找，但是沒有滿意的結果，所以我詢問學長，參考了他們的程式，後來偵測成功了，可以確定地上有線，但是還是無法分辨是藍色還是橘色  


## 2023/07/13 ~ 2023/07/15  

**member:** ZHAO,ZHEN-BO  

**content:**

Then use the algorithm to limit the value to an integer, so that the value of identifying the color looks neater, and it is easier to find problems in the debugger


之後利用演算法使數值限制成整數，讓辨識顏色的數值看起來較整齊，比較容易在偵錯器中找到問題


## 2023/07/16 ~ 2023/07/17  

**member:** ZHAO,ZHEN-BO  

**content:**

The next step is to use the gyroscope to make the machine move in a straight line, but the gyroscope is not easy to use, so it is the help of the seniors to make my machine move in a straight line


接下來就是借用陀螺儀讓機器能夠直線前進，但是陀螺儀並不好使用，因此是學長幫忙才讓我的機器能夠直線行走


## 2023/07/18 ~ 2023/07/22  

**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN  

**content:**

Although you can use the gyroscope to go straight and use the ultrasonic to turn, but it is possible to rub against the wall when turning, and then get stuck on the wall and cannot continue to run. Then we changed the ultrasonic to the laser. The laser can detect the surroundings, so it can be maintained in the middle of the road, and it can also detect the turning ahead

雖然可以藉由陀螺儀直行，和利用超音波轉彎，但是有可能轉彎時擦到牆壁，然後卡牆邊無法繼續運行，之後我們將超音波改成了光達，光達可以偵測四周，因此可以維持在道路中央，還可以偵測前方轉彎




# <div align="center">[Return Home](../)</div>