# Controlled Rectifiers & DC Converters

## Define the waveform and conduction mode
Average output depends on topology, firing angle, load and whether current is continuous. Vm below denotes the peak sinusoidal input voltage of the relevant winding. Firing angle α is measured from the appropriate natural conduction reference. An equation for a continuous-current inductive load need not hold for a resistive load, since the conduction interval changes.

For a single-phase full-controlled bridge with continuous DC current and negligible overlap, Vdc = 2Vm cosα/π. It is positive for α < 90°, zero at 90° and negative for α > 90°. Negative average voltage with positive current is inversion only if the DC side can sustain it and the commutation conditions are met; a passive resistor cannot deliver that operating mode.

$$ V_{dc,full}=\frac{2V_m}{\pi}\cos\alpha $$

For the same full bridge with a purely resistive load, current ceases at the supply zero each half-cycle, giving Vdc = Vm(1+cosα)/π. A single-phase semi-controlled bridge with appropriate continuous current/freewheeling also gives Vm(1+cosα)/π under its standard assumptions. The same-looking formula does not make the circuits identical.

$$ V_{dc,semi}=\frac{V_m}{\pi}(1+\cos\alpha) $$

An ideal single-SCR half-wave rectifier with resistive load gives Vm(1+cosα)/(2π). A full-controlled midpoint/centre-tapped arrangement with continuous current has the familiar 2Vm cosα/π result when Vm is the peak of each half-secondary. State whether the quoted transformer voltage is the whole winding or one half.

## Commutation overlap and freewheeling
Source inductance prevents instantaneous transfer of current between devices, creating overlap and reducing average rectifier output compared with the ideal result in normal rectification. An inductive load tends to maintain current. A freewheeling diode provides a path when the main source path no longer supplies it and changes output-voltage intervals. Draw conduction states before memorising an average.

## DC choppers in ideal continuous conduction
Duty ratio D = ton/T is between zero and one. Inductor volt-second balance requires average inductor voltage zero in periodic steady state; capacitor charge balance requires average capacitor current zero. Use these principles to derive conversions, which makes it easier to detect inverted formulas.

$$ V_o=DV_{in}\quad\mathrm{(buck)} $$

In a buck, on-state inductor voltage is Vin−Vo and off-state is −Vo. Balancing D(Vin−Vo)+(1−D)(−Vo)=0 gives Vo = DVin. It steps voltage down in the ideal topology. The inductor smooths current and the capacitor smooths output voltage.

$$ V_o=\frac{V_{in}}{1-D}\quad\mathrm{(boost)} $$

For a boost, the switch-on interval stores energy in the inductor; off-state energy flows through the diode to the output. Voltage rises above input in its normal ideal continuous-conduction range. The output cannot be treated as isolated from input simply because the controlled switch is off.

$$ V_o=-\frac{D}{1-D}V_{in}\quad\mathrm{(inverting\ buck\! -\! boost)} $$

The inverting buck–boost changes polarity and can step magnitude up or down. At D = 0.5 its ideal output magnitude equals input. These equations assume continuous inductor current, ideal components and periodic steady state. Discontinuous conduction introduces load dependence; real losses reduce attainable output and D → 1 is not a physically unlimited-voltage promise.

## Exam method
First identify AC-to-DC or DC-to-DC conversion. Next specify load/conduction mode and whether the asked value is average, RMS or peak. Then substitute α or D and check the limit at α = 0 or D = 0. Never substitute degrees into a radians-only numerical function without conversion.

## Worked models (original)

### Full converter

Vm = 100π V, α = 60°, continuous DC current, no overlap.

Vdc = 200×cos60° = 100 V.

### Boost duty

An ideal CCM boost raises 24 V to 60 V.

1−D = 24/60 = 0.4, so D = 0.6.

### Inverting buck–boost

Vin = 12 V and D = 0.25 in CCM.

Vo = −(0.25/0.75)×12 = −4 V.

## Practice (original)

Ideal CCM buck with 100 V input and D = 0.3 gives:

Answer: 30 V. Vo = DVin = 30 V.

Ideal CCM boost at D = 0.5 has voltage gain:

Answer: 2. 1/(1−0.5) = 2.

A full-controlled bridge continuous-current formula can be applied unchanged to every R load:

Answer: No. The conduction interval depends on the load and current continuity.