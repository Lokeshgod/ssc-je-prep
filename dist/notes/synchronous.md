# Synchronous Machines

## Alternator fundamentals
A synchronous generator normally has a stationary armature and rotating DC field. This makes high-voltage insulation and taking output current from the stator easier. Salient-pole rotors suit many poles and relatively low speed; cylindrical rotors suit high-speed turbine drives. Electrical frequency is f = PN/120, so a generator's speed and pole count fix frequency.

$$ E_{ph}=4.44 k_p k_d f\Phi T,\quad k_p=\cos(\alpha/2),\quad k_d=\frac{\sin(m\beta/2)}{m\sin(\beta/2)} $$

T means series turns per phase, not total conductors. α is chording angle from full pitch, m slots per pole per phase and β electrical slot angle. Short pitching saves end copper and can suppress selected harmonics; winding factors must be computed for the harmonic concerned. A full-pitch concentrated winding has fundamental factors equal to one.

## Armature reaction and synchronous impedance
At unity power factor, armature reaction is mainly cross-magnetising. At zero lagging power factor it is mainly demagnetising; at zero leading power factor it is mainly magnetising. Intermediate power factors combine components. Leakage reactance and an armature-reaction equivalent combine into synchronous reactance in a simplified model.

For a generator, the phasor equation is E = V + I(Ra + jXs). For a motor, E = V − I(Ra + jXs). These are phasor equations; do not add magnitudes unless all terms align. Synchronous-impedance/EMF regulation is generally pessimistic, MMF regulation optimistic, and Potier separation improves treatment of leakage and armature reaction.

## Power angle and synchronising
Ignoring armature resistance for a cylindrical-rotor machine, three-phase real power is 3VE sinδ / Xs using per-phase RMS voltages. Stable operation requires adequate synchronising torque and staying below the operating stability limit; the ideal formula peaks at δ = 90°. Salient-pole machines also have a reluctance-power term, so the cylindrical formula is not universal.

$$ P=\frac{3VE}{X_s}\sin\delta $$

Before connecting an alternator to a live bus, match voltage magnitude, frequency, phase sequence and phase angle. A synchroscope helps check the angle/frequency difference; correct phase sequence is checked separately. On an infinite bus, increasing prime-mover input mainly increases real power and torque angle; changing excitation mainly changes reactive power/power factor. The bus constrains frequency and voltage.

## Synchronous motor behaviour
A conventional synchronous motor is not inherently self-starting from a fixed-frequency supply. Damper windings or a controlled-frequency drive can assist starting. Once synchronised, speed stays at synchronous speed while load varies within capability; torque angle changes. Underexcited motors normally draw lagging current. Overexcited motors can draw leading current and support power-factor correction. V-curves plot armature current against field current at fixed load; minimum armature current is near unity power factor. Inverted V-curves plot power factor against excitation.

Hunting is oscillation about an equilibrium rotor angle after disturbances. Damper windings oppose speed oscillations. A synchronous condenser is an appropriately operated unloaded synchronous machine providing reactive support; it still has losses. Do not describe its real input as exactly zero in a practical machine.

## Worked models (original)

### Frequency from speed

A 12-pole alternator runs at 500 rpm.

f = 12×500/120 = 50 Hz.

### Power-angle change

In the cylindrical model, δ changes from 30° to 90° with V, E and Xs fixed.

Power doubles because sin90°/sin30° = 2. The latter point is the ideal maximum, not a recommended operating margin.

## Practice (original)

On an infinite bus, increasing excitation mainly changes:

Answer: Reactive power. Voltage and frequency are imposed by the bus; excitation primarily controls reactive exchange.

An overexcited synchronous motor usually draws:

Answer: Leading current. Overexcitation can make the stator current lead its voltage.

Zero-lagging-pf alternator armature reaction is mainly:

Answer: Demagnetising. The armature MMF mainly opposes the main field.