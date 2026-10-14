# Estimation, Wiring & Earthing

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

## Worked models (original)

### Motor current

A three-phase motor gives 8 kW at η = 0.8 and pf = 0.8 on 400 V.

Input = 10 kW; current = 10000/(√3×400×0.8) ≈ 18.0 A.

### Markup vs margin

Material cost 1000, labour 500; quote includes 20% markup on this cost.

Total cost = 1500; price = 1800. Profit margin is 300/1800 = 16.7%.

## Practice (original)

Protective earth is intended to:

Answer: Provide a protective connection for exposed metal. It forms part of a coordinated protective system.

Motor shaft output divided by efficiency gives:

Answer: Input electrical power. η = Pout/Pin.

Connected load equals:

Answer: Sum of installed load ratings. Maximum demand depends on how loads are used together.