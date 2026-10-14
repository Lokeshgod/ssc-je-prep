"""Build the static, editable SSC JE study library. No network or paid services."""
from pathlib import Path
import json, re, html, hashlib

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
chapters = []
subjects = [
 {'id':'machines','name':'Electrical Machines','short':'Machines','icon':'01','description':'Transformers, DC, induction, synchronous and special machines.'},
 {'id':'power','name':'Power Systems','short':'Power systems','icon':'02','description':'Generation, transmission, distribution and protection.'},
 {'id':'basic','name':'Basic Electrical & Circuits','short':'Basic electrical','icon':'03','description':'Circuit laws, networks, magnetism, AC and three-phase systems.'},
 {'id':'measurements','name':'Measurements','short':'Measurements','icon':'04','description':'Instruments, bridges, power, energy, CT and PT.'},
 {'id':'electronics','name':'Basic Electronics','short':'Electronics','icon':'05','description':'Diodes, transistors, amplifiers and oscillators.'},
 {'id':'utilisation','name':'Utilisation & Estimation','short':'Utilisation','icon':'06','description':'Lighting, heating, welding, traction, costing and earthing.'},
 {'id':'power-electronics','name':'Power Electronics','short':'Power electronics','icon':'07','description':'Thyristors, controlled rectifiers and DC converters.'}
]
def chapter(id, subject, title, summary, body, models, practice, diagram=None):
    chapters.append(dict(id=id,subject=subject,title=title,summary=summary,body=body.strip(),models=models,practice=practice,diagram=diagram))

chapter('transformers','machines','Transformers','Flux, equivalent circuit, tests, losses, regulation, connections and every important V/f case.',r'''
## 1. What actually transfers the power?
A transformer transfers AC power between circuits through a changing mutual flux. Frequency stays the same. It has no mechanical output and no rotating parts. Primary and secondary are defined by where power enters and leaves, not by which winding has more turns. The high-voltage winding uses more turns of thinner conductor; the low-voltage winding carries more current and uses thicker conductor. In a core-type transformer the windings surround the core limbs; in shell type the core surrounds much of the winding. LV is normally nearer the earthed core, reducing insulation requirements.

Laminated silicon-steel cores reduce losses: thin insulated sheets restrict eddy-current paths and silicon raises resistivity. Core material with a narrow hysteresis loop reduces energy lost per cycle. Oil provides insulation and heat transfer. A conservator accommodates oil expansion; a silica-gel breather dries the entering air; bushings insulate terminals where they pass through the tank. A Buchholz relay is discussed in Protection.

## 2. EMF equation and ratio convention
For sinusoidal flux, Faraday's law gives e = N dΦ/dt in magnitude. Differentiating a sine gives a peak voltage 2πfNΦm. Divide by √2 for RMS. The factor 4.44 assumes sinusoidal flux; it is not a universal waveform constant.

$$ E = 4.44 f N \Phi_m = 4.44 f N B_m A $$

Use a = N₁/N₂ throughout these notes. For an ideal transformer, V₁/V₂ = E₁/E₂ = a, I₁/I₂ = 1/a and input VA equals output VA. If another book defines k = N₂/N₁, then k = 1/a. Check the definition before comparing ratios. For a real transformer the terminal voltage ratio differs slightly from the turns ratio because of winding drops.

$$ Z'_2 = a^2 Z_2, \quad I'_2=I_2/a, \quad V'_2=aV_2 $$

Referred impedance is not a physical change in the load. It is the impedance seen from the selected side. Refer all quantities to the same side before adding them. Current scales inversely with turns, so I²R loss is preserved by referral.

## 3. No-load current: I₀, Iw and Im
Even with an open secondary, a practical primary takes a small current. Iw supplies the core loss and is in phase with the supply voltage. Im produces flux and is approximately 90° behind the voltage. They are perpendicular components, not currents to add arithmetically.

$$ I_w=P_0/V_0, \quad I_m=\sqrt{I_0^2-I_w^2}, \quad \cos\phi_0=P_0/(V_0 I_0) $$

Usually Im is larger than Iw because the no-load power factor is low. This is typical behaviour, not a mathematical requirement for every possible transformer. Flux is approximately in phase with the magnetising component; the induced EMF is related to the time derivative of flux. The primary counter-EMF opposes the supply under the passive winding polarity convention.

## 4. What happens when load is added?
Secondary current creates a demagnetising MMF. A tiny tendency for the flux and primary counter-EMF to fall allows extra primary current. The extra primary ampere-turns nearly balance secondary ampere-turns, restoring the flux approximately to its original value. Therefore loading mainly increases primary current, not core flux, when voltage and frequency are fixed. This is an approximate result: leakage drops, winding resistance and saturation cause departures.

The primary current is the phasor sum I₁ = I₀ + I′₂. To calculate its magnitude, resolve both currents along and perpendicular to the voltage. Adding the scalar magnitudes overestimates current unless their phase angles are equal.

## 5. Voltage and frequency changes: keep the condition visible
Ignoring small winding drops, peak flux is proportional to V/f. If V decreases at fixed f, flux decreases and magnetising current normally decreases. The transformer does not manufacture extra Im to preserve the old flux. If f decreases at fixed V, flux increases and magnetising current can rise sharply near saturation. Increasing V at fixed f has the same overfluxing risk. If V and f change by the same proportion, flux stays approximately constant.

$$ \frac{\Phi_{m2}}{\Phi_{m1}}=\frac{V_2}{V_1}\frac{f_1}{f_2} $$

For the same core, classical approximations are Ph ∝ f Bmⁿ and Pe ∝ f² Bm², where n is an empirical hysteresis exponent. At fixed f, reducing voltage reduces both losses. At fixed V, substituting Bm ∝ 1/f gives Ph ∝ f^(1−n) and Pe approximately constant. At constant V/f, Ph ∝ f and Pe ∝ f². Real material losses, harmonics and saturation can alter these approximations. Do not silently use a constant-flux loss law for a constant-voltage question.

Applying DC to an AC transformer produces no steady counter-EMF after the switching transient. Current becomes limited mainly by winding resistance and can be destructive. The correct exam reason is absence of steady induced counter-EMF, not “DC has no current”.

## 6. Equivalent circuit and tests
R₁ and R₂ represent copper resistance. X₁ and X₂ represent leakage reactance. Rc models core-loss power and Xm models magnetising reactive current. The approximate equivalent circuit moves the shunt branch to the supply terminals when the associated error is small.

Open-circuit test: normally supply rated voltage to the LV winding with HV open. The small no-load current makes copper loss small, so the wattmeter approximately reads core loss. Compute cosφ₀, Iw, Im, Rc = V₀/Iw and Xm = V₀/Im. These parameters refer to the energised side. The test may be performed from either side if instruments and ratings are appropriate.

Short-circuit test: normally short LV and apply a reduced voltage to HV until rated current flows. Low applied voltage means low flux and negligible core loss. Wattmeter power approximately equals copper loss at the test current. If the test current is not rated, scale copper loss by the square of the current ratio.

$$ Z_{eq}=V_{sc}/I_{sc},\quad R_{eq}=P_{sc}/I_{sc}^2,\quad X_{eq}=\sqrt{Z_{eq}^2-R_{eq}^2} $$

Sumpner's back-to-back test uses two suitably identical transformers. Primaries are connected in parallel and secondaries in series opposition; a small auxiliary voltage circulates rated secondary current. It permits heating and efficiency evaluation while external supply power covers the losses. A polarity test establishes relative terminal polarity; a phasing-out test identifies corresponding phase terminals in three-phase units.

## 7. Losses and maximum efficiency
At fixed rated voltage and frequency, iron loss is approximately constant. Winding copper loss varies as current squared. At load fraction x, copper loss is x² times full-load copper loss. Efficiency uses real output power, not output kVA alone.

$$ \eta=\frac{xS\cos\phi}{xS\cos\phi+P_i+x^2P_{cu,FL}} $$

Use consistent units: if S is in VA, losses must be in watts. Let A = S cosφ. Differentiating xA/(xA + Pi + x²Pc) gives a numerator proportional to Pi − x²Pc. Thus maximum efficiency occurs when variable copper loss equals constant iron loss.

$$ x_{max}=\sqrt{P_i/P_{cu,FL}} $$

The load fraction for maximum efficiency is independent of power factor under this model. The value of maximum efficiency still depends on power factor. If maximum efficiency occurs at 50% load, full-load copper loss is four times iron loss. Equal efficiencies at two different load fractions x₁ and x₂, at the same power factor and voltage, give Pi = x₁x₂ Pcu,FL.

All-day efficiency is an energy ratio. Add output kWh over each interval, constant iron loss over the hours energised, and x² copper-loss energy over each interval. A distribution transformer can remain energised even when its load is zero.

$$ \eta_{day}=\frac{\sum E_{out}}{\sum E_{out}+E_{iron}+E_{copper}} $$

## 8. Voltage regulation and leading loads
Regulation measures the secondary voltage change from no load to load at the same primary supply. The usual convention is (Vnl − Vfl)/Vfl × 100. In the approximate per-unit expression, use +X sinφ for lagging load and −X sinφ for leading load.

$$ VR_{pu}\approx R_{pu}\cos\phi\ \pm X_{pu}\sin\phi $$

Leading loads can produce zero or negative regulation. Zero regulation approximately requires tanφ = R/X for a leading power factor. Maximum positive regulation occurs near tanφ = X/R for a lagging power factor. These are different conditions; do not interchange them. At unity power factor only the resistive term remains in the approximate formula.

## 9. Three-phase transformers and parallel operation
Apply the winding turns ratio to phase voltages, then convert to line quantities. In star, VL = √3 Vph and IL = Iph. In delta, VL = Vph and IL = √3 Iph. A delta–star bank therefore does not have a line-voltage ratio equal to its individual winding turns ratio. The secondary star neutral is useful for a four-wire distribution system. Delta permits a path for triplen harmonic circulating currents and improves behaviour with some unbalanced loads.

Star–delta and delta–star connections introduce a 30° phase displacement whose sign depends on the vector group. Parallel units need compatible ratio/tap settings, polarity, phase sequence and phase displacement. Similar per-unit impedances allow proportional kVA sharing; similar X/R ratios give similar load power factors. Unequal ratios can produce circulating current even without external load.

For two equal single-phase units operating as open delta, bank capacity is √3 times one-unit kVA, or 57.7% of the corresponding three-unit closed-delta bank. It is not 66.7% of the closed bank.

## 10. Autotransformer
An autotransformer uses a common section of winding. Part of the power transfers conductively and part by induction; it does not provide galvanic isolation. It is economical when the two voltages are close. Define k = Vlow/Vhigh with 0 < k < 1 for the following copper comparison.

$$ \frac{W_{auto}}{W_{two}}=1-k,\quad \frac{S_{auto}}{S_{two}}=\frac{1}{1-k} $$

The second relation refers to using the same winding capability appropriately in an autotransformer connection. Read terminal connections before applying it. An isolation transformer is a two-winding arrangement; instrument transformers provide suitable signals for metering/protection. Power transformer efficiency is usually emphasised near operating load; distribution transformer design pays particular attention to all-day losses.

## 11. Fast checks before selecting an answer
Check VA versus W, primary versus secondary reference, RMS versus peak, load fraction versus percentage, and lagging versus leading. Preserve the stated ratio convention. State what remains fixed in every V/f problem. Never add Iw and Im as scalars. A correct formula used with the wrong fixed quantity is still the wrong answer.
''',[
 ['Maximum-efficiency load','Pi = 400 W and full-load copper loss = 1600 W.','x = √(400/1600) = 1/2. Maximum efficiency is at 50% rated kVA; no calculator is needed.','loss-balance'],
 ['OC test components','An OC test gives 200 V, 1 A and 120 W. Find the two current components.','Iw = 120/200 = 0.6 A. Im = √(1 − 0.36) = 0.8 A. Recognise the 3–4–5 triangle.','oc-test'],
 ['Changing frequency','Voltage stays fixed while frequency falls from 50 Hz to 40 Hz.','Flux ratio = 50/40 = 1.25. Flux rises 25%; magnetising current need not rise only 25% because the core is nonlinear.','vf'],
 ['All-day efficiency','Output energy is 95 kWh; total daily loss is 5 kWh.','Input = 100 kWh. All-day efficiency = 95%. Average of hourly efficiencies would give the wrong weighting.','energy-efficiency'],
 ['Leading regulation','R = 1%, X = 4%, pf = 0.8 leading.','sinφ = 0.6. Regulation ≈ 1×0.8 − 4×0.6 = −1.6%.','regulation']
],[
 ['At 80% load, copper loss is what fraction of its full-load value?',['0.8','0.64','1.25','0.16'],1,'Copper loss follows x²; 0.8² = 0.64.'],
 ['A 400/100 V ideal transformer supplies 20 A. Primary load current?',['80 A','20 A','5 A','2 A'],2,'The turns ratio is 4. Primary current is 20/4 = 5 A.'],
 ['Voltage drops by 10% at fixed frequency. Approximate peak-flux change?',['10% decrease','10% increase','No change','90% decrease'],0,'Φm ∝ V/f; at fixed f the flux follows V.'],
 ['An open-delta bank retains what fraction of the corresponding closed-delta capacity?',['66.7%','50%','86.6%','57.7%'],3,'√3 S / (3S) = 1/√3 = 57.7%.']
], 'transformer')

