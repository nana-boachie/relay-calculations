# relay-calculations
To make my life easier

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





Remember to replace the placeholders with your actual values when applying the formula. If you have any further questions or need assistance, feel free to ask
