# Three-Phase Circuits

## Phase and line quantities
A balanced three-phase set contains equal sinusoidal magnitudes separated by 120 electrical degrees. For a balanced star load VL = √3 Vph and IL = Iph. For a balanced delta load VL = Vph and IL = √3 Iph. These factors come from phasor differences and include 30° shifts between appropriate line and phase quantities. Write the connection before substituting values.

$$ P=\sqrt{3}V_LI_L\cos\phi,\quad Q=\sqrt{3}V_LI_L\sin\phi,\quad S=\sqrt{3}V_LI_L $$

The equivalent forms 3VphIph cosφ and 3Iph²Rph are often easier when branch impedances are given. At the same line voltage with the same impedance per branch, delta takes three times the real power and line current of star. This does not mean any arbitrary real motor can be reconnected without checking its rating.

## Two-wattmeter method
For a three-phase three-wire system, the algebraic sum of two properly connected wattmeters measures total real power, even for an unbalanced load. The familiar power-factor angle formula additionally assumes a balanced sinusoidal load. Labelling can swap the readings, so use a consistent connection/polarity convention.

$$ P=W_1+W_2,\quad \tan\phi=\frac{\sqrt{3}(W_1-W_2)}{W_1+W_2} $$

For balanced loads at unity pf the readings are equal. At pf 0.5, one reads zero. Below 0.5, one reading is negative with the standard connection. If a coil is reversed to get an upscale reading, retain its negative sign when calculating power. At zero pf the readings are equal and opposite, giving zero real power, not two zero readings. A magnitude-only treatment cannot by itself establish lagging versus leading without connection information.

## Neutral and unbalance
For a balanced fundamental star load, neutral current is zero because the three currents sum as phasors. With unbalance, neutral current is the phasor sum of phase currents. Triplen harmonic currents are zero-sequence and can add in the neutral of a four-wire system, so “balanced phase RMS currents” alone does not guarantee no neutral current in a nonlinear installation.

An unbalanced star with no neutral can have a displaced star point and unequal phase voltages. Do not apply VL/√3 to every branch in that case. Use nodal analysis. Delta can carry internal circulating triplen currents without the same currents appearing as line currents. Phase sequence determines the direction of a three-phase rotating field and must match for generator paralleling.

## Fast numerical method
When an impedance is given per phase, first find the actual phase voltage, then phase current, then line current, then power. If line values are given directly, the √3 line formula avoids an unnecessary conversion. Keep VA and W separate: a 10 kVA load at 0.8 pf consumes 8 kW and has 6 kvar magnitude, assuming sinusoidal conditions.

## Worked models (original)

### Connection conversion

Balanced star resistors are 10 Ω each on 100√3 V line supply.

Each phase sees 100 V and takes 10 A. Total power = 3×100×10 = 3 kW.

### Wattmeter inference

A balanced load gives W₁ = W₂ = 2 kW.

Total P = 4 kW and tanφ = 0, hence unity pf.

## Practice (original)

In balanced star, line current equals:

Answer: Phase current. Only star voltage has the √3 magnitude relation.

One wattmeter is zero for a balanced two-wattmeter test at pf:

Answer: 0.5. One cos(30°+φ) vanishes at φ = 60°.

Same resistive branches: delta power divided by star power at fixed VL is:

Answer: 3. Each delta branch sees √3 times star voltage, so branch power triples.