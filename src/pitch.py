import numpy as np

class Pitch(object):
    def __init__(self, v0, x_spin, z_spin):
        """Initialize a pitch, add more params as necessary"""
        # Starting with simplest model, add more dimensions when
        # code is working.
        # Velocity out of the pitcher's hand
        self.v0 = v0
        self.x_spin = x_spin
