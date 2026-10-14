# Transformers

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

## Worked models (original)

### Maximum-efficiency load

Pi = 400 W and full-load copper loss = 1600 W.

x = √(400/1600) = 1/2. Maximum efficiency is at 50% rated kVA; no calculator is needed.

### OC test components

An OC test gives 200 V, 1 A and 120 W. Find the two current components.

Iw = 120/200 = 0.6 A. Im = √(1 − 0.36) = 0.8 A. Recognise the 3–4–5 triangle.

### Changing frequency

Voltage stays fixed while frequency falls from 50 Hz to 40 Hz.

Flux ratio = 50/40 = 1.25. Flux rises 25%; magnetising current need not rise only 25% because the core is nonlinear.

### All-day efficiency

Output energy is 95 kWh; total daily loss is 5 kWh.

Input = 100 kWh. All-day efficiency = 95%. Average of hourly efficiencies would give the wrong weighting.

### Leading regulation

R = 1%, X = 4%, pf = 0.8 leading.

sinφ = 0.6. Regulation ≈ 1×0.8 − 4×0.6 = −1.6%.

## Practice (original)

At 80% load, copper loss is what fraction of its full-load value?

Answer: 0.64. Copper loss follows x²; 0.8² = 0.64.

A 400/100 V ideal transformer supplies 20 A. Primary load current?

Answer: 5 A. The turns ratio is 4. Primary current is 20/4 = 5 A.

Voltage drops by 10% at fixed frequency. Approximate peak-flux change?

Answer: 10% decrease. Φm ∝ V/f; at fixed f the flux follows V.

An open-delta bank retains what fraction of the corresponding closed-delta capacity?

Answer: 57.7%. √3 S / (3S) = 1/√3 = 57.7%.