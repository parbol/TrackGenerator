import random as rn
import math as math






class Particle:

    def __init__(self, pt, phi, x0, y0, m, pid):

        self.p = pt
        self.phi = math.acos(math.cos(phi))
        self.x0 = x0
        self.y0 = y0
        self.m = m
        self.E = math.sqrt(pt * pt + m * m)
        self.pid = pid

    def print(self, tag):

        print('[' + tag + '] id: ' + str(self.pid) + ' (' + str(self.E) + ', ' + str(self.p * math.cos(self.phi)) + ', ' + str(self.p * math.sin(self.phi)) + ')')
 
