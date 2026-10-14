# Electric Traction & Drives

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

## Worked models (original)

### Schedule speed

10 km run takes 12 minutes plus a 3-minute stop.

Running average = 50 km/h. Schedule speed = 10/(15/60) = 40 km/h.

### Wheel power

Tractive effort 10 kN at 36 km/h.

36 km/h = 10 m/s; wheel power = 100 kW.

## Practice (original)

Area under a speed-time curve represents:

Answer: Distance. Distance is the time integral of speed.

Regenerative braking sends energy to:

Answer: Supply or receptive storage. Electrical conversion returns useful energy if the receiving system allows it.

Schedule speed compared with running average when stops exist is:

Answer: Lower. The same distance is divided by a longer total time.