# Thyristors & Gate Circuits

## SCR states and operation
A silicon-controlled rectifier is a PNPN device with anode, cathode and gate. In reverse bias it normally blocks until its rated limit. In forward blocking, positive anode voltage alone does not cause normal conduction below breakover; a suitable gate current can trigger it. After it latches, removing the gate pulse does not normally turn a conventional SCR off. The anode current must fall below holding current and the device needs adequate recovery time.

Latching current is the minimum anode current needed immediately after the gate signal is removed for turn-on to persist. Holding current is the minimum current needed to sustain an already established on-state. Latching current is usually larger. A gate-turn-off thyristor is a different device with designed turn-off gate action; do not transfer its behaviour to a conventional SCR.

## Triggering and gate drive
Gate pulses must have suitable polarity, magnitude and duration and remain within ratings. They are timed relative to the supply waveform in phase control. Resistance/RC triggering and UJT relaxation methods are classical exam topics; practical drives may use isolated pulse transformers or optically isolated control. A UJT relaxation oscillator charges a capacitor until its firing condition is met, then discharges to produce a pulse. Trigger circuits and power circuits must be distinguished.

Increasing gate current generally reduces the forward voltage required for triggering within the characteristic family. It does not normally set an arbitrary on-state anode current; the load and supply do. An SCR has a low but nonzero forward on-state voltage and dissipates power.

## dv/dt and di/dt
A rapid rise of anode voltage drives displacement current through junction capacitance and may cause unintended triggering. A suitable RC snubber limits voltage rise in the intended design. High di/dt during turn-on can concentrate current before conduction spreads across the device; series inductance can limit it. These address different mechanisms. Heat sinks and thermal design limit junction temperature; fuses/protection address fault energy according to their coordination.

## Commutation
Natural/line commutation uses an AC current zero and reverse bias provided by the supply circuit. Forced commutation uses auxiliary circuitry to force device current down and provide recovery time, important in DC circuits. The circuit turn-off time must exceed the required device recovery time under the specified conditions. A freewheeling diode gives an inductive load current an alternative path and can clamp/reduce negative load-voltage intervals depending on topology.

## Related switches
A TRIAC conducts in either direction when properly triggered and is used for suitable AC control. A DIAC is a bidirectional breakover device often used in triggering. A power MOSFET uses gate voltage control and requires gate-charge management; an IGBT combines insulated-gate drive with a bipolar conduction structure. Frequency, voltage, current and switching-loss requirements determine switch selection. Device labels alone do not specify safe operating area.

## Worked models (original)

### Holding versus latching

An SCR needs 30 mA to latch but only 15 mA to remain on.

A 20 mA established current may sustain conduction, but 20 mA immediately after a short gate pulse may fail to latch.

### Protection matching

A question asks about accidental turn-on from a steep voltage edge.

Identify dv/dt and capacitive displacement current; an RC snubber is the standard conceptual mitigation.

## Practice (original)

Removing the gate pulse turns off a latched conventional SCR:

Answer: Normally no. It normally remains on until anode current falls below holding current with adequate recovery.

An RC snubber is associated primarily with limiting:

Answer: dv/dt. It controls the voltage transient across the switch.

Latching current is usually:

Answer: Greater than holding current. Initial establishment requires more anode current than sustaining conduction.