chapter('dc-machines','machines','DC Machines','Construction, EMF, torque, generator and motor characteristics, starting, control and braking.',r'''
## Construction and conversion
The yoke provides mechanical support and a magnetic return path. Main poles establish field flux. The laminated armature carries conductors in which EMF is induced. Brushes contact the commutator. In a generator the commutator gives a unidirectional brush voltage from alternating conductor EMFs; in a motor it reverses conductor current at the appropriate instant so torque remains unidirectional. Lap winding has A = P parallel paths for simplex construction; simplex wave winding has A = 2.

$$ E=\frac{P\Phi ZN}{60A},\quad T_e=\frac{PZ}{2\pi A}\Phi I_a $$

Here P is poles, Φ flux per pole in webers, Z active armature conductors, N rpm and A parallel paths. Electrical power converted is EIa = Teω. Electromagnetic torque is not necessarily shaft torque: mechanical and other losses separate them.

## Generator and motor voltage equations
For a motor, back EMF Eb = V − IaRa − brush drop. For a generator, terminal voltage V = Eg − IaRa − brush drop. A shunt motor takes line current IL = Ia + Ish, while a shunt generator supplies Ia = IL + Ish. Series-field resistance must be included where it carries armature current. A long-shunt and short-shunt compound connection have different shunt-field terminal voltages; sketch the actual connection.

$$ N\propto\frac{V-I_aR_a}{\Phi},\quad P_{cu,a}=I_a^2R_a $$

## Characteristics and applications
A shunt motor has approximately constant flux, so torque follows armature current and speed falls moderately with load. In an unsaturated series motor Φ ∝ Ia, making torque proportional to Ia². After saturation torque is approximately proportional to Ia. Its high starting torque suits traction-type loads, but operating an unloaded series motor can produce dangerous overspeed because flux becomes small.

A separately excited generator permits independent field control. A self-excited shunt generator needs residual magnetism, field connection that reinforces it, suitable speed, and field resistance below the critical value for that speed. Critical resistance is the slope of the tangent to the open-circuit characteristic. Reversing residual flux or field leads incorrectly prevents voltage build-up. Cumulative compounding assists main flux; differential compounding opposes it.

## Armature reaction and commutation
Armature MMF distorts the main field and may have a demagnetising component when brushes are shifted. The magnetic neutral axis moves in the direction of rotation in a generator and opposite rotation in a motor. Interpoles, connected in series with the armature, help commutation. Compensating windings counter field distortion under pole faces. Reactance voltage arises while a commutating coil reverses current; resistance commutation with carbon brushes and EMF commutation help reduce sparking.

## Starting and speed control
At standstill Eb = 0, so directly applying rated voltage can give excessive current. A starter inserts resistance and removes it as speed rises. A three-point starter has the no-voltage coil in the shunt-field circuit; deliberate field weakening can affect it. A four-point starter makes that coil independent of field current, but that feature does not itself provide field-failure protection.

Armature-voltage control gives below-base-speed operation with approximately constant field. Field weakening gives above-base-speed operation and reduces torque capability for a fixed current. Armature resistance control wastes power and gives poorer speed regulation. Reversing either armature connections or field connections reverses torque; reversing both leaves the direction unchanged.

## Braking and losses
Regenerative braking returns electrical energy when the machine operates as a generator into the supply with suitable voltage/power-flow conditions. Dynamic braking dissipates generated energy in resistance after disconnecting the armature from the supply. Plugging reverses connections to produce opposing torque and needs current limiting; disconnect near zero speed to avoid reversal. Copper losses are Ia²Ra and field loss, core losses comprise hysteresis/eddy loss, and mechanical losses include friction/windage. Maximum-efficiency shortcuts require identifying which losses are treated as constant.
''',[
 ['Back EMF','A 220 V motor takes Ia = 20 A through Ra = 0.5 Ω; neglect brush drop.','Eb = 220 − 10 = 210 V. Use the motor sign convention.','back-emf'],
 ['Series torque','Unsaturated series-motor current rises from 10 A to 15 A.','Torque ratio = (15/10)² = 2.25; after strong saturation it would be nearer 1.5.','machine-scaling'],
 ['Speed ratio','Flux falls to 80% while back EMF is unchanged.','N₂/N₁ = Φ₁/Φ₂ = 1/0.8 = 1.25. Speed rises 25%.','machine-scaling']
],[['A simplex wave winding has how many parallel paths?',['2','P','P/2','2P'],0,'Simplex wave: A = 2, independent of pole count.'],['Which machine must not normally be run unloaded?',['DC shunt motor','DC series motor','Synchronous motor','Transformer'],1,'Low load current gives weak series flux and possible overspeed.'],['Reversing both field and armature connections does what to DC motor direction?',['Reverses it','Leaves it unchanged','Stops it always','Makes it synchronous'],1,'Torque depends on the product of field and armature current; both signs reverse.']])

chapter('induction-motors','machines','Induction Motors','Slip, rotor frequency, torque, power flow, starting, control and single-phase operation.',r'''
## Rotating field and slip
A balanced three-phase stator supply produces a rotating field. Its synchronous speed is Ns = 120f/P rpm. An induction rotor needs relative motion to induce current; at synchronous speed an ideal induction motor has no induced rotor EMF and no sustained electromagnetic torque. Swap any two stator phases to reverse the field direction.

$$ s=\frac{N_s-N}{N_s},\quad f_r=sf,\quad E_{2s}=sE_2,\quad X_{2s}=sX_2 $$

Normal motoring has 0 < s < 1; generating above synchronous speed gives s < 0; plugging can give s > 1. The rotor frequency is slip times supply frequency, not mechanical revolutions per second. A squirrel-cage rotor has shorted bars and end rings. A wound rotor permits external resistance through slip rings, mainly useful during starting or certain control methods.

## Torque and maximum torque
Using a simplified rotor model at fixed supply, torque is proportional to sR₂/[R₂²+(sX₂)²]. For low slip, T ∝ s/R₂. For large slip where sX₂ dominates, T ∝ R₂/s. Maximum torque occurs at s = R₂/X₂ if stator impedance is neglected. Adding rotor resistance shifts maximum torque to higher slip without changing its approximate magnitude. Maximum starting torque occurs when total rotor resistance equals standstill rotor reactance in that model.

$$ T\propto\frac{sR_2}{R_2^2+(sX_2)^2},\quad s_{max}\approx R_2/X_2 $$

At a fixed frequency and slip, torque approximately follows supply voltage squared. An 80% voltage gives about 64% torque, not 80%. The exact Thevenin equivalent includes stator resistance/reactance, so use the simplified maximum-slip formula only when its assumptions fit.

## Power flow: the most useful numerical model
Subtract stator copper and core losses from input to obtain air-gap power Pg. Rotor copper loss is sPg. Gross mechanical power is (1−s)Pg. Subtract friction and windage to obtain shaft power. Rotor copper loss divided by gross mechanical power is s/(1−s).

$$ P_{r,cu}=sP_g,\quad P_m=(1-s)P_g,\quad T_e=P_g/\omega_s=P_m/\omega_m $$

Do not divide Pg by actual rotor speed to get developed torque. Use synchronous angular speed with air-gap power, or rotor angular speed with developed mechanical power. Shaft torque uses shaft power and actual rotor speed.

## Starting, speed control and braking
DOL starting applies rated voltage and gives high current. A star–delta starter is suitable for a motor designed to run delta at the supply voltage and having accessible winding terminals. Starting in star reduces each winding voltage to 1/√3 of delta, and line current and torque to roughly one-third of DOL delta values. With an autotransformer tap k, motor starting current is about k of DOL, supply current about k², and torque about k².

V/f control varies synchronous speed while approximately preserving flux below base speed. Pole changing changes Ns in discrete steps. Rotor resistance control works with wound rotors but dissipates slip power. Regeneration occurs when driven above synchronous speed in an appropriate connected system. Plugging reverses phase sequence and requires control near zero speed. DC-injection braking creates a stationary stator field and dissipates rotor energy.

## Single-phase induction motors
A single-phase pulsating field can be resolved into two equal opposite rotating fields. At rest their torques cancel, so the basic motor is not self-starting. An auxiliary winding supplies a phase-displaced current. Resistance-start split-phase motors use differing winding impedance; capacitor-start motors provide greater phase separation and starting torque. Capacitor-run designs retain a suitable capacitor during operation. A shaded-pole motor uses a shorted shading turn; the field sweeps from unshaded to shaded portion. Do not confuse these induction types with universal motors.
''',[
 ['Slip and frequency','A 4-pole, 50 Hz motor runs at 1440 rpm.','Ns = 1500 rpm; s = 60/1500 = 0.04; rotor frequency = 2 Hz.','slip'],
 ['Power split','Air-gap power is 20 kW at 5% slip.','Rotor copper = 1 kW; developed mechanical = 19 kW. Shaft output is lower if mechanical losses exist.','rotor-power'],
 ['Reduced-voltage starting','A starter applies 70% rated voltage.','Starting torque is about 0.7² = 49% of full-voltage starting torque.','machine-scaling']
],[['Rotor input is 10 kW at s = 0.03. Rotor copper loss?',['3 kW','300 W','970 W','30 W'],1,'sPg = 0.03 × 10000 = 300 W.'],['A 6-pole motor on 50 Hz has synchronous speed:',['1500 rpm','3000 rpm','1000 rpm','750 rpm'],2,'120×50/6 = 1000 rpm.'],['Adding wound-rotor resistance approximately changes maximum torque how?',['Doubles always','Unchanged magnitude; higher-slip location','Zero torque','Lower-slip location'],1,'In the simplified model Tmax is unchanged, while smax rises.']],'induction')

chapter('synchronous','machines','Synchronous Machines','Alternator EMF, armature reaction, regulation, synchronisation and synchronous motors.',r'''
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
''',[
 ['Frequency from speed','A 12-pole alternator runs at 500 rpm.','f = 12×500/120 = 50 Hz.','speed-frequency'],
 ['Power-angle change','In the cylindrical model, δ changes from 30° to 90° with V, E and Xs fixed.','Power doubles because sin90°/sin30° = 2. The latter point is the ideal maximum, not a recommended operating margin.','power-angle']
],[['On an infinite bus, increasing excitation mainly changes:',['Frequency','Reactive power','Pole count','Synchronous speed'],1,'Voltage and frequency are imposed by the bus; excitation primarily controls reactive exchange.'],['An overexcited synchronous motor usually draws:',['Lagging current','Leading current','No current','DC stator current'],1,'Overexcitation can make the stator current lead its voltage.'],['Zero-lagging-pf alternator armature reaction is mainly:',['Magnetising','Demagnetising','Zero','Only mechanical'],1,'The armature MMF mainly opposes the main field.']])

