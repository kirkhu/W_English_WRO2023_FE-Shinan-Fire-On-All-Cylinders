2023WRO Future Engineers Shinan Fire On All Cylinders  
=====
# <div align="center">Work Diary </div> 

## 2023/06/26 ~ 2023/07/02 
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- During today's testing, we discovered that the robot tends to misinterpret people wearing red or green clothing in its surroundings as obstacles, causing it to unnecessarily avoid them and potentially miss avoiding the next block in time. To address this issue, we added an additional layer of black masking at the top of the camera's field of view, preventing the robot from detecting colors outside of the track area.After adding the black masking, the robot will no longer detect colors outside of the track area, reducing the chances of interference.

- 今天在測試時發現當機器在周圍人穿紅色衣物或綠色衣物時會誤測成積木讓機器閃避，導致無法及時閃過下一個積木，因此我們在畫面的上方將上一層黑色遮罩，讓機器無法偵測場地以外的顏色。在加上黑色遮罩之後，就不會再偵測到場外的顏色，減少被干擾的機率。

<div align="center">
<table>
<tr align="center">
<th>使用黑色遮罩屏蔽場外的顏色</th> 
</tr>
<tr align="center">
<td><img src="./img/6/black_hid.png" width="300" alt="cover"></td>
</table>
</div>

## 2023/07/03 ~ 2023/07/09 
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- This week, most of the programming has been completed, and we began testing the robot's success rate. We started with a speed of 50%, and due to its slower pace, the robot responded well for the most part. However, when accelerating to 70% speed, the color sensor occasionally misjudged the track's color due to its high speed. As a result, we modified the turning conditions to use the LiDAR's measurements of the left and right directions for determining the turning direction. This adjustment reduces the likelihood of turning in the wrong direction because of color misjudgment.

#### Detecting the direction of the turn
```
if get_left_dis > 100:
    reverse = False
else:
    reverse = True
if get_mid_dis > 55:
    servo.angle(-40)
```


## 2023/07/10 ~ 2023/07/16 
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- The robot is now capable of successfully avoiding obstacles and completing the third lap around the track. The next task is to detect blocks and perform a turnaround maneuver. The turnaround will be executed only if the last block of the second lap is red. Therefore, it is necessary to detect the number of laps. We will use the color sensor to count the number of times the line is crossed and determine whether the set count has been reached.

- If the specified count has not yet been achieved, the system will continue to record the color of the nearest traffic sign until the count of line crossings is greater than or equal to the set count. At this point, the color recording will cease.

- After recording the color of the nearest traffic sign, the program will determine whether the color is red. If the color is indeed red, the system will adjust the angle of the servo motor to initiate a right turn and will continue turning until the vehicle is properly aligned in the specified direction, thus executing a turnaround maneuver. If the detected color is not red, the vehicle will proceed to move forward.


<div align="center">
<table>
<tr align="center">
<th>Display the number of line crossings and the color of the nearest traffic sign.</th>
<th>Adjusting the values.
</th>
</tr>
<tr align="center">
<td><img src="./img/7/detect_last_obstacle.png" width="200" alt="print color"></td>
<td><img src="./img/7/check.jpeg" width="300" alt="check"></td>
</table>
</div>

## 2023/07/17 ~ 2023/07/23  
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- As the field mission has been roughly completed, we are going to start writing the technical report. Since we are not familiar with the correct technical report format, we have referred to the official website's technical report documentation and found that the report should include the following sections.

  1. modles: This folder should contain documentation related to the vehicle models, such as files for laser cutting machines and 3D printers.

  2. other: This folder is used to store data that does not belong to other categories, such as communication protocols and engineering logs.

  3. schemes: This folder is dedicated to hardware introductions, explaining the functions of electronic components and how they are connected.

  4. src: All programs should be placed in this folder.

  5. t-photos: This folder should contain team photos, including a group photo and funny pictures.

  6. v-photos: Machine photos from six different perspectives should be placed in this folder.

  7. video: Videos demonstrating the machine's operation should be placed in this folder, with each video lasting more than 30 seconds.

- When writing the technical report, we are switching between VS Code and the GitHub website. We use a desktop computer to view the GitHub web page and a laptop to edit the report in VS Code.

<div align="center">
<table>
<tr align="center">
<th>Official website's GitHub example</th> 
<th>Laptop and desktop comparison and modifications</th>
</tr>
<tr align="center">
<td><img src="./img/7/github_example.png" width="300" alt="github_example"></td>
<td><img src="./img/7/vs_code.jpeg" width="300" alt="更改文件"></td>
</table>
</div>

