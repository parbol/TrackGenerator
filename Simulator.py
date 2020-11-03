import numpy as np
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import random as rn
import math
from optparse import OptionParser
from Core.Generator import Generator
from Core.TrackReconstruction import TrackReconstruction
from Core.Vertex import Vertex








if __name__ == "__main__":


    parser = OptionParser(usage="%prog --help")
    parser.add_option("-n", "--nevents",          dest="nevents",      type="int",      default=1000,         help="Number of events to simulate.")
    parser.add_option("-l", "--nlayers",          dest="nlayers",      type="int",      default=10,           help="Number of layers in the tracker.")
    parser.add_option("-s", "--size",             dest="trackersize",  type="float",    default=100,          help="Size (radius) of the tracker.")
    parser.add_option("-r", "--resolution",       dest="resolution",   type="float",    default=0.1,          help="Tracker resolution.")
    parser.add_option("-j", "--jetthreshold",     dest="jetthreshold", type="float",    default=1.5,          help="Jet threshold")
    (options, args) = parser.parse_args()

    nevents = options.nevents
    nlayers = options.nlayers
    trackersize = options.trackersize
    resolution = options.resolution
    jetthreshold = options.jetthreshold

    rn.seed(2)
    
    gen = Generator(jetthreshold)
    reco = TrackReconstruction(nlayers, trackersize, resolution)
    vertex = Vertex()

    phileptonval = []
    phival = []
    x0lepton = []
    y0lepton = []
    x0full = []
    y0full = []
    pt = []
    for nevent in range(0, nevents):
        genparticles = gen.runEvent()
        #for i in genparticles:
        #    i.print('particle') 
        recotracks = reco.runEvent(genparticles)

        #Select leptons    
        leptontracks = []
        othertracks = []
        for i in recotracks:
            if i.pid == 1:
                leptontracks.append(i)
            else:
                othertracks.append(i)
        fullvertex = vertex.fit(othertracks)
        leptonvertex = vertex.fit(leptontracks) 
        
        philepton = abs(leptontracks[0].phi - leptontracks[1].phi)
        pZ = [leptontracks[0].genpt * math.cos(leptontracks[0].phi) + leptontracks[1].genpt * math.cos(leptontracks[1].phi), leptontracks[0].genpt * math.sin(leptontracks[0].phi) + leptontracks[1].genpt * math.sin(leptontracks[1].phi)]    
        vdisp = [leptonvertex[0] - fullvertex[0], leptonvertex[1] - fullvertex[1]]
        pZnorm = [pZ[0] / math.sqrt(pZ[0]*pZ[0] + pZ[1]*pZ[1]), pZ[1] / math.sqrt(pZ[0]*pZ[0] + pZ[1]*pZ[1])]
        vdispnorm = [vdisp[0] / math.sqrt(vdisp[0]*vdisp[0] + vdisp[1]*vdisp[1]), vdisp[1] / math.sqrt(vdisp[0]*vdisp[0] + vdisp[1]*vdisp[1])]
        phi = math.acos(pZnorm[0] * vdispnorm[0] + pZnorm[1] * vdispnorm[1])
        phileptonval.append(philepton)
        phival.append(phi)
        x0lepton.append(leptonvertex[0])
        y0lepton.append(leptonvertex[1])
        x0full.append(fullvertex[0])
        y0full.append(fullvertex[1])
        pt.append(math.sqrt(pZ[0]*pZ[0] + pZ[1]*pZ[1]))

    thept = np.asarray(pt)
    thephi = np.asarray(phival)
    thephilepton = np.asarray(phileptonval)
    thex0lepton = np.asarray(x0lepton)
    they0lepton = np.asarray(y0lepton)
    thex0full = np.asarray(x0full)
    they0full = np.asarray(y0full)
    fig = plt.figure(figsize = (5,5))
    plt.hist(thephi, bins=50)
    plt.savefig("colinearity.png")
    fig2 = plt.figure(figsize = (5,5))
    #plt.xlim(-0.1, 0.1)
    #plt.ylim(-0.1, 0.1)
    plt.hist2d(thex0lepton, they0lepton, range = [[-0.025, 0.025], [-0.025, 0.025]], bins=100)
    plt.savefig("vertexLepton.png")
    fig3 = plt.figure(figsize = (5,5))
    #plt.xlim(-0.1, 0.1)
    #plt.ylim(-0.1, 0.1)
    plt.hist2d(thex0full, they0full, range = [[-0.025, 0.025], [-0.025, 0.025]], bins=100)
    plt.savefig("vertexFull.png") 
    fig4 = plt.figure(figsize = (5,5))
    #plt.xlim(-0.1, 0.1)
    #plt.ylim(-0.1, 0.1)
    plt.hist2d(thephi, thephilepton, range = [[0.0, 3.2], [0.0, 3.2]], bins=100, norm=colors.SymLogNorm(linthresh=0.03, linscale=0.03, vmin=-1.0, vmax=1.0)) 
    plt.savefig("phiVsPhi.png") 
    fig5 = plt.figure(figsize = (5,5))
    #plt.xlim(-0.1, 0.1)
    #plt.ylim(-0.1, 0.1)
    plt.hist(thept, bins=100)
    plt.savefig("pt.png") 