chapter('special-machines','machines','Special & Fractional Motors','Servos, steppers, universal, reluctance, hysteresis and small single-phase motors.',r'''
## Select by the task
A servo is part of a controlled system: feedback compares actual position or speed with the command and drives the error down. “Servo” describes a controlled application, not one single winding construction. DC, AC synchronous and other motor types can form servo systems. Low inertia improves rapid response; a suitable torque-speed curve and controller determine performance.

A stepper moves through discrete increments in response to pulses. Pulse count gives commanded position and pulse rate gives commanded speed. An open-loop stepper can lose steps if overloaded; command count is not proof that the shaft reached the intended position. Holding torque refers to torque with the motor energised and stationary; detent torque can exist without current for some permanent-magnet designs.

$$ \theta_{step}=360^\circ/N_{steps},\quad N_{rpm}=60 f_{pulse}/N_{steps} $$

Variable-reluctance steppers seek minimum reluctance; permanent-magnet steppers use a magnetised rotor; hybrid motors combine features. Use the geometry-specific step-angle equation only when its pole/tooth arrangement is supplied. The generic steps-per-revolution equation is safer than memorising one tooth formula for all designs.

## Universal and small motors
A universal motor is a suitably designed series commutator motor capable of AC and DC operation. Field and armature currents reverse together on AC, maintaining average torque direction. Laminations reduce AC core losses and design reduces reactance/commutation difficulty. It offers high speed and starting torque but brush wear and noise are drawbacks. It is not a synchronous motor.

A reluctance motor develops torque because the rotor seeks a low-reluctance alignment. A synchronous reluctance motor can run synchronously after appropriate starting. A hysteresis motor uses rotor hysteresis for smooth torque and can settle at synchronous speed. A shaded-pole induction motor gives modest starting torque, simple construction and a usual fixed direction determined by shading. A permanent-split-capacitor motor retains the run capacitor and avoids a centrifugal switch in that arrangement.

## Exam comparisons
For precision motion, ask whether feedback is present, how position is encoded and what happens during overload. For small appliances, compare starting torque, speed, brush maintenance and noise. A two-phase AC servomotor often uses a high-resistance rotor to obtain a useful stable torque-speed response. A brushless DC motor uses electronic commutation; it does not have a mechanical commutator even though its name contains DC.

Fractional-horsepower simply describes a power class below one horsepower, not a unique motor principle. Its units matter: approximately 746 W equals one mechanical horsepower. Choose motor construction from the physical principle, not from the size label alone.
''',[
 ['Pulse count and speed','A 1.8° stepper receives 1000 pulses/s, one full step per pulse.','200 steps/rev. Speed = 60×1000/200 = 300 rpm; 50 pulses command 90°.','pulse-position'],
 ['Open-loop error','A stepper is commanded 100 steps but stalls for 10.','The command counter still says 100. Without suitable feedback or homing, the controller may not know actual position.','motor-selection']
],[['A 0.9° full-step motor requires how many pulses per revolution?',['200','400','90','360'],1,'360/0.9 = 400.'],['Which motor uses electronic commutation?',['Conventional DC shunt','BLDC','Shaded pole','Universal'],1,'BLDC uses switches controlled by rotor-position information.'],['The main defining feature of a servo system is:',['Always open loop','Feedback control','Always brushed','Always 50 Hz'],1,'A servo compares measured response to a commanded value.']])

chapter('generation','power','Generation & Load Economics','Station types, load curves, demand/diversity factors, energy and power-factor improvement.',r'''
## Energy conversion chains
A steam plant converts fuel heat into steam energy, turbine mechanical power and generator output. A condenser lowers exhaust pressure and returns condensate. An economiser transfers flue-gas heat to feedwater; an air preheater heats combustion air; a superheater increases steam temperature above saturation. They act on different fluids. Overall efficiency is the product of correctly defined stage efficiencies, not their sum.

Hydropower uses water head and flow: P = ρgQHη. Pumped storage consumes electrical energy to store water at height and later generates; round-trip energy output is lower than input. Gas turbines use compressed hot gas; combined-cycle plants recover exhaust heat in a steam cycle. Nuclear plants use controlled fission heat; moderators, where used, slow neutrons, while control rods absorb them. Solar PV converts light electrically; solar thermal first produces heat. Wind-turbine available power scales as air density × swept area × wind-speed cubed, before aerodynamic and system losses.

## Load curve and demand definitions
A chronological load curve plots demand against time. Its area is energy. A load-duration curve rearranges the same demand values by descending magnitude and preserves energy, but loses chronological information. Average demand = energy/period. Maximum demand is the highest average demand over the stated demand interval, not necessarily an instantaneous switching peak.

$$ LF=\frac{P_{avg}}{P_{max}},\quad DF=\frac{P_{max}}{P_{connected}},\quad Diversity=\frac{\sum P_{max,individual}}{P_{max,group}} $$

Load factor and demand factor are normally at most one for consistent definitions. Diversity factor is normally at least one because individual peaks need not coincide. Capacity factor = actual energy/(installed capacity × calendar hours). Utilisation factor = maximum demand/installed capacity. Plant use factor uses hours actually operating in its denominator. Distinguish capacity from maximum demand; switching the denominator changes the meaning.

## Economics and reserve
Higher load factor spreads many fixed costs over more delivered energy and often reduces average unit cost. Base-load and peak-load duties have different running-hour and start-up requirements. Reserve capacity = installed capacity − maximum demand in the simple definition. A two-part tariff may charge for maximum demand plus energy; a three-part tariff can add a fixed customer component. Use the tariff's stated units: ₹/kW, ₹/kVA and ₹/kWh are not interchangeable.

## Power-factor correction
For a given delivered real power and voltage, a lower power factor means a larger current, greater conductor I²R loss and more kVA burden. Capacitors supply leading reactive power that offsets an inductive load's lagging requirement. Correction does not normally reduce the useful load's real power demand; it reduces reactive current upstream.

$$ Q_c=P(\tan\phi_1-\tan\phi_2) $$

Use kW to obtain kvar. For a capacitor on single-phase RMS voltage V, Q = ωCV². In a three-phase star bank each capacitor sees VL/√3; in delta each sees VL. Thus a delta capacitor of one-third the capacitance per branch can provide the same total kvar as the corresponding star bank at the same line voltage. Real selection also considers harmonics, switching and ratings.
''',[
 ['Load factor','Energy over 10 h is 600 kWh; peak demand is 100 kW.','Average = 60 kW, so load factor = 0.6. Do not use connected load as the denominator.','load-factors'],
 ['Capacitor kvar','A 100 kW load improves from 0.8 lagging to unity.','tanφ₁ = 0.6/0.8 = 0.75; Qc = 75 kvar.','power-factor']
],[['Individual peaks total 500 kW; group peak is 400 kW. Diversity factor?',['0.8','1.25','0.2','900'],1,'500/400 = 1.25.'],['An economiser primarily heats:',['Feedwater','Generator windings','Cooling air','Lubricating oil'],0,'It recovers flue-gas heat into feedwater.'],['At fixed real power and voltage, improving pf reduces:',['Useful real power necessarily','Supply current','Frequency','Energy-conversion requirement to zero'],1,'I = P/(√3 VL pf) for balanced three-phase loads.']])

chapter('transmission','power','Transmission, Distribution & Cables','Line parameters, voltage drop, corona, Ferranti effect, insulators and cable stress.',r'''
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
''',[
 ['Line-loss scaling','Transmission voltage doubles; real power, pf and conductor resistance stay fixed.','Current halves; copper loss becomes one quarter.','power-factor'],
 ['String efficiency','Three discs: total 60 kV, most-stressed disc 25 kV.','Efficiency = 60/(3×25) = 80%.','voltage-distribution']
],[['Ferranti effect is most associated with:',['Long lightly loaded AC lines','Short heavily loaded DC circuits','Only transformers at full load','Pure resistors'],0,'Charging current and line inductance can raise receiving-end voltage.'],['Maximum coaxial cable stress occurs:',['At conductor surface','At sheath always','At the mid-radius always','Uniformly everywhere'],0,'Stress falls as 1/x through the insulation.'],['If current doubles, fixed-resistance line loss becomes:',['Half','Double','Four times','Unchanged'],2,'Loss is proportional to I²; doubling current multiplies loss by four.']])

chapter('protection','power','Switchgear & Protection','Faults, relays, breakers, fuses, transformer and generator protection.',r'''
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
''',[
 ['Fault MVA','At 11 kV, a balanced fault current is 10 kA.','Fault level = √3×11×10 ≈ 190.5 MVA. No extra factor of 1000 is needed for kV×kA.','fault-level'],
 ['Protection identification','An oil/conservator transformer develops internal gas slowly.','A Buchholz alarm may operate from accumulated gas; an oil surge may operate the trip element.','protection-choice']
],[['Which device interrupts the main fault current?',['Relay coil','Circuit breaker','Voltmeter','Isolator used as a switch'],1,'The relay issues a trip command; the breaker interrupts.'],['A Buchholz relay requires the appropriate:',['Dry-type air core','Oil-filled conservator arrangement','DC battery','Cable insulation only'],1,'Its operation depends on gas/oil movement in that arrangement.'],['Generator negative-sequence protection primarily addresses:',['Rotor heating','Higher illumination','Battery charging','Transformer turns ratio'],0,'The reverse rotating field induces damaging rotor-frequency effects.']])
chapter('fundamentals','basic','Electrical Fundamentals & Storage','Units, resistance, temperature, batteries, capacitors, inductors and switching.',r'''
## Quantities, signs and units
Current is charge flow rate i = dq/dt, voltage is energy per unit charge, instantaneous power is p = vi and energy is the time integral of power. With current entering a labelled positive terminal, positive p means absorption; negative p means delivery. One ampere is one coulomb per second. A joule is a watt-second, whereas a kWh is 3.6 million joules. Conductance is measured in siemens; resistance in ohms; capacitance in farads; inductance in henries; flux in webers and flux density in teslas.

$$ R=\rho l/A,\quad R_T=R_0[1+\alpha_0(T-T_0)] $$

The temperature coefficient must correspond to its stated reference temperature. For a wire stretched to k times its length with constant volume and resistivity, area falls to 1/k and resistance becomes k²R. Simply cutting a same-section wire to k times its original length instead gives kR. Metallic resistance normally rises with temperature over ordinary ranges; semiconductor behaviour need not follow that rule.

## Series, parallel and source loading
Series resistors share current and add. Parallel resistors share voltage and their conductances add. Equal n resistors give nR in series and R/n in parallel. Voltage division applies to series impedances; current division distributes inversely to resistance for two parallel resistors. A voltmeter with finite resistance loads a circuit; an ammeter's resistance introduces a series drop.

A practical voltage source has internal series resistance. With EMF E and external load R, current is E/(R+r) and terminal voltage on discharge is E−Ir. Identical cells in series add EMFs and internal resistances. Identical parallel strings increase current capability while preserving terminal EMF. Battery Ah measures charge capacity; Wh also depends on voltage. Approximate runtime from Ah/current neglects rate, temperature and cutoff effects. Ah efficiency and Wh efficiency differ because charge/discharge voltages differ.

## Capacitors and inductors
An ideal capacitor follows i = C dv/dt. Its voltage cannot jump without an impulse of current. At DC steady state it is open, but an initially charged capacitor is not a zero-voltage element. Parallel capacitances add; series reciprocals add. An ideal inductor follows v = L di/dt. Its current cannot jump without an impulse of voltage. At DC steady state an ideal inductor is a short, while a real coil still has winding resistance.

$$ C=\epsilon A/d,\quad W_C=\frac{1}{2}CV^2,\quad W_L=\frac{1}{2}LI^2 $$

For a capacitor left connected to an ideal voltage source, inserting dielectric increases C and stored energy at fixed V, with energy exchanged with the source. If isolated at fixed charge, voltage and stored energy decrease. For coupled inductors, mutual terms modify the energy and series inductance; use the magnetic-circuits chapter.

## First-order switching
Find the initial state just before switching, preserve capacitor voltage/inductor current just after switching, and find the final DC state. Then use the exponential form. The resistance used for the time constant is the resistance seen by the energy-storage element with independent sources deactivated and dependent sources retained.

$$ x(t)=x(\infty)+[x(0^+)-x(\infty)]e^{-t/\tau},\quad \tau_{RC}=R_{th}C,\quad \tau_{RL}=L/R_{th} $$

At one time constant a charging response has completed 63.2% of the change; at about five it has completed 99.3%. This is not an instantaneous jump. Time constants have units of seconds and provide an immediate unit check.
''',[
 ['Wire stretching','A wire doubles in length at constant volume.','Area halves; R₂/R₁ = 2/(1/2) = 4.','resistance'],
 ['Stored energy','A 20 μF capacitor is charged to 100 V.','W = 0.5×20×10⁻⁶×100² = 0.1 J.','storage'],
 ['Time constant','A 10 kΩ resistance charges 100 μF.','τ = 10⁴×10⁻⁴ = 1 s. At 1 s, 63.2% of the final voltage change is complete.','transient']
],[['Five 20 Ω resistors in parallel give:',['100 Ω','4 Ω','25 Ω','0.25 Ω'],1,'R/n = 20/5 = 4 Ω.'],['An ideal inductor preserves which quantity at ordinary switching?',['Voltage','Current','Power','Resistance'],1,'Inductor current is continuous unless there is an impulse voltage.'],['2 kW used for 3 hours consumes:',['6 kWh','6 W','1.5 kWh','6000 kWh'],0,'Energy = power × time = 6 kWh.']],'rc')

