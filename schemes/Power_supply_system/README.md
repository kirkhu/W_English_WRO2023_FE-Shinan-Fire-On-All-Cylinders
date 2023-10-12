<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">Power_Supply_System</div> 
## 電源供應圖
- ###  Power_supply_system of Summary diagram  
<div align="center"><img src="./img/Power_supply_system.png" width="600"></div>

- ###  Physical Connection Diagram of Power Supply System 
<div align="center"><img src="./img/Power_supply_system of Summary diagram1.png" width="600"></div>

- ### Explanation of the Power Supply System Diagram

  The battery supplies 12V to power the L293D for starting the DC motors, as well as a voltage step-down module. This module reduces the voltage from 12V to 5V, which is then distributed to the Raspberry Pi, light sensor, motor controller, and servo motor. The Raspberry Pi further directly interfaces with the lidar and camera for data transmission.


## choose battery 
- Due to the continuous movement of the vehicle, the power source needs to be changed to a battery. Considering that the motors require a 12V voltage to operate, we need to choose a battery with a voltage of 12V and a current of 3A. There are two options: lithium-ion batteries (18650) and lithium polymer batteries (3S). However, the 18650 battery is heavier and takes up more space, so we opted for the lithium polymer battery.



### Batteries
<div align="center" width=100%>
<table>
<tr align="center">
  <th> 18650 Lithium Batteries </th> <th>Li-Polymer 3S Battery 
  </th>
</tr>
<tr align="center">
  <td>
  <img src="./img/18650.jpeg" width = "300"  alt="18650" /> </td>
  <td>
  <img src="./img/lipo_battery.png" width = "300" alt="lipo_battery"  />
  </td>

</tr>
</table>
</div>


- However, the maximum voltage supported by the Jetson Nano is only 5.2V. Therefore, we need to use a step-down module to reduce the voltage to prevent damage to the Raspberry Pi. We initially considered using the LM2596 DC-DC adjustable step-down module, as it has a numerical display to show the current output voltage. However, its maximum current capacity is only 3A. Therefore, we chose a constant voltage and constant current step-down power supply module that can handle up to 5A. Though it lacks a numerical display, we will install a low voltage alarm to detect the battery voltage and ensure its safety.


#### Step-Down Module
<div align="center">
<table with=100%>
<tr align="center">
<th> LM2596 DC-DC Adjustable Buck Converter Module </th>
<th>5V Constant Voltage Constant Current Buck Power Supply Module</th>
</tr>
<tr align="center">
  <td><img src="./img/LM25.jpeg" width = "250" height = "" alt="MG90S" align=center />  </td>
  <td><img src="./img/ADIO-DC36V5A.png" width = "300" height = "" alt="MG90S" align=center /> 
  </td>

</tr>
</table>
</div>

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  

