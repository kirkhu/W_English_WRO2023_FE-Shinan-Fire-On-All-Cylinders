<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">Vehicle Power Supply System Introduction</div> 
- ### Power Supply Operation System Overview Diagram
<div align="center"><img src="./img/Power_supply_system.png" width="600"></div>

- ###  Physical Connection Diagram of Power Supply System 
<div align="center"><img src="./img/Power_supply_system of Summary diagram1.png" width="600"></div>

- ### Power supply system operation Instruction
  Each type of device operates at its respective working voltage, as explained below:
  - Powered by a lithium-polymer battery, it provides 11.1V, simultaneously serving as the working voltage for the 12V-to-5V step-down power supply module and the L293D motor control chip to drive the 12V DC motors.
  - The step-down power supply module reduces 11.1V to 5V, supplying the working voltage to the 5V Raspberry Pi, 5V color sensor, 5V L293D motor controller, and 5V servo motors.
  - The Raspberry Pi, in turn, supplies 5V as the working voltage for the Lidar and camera module.  - 
- ###  Battery Selection 電池選擇
  - As the vehicle requires continuous movement, it was necessary to switch the power source to batteries. Considering that the motors require a voltage of 12V to operate, we chose a 12V battery with a current rating of 3A.
  - There are two common battery options: lithium-ion batteries (18650) and lithium-polymer batteries (3S). However, due to the heavier weight and larger size of 18650 batteries, we opted for the compact and lightweight lithium-polymer battery.
  - #### Battery Comparison

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

 - ### Step-Down Power Supply Module  Selection(降壓模組選擇)
    - The Raspberry Pi can only operate at a voltage of up to 5.2V, so we need to use a 12V-to-5V step-down power supply module to lower the voltage and prevent damage to the Raspberry Pi.
    - Initially, we used the LM2596 DC-DC adjustable step-down module because it had a digital display that could show the current output voltage. However, its maximum output current was only 3A, which couldn't meet the device's operating current, so we didn't use it.
    - Therefore, we opted for a constant voltage and constant current step-down power supply module with a maximum output current of 5A, which allows the self-driving car to operate normally. While it lacks a digital display, we can determine the current battery voltage through a low-voltage alarm, ensuring that the battery voltage is sufficient.
    - #### Step-Down Power Supply Module Comparison
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

