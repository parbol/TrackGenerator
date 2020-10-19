import numpy as np
import matplotlib.pyplot as plt
import random as rn
import math
from optparse import OptionParser
from Core.Generator import Generator








if __name__ == "__main__":


    parser = OptionParser(usage="%prog --help")
    parser.add_option("-n", "--nevents",          dest="nevents",      type="int",      default=1000,         help="Number of events to simulate.")
    parser.add_option("-l", "--nlayers",          dest="nlayers",      type="int",      default=10,           help="Number of layers in the tracker.")
    parser.add_option("-s", "--size",             dest="trackersize",  type="float",    default=100,          help="Size (radius) of the tracker.")
    parser.add_option("-j", "--jetthreshold",     dest="jetthreshold", type="float",    default=1.5,          help="Jet threshold")
    (options, args) = parser.parse_args()

    nevents = options.nevents
    nlayers = options.nlayers
    trackersize = options.trackersize
    jetthreshold = options.jetthreshold

    gen = Generator(jetthreshold)

    k = gen.runEvent()

    print(k)