chapter('networks','basic','Circuit Laws & Network Theorems','KCL/KVL, node/mesh, source conversion, Thevenin, Norton and maximum power.',r'''
## Start with topology
Label nodes and choose a reference. KCL expresses conservation of charge: the algebraic sum of branch currents at a node is zero in a lumped circuit. KVL expresses the loop voltage balance consistent with energy conservation. Be consistent with polarities and account for induced EMFs where present. Negative solved current means the actual direction is opposite to the chosen reference; it does not invalidate the solution.

Nodal analysis writes each branch current as (node voltage − neighbouring voltage)/impedance. With a voltage source between two unknown nodes, form a supernode and add its voltage constraint. Mesh analysis assigns loop currents in a planar circuit; shared-element current is the difference between adjacent mesh currents. A current source between meshes calls for a supermesh and current constraint. Pick the method with fewer unknowns.

## Source conversion
A voltage source V in series with R is terminal-equivalent to a current source I = V/R in parallel with the same R. This preserves the terminal V–I relation, not necessarily power in internal elements. Do not convert an ideal source alone without its required resistance. Dependent sources must preserve their controlling variable and connection.

## Thevenin and Norton
Remove the load and calculate open-circuit terminal voltage Vth. Find Rth looking into the terminals with independent ideal voltage sources shorted and independent ideal current sources opened. Keep dependent sources active; use a test source when necessary. Reattach the load and solve. Norton current is the terminal short-circuit current with consistent sign; Rn = Rth and Vth = InRth when the equivalent is well defined.

$$ I_L=\frac{V_{th}}{R_{th}+R_L},\quad P_L=\frac{V_{th}^2R_L}{(R_{th}+R_L)^2} $$

For AC sinusoidal steady state use impedances and phasors at the specified frequency. An Rth found at DC is not automatically the equivalent for an AC capacitor/inductor network.

## Superposition
For a linear network, calculate the voltage/current contribution of each independent source with the others deactivated, and add signed or phasor responses. Retain dependent sources throughout. Power is nonlinear in current/voltage, so compute it after adding the responses. A diode network is not globally linear; an assumed fixed small-signal region must be justified before applying a linear model.

## Maximum power transfer
For a DC resistive source with Rth > 0 and variable positive load resistance, differentiating PL gives RL = Rth and Pmax = Vth²/(4Rth). At this condition half the ideal source power is dissipated in source resistance, so transfer efficiency is 50% in this model. Maximum efficiency is not the same optimisation objective as maximum load power.

$$ R_L=R_{th},\quad P_{max}=\frac{V_{th}^2}{4R_{th}} $$

For an AC load with both resistance and reactance adjustable, maximum average power uses ZL = conjugate(Zth). If the load is restricted to be purely resistive while source reactance is nonzero, the optimum is RL = |Zth|. Read the allowed load constraint before choosing a condition.

## Star–delta resistance transformation
A delta branch between two terminals equals the sum of pairwise products of star arms divided by the opposite star arm. A star arm equals the product of its two adjacent delta branches divided by the sum of all delta branches. For balanced networks, Rdelta = 3Rstar. These transformations concern terminal equivalence and are separate from three-phase line/phase voltage relationships.
''',[
 ['Thevenin load','Vth = 24 V, Rth = 4 Ω, RL = 8 Ω.','IL = 24/12 = 2 A; PL = 2²×8 = 32 W.','thevenin'],
 ['Matched load','Vth = 20 V, Rth = 5 Ω.','For maximum load power choose RL = 5 Ω. Pmax = 400/20 = 20 W.','max-power'],
 ['Power is not additive','Separate sources produce 2 A and 3 A in the same direction through 1 Ω.','Net current is 5 A; net power is 25 W, not 4+9 = 13 W.','superposition']
],[['When finding Rth, an independent ideal current source becomes:',['A short','An open','A 1 Ω resistor','A voltage source'],1,'Zero current through an ideal source corresponds to an open circuit.'],['Vth = 12 V, Rth = 3 Ω. Norton current?',['4 A','36 A','0.25 A','9 A'],0,'In = Vth/Rth = 4 A.'],['Which cannot be directly superposed?',['Voltage','Current','Power','Linear response'],2,'Power includes squared terms and cross-terms.']])

chapter('magnetic','basic','Magnetic Circuits & Coupled Coils','MMF, reluctance, air gaps, B–H curves, core loss, mutual inductance and dots.',r'''
## Magnetic-circuit analogy
Flux Φ is measured in webers, B = Φ/A in teslas, field strength H in A/m and MMF NI in ampere-turns. For a uniform linear section, reluctance is l/(μA) and Φ = NI/reluctance. Series magnetic sections approximately carry the same flux when leakage is neglected; their required MMFs add. Permeability is generally not constant in a ferromagnetic core near saturation, so a B–H curve may be necessary.

$$ \mathcal{R}=\frac{l}{\mu A},\quad NI=\sum H_i l_i,\quad \Phi=\frac{NI}{\mathcal{R}} $$

Air has much lower permeability than an unsaturated iron core, so even a short air gap can dominate total MMF. At an air gap, flux spreads into a larger effective area: fringing lowers average gap flux density for the same total flux. Leakage means some flux does not follow the intended useful path; it is not the same as fringing. A leakage coefficient defined as total/useful flux is greater than one.

## Induction and material behaviour
Faraday's law gives induced EMF from changing flux linkage. Lenz's minus sign says the induced effect opposes the change causing it, consistent with energy conservation. It does not mean induced current always opposes the original current. In a moving straight conductor, e = Blv when length, velocity and field are mutually perpendicular; use the appropriate angular factor otherwise.

A B–H loop records hysteresis. Retentivity is residual flux density when H returns to zero after magnetisation; coercive field is the reverse field needed to bring B to zero. Soft magnetic materials have relatively narrow loops and suit alternating cores. Hard magnetic materials have larger coercivity and suit permanent magnets. Nickel, iron and cobalt are familiar ferromagnetic examples under ordinary conditions.

Hysteresis energy per cycle per unit volume is the area of the B–H loop. Classical hysteresis power varies approximately as fBmⁿ. Eddy-current loss varies approximately as f²Bm²t² for otherwise unchanged lamination/material conditions. Lamination thickness therefore matters strongly. Skin/proximity effects in conductors are related AC-field effects but are not names for hysteresis.

## Self and mutual inductance
For a linear magnetic circuit L = NΦ/I = N²/reluctance. Self-induced voltage is L di/dt under passive convention; mutual-induced voltage involves M times the other coil's current derivative. The coupling coefficient k measures what fraction of linkage is shared and satisfies 0 ≤ k ≤ 1 for the usual magnitude convention.

$$ M=k\sqrt{L_1L_2},\quad L_{aiding}=L_1+L_2+2M,\quad L_{opposing}=L_1+L_2-2M $$

Subtracting the two series measurements gives M = (Laiding − Lopposing)/4. This factor of four is a recurring trap. With dot-marked coils, currents entering both dotted terminals produce mutually aiding flux under the standard dot convention. Reversing one current reference reverses the sign of the mutual term. Stored energy includes ±Mi₁i₂ in addition to the two self-energy terms; select the sign from references, not guesswork.

## Circular conductor and solenoid models
For a long straight conductor, H = I/(2πr) and B = μH outside the conductor. An ideal long solenoid gives H ≈ NI/l. These formulas assume their respective geometries; the mean path length in a toroid is not the same as radial distance from a straight wire.
''',[
 ['Two inductance measurements','Series aiding gives 18 mH; opposing gives 10 mH.','M = (18−10)/4 = 2 mH. Also L₁+L₂ = 14 mH.','coupled-coils'],
 ['Coupling limit','L₁ = 4 H and L₂ = 9 H.','Maximum M = √36 = 6 H. Any value above 6 H violates k ≤ 1.','coupled-coils']
],[['Aiding is 12 H and opposing is 4 H. Mutual inductance?',['8 H','4 H','2 H','16 H'],2,'Their difference is 4M, so M = 2 H.'],['Air-gap flux spreading is called:',['Hysteresis','Fringing','Skin effect','Commutation'],1,'Fringing increases the effective gap area.'],['Lenz law is consistent with conservation of:',['Only charge','Energy','Resistance','Frequency'],1,'The induced effect opposes its cause rather than creating free energy.']])

chapter('ac','basic','AC Fundamentals & Resonance','RMS, phasors, impedance, complex power, harmonics and series/parallel resonance.',r'''
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
''',[
 ['Impedance triangle','R = 6 Ω and net inductive reactance = 8 Ω across 100 V.','|Z| = 10 Ω, I = 10 A and pf = 0.6 lagging. P = 600 W.','impedance'],
 ['Harmonic heating','v = 6 sinωt + 8 sin3ωt volts.','Vrms² = (36+64)/2 = 50; Vrms = 5√2 V.','rms'],
 ['Resonance magnification','A series RLC has Q = 5 and supply 20 V at resonance.','Each reactive voltage is 100 V; opposite phasors cancel, leaving the resistor drop equal to 20 V.','resonance']
],[['A sine-wave peak is 100√2 V. RMS is:',['50 V','100 V','200 V','100√2 V'],1,'Divide the peak by √2.'],['At ideal series resonance, input power factor is:',['0','0.5 lag','1','0.5 lead'],2,'Net reactance is zero and input impedance is resistive.'],['For P = 3 kW and Q = 4 kvar, apparent power is:',['7 kVA','1 kVA','5 kVA','12 kVA'],2,'Use √(3²+4²) = 5 kVA.']],'phasor')

