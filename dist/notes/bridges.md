# Bridges & Resistance Measurement

## Null measurement
A bridge compares an unknown element with known arms. At balance the detector has zero response, so the unknown can be found from arm ratios without needing its detector deflection scale. A galvanometer detects small currents and their direction; it is not always operated as a power-carrying ammeter. Sensitivity, damping and loading influence how clearly a null is found.

For a four-arm bridge with arms Z₁, Z₂ in one series path and Z₃, Z₄ in the other, supply between the path ends and detector between midpoints, balance means Z₁/Z₂ = Z₃/Z₄. Sketch and label the arms before recalling a product rule; swapping labels can invert a ratio.

$$ Z_1 Z_4=Z_2 Z_3 $$

## Resistance ranges
The Wheatstone bridge is suitable for medium resistance. For very low resistance, lead and contact resistance become comparable to the unknown. Kelvin's double bridge adds a second ratio arrangement to reduce their effect when correctly balanced. Four-terminal measurement separates current-carrying leads from potential-sensing leads. A two-wire measurement of a milliohm object can mostly measure the leads.

High resistance is affected by leakage over dirty or damp surfaces. A guard diverts surface leakage away from the measured path. A megger applies an appropriate test voltage and measures insulation resistance, typically in megohms. Insulation tests are performed on appropriately isolated equipment using the applicable procedure; an ordinary ohmmeter is not equivalent to a voltage-stress insulation test. A loss-of-charge method estimates resistance from capacitor voltage decay if other leakage paths are accounted for.

$$ R=\frac{t}{C\ln(V_1/V_2)} $$

## AC bridges
At sinusoidal balance, both real and imaginary parts of the complex balance equation must hold. Maxwell-type bridges compare inductance using a standard capacitor and suit a range of coil Q values. Hay's bridge is commonly associated with high-Q inductors. Schering bridges measure capacitance and dielectric loss. Wien bridges can measure frequency for an appropriate RC configuration. De Sauty comparison assumes nearly lossless capacitors and does not independently separate lossy dielectric effects.

Do not memorise one inductance formula without its circuit: the resistor and capacitor placement defines the equation. Start from the impedance-product balance and separate real/imaginary parts. The detector frequency response must be appropriate to the test signal.

## Earth and insulation resistance
Earth-electrode resistance concerns an electrode/soil path and is distinct from insulation resistance between conductors or conductor and earth. Fall-of-potential testing uses suitable current and potential electrodes and requires attention to spacing and overlapping resistance areas. A low numerical earth resistance alone does not establish complete installation safety; protective-device operation, bonding and touch voltage also matter. For exam questions, identify which resistance is requested before choosing the instrument.

## Worked models (original)

### Bridge balance

Z₁ = 10 Ω, Z₂ = 20 Ω, Z₃ = 30 Ω in the labelled bridge convention.

Z₄ = Z₂Z₃/Z₁ = 60 Ω. Write the ratio first to avoid reversal.

### Low resistance choice

Measure a 0.01 Ω shunt accurately.

Use a suitable Kelvin/four-terminal method; lead resistance can dominate a two-wire reading.

## Practice (original)

Best classical bridge choice for very low resistance?

Answer: Kelvin double. Kelvin minimises lead/contact-resistance error.

An insulation-resistance tester is commonly called:

Answer: Megger. It measures high insulation resistance under an applied test voltage.

AC bridge balance requires equality of:

Answer: Both real and imaginary parts. A complex equality imposes both conditions.