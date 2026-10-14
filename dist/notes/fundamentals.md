# Electrical Fundamentals & Storage

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

## Worked models (original)

### Wire stretching

A wire doubles in length at constant volume.

Area halves; R₂/R₁ = 2/(1/2) = 4.

### Stored energy

A 20 μF capacitor is charged to 100 V.

W = 0.5×20×10⁻⁶×100² = 0.1 J.

### Time constant

A 10 kΩ resistance charges 100 μF.

τ = 10⁴×10⁻⁴ = 1 s. At 1 s, 63.2% of the final voltage change is complete.

## Practice (original)

Five 20 Ω resistors in parallel give:

Answer: 4 Ω. R/n = 20/5 = 4 Ω.

An ideal inductor preserves which quantity at ordinary switching?

Answer: Current. Inductor current is continuous unless there is an impulse voltage.

2 kW used for 3 hours consumes:

Answer: 6 kWh. Energy = power × time = 6 kWh.