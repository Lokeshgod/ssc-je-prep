# Amplifiers, Feedback & Oscillators

## Small-signal amplification
Bias establishes an operating point; a small signal produces incremental changes around it. Voltage gain is output signal/input signal, current gain is output current/input current and power gain combines them with the appropriate impedances. Cascaded voltage gains multiply, while their decibel gains add. For voltage gain, 20 log₁₀|Av| applies to voltage ratios; interpreting that as power gain assumes the relevant impedance relation. A 10× voltage ratio is 20 dB and a 100× ratio is 40 dB.

Coupling/bypass capacitors often set low-frequency roll-off; device and stray capacitances contribute to high-frequency roll-off. The passband lies between the relevant cutoff frequencies, conventionally where gain falls to 1/√2 of midband magnitude. Loading by the next stage can reduce actual gain; an unloaded stage gain is not automatically preserved in a cascade.

## Negative feedback
With negative feedback and a consistent sign convention, closed-loop gain is A/(1+Aβ). Large loop gain makes gain depend mainly on the feedback network, reduces sensitivity to the raw gain and often reduces distortion while widening bandwidth. Input/output impedance changes depend on whether the circuit samples voltage/current and mixes series/shunt; there is no single direction valid for every feedback topology.

$$ A_f=\frac{A}{1+A\beta} $$

At frequencies where phase lag converts intended negative feedback toward positive feedback, stability can be lost. A simple DC gain formula is not a full stability proof. Positive feedback reinforces a signal and is used in oscillators and hysteretic switching.

## Power-amplifier classes
Class A conducts for a full cycle, gives good linearity but dissipates power even without a signal. Class B ideally conducts for half a cycle per device and usually uses push-pull pairs, with crossover distortion near zero. Class AB biases slightly above cutoff to reduce that distortion. Class C conducts for less than half a cycle and uses a tuned load in suitable applications. Class D uses switching and output filtering; its efficiency is high in a practical design but not exactly 100% with real losses.

## Oscillation
A sinusoidal feedback oscillator must have a loop phase of 0° modulo 360° and unity loop magnitude at sustained amplitude in the simplified Barkhausen description. Startup generally needs loop gain greater than one before nonlinear amplitude stabilisation reduces effective gain. These conditions identify candidate oscillation but are not a complete universal nonlinear existence/stability proof.

$$ f_{LC}=\frac{1}{2\pi\sqrt{LC}},\quad f_{Wien}=\frac{1}{2\pi RC} $$

The Wien formula assumes its standard equal-R, equal-C network. A three-section RC phase-shift oscillator has a different frequency/gain requirement. Hartley uses an inductive divider, Colpitts a capacitive divider and a crystal oscillator exploits a resonator with high frequency selectivity. Do not interchange divider component arrangements. Amplifiers need an input signal to reproduce; oscillators obtain their output from DC power plus an internal feedback/resonator mechanism.

## Worked models (original)

### Feedback gain

A = 100 and β = 0.09 with negative feedback.

Af = 100/(1+9) = 10.

### Cascade gain

Two voltage-gain stages are 10 and 20 without loading change.

Total gain = 200. Multiplication, not 10+20.

## Practice (original)

Colpitts feedback divider is:

Answer: Capacitive. Its tank includes a capacitive divider.

Class B ideal conduction angle per device is:

Answer: 180°. Each device conducts over one half-cycle.

A 10× voltage gain corresponds to:

Answer: 20 dB. 20 log₁₀(10) = 20 dB.