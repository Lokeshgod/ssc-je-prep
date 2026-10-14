# Magnetic Circuits & Coupled Coils

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

## Worked models (original)

### Two inductance measurements

Series aiding gives 18 mH; opposing gives 10 mH.

M = (18−10)/4 = 2 mH. Also L₁+L₂ = 14 mH.

### Coupling limit

L₁ = 4 H and L₂ = 9 H.

Maximum M = √36 = 6 H. Any value above 6 H violates k ≤ 1.

## Practice (original)

Aiding is 12 H and opposing is 4 H. Mutual inductance?

Answer: 2 H. Their difference is 4M, so M = 2 H.

Air-gap flux spreading is called:

Answer: Fringing. Fringing increases the effective gap area.

Lenz law is consistent with conservation of:

Answer: Energy. The induced effect opposes its cause rather than creating free energy.