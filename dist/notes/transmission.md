# Transmission, Distribution & Cables

## Why high voltage?
For the same real power and power factor, current is inversely proportional to voltage. Conductor loss is proportional to current squared, so increasing transmission voltage reduces losses for a given conductor. It also raises insulation, clearance and equipment requirements. A feeder carries power to distribution points and is commonly sized for current capacity; a distributor has tapped loads and voltage-drop constraints; a service main connects a consumer.

Radial systems are simple but a feeder outage can interrupt downstream supply. Ring systems give alternate paths when appropriately switched. Interconnected systems improve flexibility and sharing but require more protection coordination. Distribution voltage and installation rules must be taken from the applicable system/design requirements rather than assumed universal.

## Resistance, inductance and capacitance
Resistance increases with conductor length and decreases with cross-section. Skin effect increases effective AC resistance as frequency rises by crowding current toward the surface. Proximity effect arises from nearby conductors. Inductance depends on magnetic geometry; capacitance depends on electric-field geometry and dielectric. Transposition helps balance phase parameters over a line. Bundled conductors reduce surface electric stress and can reduce reactance and corona.

Short-line models neglect shunt capacitance; medium-line nominal-π or nominal-T models include lumped capacitance; long lines use distributed parameters. For a short line, Vs = Vr + IZ per phase. Approximate lagging-load voltage drop is I(R cosφ + X sinφ). A leading load changes the sign of the reactive contribution.

$$ P_{loss}=3I^2R,\quad P_R=\sqrt{3}V_L I\cos\phi $$

## Ferranti effect, corona and compensation
On a long lightly loaded or open-circuit AC line, receiving voltage can exceed sending voltage because charging current interacts with line inductance. This is the Ferranti effect. Shunt reactors absorb reactive power and help control light-load voltage. Series capacitors compensate part of line reactance; shunt capacitors support load reactive demand. They are different interventions.

Corona is ionisation of air when local surface electric stress is high. It causes loss, audible noise and interference. Larger effective conductor diameter, smoother surfaces and bundles reduce surface stress. Weather, air density and conductor spacing matter. Sag approximately follows wL²/(8T) for a level-span parabolic approximation, where T is horizontal tension. Use consistent units and do not apply it unchanged to every unequal-support case.

## Insulators and underground cables
Suspension strings do not normally share voltage equally: the disc nearest the conductor is usually most stressed due to shunt capacitance. String efficiency = string voltage/(number of discs × maximum disc voltage) × 100. Guard rings/capacitance grading improve distribution. Pin-type, suspension and strain insulators serve different mechanical/voltage duties.

For a single-core coaxial cable with conductor radius r and sheath inner radius R, capacitance per length is 2πε/ln(R/r), and radial stress is V/[x ln(R/r)]. Stress is greatest at the conductor surface. For fixed sheath radius and voltage, minimum maximum stress occurs at R/r = e. V in this formula is conductor-to-sheath voltage, not automatically three-phase line voltage. Cable ratings depend on insulation, permissible temperature, thermal environment, installation and current; capacitance can create appreciable charging current.

$$ C'=\frac{2\pi\epsilon}{\ln(R/r)},\quad g_{max}=\frac{V}{r\ln(R/r)} $$

## Worked models (original)

### Line-loss scaling

Transmission voltage doubles; real power, pf and conductor resistance stay fixed.

Current halves; copper loss becomes one quarter.

### String efficiency

Three discs: total 60 kV, most-stressed disc 25 kV.

Efficiency = 60/(3×25) = 80%.

## Practice (original)

Ferranti effect is most associated with:

Answer: Long lightly loaded AC lines. Charging current and line inductance can raise receiving-end voltage.

Maximum coaxial cable stress occurs:

Answer: At conductor surface. Stress falls as 1/x through the insulation.

If current doubles, fixed-resistance line loss becomes:

Answer: Four times. Loss is proportional to I²; doubling current multiplies loss by four.