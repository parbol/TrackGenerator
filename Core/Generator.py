import random as rn
import math as math
from Core.Particle import Particle



class Generator:

    def __init__(self, threshold):

        self.threshold = threshold

    def runEvent(self):

        pt = rn.expovariate(-1.0/2.0) * 20
        phi = rn.uniform(0, 2.0*3.1416)
        Zboson = Particle(pt, phi, 0, 0, 91)
        Quark = Particle(pt, phi + 3.1416, 0, 0, 1)
        listOfParticles = []
        leptons = self.decayParticle(Zboson, 0.1)
        listOfParticles.append(leptons[0])
        listOfParticles.append(leptons[1])
        hadrons = self.hadronizeJet(Quark)
        particles = listOfParticles + hadrons
        return particles


    def hadronizeJet(self, quark):
	    
        listOfHadrons = self.splitQuark(quark)


    def splitQuark(self, quark):
	    
        listOfHadrons = []
        for i in self.decayParticle(quark, 1.0):
            if i.E < self.thresnold:
                listOfHadrons.append(i)
        else:
            listOfHadrons = listOfHadrons + self.splitQuark(i)
        return listfHadrons


    def decayParticle(self, mom, childmass):
        
        
        p1x = mom.p * rn.uniform(0.05, 0.95)
        p2x = mom.p - p1x
        while ((mom.E * mom.E + p1x * p1x - p2x * p2x) * (mom.E * mom.E + p1x * p1x - p2x * p2x)) / (4.0*mom.E*mom.E) <= p1x * p1x + childmass * childmass:
            p1x = mom.p * rn.uniform(0.05, 0.95)
            p2x = mom.p - p1x
        py = math.sqrt( ((mom.E * mom.E + p1x * p1x - p2x * p2x) * (mom.E * mom.E + p1x * p1x - p2x * p2x)) / (4.0*mom.E*mom.E) - p1x * p1x - childmass * childmass)
        phi1 = mom.phi + math.atan(-py/p1x)
        phi2 = mom.phi + math.atan(py/p2x)
        p1 = math.sqrt(p1x * p1x + py * py) 
        p2 = math.sqrt(p2x * p2x + py * py) 
        particle1 = Particle(p1, phi1, mom.x0, mom.y0, childmass)
        particle2 = Particle(p2, phi2, mom.x0, mom.y0, childmass)
        mom.print('mom')
        particle1.print('child1')
        particle2.print('child2')
        return [particle1, particle2]


