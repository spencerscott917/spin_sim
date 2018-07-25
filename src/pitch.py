"""My implementation of the complicated physics of ball flight. Built
from scratch, refs for physics to be added in writeups,"""


class Pitch(object):
    def __init__(self, v0, xy_spin):
        """Initialize a pitch, add more params as necessary
        Starting with simplest model, add more dimensions when
        code is working.
        Axes:
        x is positive from pitcher to catcher,
        y is positive to the pitcher's right,
        z is positive up."""
        # Velocity out of the pitcher's hand
        self.v0 = v0
        # spin in the xy plane, clockwise from top-down is positive.
        self.xy_spin = xy_spin
        # initialize pitch release as 0,0,0 (Change?)
        self.x = [0]
        self.y = [0]
        self.z = [0]

    def _update_pos(self, t, dt):
        """private method for updating position based on params
        dt is time since last time step"""
        x0 = self.x[-1]
        y0 = self.y[-1]
        z0 = self.z[-1]

        # need to account for drag, doing simplest implementation first
        # need to solve gravity equation properly, currently the ball falls
        # further and further as time resolution increases. SOLN: break v0
        # into component vectors
        x1 = x0 + self.v0*dt
        y1 = y0
        z1 = z0 - 0.5*9.81*t**2

        self.x.append(x1)
        self.y.append(y1)
        self.z.append(z1)

    def throw(self, dt):
        """the main simulation portion of the code"""
        t = 0
        # 18.44 is distance from mound to plate in meters
        while self.x[-1] <= 18.44:
            self._update_pos(t, dt)
            t += dt
        # make trajectory a copy of the lists so reset doesn't erase results
        trajectory = [self.x[:], self.y[:], self.z[:]]
        # reset coordinates for new run
        self.x = [0]
        self.y = [0]
        self.z = [0]
        return trajectory
