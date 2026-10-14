# AC Fundamentals & Resonance

## Average and effective values
RMS is the DC-equivalent heating measure for a resistor and equals the square root of the mean of the squared waveform. A sine has RMS Vm/√2 and full-cycle average zero. Its rectified average is 2Vm/π. Form factor is RMS divided by rectified average, approximately 1.11 for a sine. Crest factor is peak/RMS, √2 for a sine. A symmetrical square wave has RMS equal to its magnitude; a symmetrical triangular wave has RMS Vm/√3.

$$ V_{rms}=\sqrt{\frac{1}{T}\int_0^T v^2(t)dt} $$

For distinct orthogonal harmonics over their common period, RMS squares add; include the square of any DC component. You cannot simply sum harmonic RMS magnitudes. Two sinusoids at the same frequency must first be combined as phasors, since their cross-term need not average to zero.

## Impedance and phasors
Take voltage as a reference when helpful. Resistor current is in phase, inductor current lags voltage by 90°, and capacitor current leads by 90°. Inductive impedance is jωL; capacitive impedance is −j/(ωC). Series impedances add directly. Parallel admittances add, with Y = 1/Z; conductance is the real part and susceptance the imaginary part.

$$ Z=R+j(X_L-X_C),\quad |Z|=\sqrt{R^2+(X_L-X_C)^2},\quad \cos\phi=R/|Z| $$

Convert polar to rectangular using x = r cosθ and y = r sinθ. Add phasors in rectangular form and multiply/divide conveniently in polar form. The 3–4–5 and 5–12–13 triangles save calculator time. The magnitude of R+jX is not R+X.

## Real, reactive and apparent power
For RMS phasors, complex power is S = VI* = P+jQ. P is watts, Q var and |S| VA. Inductive loads have positive Q under the passive convention, capacitive loads negative Q. Power factor is P/|S|; lagging/leading gives the reactive sense that a scalar cosine alone cannot show.

$$ P=VI\cos\phi,\quad Q=VI\sin\phi,\quad |S|=\sqrt{P^2+Q^2} $$

## Series resonance
For an ideal series RLC with fixed positive R, resonance occurs when XL = XC. The net input impedance is R, current is maximum and power factor unity. Inductor and capacitor voltages can be much larger than the supply but cancel as phasors. The supply voltage is not zero.

$$ f_0=\frac{1}{2\pi\sqrt{LC}},\quad Q=\frac{\omega_0L}{R},\quad BW=\frac{R}{2\pi L}=\frac{f_0}{Q} $$

At resonance VL = VC = QV for the series circuit. At half-power frequencies current is its peak divided by √2. Their difference equals bandwidth, and their geometric mean equals f₀ in this ideal model. Higher Q gives sharper selectivity and larger reactive-voltage magnification.

## Parallel resonance and damping
An ideal parallel LC has cancelling susceptances. With finite parallel loss resistance, input impedance peaks and line current is minimum near resonance, while branch currents can be large. A practical coil has series resistance, shifting the resonant frequency; derive zero imaginary admittance rather than copying the ideal LC formula blindly. “Current maximum” means line current for series resonance and can mean circulating branch current for parallel resonance; read which current is requested.

For a source-free series RLC, α = R/(2L) and ω₀ = 1/√LC. Underdamped means α < ω₀, critical means equality and overdamped means α > ω₀. This transient classification is related to but distinct from a driven steady-state resonance question.

## Worked models (original)

### Impedance triangle

R = 6 Ω and net inductive reactance = 8 Ω across 100 V.

|Z| = 10 Ω, I = 10 A and pf = 0.6 lagging. P = 600 W.

### Harmonic heating

v = 6 sinωt + 8 sin3ωt volts.

Vrms² = (36+64)/2 = 50; Vrms = 5√2 V.

### Resonance magnification

A series RLC has Q = 5 and supply 20 V at resonance.

Each reactive voltage is 100 V; opposite phasors cancel, leaving the resistor drop equal to 20 V.

## Practice (original)

A sine-wave peak is 100√2 V. RMS is:

Answer: 100 V. Divide the peak by √2.

At ideal series resonance, input power factor is:

Answer: 1. Net reactance is zero and input impedance is resistive.

For P = 3 kW and Q = 4 kvar, apparent power is:

Answer: 5 kVA. Use √(3²+4²) = 5 kVA.