chapter('three-phase','basic','Three-Phase Circuits','Star/delta, balanced power, two wattmeters, phase sequence and neutral current.',r'''
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
''',[
 ['Connection conversion','Balanced star resistors are 10 Ω each on 100√3 V line supply.','Each phase sees 100 V and takes 10 A. Total power = 3×100×10 = 3 kW.','line-phase'],
 ['Wattmeter inference','A balanced load gives W₁ = W₂ = 2 kW.','Total P = 4 kW and tanφ = 0, hence unity pf.','two-wattmeter']
],[['In balanced star, line current equals:',['√3 times phase current','Phase current','Phase current/√3','3 times phase current'],1,'Only star voltage has the √3 magnitude relation.'],['One wattmeter is zero for a balanced two-wattmeter test at pf:',['1','0.866','0.5','0'],2,'One cos(30°+φ) vanishes at φ = 60°.'],['Same resistive branches: delta power divided by star power at fixed VL is:',['1/3','√3','3','1'],2,'Each delta branch sees √3 times star voltage, so branch power triples.']])
chapter('instruments','measurements','Instruments & Errors','PMMC, MI, dynamometer, electrostatic, range extension, errors and CRO.',r'''
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
''',[
 ['Full-scale error','A 100 V range has ±1% full-scale accuracy. It reads 20 V.','Absolute limit is ±1 V. Relative to 20 V this is ±5%, not ±1%.','measurement-error'],
 ['Meter shunt','A 1 mA, 100 Ω movement is extended to 1 A.','Rsh = 0.001×100/(1−0.001) ≈ 0.1001 Ω.','meter-range'],
 ['CRO period','One cycle occupies four divisions at 0.5 ms/div.','T = 2 ms and f = 500 Hz.','time-frequency']
],[['PMMC directly measures:',['DC','All AC waveforms without rectifier','Only reactive power','Frequency only'],0,'Direct PMMC average AC torque reverses and averages to zero.'],['A voltmeter is connected:',['In series','In parallel','Only through a CT','Across a fuse alone'],1,'It measures the potential difference between two nodes.'],['A 0.35 μs rise time corresponds approximately to bandwidth:',['1 MHz','10 MHz','0.1 MHz','100 MHz'],0,'BW ≈ 0.35/tr = 10⁶ Hz.']])

chapter('bridges','measurements','Bridges & Resistance Measurement','Wheatstone, Kelvin, AC bridges, insulation resistance and galvanometers.',r'''
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
''',[
 ['Bridge balance','Z₁ = 10 Ω, Z₂ = 20 Ω, Z₃ = 30 Ω in the labelled bridge convention.','Z₄ = Z₂Z₃/Z₁ = 60 Ω. Write the ratio first to avoid reversal.','bridge-balance'],
 ['Low resistance choice','Measure a 0.01 Ω shunt accurately.','Use a suitable Kelvin/four-terminal method; lead resistance can dominate a two-wire reading.','instrument-choice']
],[['Best classical bridge choice for very low resistance?',['Kelvin double','De Sauty','Wien frequency bridge','Schering'],0,'Kelvin minimises lead/contact-resistance error.'],['An insulation-resistance tester is commonly called:',['Megger','Tachometer','Luxmeter','Wattmeter'],0,'It measures high insulation resistance under an applied test voltage.'],['AC bridge balance requires equality of:',['Only real parts','Only imaginary parts','Both real and imaginary parts','Only magnitudes'],2,'A complex equality imposes both conditions.']])

chapter('power-energy','measurements','Power & Energy Measurement','Wattmeters, energy meters, calibration, creeping and electronic metering.',r'''
## Wattmeter connections
A wattmeter current coil is connected in series with the load and its pressure/voltage coil across an appropriate voltage. An ideal reading is the average of instantaneous vi; for sinusoidal supply it becomes VI cosφ. Coil connections can include current-coil loss or pressure-coil consumption in the reading. Correct the loss according to the actual connection and meter resistances. Do not select a correction formula without the diagram.

Low-power-factor measurement is sensitive to pressure-coil phase error because the wanted real-power component is small. A negative wattmeter reading can be physically meaningful, including in the two-wattmeter method; reversing a coil for an upscale reading does not remove the algebraic sign.

## Induction energy meter
The driving system produces interacting alternating fluxes and eddy currents in an aluminium disc. A permanent magnet provides braking torque approximately proportional to speed. At normal calibration, speed is proportional to power and accumulated revolutions to energy. The registering mechanism counts revolutions. Friction compensation, phase-angle adjustment and braking-magnet adjustment affect calibration.

Creeping is slow disc rotation under voltage with no load current when it should remain still. Holes or slots and suitable adjustments can reduce it. Do not call every meter motion creeping: at a real connected load rotation is normal. This construction needs AC; it is different from a static electronic meter.

## Electronic energy meter
Voltage and current sensors feed analogue processing or ADCs. The metering circuit computes instantaneous power and accumulates it with time; a pulse output represents a fixed energy increment, and a display/register stores consumption. Sampling, phase matching, clock accuracy, calibration and anti-alias filtering affect performance. A true energy meter integrates power; multiplying independent average voltage and average current is generally insufficient for arbitrary waveforms.

$$ E_{kWh}=\frac{N_{pulses}}{K_{imp/kWh}} $$

Some questions specify a meter constant in revolutions/kWh or impulses/kWh; others specify Wh/revolution. One is the reciprocal form of the other. Read the units before dividing or multiplying.

## Calibration and error
Reference energy equals known real power multiplied by elapsed time. Measured energy comes from the meter constant and pulse/revolution count. Percentage error = (registered energy − true energy)/true energy × 100. Positive error means fast/over-registering. If asked for correction rather than error, the sign reverses under the corresponding convention.

A meter constant of 1200 rev/kWh with 60 revolutions in 3 minutes registers 0.05 kWh in 0.05 h, equivalent to 1 kW. A stopwatch conversion error can make the result wrong by a factor of 60. For a current-transformer-operated meter, account for CT/PT ratios if the displayed values have not already been programmed to primary quantities.
''',[
 ['Meter pulses','A 1600 imp/kWh meter produces 800 pulses.','Registered energy = 800/1600 = 0.5 kWh.','meter-energy'],
 ['Meter error','Reference energy is 2 kWh; meter registers 2.1 kWh.','Error = 0.1/2×100 = +5%; the meter is fast.','measurement-error']
],[['A wattmeter measures:',['Apparent power only','Average real power','Energy directly','Only current'],1,'Its average torque/processing corresponds to real power.'],['A 1000 imp/kWh meter gives 250 pulses. Energy?',['4 kWh','0.25 kWh','250 kWh','25 kWh'],1,'250/1000 = 0.25 kWh.'],['No-load disc rotation in an induction meter is:',['Creeping','Slip','Hunting','Saturation necessarily'],0,'Creeping is unintended no-load disc motion.']])

chapter('ct-pt','measurements','CT, PT & Instrument Transformers','Connections, ratios, burden, phase error and measurement chains.',r'''
## Why instrument transformers?
Instrument transformers give scaled signals to meters and relays and provide suitable isolation within their designed ratings. A CT primary is in series with the measured circuit and its secondary supplies a low-impedance burden. A PT/VT primary is across the measured voltage and its secondary supplies a relatively high-impedance voltage circuit. Their normal connection requirements differ from a power transformer supplying an arbitrary load.

For an ideal CT, NpIp = NsIs, so a one-turn primary with many secondary turns gives a reduced secondary current. A nominal 200/5 A CT has ratio 40; a 4 A secondary corresponds to 160 A primary. Meter ratios must be included only once—some meters already display scaled primary values.

## Secondary safety principles
Do not open a CT secondary while the primary carries current. With secondary ampere-turns removed, core excitation and induced secondary voltage can become hazardous. Approved shorting/test arrangements are used by trained personnel. A PT secondary must not be short-circuited: it behaves as a voltage-source winding and can supply excessive current. These are opposite exam traps.

## Burden and errors
Burden is commonly specified as VA at a rated secondary current or voltage and a power factor. For a CT with secondary current Is and burden impedance magnitude |Zb|, apparent burden is Is²|Zb|. Wiring adds burden and can affect ratio and phase errors. Excitation current is one reason actual current ratio departs from the turns ratio.

$$ S_b=I_s^2|Z_b|,\quad I_p\approx K_I I_s,\quad V_p\approx K_V V_s $$

A metering CT aims at accurate normal-range measurement. A protection CT must reproduce fault signals suitably until its specified limit; saturation can distort relay input. A knee-point voltage concerns the nonlinear excitation curve under a defined test convention, not the normal secondary terminal voltage alone.

## Wattmeter multiplying factors
If an unscaled wattmeter reads secondary real power, primary power is approximately its reading multiplied by CT ratio and PT ratio, ignoring instrument-transformer errors. For energy, the same multiplication applies if the meter constant/register is in secondary units. Incorrect polarity can reverse power indication or cause erroneous differential spill current. Ratio error affects magnitude; phase-angle error particularly affects power measurement at low power factor.

## Choose the correct device
Use a CT for current scaling, PT for voltage scaling, wattmeter for real power and an energy meter for time-integrated consumption. A transformer name alone does not determine its entire application: protection and metering classes impose different accuracy/burden needs. Nameplate ratings and the actual connection govern whether a multiplication is required.
''',[
 ['Burden','A 5 A CT supplies 0.4 Ω resistive burden.','VA = 25×0.4 = 10 VA.','instrument-ratio'],
 ['Wattmeter scale','CT = 100/5, PT = 11000/110, meter reads 50 W.','Multiplier = 20×100 = 2000. Primary power = 100 kW.','instrument-ratio']
],[['A 300/5 CT has nominal current ratio:',['60','1500','0.0167','305'],0,'Primary/secondary = 300/5.'],['A live CT secondary should never be:',['Connected to its rated burden','Open-circuited','Kept in its designed metering circuit','Used with correct polarity'],1,'An open secondary can develop hazardous voltage.'],['A PT is normally connected to the measured circuit:',['In series','In parallel','Only as a short','Only to neutral'],1,'It samples the circuit voltage.']])

chapter('diodes','electronics','Diodes, Rectifiers & Wave Shaping','PN junctions, Zener regulation, rectifier values, clipping, clamping and filters.',r'''
## PN junction and models
Diffusion forms a depletion region with an internal electric field. Forward bias reduces the barrier and permits substantial current; reverse bias widens the depletion region and normally gives a small leakage current until breakdown. The common 0.7 V silicon and 0.3 V germanium drops are rough circuit approximations, not immutable thresholds. Current and temperature affect forward voltage.

An ideal diode is a short when on and an open when off. The constant-drop model adds an assumed forward drop. A small-signal resistance model linearises around a bias point. Solve by assuming states, calculating voltages/currents and checking that each assumed state is consistent. Zener diodes operate in a specified reverse-breakdown range with a series current-limiting resistor; ensure current and power stay within rating.

## Uncontrolled rectifiers
An ideal half-wave rectifier with a resistive load conducts for one half-cycle. Vdc = Vm/π and Vrms = Vm/2; ripple frequency is f. An ideal full-wave rectifier gives Vdc = 2Vm/π and Vrms = Vm/√2; ripple frequency is 2f. A bridge uses two conducting diodes in each path, so include two forward drops in a constant-drop approximation. A centre-tapped arrangement uses half the secondary at a time.

$$ V_{dc,HW}=V_m/\pi,\quad V_{dc,FW}=2V_m/\pi $$

Peak inverse voltage is Vm per diode for the ideal bridge and 2Vm for a centre-tapped full-wave circuit when Vm is the peak of each half-secondary. Define Vm carefully: using total secondary voltage with a half-secondary formula gives a factor-of-two error. Ideal maximum rectification efficiencies for resistive loads are approximately 40.6% half-wave and 81.2% full-wave, under their standard definitions and assumptions.

## Filters and wave shaping
A capacitor-input filter charges near peaks and discharges through the load between peaks. Larger capacitance, lower current and higher ripple frequency reduce ripple. For modest ripple, ΔVpp ≈ Iload/(fripple C); it is an approximation, not the unfiltered RMS formula. An inductor opposes changes in current; RC/LC filters have load-dependent behaviour.

A clipper limits part of a waveform. Diode orientation, bias source and diode drop set the clipping level. A clamper adds a DC shift using a diode-capacitor-resistor arrangement, approximately preserving peak-to-peak amplitude when the time constant is sufficiently large. It does not ideally amplify the waveform. Trace the diode's conducting interval and the capacitor's stored polarity before drawing the output.

## LEDs and photodevices
An LED needs current control; the resistor is (Vs−Vf)/I under the constant-drop model. Resistor power is I²R. A photodiode is commonly reverse-biased for detection and changes current with illumination. A solar cell supplies power in photovoltaic operation. A Zener regulator is neither a universal current source nor an unlimited-power clamp.
''',[
 ['LED resistor','Supply 9 V, LED drop 3 V, target current 20 mA.','R = 6/0.02 = 300 Ω; resistor dissipation = 0.12 W.','diode-circuit'],
 ['Ripple frequency','A full-wave bridge takes 50 Hz AC.','Unfiltered rectified ripple repeats at 100 Hz.','rectifier-waveform']
],[['A clamper ideally changes:',['DC level','Only frequency','Peak-to-peak amplitude by gain','Resistance of the source'],0,'It shifts the waveform vertically.'],['An ideal bridge rectifier has how many diodes conducting at once?',['1','2','3','4'],1,'Each current path passes through two diodes.'],['A reverse-biased Zener used for regulation needs:',['No resistor at any voltage','Current limiting','Only a transformer core','A short circuit'],1,'The external circuit must limit current and power.']])

