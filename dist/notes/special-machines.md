# Special & Fractional Motors

## Select by the task
A servo is part of a controlled system: feedback compares actual position or speed with the command and drives the error down. “Servo” describes a controlled application, not one single winding construction. DC, AC synchronous and other motor types can form servo systems. Low inertia improves rapid response; a suitable torque-speed curve and controller determine performance.

A stepper moves through discrete increments in response to pulses. Pulse count gives commanded position and pulse rate gives commanded speed. An open-loop stepper can lose steps if overloaded; command count is not proof that the shaft reached the intended position. Holding torque refers to torque with the motor energised and stationary; detent torque can exist without current for some permanent-magnet designs.

$$ \theta_{step}=360^\circ/N_{steps},\quad N_{rpm}=60 f_{pulse}/N_{steps} $$

Variable-reluctance steppers seek minimum reluctance; permanent-magnet steppers use a magnetised rotor; hybrid motors combine features. Use the geometry-specific step-angle equation only when its pole/tooth arrangement is supplied. The generic steps-per-revolution equation is safer than memorising one tooth formula for all designs.

## Universal and small motors
A universal motor is a suitably designed series commutator motor capable of AC and DC operation. Field and armature currents reverse together on AC, maintaining average torque direction. Laminations reduce AC core losses and design reduces reactance/commutation difficulty. It offers high speed and starting torque but brush wear and noise are drawbacks. It is not a synchronous motor.

A reluctance motor develops torque because the rotor seeks a low-reluctance alignment. A synchronous reluctance motor can run synchronously after appropriate starting. A hysteresis motor uses rotor hysteresis for smooth torque and can settle at synchronous speed. A shaded-pole induction motor gives modest starting torque, simple construction and a usual fixed direction determined by shading. A permanent-split-capacitor motor retains the run capacitor and avoids a centrifugal switch in that arrangement.

## Exam comparisons
For precision motion, ask whether feedback is present, how position is encoded and what happens during overload. For small appliances, compare starting torque, speed, brush maintenance and noise. A two-phase AC servomotor often uses a high-resistance rotor to obtain a useful stable torque-speed response. A brushless DC motor uses electronic commutation; it does not have a mechanical commutator even though its name contains DC.

Fractional-horsepower simply describes a power class below one horsepower, not a unique motor principle. Its units matter: approximately 746 W equals one mechanical horsepower. Choose motor construction from the physical principle, not from the size label alone.

## Worked models (original)

### Pulse count and speed

A 1.8° stepper receives 1000 pulses/s, one full step per pulse.

200 steps/rev. Speed = 60×1000/200 = 300 rpm; 50 pulses command 90°.

### Open-loop error

A stepper is commanded 100 steps but stalls for 10.

The command counter still says 100. Without suitable feedback or homing, the controller may not know actual position.

## Practice (original)

A 0.9° full-step motor requires how many pulses per revolution?

Answer: 400. 360/0.9 = 400.

Which motor uses electronic commutation?

Answer: BLDC. BLDC uses switches controlled by rotor-position information.

The main defining feature of a servo system is:

Answer: Feedback control. A servo compares measured response to a commanded value.