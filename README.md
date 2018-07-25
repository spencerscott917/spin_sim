# spin_sim
A numerical simulation of the effect of spin on the trajectory of a ball. 

Main code is found in the src/ directory. The code relies on Pitch objects with various parameters, to be expanded on as simulation gets more realistic. Current implementation only simulates effect of initial velocity and gravity. 

Define a Pitch object with its initial velocity and spin in the x-y plane (dummy parameter at this point, not used except by __init__(). To simulate a pitch, use Pitch.throw, and specify a timestep.