chapter('transistors','electronics','BJT & FET','Operating regions, gains, bias, load line, MOSFET/JFET and switching.',r'''
## BJT currents and regions
A bipolar transistor has emitter, base and collector. IE = IC + IB. Common-emitter current gain β = IC/IB and common-base gain α = IC/IE, hence β = α/(1−α). These gains describe the relevant operating region and vary with device, current and temperature.

$$ \alpha=\frac{\beta}{\beta+1},\quad \beta=\frac{\alpha}{1-\alpha} $$

For an NPN transistor in forward-active operation, the base-emitter junction is forward biased and base-collector reverse biased. In saturation both are forward biased; in cutoff both are not driven into normal conduction. A saturated switching transistor does not obey IC = βIB without considering the load limit. PNP polarities reverse while the basic relationships remain.

## Configuration and bias
Common emitter provides substantial current and voltage gain and inverts the voltage signal. Common base has current gain slightly below one with low input resistance and high output resistance. Common collector/emitter follower has voltage gain near one, high input resistance and low output resistance, useful as a buffer. These are typical small-signal comparisons under suitable bias/load, not exact constants.

The DC load line expresses supply voltage shared between transistor and collector resistance. With an emitter resistor, include its drop in the loop. The quiescent or Q point is the no-signal operating condition. Place it to allow the required signal swing while avoiding unwanted cutoff/saturation. Voltage-divider bias with emitter feedback generally reduces dependence on β compared with simple fixed bias. Thermal runaway involves rising current and power causing additional heating; bias stabilisation and thermal design address it.

## JFET
A JFET uses a reverse-biased gate junction to control channel current. For an n-channel device VGS is normally nonpositive. In the pinch-off/saturation region, the Shockley transfer approximation is ID = IDSS(1−VGS/VP)² within its valid range. VP is negative for the usual n-channel convention. Pinch-off of the channel along the drain end is not the same as complete cutoff of drain current; gate cutoff occurs near VGS = VP.

$$ I_D=I_{DSS}(1-V_{GS}/V_P)^2 $$

## MOSFET
An insulated gate gives high DC input resistance, though capacitance still needs charging/discharging during switching. An enhancement n-MOS device forms a conducting channel when VGS exceeds its threshold in the model; a depletion device can conduct at zero gate bias. The long-channel saturation condition is VDS ≥ VGS−VT, and the square-law model is an approximation. Do not confuse MOSFET saturation with BJT saturation: MOS saturation is the current-source-like amplifier region, whereas a BJT saturated switch has low collector-emitter voltage.

FETs are voltage-controlled in the usual circuit description; BJTs need base drive in their current-gain model. Neither ideal label means zero gate switching energy or no base-emitter voltage requirement. Static gains alone do not specify switching speed.
''',[
 ['Current gains','β = 99. Find α.','α = 99/100 = 0.99; IE = 100IB.','transistor-gain'],
 ['JFET transfer','IDSS = 8 mA, VP = −4 V, VGS = −2 V.','ID = 8(1−1/2)² = 2 mA.','fet-bias']
],[['A BJT forward-active NPN has:',['Both junctions reverse','BE forward, BC reverse','Both forward','BE reverse, BC forward'],1,'That bias supports the normal forward-active gain relation.'],['An emitter follower has voltage gain approximately:',['One','One hundred always','Zero','Negative infinity'],0,'Its voltage follows the base with a bias offset.'],['The Q point is the:',['Peak overload point','Quiescent operating point','Breakdown point always','Frequency limit'],1,'It is the DC/no-signal bias condition.']])

chapter('amplifiers','electronics','Amplifiers, Feedback & Oscillators','Gain, bandwidth, amplifier classes, feedback and oscillation conditions.',r'''
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
''',[
 ['Feedback gain','A = 100 and β = 0.09 with negative feedback.','Af = 100/(1+9) = 10.','feedback'],
 ['Cascade gain','Two voltage-gain stages are 10 and 20 without loading change.','Total gain = 200. Multiplication, not 10+20.','gain-chain']
],[['Colpitts feedback divider is:',['Capacitive','Inductive only','Mechanical','A transformer turns ratio only'],0,'Its tank includes a capacitive divider.'],['Class B ideal conduction angle per device is:',['360°','180°','90° always','0°'],1,'Each device conducts over one half-cycle.'],['A 10× voltage gain corresponds to:',['10 dB','20 dB','100 dB','1 dB'],1,'20 log₁₀(10) = 20 dB.']])
chapter('illumination','utilisation','Illumination','Photometric quantities, inverse-square law, lumen method and lamp comparisons.',r'''
## Units before formulas
Luminous flux is measured in lumens; luminous intensity in candela, equivalent to lumens per steradian. Illuminance is incident luminous flux per unit area, measured in lux = lumen/m². Luminance concerns light leaving a surface in a particular direction and is measured in cd/m². Luminous efficacy compares luminous flux with electrical power in lm/W. These are not interchangeable names for brightness.

For an isotropic point source, total flux is 4πI. Real lamps are not perfectly isotropic, so a polar intensity curve may be needed. For a point source illuminating a small surface at distance r, illuminance is I cosθ/r², where θ is the angle to the surface normal. For a horizontal plane a vertical distance h below the lamp, r = h/cosθ, producing the cos³ form.

$$ E=\frac{I\cos\theta}{r^2}=\frac{I\cos^3\theta}{h^2} $$

The h-based expression assumes the stated geometry and intensity in that direction. Doubling direct distance gives one-quarter illuminance only when intensity and incidence angle stay fixed. Sources very close to large surfaces may not be well modelled as point sources.

## Lumen method
For average room illuminance, the required lumens from lamps depend on floor/work-plane area, utilisation factor and maintenance factor. If each lamp has flux F, then N = EA/(F × UF × MF), rounded up to a feasible layout. UF accounts for how much emitted flux reaches the useful plane. MF represents the retained fraction after depreciation/dirt in the chosen convention. Some books instead use a depreciation factor greater than one; then the corresponding factor moves to the numerator. Check the definition.

$$ N=\frac{EA}{F\,UF\,MF} $$

Average lux is not sufficient to establish uniformity or glare performance. Lamp spacing, mounting height, reflectances and distribution influence the layout. The watts-per-square-metre approach is a rough estimating method; the lumen/point methods explicitly use photometric data.

## Lamp types
Incandescent lamps heat a tungsten filament and have low efficacy compared with many modern sources. Fluorescent lamps use a gas discharge and phosphor conversion and need appropriate control gear. Sodium and mercury discharge lamps have distinctive spectra and starting/control requirements. LEDs are semiconductor emitters whose driver, thermal design and optical distribution affect performance. Colour temperature describes appearance, while colour rendering concerns how colours of objects are reproduced; neither is equal to efficacy.

Stroboscopic effects from time-varying light can make rotating machinery appear misleadingly stationary or slow. Glare can be direct or reflected. For exam questions distinguish illumination level from lamp power and avoid assuming one universal street-light lux value without its referenced classification and edition.
''',[
 ['Inverse-square law','A perpendicular surface receives 100 lux at 2 m from a point source. Find lux at 4 m.','Distance doubles, so illuminance becomes 25 lux.','illumination-law'],
 ['Lumen method','E = 200 lux, area = 50 m², lamp = 2000 lm, UF = 0.5, MF = 0.8.','N = 10000/(2000×0.5×0.8) = 12.5. Provide at least 13 lamps before layout checks.','lighting-design']
],[['Illuminance unit is:',['Candela','Lux','Lumen only','Watt'],1,'Lux is lumen per square metre.'],['An isotropic source of 1 cd emits total flux:',['1 lm','2π lm','4π lm','1/4π lm'],2,'The full sphere subtends 4π steradians.'],['Maintenance factor below one generally makes required initial lamp count:',['Larger','Smaller','Always unchanged','Zero'],0,'More initial light compensates for future depreciation.']])

chapter('heating-welding','utilisation','Heating, Welding & Electroplating','Resistance, induction, dielectric and arc heating; weld energy and Faraday laws.',r'''
## Heating principles
Resistance heating uses Joule loss I²Rt. Direct resistance heating passes current through the work; indirect resistance heating heats an element that transfers heat to the work. Temperature rise requires mcΔT and a phase change requires latent heat mL. Input electrical energy must exceed useful thermal energy when efficiency is below one. Include the workpiece, fixtures and losses only as specified.

$$ E_{in}=\frac{mc\Delta T+mL}{\eta} $$

Induction heating creates eddy currents in conducting work through a changing magnetic field; ferromagnetic hysteresis may also contribute below the relevant material transition. Higher frequency reduces penetration depth, useful for surface heating. Coreless furnaces use induction into a conductive charge; the work is analogous to a shorted secondary. Dielectric heating applies a high-frequency electric field to lossy insulating material.

$$ P_{dielectric}\approx 2\pi fCV^2\tan\delta $$

V is RMS and tanδ is loss tangent under the standard capacitor model. Dielectric heating is not based on the work being a good conductor. Arc heating uses the high-temperature electrical discharge; furnaces can be direct-arc or indirect-arc depending on whether the work is in the arc current path.

## Welding
Resistance welding concentrates I²Rt heating at the joint under pressure; spot, seam and butt methods differ in electrodes and joint geometry. It typically uses high current at low voltage. Heat depends on contact resistance, time and current distribution, not only on the bulk material resistance. Arc welding maintains an arc between electrode and work or another electrode arrangement, with suitable current control.

Welding sources often use a drooping voltage-current characteristic for manual arc-current stability. AC and DC welding have different arc stability, polarity and equipment considerations. Arc blow is associated with magnetic deflection of the arc, often significant with DC. Electrode coating/flux and shielding protect the weld pool and influence weld properties; they are not just decorative coverings.

## Electroplating and Faraday laws
Electroplating deposits material on a cathodic workpiece from an electrolyte. The first law gives deposited mass proportional to charge It. The second relates masses for the same charge to chemical equivalents. Electrochemical equivalent Z has mass per coulomb; efficiency accounts for current not producing the wanted deposition.

$$ m=ZIt\eta_c $$

Convert hours to seconds when Z is given per coulomb. If a deposit thickness is requested, mass = density × plated area × thickness. Count all plated faces. Anode behaviour depends on whether it is soluble or inert. Reversing an electrode label can reverse the physical interpretation even when the arithmetic is correct.
''',[
 ['Useful heat','2 kg of material, c = 500 J/(kg K), rise 100 K, efficiency 80%.','Useful heat = 100 kJ; input = 125 kJ. Divide by efficiency.','thermal-energy'],
 ['Welding scaling','Current doubles with the same resistance and time.','Heat becomes four times as large, from I²Rt.','thermal-energy'],
 ['Deposition','Z = 0.001 g/C, current 2 A, time 100 s, 100% current efficiency.','m = 0.001×2×100 = 0.2 g.','electrolysis']
],[['Dielectric heating suits:',['Lossy insulating material','Only perfect metals','Only vacuum','Only superconductors'],0,'Alternating electric-field losses produce heat in a dielectric.'],['The workpiece in electroplating is normally the:',['Cathode','Anode always','Neutral point','Transformer core'],0,'Metal ions are reduced and deposited at the cathode.'],['Resistance welding commonly requires:',['High current, low voltage','Low current, very high voltage only','No current','Only reactive power'],0,'High current produces concentrated joint heating.']])

