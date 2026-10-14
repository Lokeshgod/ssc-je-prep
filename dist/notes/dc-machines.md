# DC Machines

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

## Worked models (original)

### Back EMF

A 220 V motor takes Ia = 20 A through Ra = 0.5 Ω; neglect brush drop.

Eb = 220 − 10 = 210 V. Use the motor sign convention.

### Series torque

Unsaturated series-motor current rises from 10 A to 15 A.

Torque ratio = (15/10)² = 2.25; after strong saturation it would be nearer 1.5.

### Speed ratio

Flux falls to 80% while back EMF is unchanged.

N₂/N₁ = Φ₁/Φ₂ = 1/0.8 = 1.25. Speed rises 25%.

## Practice (original)

A simplex wave winding has how many parallel paths?

Answer: 2. Simplex wave: A = 2, independent of pole count.

Which machine must not normally be run unloaded?

Answer: DC series motor. Low load current gives weak series flux and possible overspeed.

Reversing both field and armature connections does what to DC motor direction?

Answer: Leaves it unchanged. Torque depends on the product of field and armature current; both signs reverse.