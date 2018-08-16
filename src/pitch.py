"""My implementation of the complicated physics of ball flight. Built
from scratch, refs for physics to be added in writeups"""

# TODO: - euler's method
#       - see what Pitch f/x data are available to be able to use in
#         simulation. GOAL: use only the data currently provided.
#       - look at using Pitch f/x data as a calibration tool


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
        # TODO: split this into component vectors
        self.v0 = v0

        # spin in the xy plane, clockwise from top-down view is positive.
        self.xy_spin = xy_spin

        # initialize pitch release as 0,0,0 (Change?)
        self.x = [0]
        self.y = [0]
        self.z = [0]

    def _update_pos(self, t, dt):
        """private method for updating position based on params
        dt is time since last time step"""
        # x0 = self.x[-1]
        # y0 = self.y[-1]
        # z0 = self.z[-1]

        # need to account for drag, doing simplest implementation first
        # SOLN: break v0 into component vectors
        # implement euler's method for Diff Eq solver (or something
        # more computationally efficient)
        x1 = self.x[0] + self.v0*t
        y1 = self.y[0]
        z1 = self.z[0] - 0.5*9.81*t**2

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
