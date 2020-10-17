import random as rn
import math as math
import ROOT as 







class Track:

    def __init__(self, pt, phi, x0, y0):

        self.pt = pt
        self.phi = phi
        self.x0 = x0
        self.y0 = y0

    def decayTrack(self, M):
        
        E = math.sqrt(self.pt * self.pt + M * M)
        x = rn.uniform(0.05, 0.95)
        p1 = self.pt * x
        
        
 
