<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Circuit Schematic Drawing </div>

- ### Circuit Board 
<div align="center">
<table>
  <tr align="center">
      <th> Circuit Board of Top View </th><th>Circuit Board of Bottom View</th>
  </tr>
  <tr align="center">
     <td> <img src="../../schemes/Assembly_Instructions/img/circuit_up.jpg" width="300" alt="circuit_up.jpg"> </td><td><img src="../../schemes/Assembly_Instructions/img/circuit_lower.jpg" width="300" alt="circuit_lower.jpg"></td>
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

## Explanation of Circuit Principles

Welding is mainly based on the PCB configuration diagram, where yellow lines represent single-core wires, and blue lines represent jumpers. Jumpers can prevent two single-core wires from touching and causing damage to sensors, batteries, or the main unit.

Circuit Diagram Introduction:
In the top-left corner is the battery socket, which is connected first to a switch and then to a voltage regulator. This arrangement allows us to achieve the effect of powering on using the switch. The four-pin socket on the right side is for the color sensor, responsible for outputting voltage to the color sensor and receiving I2C signals. The four-pin socket on the left is for the DC motor, providing power. The three-pin socket in the bottom-right corner is for the servo motor, providing power and transmitting PWM signals to control the servo motor.

### Introduction to Fritzing
- Fritzing is a convenient and user-friendly tool that can be used to draw circuit diagrams for self-driving cars, and it does not require any software installation. Fritzing provides a variety of electronic components and modules, which users can simply drag and drop onto the canvas to quickly create and design their circuit diagrams. This makes it particularly suitable for beginners or those unfamiliar with complex circuit design software.
- In addition to circuit diagrams, Fritzing also allows users to create schematics, breadboard views, and even design custom PCB (Printed Circuit Board) layouts. This comprehensive feature set makes it a valuable tool for prototyping and educational purposes. 
- After drawing the circuit diagram using Fritzing, it becomes convenient to solder the circuit on a breadboard following the diagram. This reduces the error rate and allows for easy corrections.
- Software link：[Fritzing](https://fritzing.org/) 
- The circuit diagrams created for this competition are all designed using Fritzing.
<div align="center"><img src="./img/Fritzing.png" width="500" alt=" Fritzing">   <img src="./img/frtzing2.png" width="500" alt=" Fritzing"></div>



# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
