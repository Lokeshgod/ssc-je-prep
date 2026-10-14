# Switchgear & Protection

## Protection objectives and zones
A protection system detects abnormal conditions and isolates the smallest necessary faulty section quickly, while remaining stable for permissible conditions and faults outside its zone. Selectivity, sensitivity, speed and reliability must be balanced. Primary protection acts first; backup operates if primary protection or its breaker fails. Zones usually overlap around breakers so no element is left unprotected.

An overcurrent relay responds to current above pickup. IDMT relays operate faster for larger fault current while maintaining a defined minimum-time characteristic. Earth-fault protection responds to residual/zero-sequence current where the system permits it. A directional relay uses a reference quantity to discriminate power/fault direction. A distance relay uses measured V/I as apparent impedance; reach settings and power swings matter.

## Differential protection
Compare currents entering and leaving a defined zone, correcting for CT ratio, phase shift and connection. During normal operation or external faults their compensated difference is small. An internal fault produces spill current. Percentage bias/restraint improves stability with CT errors or saturation. Transformer inrush can contain a strong second-harmonic component; many schemes use harmonic restraint or other inrush detection. Do not confuse inrush with an internal fault solely because the current is large.

A Buchholz relay uses gas accumulation/oil surge in the pipe between the main tank and conservator of a suitable oil-filled transformer. It does not apply to every dry-type or sealed transformer. Restricted earth-fault protection covers a defined winding earth-fault zone. Temperature devices monitor overheating but are not substitutes for fast short-circuit protection.

## Generators and lines
Generator protection may include stator differential, stator earth fault, rotor earth fault, loss of excitation, negative-sequence heating, reverse power and over/under-frequency. Reverse-power protection can prevent a generator from motoring its prime mover after loss of input. Negative-sequence current creates damaging rotor heating. A first rotor earth fault may not alone complete a large-current circuit, but it creates risk if another fault occurs.

## Breakers, isolators and fuses
A circuit breaker is designed to make/carry/interrupt specified currents, including fault duties. An isolator provides isolation and is normally operated without load current; it is not a fault-interrupting substitute. A fuse melts under sufficient heating, with characteristics depending on its time-current curve and construction. HRC fuses provide high breaking capacity. A relay detects and commands; the breaker interrupts the main circuit.

In AC interruption, the arc can extinguish near current zero, but dielectric recovery must withstand transient recovery voltage. Restriking and recovery-voltage questions concern the race between recovery of dielectric strength and applied voltage. Vacuum breakers use a vacuum interrupter; SF₆ breakers exploit gas insulation/arc-quenching properties. Equipment selection must use actual duty ratings.

$$ S_{sc}=\sqrt{3}V_L I_{sc} $$

This balanced three-phase apparent fault-power expression uses RMS line voltage and current. kV × kA gives MVA. Making current is a peak duty influenced by DC offset; breaking current is specified differently. Do not equate their numerical ratings without the given convention. CT secondary circuits must not be opened while the primary carries current; see the instrument-transformer chapter.

## Worked models (original)

### Fault MVA

At 11 kV, a balanced fault current is 10 kA.

Fault level = √3×11×10 ≈ 190.5 MVA. No extra factor of 1000 is needed for kV×kA.

### Protection identification

An oil/conservator transformer develops internal gas slowly.

A Buchholz alarm may operate from accumulated gas; an oil surge may operate the trip element.

## Practice (original)

Which device interrupts the main fault current?

Answer: Circuit breaker. The relay issues a trip command; the breaker interrupts.

A Buchholz relay requires the appropriate:

Answer: Oil-filled conservator arrangement. Its operation depends on gas/oil movement in that arrangement.

Generator negative-sequence protection primarily addresses:

Answer: Rotor heating. The reverse rotating field induces damaging rotor-frequency effects.