## 2023/07/24 ~ 2023/07/30  
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- We organized and listed the components in the parts inventory, and we uploaded them to the technical documentation.Additionally, we completed the drawing of the vehicle's introduction diagram. Throughout this process, we embarked on a learning journey, gradually familiarizing ourselves with GitHub syntax. Although we are not yet fully proficient in using GitHub, we dedicated time to researching relevant information online and steadily improving our skills. These achievements have brought valuable advancements to our report and project as a whole.
- Over the past few days, we have been continuously adjusting and fine-tuning the execution of the tasks at the venue, making constant adjustments to motor speed and various parameters, with the hope of effectively reducing the error rate. We are eager to achieve better performance and improve our overall competition results.
- During practical testing, we discovered that the vehicle was getting stuck at the junctions of the terrain due to protrusions, which was affecting its normal operation. To address this issue, we adopted a method of using a laser cutting machine to create 3mm thick spacers. These spacers were then placed under the vehicle chassis to elevate its height, enabling the vehicle to pass over the obstacles smoothly.

#### Overcoming Terrain Protrusions 

<div align="center">
<table>
<tr align="center">
<th> <img src="./img/7/Spacer1.png" alt="Spacer" width=300 /></th> 
<th><img src="./img/7/Spacer2.jpg" alt="Spacer" width=300 /></th>
<th><img src="./img/7/Spacer3.jpg" alt="Spacer"  width=300/></th>
</tr>
<tr align="center">
<td><img src="./img/7/Spacer4.jpg" alt="Spacer" width=300 /></td>
<td><img src="./img/7/Spacer5.jpg" alt="Spacer" width=300 /></td>
<td><img src="./img/7/Spacer6.jpg" alt="Spacer"  width=300/></td>
</table>
</div>

### Team Members' Practice Status

<div align="center">
<table>
<tr  align="center"> 
<th> <img src="./img/7/work_photo_2_1_0729.jpg" alt="work_photo_2_1_0729" width=300 /></th> 
<th><img src="./img/7/work_photo_2_2_0729.jpg" alt="work_photo_2_2_0729" width=300 /></th>
</tr>
<tr align="center">
<td><img src="./img/7/work_photo_1_1_0727.jpg" alt="work_photo_1_1_0727"  width=300/></td>
<td><img src="./img/7/work_photo_2_1_0727.jpg" alt="work_photo_2__0727" width=300 /></td>
</tr>
</table>
</div> 

## 2023/07/31 ~ 2023/08/06
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**  

- As the deadline for submitting the technical report is next week, we have begun revising the content of the technical documentation. We are also adjusting the website according to the official grading criteria and continuously adding to the technical report.
- Complete recording videos for each task and upload them to YouTube.


