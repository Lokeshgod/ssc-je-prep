# Instruments & Errors

## What a reading means
Accuracy describes closeness to the true value; precision describes repeatability. Resolution is the smallest distinguishable change and is not automatically accuracy. Absolute error is measured minus true value; relative error divides by the true value. If accuracy is specified as a percentage of full scale, use full scale, not the present reading. Relative uncertainty becomes larger near the bottom of the scale. Calibration compares indication against a suitable reference under stated conditions.

Systematic errors can arise from calibration, loading, environment or observer procedure; random variation is handled statistically. Instrument loading changes the circuit itself. A high-resistance voltmeter and low-resistance ammeter minimise their respective loading effects. Deflecting torque moves the pointer, controlling torque establishes equilibrium, and damping reduces oscillation without setting the steady deflection.

## Instrument principles
PMMC torque is proportional to current in a permanent magnetic field, giving a nearly uniform DC scale. Direct AC reverses the torque each half-cycle and gives no useful average deflection; rectifier-assisted instruments can measure AC but their waveform calibration matters. Moving-iron torque is approximately proportional to current squared; it works on AC and DC and has a nonuniform scale. Hysteresis and frequency errors can matter.

Electrodynamometer instruments use interacting coil fields and can measure AC/DC power with appropriate connections. Induction instruments need alternating flux and are for AC. Electrostatic instruments use force between charged electrodes, draw little steady current and are suited to voltage measurement; torque follows a voltage-squared dependence. Hot-wire/thermal instruments respond to heating and can indicate RMS within their frequency/thermal limits.

## Extending ranges
A low-resistance shunt diverts most current around a meter movement. A series multiplier limits current for voltage measurement. For movement resistance Rm, full-scale movement current Im, desired current range I and voltage range V:

$$ R_{sh}=\frac{I_mR_m}{I-I_m},\quad R_{series}=\frac{V}{I_m}-R_m $$

An Ayrton/universal shunt arrangement can keep a movement shunted while ranges change. A swamping resistor with a small temperature coefficient in series with a copper movement helps reduce temperature sensitivity. It is not a parallel substitute for a current shunt.

## CRO measurements
A cathode-ray oscilloscope's vertical system maps input voltage to vertical deflection and the time base produces horizontal sweep. A trigger gives a stable repeated display. Voltage = vertical divisions × volts/division, including probe attenuation. Period = horizontal divisions × time/division, so frequency = 1/T. For a single-pole-type bandwidth/rise-time approximation, BW × tr ≈ 0.35; use compatible units. A probe adds resistance and capacitance and can alter the circuit.

Lissajous figures can compare frequencies or phase under suitable stable sinusoidal inputs, but counting tangencies requires knowing which signal goes to which axis. Digital sampling introduces aliasing if bandwidth and sample rate are unsuitable. A display containing many digits is not proof of measurement accuracy.

## Worked models (original)

### Full-scale error

A 100 V range has ±1% full-scale accuracy. It reads 20 V.

Absolute limit is ±1 V. Relative to 20 V this is ±5%, not ±1%.

### Meter shunt

A 1 mA, 100 Ω movement is extended to 1 A.

Rsh = 0.001×100/(1−0.001) ≈ 0.1001 Ω.

### CRO period

One cycle occupies four divisions at 0.5 ms/div.

T = 2 ms and f = 500 Hz.

## Practice (original)

PMMC directly measures:

Answer: DC. Direct PMMC average AC torque reverses and averages to zero.

A voltmeter is connected:

Answer: In parallel. It measures the potential difference between two nodes.

A 0.35 μs rise time corresponds approximately to bandwidth:

Answer: 1 MHz. BW ≈ 0.35/tr = 10⁶ Hz.