chapter('traction','utilisation','Electric Traction & Drives','Speed-time curves, tractive effort, adhesion, braking and drive selection.',r'''
## Motion and the speed-time curve
A traction cycle can include acceleration, free running, coasting and braking. During coasting the supply power is reduced or cut while resistance gradually lowers speed. Area under a speed-time graph is distance, provided units are consistent. If speed is km/h and time seconds, divide the area by 3600 to obtain kilometres. Average speed excludes stop time when defined over actual running; schedule speed includes stops and is consequently lower.

For a trapezoidal graph, add acceleration triangle, constant-speed rectangle and braking triangle. A quadrilateral graph includes coasting. Do not treat every curve as a rectangle at maximum speed. Acceleration expressed in km/h/s needs division by 3.6 to obtain m/s².

## Tractive effort
Required force includes acceleration, gradient and train resistance. Equivalent mass can include a rotating-mass allowance. For a small gradient G expressed as a decimal rise/run, gradient force is approximately mgG. Adhesion limits transferable wheel force to approximately μ times the driven-wheel normal load, not necessarily the entire train weight.

$$ F_{acc}=m_{eq}a,\quad P_{wheel}=Fv,\quad P_{input}=P_{wheel}/\eta $$

Use v in m/s to obtain watts from newtons. G = 1% means 0.01, not 1. For descending gradients the gravitational term assists motion. Specific energy consumption is often expressed in Wh per tonne-km; specify whether it is wheel energy or electrical input.

## Motor and drive choice
Traction needs high starting torque, overload capability, speed control, reliable braking and suitable efficiency. Traditional DC series motors have high starting torque. Modern controlled AC drives offer effective traction with power electronic converters. A drive comprises motor, converter, controller and mechanical load; the motor name alone does not specify its operating envelope.

Below base speed, a controlled drive may provide an approximately constant-torque region limited by current. Above base speed, voltage limits lead to field weakening and an approximately constant-power region with torque decreasing as speed rises. Actual limits depend on the motor and drive design. Multi-quadrant operation describes signs of speed and torque: opposite signs imply mechanical braking power at the shaft.

## Braking and duty
Regenerative braking returns energy to a receptive supply or storage system, subject to control and infrastructure conditions. Rheostatic braking dissipates it in resistors. Mechanical braking provides required stopping/holding functions independently of whether regeneration is possible. A supply that cannot absorb returned energy changes the available braking strategy.

Motor selection also considers continuous, short-time or intermittent duty, thermal time constants and starting frequency. An equivalent RMS current/torque calculation can estimate heating only when its assumptions on losses, cooling and speed are suitable. A high peak torque for a short time is not the same rating as continuous torque.
''',[
 ['Schedule speed','10 km run takes 12 minutes plus a 3-minute stop.','Running average = 50 km/h. Schedule speed = 10/(15/60) = 40 km/h.','traction-motion'],
 ['Wheel power','Tractive effort 10 kN at 36 km/h.','36 km/h = 10 m/s; wheel power = 100 kW.','traction-motion']
],[['Area under a speed-time curve represents:',['Acceleration','Distance','Energy always','Power'],1,'Distance is the time integral of speed.'],['Regenerative braking sends energy to:',['Supply or receptive storage','Only a friction pad','Only heat in a resistor','The ground always'],0,'Electrical conversion returns useful energy if the receiving system allows it.'],['Schedule speed compared with running average when stops exist is:',['Higher','Lower','Always equal','Unrelated to stopping time'],1,'The same distance is divided by a longer total time.']])

chapter('estimation','utilisation','Estimation, Wiring & Earthing','Load assessment, bills of quantities, cable selection, protection and safety-rule references.',r'''
## Build the estimate from the circuit
Begin with a load list: quantity, rating, phase, location and expected simultaneous use. Connected load is the sum of installed ratings, while maximum demand reflects coincidence and use. Determine design current using voltage, efficiency and power factor as applicable. Divide loads into suitable circuits and prepare a layout, conductor route lengths and a single-line representation before pricing.

For a motor with shaft rating Pout, electrical input is Pout/η. A three-phase current estimate is Pout/(√3 VL η pf). Confusing output kW with input kW underestimates current. Starting current, duty and voltage drop can govern cable/protection selection even when steady current seems small.

$$ I_{3ph}=\frac{P_{out}}{\sqrt{3}V_L\eta\cos\phi} $$

## Cable and protection selection
Check current-carrying capacity after applicable installation/temperature/grouping corrections, voltage drop, short-circuit thermal withstand and mechanical requirements. Select protective devices for overload, fault current, required disconnection and discrimination. A breaker current rating alone does not prove adequate breaking capacity. Neutral current can be significant with unbalanced and nonlinear loads, so it must not be assumed zero.

For a simple single-phase two-wire circuit, the outgoing and return conductor resistances both contribute to loop drop. For a balanced three-phase circuit, use its phase/line relationship. Copper/aluminium resistivity, conductor temperature and length affect the result. Do not use one memorised wire size for every load without installation conditions.

## Bill of quantities and costing
Measure route lengths and allow for terminations, rises, drops and realistic wastage according to the estimate. Count switches, sockets, luminaires, junction boxes, conduits/trays, distribution boards, protection, earthing and accessories. Separate material, labour, transport, overheads and the specified taxes/contingencies. Unit rates must match units such as metre, number or set. A quantity take-off and a quotation are related but different records.

For repeated rooms, calculate a typical room carefully and check exceptions before multiplying. A discount on material purchase does not automatically apply to labour. Distinguish a percentage markup on cost from a profit margin on selling price: cost 100 marked up 20% sells for 120, giving a margin of 16.7% of selling price.

## Earthing, bonding and protective devices
Protective earthing connects exposed conductive parts to the protective system. Equipotential bonding reduces potential differences between accessible conductive parts. The neutral carries normal load current in applicable systems; protective earth is not intended as a substitute load-return conductor. A residual-current device detects imbalance between outgoing and returning monitored currents; it does not by itself provide every overload/short-circuit function unless combined with those protections.

Earthing electrodes can be rods, pipes, plates or grids as appropriate. Soil resistivity, moisture, geometry and seasonal conditions affect electrode resistance. Installation safety requires coordinated protection, bonding, insulation and disconnection, not just achieving one universal earth-resistance number.

## Reading rules in exam questions
Older question papers may cite the Indian Electricity Rules by historical rule number; current installation practice must be checked against the applicable CEA regulations and amendments. Keep the edition/year attached to any numerical clearance, circuit limit or rule citation. These notes intentionally do not turn an old exam value into a universal current legal requirement. Use the official CEA safety-regulations link in Sources alongside the specific notification and question wording.
''',[
 ['Motor current','A three-phase motor gives 8 kW at η = 0.8 and pf = 0.8 on 400 V.','Input = 10 kW; current = 10000/(√3×400×0.8) ≈ 18.0 A.','load-estimation'],
 ['Markup vs margin','Material cost 1000, labour 500; quote includes 20% markup on this cost.','Total cost = 1500; price = 1800. Profit margin is 300/1800 = 16.7%.','costing']
],[['Protective earth is intended to:',['Carry ordinary load current as neutral','Provide a protective connection for exposed metal','Replace insulation','Eliminate every fault current'],1,'It forms part of a coordinated protective system.'],['Motor shaft output divided by efficiency gives:',['Input electrical power','Reactive power only','Voltage','Frequency'],0,'η = Pout/Pin.'],['Connected load equals:',['Only one largest appliance','Sum of installed load ratings','Always actual maximum demand','Always average demand'],1,'Maximum demand depends on how loads are used together.']])

chapter('thyristors','power-electronics','Thyristors & Gate Circuits','SCR states, latching/holding current, triggering, commutation and protection.',r'''
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
''',[
 ['Holding versus latching','An SCR needs 30 mA to latch but only 15 mA to remain on.','A 20 mA established current may sustain conduction, but 20 mA immediately after a short gate pulse may fail to latch.','scr-states'],
 ['Protection matching','A question asks about accidental turn-on from a steep voltage edge.','Identify dv/dt and capacitive displacement current; an RC snubber is the standard conceptual mitigation.','switch-protection']
],[['Removing the gate pulse turns off a latched conventional SCR:',['Always','Normally no','Only because gate resistance is zero','Every half microsecond'],1,'It normally remains on until anode current falls below holding current with adequate recovery.'],['An RC snubber is associated primarily with limiting:',['dv/dt','Shaft speed','Illuminance','Turns ratio'],0,'It controls the voltage transient across the switch.'],['Latching current is usually:',['Greater than holding current','Less than zero','Exactly zero','Always identical to gate current'],0,'Initial establishment requires more anode current than sustaining conduction.']])

chapter('converters','power-electronics','Controlled Rectifiers & DC Converters','Firing angle, R/RL loads, freewheeling, buck, boost and buck–boost.',r'''
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
''',[
 ['Full converter','Vm = 100π V, α = 60°, continuous DC current, no overlap.','Vdc = 200×cos60° = 100 V.','controlled-rectifier'],
 ['Boost duty','An ideal CCM boost raises 24 V to 60 V.','1−D = 24/60 = 0.4, so D = 0.6.','duty-conversion'],
 ['Inverting buck–boost','Vin = 12 V and D = 0.25 in CCM.','Vo = −(0.25/0.75)×12 = −4 V.','duty-conversion']
],[['Ideal CCM buck with 100 V input and D = 0.3 gives:',['30 V','333 V','70 V','−30 V'],0,'Vo = DVin = 30 V.'],['Ideal CCM boost at D = 0.5 has voltage gain:',['0.5','1','2','−1'],2,'1/(1−0.5) = 2.'],['A full-controlled bridge continuous-current formula can be applied unchanged to every R load:',['Yes','No','Only at all firing angles','Because RMS equals average'],1,'The conduction interval depends on the load and current continuity.']],'buck')
sources = [
 {'id':'ssc2026','title':'SSC JE 2026 · official notification','url':'https://ssc.gov.in/api/attachment/uploads/masterData/NoticeBoards/Notice_of_adv_je_2026.pdf','kind':'Official syllabus','detail':'Sections 13 and 14. Electrical syllabus: printed pp. 23–24 and 26–27.'},
 {'id':'p24a','title':'2024 · 5 June · Shift 3 · Paper I','url':'https://cdn-images.prepp.in/public/image/SSC_JE_2024_Paper_1_Electrical_Question_Paper_with_Answer_Key_PDF_English_June_5_2024__b84c7b7fa61022fe724c263e4f9b895b.pdf','kind':'Paper reproduction','detail':'SSC response-sheet reproduction hosted by Prepp. Electrical-section question numbers.'},
 {'id':'p24b','title':'2024 · 6 June · Shift 2 · Paper I','url':'https://cdn-images.prepp.in/public/image/SSC_JE_2024_Paper_1_Electrical_Question_Paper_with_Answer_Key_PDF_English_June_6_2024__1787055475ddc3aa4f4fca32c4841ee5.pdf','kind':'Paper reproduction','detail':'SSC response-sheet reproduction hosted by Prepp. Electrical-section question numbers.'},
 {'id':'p24c','title':'2024 · 7 June · Shift 3 · Paper I','url':'https://cdn-images.prepp.in/public/image/SSC_JE_2024_Paper_1_Electrical_Question_Paper_with_Answer_Key_PDF_English_June_7_2024__1c78875d1c915f62665a9f7b98d34547.pdf','kind':'Paper reproduction','detail':'SSC response-sheet reproduction hosted by Prepp. Electrical-section question numbers.'},
 {'id':'p24ii','title':'2024 · 6 November · Paper II','url':'https://cdn-images.prepp.in/public/image/SSC_JE_2024_Paper_2_Electrical_Question_Paper_with_Answer_Key_PDF_Nov_06_2024__ca51123241f473e39c28401d2b095ed6.pdf','kind':'Paper reproduction','detail':'SSC response-sheet reproduction hosted by Prepp. Selected text-legible questions reviewed.'},
 {'id':'p23a','title':'2023 · 9 October · Shift 3 · Paper I','url':'https://cdn-images.prepp.in/public/image/SSC_JE_Electrical_Oct_9_2023_Shift_3_76282c6a10ce0113fc001f90fe32abc5.pdf','kind':'Paper reproduction','detail':'SSC response-sheet reproduction hosted by Prepp. Electrical-section question numbers.'},
 {'id':'p23b','title':'2023 · 11 October · Shift 3 · Paper I','url':'https://cdn-images.prepp.in/public/image/SSC_JE_Electrical_2023_Oct_11_Shift_3_d281d6e11ed3ecd2fd3ddbe26a261362_1__a45c42c3795832d0feefd6f1e6499cbc.pdf','kind':'Paper reproduction','detail':'SSC response-sheet reproduction hosted by Prepp. Electrical-section question numbers.'},
 {'id':'archive','title':'Previous-paper directory · additional years','url':'https://prepp.in/ssc-je-exam/practice-papers','kind':'Discovery index','detail':'Browse other papers. Linked papers are not all transcribed or checked in this website.'},
 {'id':'cea','title':'Central Electricity Authority · regulations','url':'https://cea.nic.in/regulations/?lang=en','kind':'Official reference portal','detail':'Use the applicable safety regulations and amendments. Portal could not be retrieved during this build; numerical legal requirements are not asserted here.'}
]
pyqs=[]
def pyq(source,q,page,chapter_id,prompt,answer,model):
    pyqs.append(dict(id=f'{source}-{q}',source=source,q=q,page=page,chapter=chapter_id,prompt=prompt,answer=answer,model=model))

