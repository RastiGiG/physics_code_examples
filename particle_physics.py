from scipy import constants

def possible_flavors():
    return["up", "down", "top", "bottom", "strange", "charm"]

class Particle(object):
    """A particle is a constituent unit of the universe.

    Attributes
    ----------
    c : charge in units of [c] = e
    m : mass in units of [m] = kg
    r : postition in units of [r] = m"""

    roar = "I am a particle!"

    def __init__(self, charge, mass, position):
        """Initializes the particle with default values for charge c, mass m and position r."""
        self.c = charge
        self.m = mass
        self.r = position

    def hear_me(self):
        myroar = self.roar + (
            " My charge is:     " + str(self.c) +
            " My mass is:       " + str(self.m) +
            " My x position is: " + str(self.r['x']) +
            " My y position is: " + str(self.r['y']) +
            " My z position is: " + str(self.r['z']))
        print(myroar)

    def delta_x_min(self, delta_p_x):
        hbar = constants.hbar
        delx_min = hbar / (2.0 * delta_p_x)
        return delx_min

    @staticmethod
    def possible_flavors():
        return["up", "down", "top", "bottom", "strange", "charm"]
