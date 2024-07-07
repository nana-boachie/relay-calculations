# relay-calculations
To make my life easier

OVERCURRENT
The Inverse Time Overcurrent (TOC/IDMT) relay trip time is calculated using the IEC 60255 standard and the IEEE C37.112-1996 protection curves. Let’s explore the formula for the IDMT curve according to IEC 60255:


IDMT Curve Formula (IEC 60255):


The trip time t(I) is inversely proportional to the fault current I. It can be calculated using the following formula:
t(I)=TMS(k−1k(I/Is​)α−1​)

Is: The current setting (pickup set point) in the relay.
I: The actual fault current.
k and α: Constants specific to the curve type (see table below).



The IEC standard defines several curve types with different constants:

Standard inverse curve: (k = 0.140), (α = 0.020)
Very inverse curve: (k = 13.5), (α = 1)
Extremely inverse curve: (k = 80), (α = 2)
Long time standard inverse curve: (k = 120), (α = 1)





IEEE C37.112-1996 IDMT Curve:


The formula for the IEEE IDMT curve is similar:
t(I)=TMS(k−1k(I/Is​)α−1​)

Is: Current setting (pickup set point).
I: Actual fault current.
k and α: Constants specific to the curve type (see table below).



Constants for IEEE curves:

Moderately inverse curve: (k = 0.0515), (α = 0.02)
Very inverse curve: (k = 19.61), (α = 0.491)
Extremely inverse curve: (k = 28.2), (α = 0.1217)



DISTANCE PROTECTION

Setting the reach point for your distance relay is crucial to ensure effective protection. Let’s explore how to determine the reach point:

Impedance Measurement Principle:
Distance protection relies on measuring the impedance of a transmission line.
The relay calculates the apparent impedance using voltage and current measurements.
This apparent impedance is then compared with the reach point impedance.
Reach Point Setting Guidelines:
Zone 1 (Primary Zone):
Set the relay to reach 80% of the impedance of the protected line.
This ensures that the relay does not reach the remote end of the line.
Zone 2 (Backup Zone):
Set the relay to reach 120% of the impedance of the protected line.
Zone 2 provides dependable overreach to cover the entire line.
Zone 3 (Emergency Zone):
Zone 3 may be disabled or set to cover an adjacent line.
Consider system stability and coordination.
Parallel Lines and Mutual Coupling:
In parallel lines, mutual coupling can cause distance relays to underreach or overreach.
Relay settings must account for this effect.
Some relays have algorithms to compensate, but it’s essential to consider the current of the parallel line.
Ground Elements:
For ground elements, take any parallel line elements out of service.
Set the relay impedance to the nearest terminal without infeed.
Considerations:
Some countries restrict distance protection from reaching faults in other voltage levels (e.g., sub-transmission vs. transmission).
Combining fast fault clearance with selective tripping is crucial for power system protection.

DIFFERENTIAL

Differential protection is commonly used to safeguard electrical equipment such as generators, motors, and transformers. Here are the key principles and equations:


Current Differential Protection:

The simplest form of differential protection.
Measuring Principle:

Current transformers (CTs) at the extremities of the differential protection zone are connected in series on the secondary side.
During an external fault (e.g., short circuit downstream), the currents circulate through the CTs, and no current flows through the differential measuring branch where the differential relay is situated.
In the event of an internal fault (e.g., a winding-to-winding fault within a transformer), the fault currents flow towards the fault location. The secondary currents add up and flow via the differential branch.
The differential relay detects this imbalance and initiates tripping.


The equation for Non-Biased Differential Protection:

The operating current (I_0) is calculated as:I0​=∣I1​−I2​∣

The bias current (I_B) is calculated as:IB​=2I1​+I2​​

The bias quantity (B) is a user-defined parameter.
The relay operates if: I0​>B⋅IB​






Biased (Stabilized) Differential Protection:

Provides additional stability and security.
Introduces a bias or restraint quantity to prevent false tripping during external faults.
The principle equation for biased differential protection is:∣I1​+I2​∣>k⋅∣I1​−I2​∣+B

Here, (k) represents the ratio of restraining current to operating current.





Parallel Lines and Mutual Coupling:

Mutual coupling in parallel lines can cause differential relays to underreach or overreach.
Relay settings must account for this effect.



Remember that differential protection minimizes damage by quickly detecting internal faults. 



Here are the key steps and formulas for calculating earth fault currents:

Ground Fault Current Calculation:
The ground fault current ((I_f)) can be calculated using the following formula: [ I_f = \frac{p \cdot 100}{V \cdot R_n} ]
Where:
(p) is the percentage of the system voltage (usually 100%).
(V) is the line-to-neutral voltage.
(R_n) is the neutral grounding resistance.
Relay Operation:
For the relay to operate, the fault current ((I_f)) must be greater than the relay pickup current.
The relay settings are determined based on the expected fault current levels and coordination requirements.
Example Calculation:
Let’s assume:
Line-to-neutral voltage ((V)) = 120 V
Neutral grounding resistance ((R_n)) = 0.1217 ohms (specific to the system)
Calculate the fault current: [ I_f = \frac{p \cdot 100}{V \cdot R_n} = \frac{100 \cdot 100}{120 \cdot 0.1217} = 9876.74 , \text{A} ]
Relay Settings:
The relay settings are determined to provide the shortest operating times at maximum fault levels.
Check if the relay operation is satisfactory at the minimum expected fault current.
Proper coordination and accurate fault current calculations are essential for effective earth fault protection.