# Short independently solved paraphrases; response-sheet chosen options are not answer keys.
pyq('p24a',6,36,'instruments','CRO rise time 0.5 μs: estimate bandwidth.','0.7 MHz, using BW ≈ 0.35/tr.','time-frequency')
pyq('p24a',14,39,'fundamentals','C = 10 F; v = 10t³−5t+10. Find i at t = 2 s.','1150 A: i = C(30t²−5).','storage')
pyq('p24a',15,39,'ac','Series resonance: R=5 Ω, L=400 H, C=4 F, V=400 V. Find VC.','800 V. I=80 A; XC=√(L/C)=10 Ω.','resonance')
pyq('p24a',18,40,'three-phase','Two wattmeters read 200 W and −35 W. Total real power?','165 W; retain the negative sign.','two-wattmeter')
pyq('p24a',73,57,'networks','Identify the Thevenin source arrangement.','Voltage source with series resistance.','thevenin')
pyq('p24a',74,57,'dc-machines','DC motor: V=200 V, Ia=20 A, Ra=0.5 Ω. Back EMF?','190 V: Eb=V−IaRa.','back-emf')
pyq('p24a',76,58,'transmission','For unchanged delivered power and voltage, higher pf changes line efficiency how?','Improves it: current and copper loss fall.','power-factor')
pyq('p24a',78,59,'ac','Find RMS for v=2sinωt+3sin3ωt+5sin5ωt volts.','√19 V; add harmonic mean squares.','rms')

pyq('p24b',38,48,'transformers','Purpose of transformer bushings?','Insulate leads passing through the tank.','transformer-construction')
pyq('p24b',39,48,'instruments','How does increasing electrostatic-instrument plate area affect sensitivity?','Generally increases it in the stated geometry.','instrument-choice')
pyq('p24b',40,49,'networks','Can linear superposition directly calculate power?','No. Add voltage/current responses first.','superposition')
pyq('p24b',54,53,'induction-motors','Gross mechanical power in terms of rotor input Pg and slip s?','(1−s)Pg; rotor copper loss is sPg.','rotor-power')
pyq('p24b',61,55,'induction-motors','Induction-motor transformer analogy: secondary condition?','Short-circuited secondary.','machine-equivalent')
pyq('p24b',78,61,'ac','Convert 10∠30° into rectangular form.','5√3+j5.','phasor-conversion')
pyq('p24b',84,62,'fundamentals','n equal resistors R in parallel: equivalent resistance?','R/n.','resistance')
pyq('p24b',85,63,'illumination','Usual incandescent filament material?','Tungsten.','lamp-selection')

pyq('p24c',2,36,'magnetic','L₁=8 H, L₂=32 H, k=0.4. Find M.','6.4 H: 0.4√(8×32).','coupled-coils')
pyq('p24c',3,36,'power-energy','Fixed V and I: what happens to wattmeter reading as pf rises?','It rises: P=VIpf.','power-factor')
pyq('p24c',44,50,'magnetic','Aiding/opposing inductances are 38/12 mH. Find M.','6.5 mH: difference divided by four.','coupled-coils')
pyq('p24c',85,62,'fundamentals','Ten 10 Ω resistors in parallel: equivalent?','1 Ω.','resistance')
pyq('p24c',86,63,'magnetic','Air-gap flux spreads and effective area grows. Name the effect.','Magnetic fringing.','magnetic-geometry')
pyq('p24c',87,63,'magnetic','L₁=20 H and L₂=320 H. Largest possible M?','80 H at k=1.','coupled-coils')
pyq('p24c',89,64,'transistors','What is a transistor’s no-signal operating point called?','Quiescent or Q point.','transistor-bias')

pyq('p24ii',1,1,'ac','What operation finds the difference between phasors?','Phasor subtraction with magnitude and phase retained.','phasor-conversion')
pyq('p24ii',16,7,'networks','Vth=40 V, Rth=5 Ω, RL=15 Ω. Load current?','2 A: 40/(5+15).','thevenin')
pyq('p24ii',45,18,'ct-pt','Which transformer class scales voltage/current for meters?','Instrument transformers: PT/VT and CT.','instrument-choice')
pyq('p24ii',78,31,'estimation','What commercial quantity is central to an installation quotation?','Component pricing within the complete scope.','costing')
pyq('p24ii',86,34,'fundamentals','Match resistive energy, DC power and SI units.','I²Rt; VI; joule for energy; watt=joule/second.','units')

pyq('p23a',2,41,'special-machines','Why can an AC series motor have low pf?','Substantial field/armature inductive reactance.','motor-selection')
pyq('p23a',3,42,'magnetic','Identify a ferromagnet among gold, nickel, water and oxygen.','Nickel.','magnetic-material')
pyq('p23a',5,42,'ac','P=40 W and pf=0.8. Apparent power?','50 VA: P/pf.','power-factor')
pyq('p23a',6,43,'illumination','Which lighting estimate is quick and approximate?','Watts per square metre.','lighting-design')
pyq('p23a',9,44,'transformers','OC readings: 200 V, 0.5 A, 50 W. Find Im.','√(0.5²−0.25²) ≈ 0.433 A.','oc-test')
pyq('p23a',33,52,'transformers','Typical three-phase distribution connection with LV neutral?','Delta–star.','transformer-connections')
pyq('p23a',34,53,'transformers','Typical laminated transformer-core steel?','Silicon steel.','transformer-construction')
pyq('p23a',54,59,'transformers','Daily delivered energy 120 kWh; losses 5 kWh. Efficiency?','120/125 = 96%.','energy-efficiency')

pyq('p23b',20,49,'ac','Series R–L circuit: express impedance.','Z=R+jXL; magnitude √(R²+XL²).','impedance')
pyq('p23b',38,55,'thyristors','Which is not a FET: JFET, MOSFET or thyristor?','Thyristor.','device-identification')
pyq('p23b',39,55,'fundamentals','A 100 A inductor stores 2 kWh. Required inductance?','1440 H: convert to joules, then L=2W/I².','storage')
pyq('p23b',44,57,'diodes','Half-wave rectifier on 50 Hz: ripple frequency?','50 Hz.','rectifier-waveform')
pyq('p23b',80,69,'ac','Sine peak 388 V: approximate RMS?','274.4 V; nearest given option 275 V.','rms')
pyq('p23b',81,70,'magnetic','Aiding/opposing inductances 4/2 H: mutual inductance?','0.5 H.','coupled-coils')
pyq('p23b',82,70,'diodes','12 V supply, 3 V LED, 36 mA: series resistance?','250 Ω: (12−3)/0.036.','diode-circuit')
pyq('p23b',88,72,'estimation','Contractor quotes each work item separately: contract type?','Item-rate contract.','costing')

nontechnical = [
 {'id':'reasoning','title':'General Intelligence & Reasoning','topics':['Analogies and classification','Number and letter series','Coding and symbolic operations','Relationships and directions','Spatial visualisation and figures','Logical judgement and problem solving','Arithmetic reasoning and observation']},
 {'id':'awareness','title':'General Awareness','topics':['Current events','History and culture','Geography and environment','Economy and polity','General science and research','India and neighbouring countries']}
]

def make_html(markdown):
    blocks=[]; headings=[]
    for chunk in markdown.strip().split('\n\n'):
        chunk=chunk.strip()
        if chunk.startswith('## '):
            title=chunk[3:]; anchor='s'+str(len(headings)+1)
            headings.append({'title':title,'anchor':anchor})
            blocks.append(f'<h2 id="{anchor}">{html.escape(title)}</h2>')
        elif chunk.startswith('$$ ') and chunk.endswith(' $$'):
            formula=chunk[3:-3]
            name='eq-'+hashlib.sha256(formula.encode()).hexdigest()[:16]+'.svg'
            folder=DIST/'assets'/'equations'; folder.mkdir(parents=True,exist_ok=True)
            target=folder/name
            if not target.exists():
                import matplotlib
                matplotlib.use('Agg')
                import matplotlib.pyplot as plt
                from matplotlib import rcParams
                rcParams['svg.hashsalt']='ssc-je-prep'
                fig=plt.figure(figsize=(1,0.4)); fig.patch.set_alpha(0)
                t=fig.text(0,0,'$'+formula+'$',fontsize=17,color='#143f35')
                fig.canvas.draw(); box=t.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
                fig.savefig(target,format='svg',bbox_inches=box.expanded(1.02,1.25),pad_inches=0.06,transparent=True,metadata={'Date':None})
                plt.close(fig)
            blocks.append(f'<div class="equation"><img src="assets/equations/{name}" alt="{html.escape(formula,quote=True)}" loading="lazy"></div>')
        else:
            blocks.append('<p>'+html.escape(chunk).replace('\n',' ')+'</p>')
    return '\n'.join(blocks),headings

def build():
    for c in chapters:
        c['html'],c['headings']=make_html(c['body'])
        c['words']=len(c['body'].split())
        c['minutes']=max(3,round(c['words']/150))
        c['practice']=[dict(id=f"{c['id']}-practice-{i+1}",chapter=c['id'],prompt=q[0],options=q[1],answer=q[2],explanation=q[3]) for i,q in enumerate(c['practice'])]
        c['models']=[dict(id=f"{c['id']}-model-{i+1}",chapter=c['id'],title=m[0],prompt=m[1],solution=m[2],tag=m[3]) for i,m in enumerate(c['models'])]
        text='# '+c['title']+'\n\n'+c['body']+'\n\n## Worked models (original)\n\n'
        text+='\n\n'.join('### '+m['title']+'\n\n'+m['prompt']+'\n\n'+m['solution'] for m in c['models'])
        text+='\n\n## Practice (original)\n\n'+'\n\n'.join(q['prompt']+'\n\nAnswer: '+q['options'][q['answer']]+'. '+q['explanation'] for q in c['practice'])
        (DIST/'notes'/f"{c['id']}.md").write_text(text,encoding='utf-8')
    data=dict(title='Lokesh’s SSC JE study desk',edition='14 October 2026',target='2026-10-30T00:00:00+05:30',subjects=subjects,chapters=chapters,pyqs=pyqs,sources=sources,nontechnical=nontechnical)
    (DIST/'content.js').write_text('window.STUDY_DATA = '+json.dumps(data,ensure_ascii=False)+';\n',encoding='utf-8')
    (DIST/'content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    import zipfile
    with zipfile.ZipFile(DIST/'materials'/'ssc-je-chapter-notes.zip','w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted((DIST/'notes').glob('*.md')): z.write(p,'notes/'+p.name)
    print(json.dumps({'chapters':len(chapters),'words':sum(c['words'] for c in chapters),'models':sum(len(c['models']) for c in chapters),'practice':sum(len(c['practice']) for c in chapters),'pyqs':len(pyqs)}))

if __name__ == '__main__': build()
