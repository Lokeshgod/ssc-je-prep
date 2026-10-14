# Diodes, Rectifiers & Wave Shaping

## PN junction and models
Diffusion forms a depletion region with an internal electric field. Forward bias reduces the barrier and permits substantial current; reverse bias widens the depletion region and normally gives a small leakage current until breakdown. The common 0.7 V silicon and 0.3 V germanium drops are rough circuit approximations, not immutable thresholds. Current and temperature affect forward voltage.

An ideal diode is a short when on and an open when off. The constant-drop model adds an assumed forward drop. A small-signal resistance model linearises around a bias point. Solve by assuming states, calculating voltages/currents and checking that each assumed state is consistent. Zener diodes operate in a specified reverse-breakdown range with a series current-limiting resistor; ensure current and power stay within rating.

## Uncontrolled rectifiers
An ideal half-wave rectifier with a resistive load conducts for one half-cycle. Vdc = Vm/π and Vrms = Vm/2; ripple frequency is f. An ideal full-wave rectifier gives Vdc = 2Vm/π and Vrms = Vm/√2; ripple frequency is 2f. A bridge uses two conducting diodes in each path, so include two forward drops in a constant-drop approximation. A centre-tapped arrangement uses half the secondary at a time.

$$ V_{dc,HW}=V_m/\pi,\quad V_{dc,FW}=2V_m/\pi $$

Peak inverse voltage is Vm per diode for the ideal bridge and 2Vm for a centre-tapped full-wave circuit when Vm is the peak of each half-secondary. Define Vm carefully: using total secondary voltage with a half-secondary formula gives a factor-of-two error. Ideal maximum rectification efficiencies for resistive loads are approximately 40.6% half-wave and 81.2% full-wave, under their standard definitions and assumptions.

## Filters and wave shaping
A capacitor-input filter charges near peaks and discharges through the load between peaks. Larger capacitance, lower current and higher ripple frequency reduce ripple. For modest ripple, ΔVpp ≈ Iload/(fripple C); it is an approximation, not the unfiltered RMS formula. An inductor opposes changes in current; RC/LC filters have load-dependent behaviour.

A clipper limits part of a waveform. Diode orientation, bias source and diode drop set the clipping level. A clamper adds a DC shift using a diode-capacitor-resistor arrangement, approximately preserving peak-to-peak amplitude when the time constant is sufficiently large. It does not ideally amplify the waveform. Trace the diode's conducting interval and the capacitor's stored polarity before drawing the output.

## LEDs and photodevices
An LED needs current control; the resistor is (Vs−Vf)/I under the constant-drop model. Resistor power is I²R. A photodiode is commonly reverse-biased for detection and changes current with illumination. A solar cell supplies power in photovoltaic operation. A Zener regulator is neither a universal current source nor an unlimited-power clamp.

## Worked models (original)

### LED resistor

Supply 9 V, LED drop 3 V, target current 20 mA.

R = 6/0.02 = 300 Ω; resistor dissipation = 0.12 W.

### Ripple frequency

A full-wave bridge takes 50 Hz AC.

Unfiltered rectified ripple repeats at 100 Hz.

## Practice (original)

A clamper ideally changes:

Answer: DC level. It shifts the waveform vertically.

An ideal bridge rectifier has how many diodes conducting at once?

Answer: 2. Each current path passes through two diodes.

A reverse-biased Zener used for regulation needs:

Answer: Current limiting. The external circuit must limit current and power.