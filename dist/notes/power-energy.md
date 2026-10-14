# Power & Energy Measurement

## Wattmeter connections
A wattmeter current coil is connected in series with the load and its pressure/voltage coil across an appropriate voltage. An ideal reading is the average of instantaneous vi; for sinusoidal supply it becomes VI cosφ. Coil connections can include current-coil loss or pressure-coil consumption in the reading. Correct the loss according to the actual connection and meter resistances. Do not select a correction formula without the diagram.

Low-power-factor measurement is sensitive to pressure-coil phase error because the wanted real-power component is small. A negative wattmeter reading can be physically meaningful, including in the two-wattmeter method; reversing a coil for an upscale reading does not remove the algebraic sign.

## Induction energy meter
The driving system produces interacting alternating fluxes and eddy currents in an aluminium disc. A permanent magnet provides braking torque approximately proportional to speed. At normal calibration, speed is proportional to power and accumulated revolutions to energy. The registering mechanism counts revolutions. Friction compensation, phase-angle adjustment and braking-magnet adjustment affect calibration.

Creeping is slow disc rotation under voltage with no load current when it should remain still. Holes or slots and suitable adjustments can reduce it. Do not call every meter motion creeping: at a real connected load rotation is normal. This construction needs AC; it is different from a static electronic meter.

## Electronic energy meter
Voltage and current sensors feed analogue processing or ADCs. The metering circuit computes instantaneous power and accumulates it with time; a pulse output represents a fixed energy increment, and a display/register stores consumption. Sampling, phase matching, clock accuracy, calibration and anti-alias filtering affect performance. A true energy meter integrates power; multiplying independent average voltage and average current is generally insufficient for arbitrary waveforms.

$$ E_{kWh}=\frac{N_{pulses}}{K_{imp/kWh}} $$

Some questions specify a meter constant in revolutions/kWh or impulses/kWh; others specify Wh/revolution. One is the reciprocal form of the other. Read the units before dividing or multiplying.

## Calibration and error
Reference energy equals known real power multiplied by elapsed time. Measured energy comes from the meter constant and pulse/revolution count. Percentage error = (registered energy − true energy)/true energy × 100. Positive error means fast/over-registering. If asked for correction rather than error, the sign reverses under the corresponding convention.

A meter constant of 1200 rev/kWh with 60 revolutions in 3 minutes registers 0.05 kWh in 0.05 h, equivalent to 1 kW. A stopwatch conversion error can make the result wrong by a factor of 60. For a current-transformer-operated meter, account for CT/PT ratios if the displayed values have not already been programmed to primary quantities.

## Worked models (original)

### Meter pulses

A 1600 imp/kWh meter produces 800 pulses.

Registered energy = 800/1600 = 0.5 kWh.

### Meter error

Reference energy is 2 kWh; meter registers 2.1 kWh.

Error = 0.1/2×100 = +5%; the meter is fast.

## Practice (original)

A wattmeter measures:

Answer: Average real power. Its average torque/processing corresponds to real power.

A 1000 imp/kWh meter gives 250 pulses. Energy?

Answer: 0.25 kWh. 250/1000 = 0.25 kWh.

No-load disc rotation in an induction meter is:

Answer: Creeping. Creeping is unintended no-load disc motion.