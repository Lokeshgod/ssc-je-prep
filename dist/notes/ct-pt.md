# CT, PT & Instrument Transformers

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

## Worked models (original)

### Burden

A 5 A CT supplies 0.4 Ω resistive burden.

VA = 25×0.4 = 10 VA.

### Wattmeter scale

CT = 100/5, PT = 11000/110, meter reads 50 W.

Multiplier = 20×100 = 2000. Primary power = 100 kW.

## Practice (original)

A 300/5 CT has nominal current ratio:

Answer: 60. Primary/secondary = 300/5.

A live CT secondary should never be:

Answer: Open-circuited. An open secondary can develop hazardous voltage.

A PT is normally connected to the measured circuit:

Answer: In parallel. It samples the circuit voltage.