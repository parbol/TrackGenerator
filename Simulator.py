import numpy as np
import matplotlib.pyplot as plt
import random as rn
import math
from optparse import OptionParser





def de



def generateTracks(numberofjets):

    if numberofjets == 0:
        pt = 0
    else:
        pt = rn.expovariate(-1.0/2.0) * 10
    








if __name__ == "__main__":


    parser = OptionParser(usage="%prog --help")
    parser.add_option("-n", "--nevents",   dest="nevents",      type="int",      default=1000,         help="Number of events to simulate.")
    parser.add_option("-l", "--nlayers",   dest="nlayers",      type="int",      default=10,           help="Number of layers in the tracker.")
    parser.add_option("-s", "--size",      dest="trackersize",  type="float",    default=100,          help="Size (radius) of the tracker.")
    parser.add_option("-j", "--njets",     dest="numberofjets", type="int",      default=1,            help="Number of jets.")
    (options, args) = parser.parse_args()

    nevents = options.nevents
    nlayers = options.nlayers
    trackersize = options.trackersize
    numberofjets = options.numberofjets


    for i in range(0, nevents):

        tracks = generateTracks(numberofjets)





