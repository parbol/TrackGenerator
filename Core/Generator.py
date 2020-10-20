import random as rn
import math as math
from Core.Particle import Particle



class Generator:

    def __init__(self, threshold):

        self.threshold = threshold
        self.quarkDecayMasses = [4.1, 2, 0.95, 0.45, 0.1]

    def runEvent(self):

        pt = 2 + rn.expovariate(-1.0/2.0) * 20
        phi = rn.uniform(0, 2.0*3.1416)
        Zboson = Particle(pt, phi, 0, 0, 91, 2)
        Quark = Particle(pt, phi + 3.1416, 0, 0, self.quarkDecayMasses[0], 0)
        listOfParticles = []
        leptons = self.decayParticle(Zboson, 0.1, 1)
        listOfParticles.append(leptons[0])
        listOfParticles.append(leptons[1])
        hadrons = self.hadronizeJet(Quark)
        particles = listOfParticles + hadrons
        
        return particles

    def hadronizeJet(self, quark):
	    
        listOfHadrons = self.splitQuark(quark)
        return listOfHadrons

    def splitQuark(self, quark):
	    
        listOfHadrons = []
        mass = self.quarkDecayMasses[0]
        success = 0
        for j in self.quarkDecayMasses:
            if quark.m > j:
                mass = j
                success = 1
                break
        if not success:
            listOfHadrons.append(quark)
            return listOfHadrons
        else:
            for i in self.decayParticle(quark, mass, 0): 
                listOfHadrons = listOfHadrons + self.splitQuark(i)
        return listOfHadrons


    def decayParticle(self, mom, childmass, pid):

        angle = rn.uniform(0, 2.0*3.1416)
        Erest = mom.m / 2.0
        prest = math.sqrt(Erest*Erest - childmass * childmass)
        p1xrest = prest * math.cos(angle) 
        p1yrest = prest * math.sin(angle) 
        p2xrest = prest * math.cos(angle+3.1416) 
        p2yrest = prest * math.sin(angle+3.1416) 
        gamma = mom.E/mom.m
        beta = mom.p/mom.E
        E1boost = gamma * (Erest + beta * p1xrest)
        p1xboost = gamma * (p1xrest + beta * Erest)
        E2boost = gamma * (Erest + beta * p2xrest)
        p2xboost = gamma * (p2xrest + beta * Erest)
        p1 = math.sqrt(p1xboost*p1xboost + p1yrest*p1yrest) 
        p2 = math.sqrt(p2xboost*p2xboost + p2yrest*p2yrest) 
        phi1 = mom.phi + math.atan2(p1yrest, p1xboost)
        phi2 = mom.phi + math.atan2(p2yrest, p2xboost)
        particle1 = Particle(p1, phi1, mom.x0, mom.y0, childmass, pid)
        particle2 = Particle(p2, phi2, mom.x0, mom.y0, childmass, pid)
        return [particle1, particle2]