<table>
<tr align="center">
<th> old directory </th>
<th> Revised Directory (Upper Section) </th>
<th> Revised Directory (Lower Section) </th>
</tr>
<tr align="center">
<td><img src="./img/8/old_content.png" alt="old_content"  width="300"/> </td>
<td> <img src="./img/8/new1_content.png" alt="new1_content"  width="300"/></td>
<td> <img src="./img/8/new2_content.png" alt="new1_content"  width="300"/></td>
</tr>
</table>

  __Open Challenge__
  - [Open Challenge full narrow speed 70%](https://youtu.be/QtpuHt05MDg)
  - [Open Challenge full anrrow speed 50%](https://youtu.be/QaYUrrdAtE8)
  - [Open Challenge half width and half narrow speed 70%](https://youtu.be/pcTpH8QgJFU)
  - [Open Challenge half width and half narrow speed 50%](https://youtu.be/7HdWxfWPfWc)
  - [Open Challenge all width speed 70%](https://youtu.be/MA1k2P87LdE)
  - [Open Challenge all Width speed 50%](https://youtu.be/OUg0x4Qdc0c)  

 __Open Challenge__
  - [Obstacle Challenge speed 50% ](https://youtu.be/Jo7555gfXG8)
  - [Obstacle Challenge speed 70% ](https://youtu.be/iCmcXbACizY)

__Team Members' Practice Status__

<div align="center">
<table>
<tr align="center">
<th>report writing</th> 
<th>mechanism adjustment</th>
<th>report writing</th>
<th>field mission practice</th>
</tr>
<tr align="center">
<td><img src="./img/8/work_photo_1_0805.jpg" width="500" alt="work_daily"></td>
<td><img src="./img/8/work_photo_2_0805.jpg" width="500" alt="work_daily"></td>
<td><img src="./img/8/work_photo_3_0805.jpg" width="500" alt="work_daily"></td>
<td><img src="./img/8/work_photo_4_0805.jpg" width="500" alt="work_daily"></td>
</table>
</div>

## 2023/08/07 ~ 2023/08/13
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- This week, with our machine now adjusted to smoothly complete the mission race on the field, we have begun filming an introductory video for the race. In the video, we will showcase the actions our vehicle performs during the mission race, providing explanations through subtitles synchronized with the video.


<div align="center">
<table>
<tr align="center">
<th>modifying code and testing vehicles</th>
<th>currently editing videos</th>
</tr><tr align="center">
<td><img src="./img/8/work_photo_1_0813.jpg" width="300" alt="work_daily"></td>
<td><img src="./img/8/813.jpg" width="300" alt="work_daily"></td>
</tr><tr align="center">
</table>

<table>
<th>mission race introduction video</th>
</tr>
<td>

[![video](https://res.cloudinary.com/marcomontalbano/image/upload/v1691907166/video_to_markdown/images/youtube--VrU3wQa6h5M-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/VrU3wQa6h5M "video")</td>
</table>
</div>



## 2023/08/14 ~ 2023/08/20
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- As the competition is scheduled for this week, we have intensified our practice efforts, trying out various scenarios and adjusting our program to adapt to a wide range of situations. Experimenting with different scenarios has the advantage of helping us anticipate challenges that our machine might face and making necessary adjustments in advance. Here's our practice approach:

- We have assigned lane labels A, B, C, and D. Each lane is divided into three sections, with placement points for blocks both on the inner and outer sides in each section. Red blocks indicating turning conditions will be placed sequentially, while the positions of other blocks will be randomized.
- The record sheet will include the following information:
  1. Completion time
  2. Number of successful attempts/number of failed attempts
We believe that this approach will assist our machine in preparing for a variety of scenarios, ensuring that we are well-prepared for the competition.

- Today is 8/19, our match day. In the first half of the qualifying round, due to our Request for Maintenance during the initial round, the score was reduced by 50%, resulting in our obtaining 15 points. In the second round, we successfully completed it and achieved a full score of 30 points, allowing us to advance to the second half of the obstacle course. During the first obstacle race, our robot hit the wall and stopped due to excessive avoidance; fortunately, after adjustments, the second attempt by our team resulted in a perfect score. This marked a successful conclusion to today's competition.


<div align="center">
<table>
<tr align="center">
<th>field layout</th>
<th>record sheet</th> 
</tr>
<tr align="center">
<td><img src="./img/8/block.png" width="400" alt="work_daily"></td>
<td><img src="./img/8/grade.png" width="500" alt="work_daily"></td>
</table>
</div>
<div align="center">
<table>
<tr align="center">
<th>competition photos</th>
<th>award-winning photo</th> 
</tr>
<tr align="center">
<td><img src="./img/8/0819_1.jpg" width="600" alt="contest"></td>
<td><img src="./img/8/0819_2.jpg" width="600" alt="award-winning photo"></td>
</table>
</div>

## 2023/08/21 ~ 2023/08/27
**member:** ZHAO,ZHEN-BO、LIN,JHONG-BIN、Hu,Yun-Ruei  
**content:**

- As we have confirmed our participation in the international competition, we are undergoing significant modifications to our vehicle. We are transitioning from the use of wooden boards to a 3D-printed chassis for a more integrated structure, optimizing the space available. Moreover, this redesign will allow us to incorporate threaded components for added stability. Additionally, we are upgrading the controller from Raspberry Pi 4B to the higher computing power provided by the Jetson Nano microcomputer. The Jetson Nano supports programming in Python, thus most of our existing code does not need significant modifications. However, one notable difference with the Jetson Nano is that the generation of PWM signals requires an external board for implementation.



<div align="center">
<table>
<tr align="center">
<td rowspan="2">Controller</td>
<td>Jeston Nano</td>
<td>Raspberry Pi 4B</td>
<tr align="center">
<td><img src="./img/8/jeston_nano.png" width="200" alt="work_daily"></td>
<td><img src="./img/8/raspberry_pi_4.png" width="200" alt="work_daily"></td>
</tr>
<tr align="center">
<td>Computational efficiency</td>
<td>472 GFLOPs</td>
<td>13.5 GFLOPs</td>
</table>
</div>

<small>Data source</small>  
<small>[Taiwansersor](https://www.taiwansensor.com.tw/product/nvidia-jetson-nano-developer-kit-%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E9%96%8B%E7%99%BC%E5%A5%97%E4%BB%B6-ai-%E9%96%8B%E7%99%BC%E5%A5%97%E4%BB%B6/)</small>  
<small>[University of Maine System](https://web.eece.maine.edu/~vweaver/group/green_machines.html)</small>

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
