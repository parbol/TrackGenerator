import random as rn
import math as math
from Core.Particle import Particle
from Core.Track import Track



class Vertex:

    def __init__(self):

        self.id = 1

    def fit(self, tracks):
        x_vertex = 0
        y_vertex = 0
        pt2 = 0
        for i in tracks:
            x_vertex += i.x0 * i.genpt * i.genpt
            y_vertex += i.y0 * i.genpt * i.genpt
            pt2 += i.genpt * i.genpt
        x_vertex /= pt2    
        y_vertex /= pt2
        fullvertex = [x_vertex, y_vertex]
        return fullvertex



