# Induction Motors

## Rotating field and slip
A balanced three-phase stator supply produces a rotating field. Its synchronous speed is Ns = 120f/P rpm. An induction rotor needs relative motion to induce current; at synchronous speed an ideal induction motor has no induced rotor EMF and no sustained electromagnetic torque. Swap any two stator phases to reverse the field direction.

$$ s=\frac{N_s-N}{N_s},\quad f_r=sf,\quad E_{2s}=sE_2,\quad X_{2s}=sX_2 $$

Normal motoring has 0 < s < 1; generating above synchronous speed gives s < 0; plugging can give s > 1. The rotor frequency is slip times supply frequency, not mechanical revolutions per second. A squirrel-cage rotor has shorted bars and end rings. A wound rotor permits external resistance through slip rings, mainly useful during starting or certain control methods.

## Torque and maximum torque
Using a simplified rotor model at fixed supply, torque is proportional to sR₂/[R₂²+(sX₂)²]. For low slip, T ∝ s/R₂. For large slip where sX₂ dominates, T ∝ R₂/s. Maximum torque occurs at s = R₂/X₂ if stator impedance is neglected. Adding rotor resistance shifts maximum torque to higher slip without changing its approximate magnitude. Maximum starting torque occurs when total rotor resistance equals standstill rotor reactance in that model.

$$ T\propto\frac{sR_2}{R_2^2+(sX_2)^2},\quad s_{max}\approx R_2/X_2 $$

At a fixed frequency and slip, torque approximately follows supply voltage squared. An 80% voltage gives about 64% torque, not 80%. The exact Thevenin equivalent includes stator resistance/reactance, so use the simplified maximum-slip formula only when its assumptions fit.

## Power flow: the most useful numerical model
Subtract stator copper and core losses from input to obtain air-gap power Pg. Rotor copper loss is sPg. Gross mechanical power is (1−s)Pg. Subtract friction and windage to obtain shaft power. Rotor copper loss divided by gross mechanical power is s/(1−s).

$$ P_{r,cu}=sP_g,\quad P_m=(1-s)P_g,\quad T_e=P_g/\omega_s=P_m/\omega_m $$

Do not divide Pg by actual rotor speed to get developed torque. Use synchronous angular speed with air-gap power, or rotor angular speed with developed mechanical power. Shaft torque uses shaft power and actual rotor speed.

## Starting, speed control and braking
DOL starting applies rated voltage and gives high current. A star–delta starter is suitable for a motor designed to run delta at the supply voltage and having accessible winding terminals. Starting in star reduces each winding voltage to 1/√3 of delta, and line current and torque to roughly one-third of DOL delta values. With an autotransformer tap k, motor starting current is about k of DOL, supply current about k², and torque about k².

V/f control varies synchronous speed while approximately preserving flux below base speed. Pole changing changes Ns in discrete steps. Rotor resistance control works with wound rotors but dissipates slip power. Regeneration occurs when driven above synchronous speed in an appropriate connected system. Plugging reverses phase sequence and requires control near zero speed. DC-injection braking creates a stationary stator field and dissipates rotor energy.

## Single-phase induction motors
A single-phase pulsating field can be resolved into two equal opposite rotating fields. At rest their torques cancel, so the basic motor is not self-starting. An auxiliary winding supplies a phase-displaced current. Resistance-start split-phase motors use differing winding impedance; capacitor-start motors provide greater phase separation and starting torque. Capacitor-run designs retain a suitable capacitor during operation. A shaded-pole motor uses a shorted shading turn; the field sweeps from unshaded to shaded portion. Do not confuse these induction types with universal motors.

## Worked models (original)

### Slip and frequency

A 4-pole, 50 Hz motor runs at 1440 rpm.

Ns = 1500 rpm; s = 60/1500 = 0.04; rotor frequency = 2 Hz.

### Power split

Air-gap power is 20 kW at 5% slip.

Rotor copper = 1 kW; developed mechanical = 19 kW. Shaft output is lower if mechanical losses exist.

### Reduced-voltage starting

A starter applies 70% rated voltage.

Starting torque is about 0.7² = 49% of full-voltage starting torque.

## Practice (original)

Rotor input is 10 kW at s = 0.03. Rotor copper loss?

Answer: 300 W. sPg = 0.03 × 10000 = 300 W.

A 6-pole motor on 50 Hz has synchronous speed:

Answer: 1000 rpm. 120×50/6 = 1000 rpm.

Adding wound-rotor resistance approximately changes maximum torque how?

Answer: Unchanged magnitude; higher-slip location. In the simplified model Tmax is unchanged, while smax rises.