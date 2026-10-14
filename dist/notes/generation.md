# Generation & Load Economics

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

## Worked models (original)

### Load factor

Energy over 10 h is 600 kWh; peak demand is 100 kW.

Average = 60 kW, so load factor = 0.6. Do not use connected load as the denominator.

### Capacitor kvar

A 100 kW load improves from 0.8 lagging to unity.

tanφ₁ = 0.6/0.8 = 0.75; Qc = 75 kvar.

## Practice (original)

Individual peaks total 500 kW; group peak is 400 kW. Diversity factor?

Answer: 1.25. 500/400 = 1.25.

An economiser primarily heats:

Answer: Feedwater. It recovers flue-gas heat into feedwater.

At fixed real power and voltage, improving pf reduces:

Answer: Supply current. I = P/(√3 VL pf) for balanced three-phase loads.