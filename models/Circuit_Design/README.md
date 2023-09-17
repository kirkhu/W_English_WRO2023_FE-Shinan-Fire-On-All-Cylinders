<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

2023WRO Future Engineersn Shinan Fire On All Cylinders  
====
## <div align="center">Circuit Schematic Drawing </div>

- ### Circuit Board
<div align="center">
<table>
  <tr align="center">
      <th> Circuit Board of Top View </th>
  </tr>
  <tr align="center">
     <td> <img src="../../schemes/Assembly_Instructions/img/board_up.jpg" width="300" alt="circuit_up.jpg"> </td>
  </tr>
</table>
</div>

- ### Circuit Schematic Drawing
<div align="center">
<table>
  <tr align="center">
      <th>Circuit Diagram</th><th>PCB Diagram</th><th>Circuit Wiring Diagram</th>
  </tr>
  <tr align="center">
     <td><img src="./img/simulation_2.png" width="500" alt="Circuit schematic drawing"></td><td><img src="./img/simulation.png" width="500" alt="Circuit schematic drawing"></td><td><img src="./img/Altium Designer.png" width="500" alt="Circuit schematic drawing"></td>
  </tr>
</table>
</div>

## Explanation of Circuit Principles(電路原理說明)

Welding is mainly based on the PCB configuration diagram, where yellow lines represent single-core wires, and blue lines represent jumpers. Jumpers can prevent two single-core wires from touching and causing damage to sensors, batteries, or the main unit.

In the top-left corner, there are two PIN sockets for the battery. They are connected to a switch and then to a voltage regulator board. This setup allows the system to be powered on and off using the switch. The four-PIN socket on the left side is for the color sensor, responsible for providing voltage to the color sensor and receiving I2C signals. The four-PIN socket on the right side is for the DC motor, supplying power to it. In the bottom-right corner is the socket for the servo motor, which provides power and transmits PWM signals to control the servo motor.

焊接是以PCB 配置圖為主，黃色的線代表單心線，藍色的代表跳線，跳線可以避免兩條單心線碰到造成感測器、電池或主機被燒毀。

左上角是的兩PIN插座是電池插座，會先接到開關在接到降壓板，這樣才會達到利用開關開機的效果，左邊的四PIN插座是顏色感測器的插座，負責輸出電壓給顏色感測器和接收I2C的訊號，右邊的四PIN插座是接給直流馬達的，負責提供電壓，右下角的是伺服馬達的插座，負責提供電和傳輸PWM訊號給伺服馬達。

### Introduction to Fritzing
- Fritzing is a convenient and user-friendly tool that can be used to draw circuit diagrams for self-driving cars, and it does not require any software installation. Fritzing provides a variety of electronic components and modules, which users can simply drag and drop onto the canvas to quickly create and design their circuit diagrams. This makes it particularly suitable for beginners or those unfamiliar with complex circuit design software.
- In addition to circuit diagrams, Fritzing also allows users to create schematics, breadboard views, and even design custom PCB (Printed Circuit Board) layouts. This comprehensive feature set makes it a valuable tool for prototyping and educational purposes. 
- After drawing the circuit diagram using Fritzing, it becomes convenient to solder the circuit on a breadboard following the diagram. This reduces the error rate and allows for easy corrections.
- Software link：[Fritzing](https://fritzing.org/) 
- The circuit diagrams created for this competition are all designed using Fritzing.
<div align="center"><img src="./img/Fritzing.png" width="500" alt=" Fritzing">   <img src="./img/frtzing2.png" width="500" alt=" Fritzing"></div>



# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
