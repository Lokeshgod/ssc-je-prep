# BJT & FET

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

## Worked models (original)

### Current gains

β = 99. Find α.

α = 99/100 = 0.99; IE = 100IB.

### JFET transfer

IDSS = 8 mA, VP = −4 V, VGS = −2 V.

ID = 8(1−1/2)² = 2 mA.

## Practice (original)

A BJT forward-active NPN has:

Answer: BE forward, BC reverse. That bias supports the normal forward-active gain relation.

An emitter follower has voltage gain approximately:

Answer: One. Its voltage follows the base with a bias offset.

The Q point is the:

Answer: Quiescent operating point. It is the DC/no-signal bias condition.