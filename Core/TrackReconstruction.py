import random as rn
import math as math
from Core.Particle import Particle
from Core.Track import Track



class TrackReconstruction:

    def __init__(self, nlayers, trackersize, resolution):

        self.nlayers = nlayers
        self.trackersize = trackersize
        self.resolution = resolution
        self.rdet = []
        for i in range(0, nlayers):
            self.rdet.append((i+1) * (trackersize / nlayers))

    def runEvent(self, particles):

        tracks = []
        for i in particles:
            tracks.append(self.produceTrack(i)) 
        return tracks

    def produceTrack(self, particle):
	    
        simhits = self.getSimHits(particle)
        smearedsimhits = self.smearSimHits(simhits)
        track = self.fitTrack(smearedsimhits, particle)
        return track

    def fitTrack(self, simhits, particle):

        xmean = 0
        ymean = 0
        x2mean = 0
        xymean = 0
        for i in simhits:
            xmean += i[0]
            ymean += i[1]
            x2mean += i[0]*i[0]
            xymean += i[0]*i[1]
        xmean /= len(simhits)
        ymean /= len(simhits)
        x2mean /= len(simhits)
        xymean /= len(simhits)
        b = (xymean - xmean * ymean)/(x2mean - xmean * xmean)
        a = (ymean - b * xmean)
        phi = math.atan(b)
        y0 = a / (b * b + 1.0)
        x0 = -b * y0
        track = Track(x0, y0, phi, simhits, particle.p, particle.x0, particle.y0, particle.phi, particle.pid)
        return track                
        

    def smearSimHits(self, simhits):

        smearedSimHits = []
        for i in simhits:
            r = math.sqrt(i[0] * i[0] + i[1] * i[1])
            phi = math.atan2(i[1], i[0])
            phires = self.resolution / r
            ranphi = rn.gauss(0, phires)
            x = r * math.cos(phi + ranphi)
            y = r * math.sin(phi + ranphi) 
            smearedSimHits.append([x, y])
        return smearedSimHits

    def getSimHits(self, particle):

        simhits = []
        x0 = particle.x0
        y0 = particle.y0
        phi = particle.phi
        a = math.tan(phi)
        b = y0 - x0 * a
        for i in self.rdet:
            xcross = self.intersection(a, b, i)
            point1 = [xcross[0], a * xcross[0] + b]
            point2 = [xcross[1], a * xcross[1] + b]
            if (xcross[0] - x0)/math.cos(phi) < 0:
                simhits.append(point2)
            else: 
                simhits.append(point1)
        return simhits
        
    def intersection(self, a, b, r):
        
        aterm = (1.0 + a * a)
        bterm = (2.0 * a * b)
        cterm = (b * b - r * r)
        x1 = (-bterm + math.sqrt(bterm * bterm - 4.0 * aterm * cterm))/(2.0*aterm)
        x2 = (-bterm - math.sqrt(bterm * bterm - 4.0 * aterm * cterm))/(2.0*aterm)
        return [x1, x2]

    

