import random as rn
import math as math
from Core.Particle import Particle



class Generator:

    def __init__(self, njets):

        self.njets = njets

    def runEvent(self):

        if self.njets == 0:
            pt = 0
            Zboson = particle(pt, rn.Uniform(0, 2.0*3.1416), 0, 0, 91)
        else:
            pt = rn.expovariate(-1.0/2.0) * 10
        


        

    def decayParticle(self, mom, childmass):
        
        p1x = mom.p * rn.Uniform(0.05, 0.095)
        p2x = mom.p - p1x
        py = math.sqrt( (mom.E * mom.E + p1x * p1x - p2x * p2x) / (4.0*mom.E*mom.E) - p1x * p1x - childmass * childmass)
        phi1 = mom.phi + math.atan(py/p1x)
        phi2 = mom.phi + math.atan(-py/p2x)
        p1 = math.sqrt(p1x * p1x + py * py) 
        p2 = math.sqrt(p2x * p2x + py * py) 
        particle1 = Particle(p1, phi1, mom.x0, mom.y0, childmass)
        particle2 = Particle(p2, phi2, mom.x0, mom.y0, childmass)
        return [particle1, particle2]


                 


