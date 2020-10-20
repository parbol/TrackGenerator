import random as rn
import math as math







class Track:

    def __init__(self, x0, y0, phi, simhits, genpt, genx0, geny0, genphi, pid):

        self.phi = phi
        self.x0 = x0
        self.y0 = y0
        self.simhits = simhits
        self.genx0 = genx0
        self.geny0 = geny0
        self.genphi = math.acos(math.cos(genphi))
        self.pid = pid
        self.genpt = genpt

    def print(self, tag):
        print('----Track----')
        print ('[' + tag + '] x0: ' + str(self.x0) + ' y0: ' + str(self.y0) + ' phi: ' + str(self.phi) + ' xgen: ' + str(self.genx0) + ' ygen: ' + str(self.geny0) + ' phigen: ' + str(self.genphi))
        for i in self.simhits:
            print('Hit: (' + str(i[0]) + ', ' + str(i[1]) + '), r: ' + str(math.sqrt(i[0]*i[0]+i[1]*i[1])) + ' phi: ' + str(math.atan2(i[1],i[0])))
 
        
        
 
