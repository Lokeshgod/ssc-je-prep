# Circuit Laws & Network Theorems

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

## Worked models (original)

### Thevenin load

Vth = 24 V, Rth = 4 Ω, RL = 8 Ω.

IL = 24/12 = 2 A; PL = 2²×8 = 32 W.

### Matched load

Vth = 20 V, Rth = 5 Ω.

For maximum load power choose RL = 5 Ω. Pmax = 400/20 = 20 W.

### Power is not additive

Separate sources produce 2 A and 3 A in the same direction through 1 Ω.

Net current is 5 A; net power is 25 W, not 4+9 = 13 W.

## Practice (original)

When finding Rth, an independent ideal current source becomes:

Answer: An open. Zero current through an ideal source corresponds to an open circuit.

Vth = 12 V, Rth = 3 Ω. Norton current?

Answer: 4 A. In = Vth/Rth = 4 A.

Which cannot be directly superposed?

Answer: Power. Power includes squared terms and cross-terms.