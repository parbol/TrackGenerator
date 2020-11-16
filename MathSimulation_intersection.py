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
    parser.add_option("-d", "--deltaphi",         dest="deltaphi",     type="float",    default=1.5,          help="Deltaphi")
    (options, args) = parser.parse_args()

    nevents = options.nevents
    nlayers = options.nlayers
    trackersize = options.trackersize
    resolution = options.resolution
    deltaphi = options.deltaphi

    #Init random number generator
    rn.seed(2)

    #Covariance matrix 
    x = []
    for i in range(nlayers):
        x.append((trackersize/nlayers)*(i+1))
    xmean = 0
    x2mean = 0
    for j in x:
        xmean += j
        x2mean += j * j
    xmean /= len(x)
    x2mean /= len(x)
    x2mumean = 0
    for j in x:
        x2mumean += (j - xmean) * (j - xmean)
    res2 = resolution * resolution  
    cov = [ [res2 * x2mean / x2mumean, - res2 * xmean / x2mumean], [- res2 * xmean / x2mumean, res2 / x2mumean] ]
    phi = 0
    mu = [math.tan(phi), 0]
   
    #Running 
    x0 = []
    y0 = []
    x02 = []
    y02 = []
    xc = []
    yc = []

    for i in range(nevents):
        x = np.random.multivariate_normal(mu, cov) # recta 1
        x2 = np.random.multivariate_normal(mu, cov) # recta 2
        rotx2 = [0, 0] # recta 2 rotada
        rotx2[0] = (x2[0]*math.cos(deltaphi) + math.sin(deltaphi))/(math.cos(deltaphi) - x2[0]*math.sin(deltaphi))
        rotx2[1] = x2[1]/(math.cos(deltaphi)-x2[0]*math.sin(deltaphi)) 

        xi = 0 #intersection
        yi = 0

        xi = - (x[1]-rotx2[1])/(x[0] - rotx2[0])
        yi = (x[0]*rotx2[1] - rotx2[0]*x[1])/(x[0] - rotx2[0])

        xc.append(xi)
        yc.append(yi)

 
    """
    fig = plt.figure(figsize = (5,5))
    plt.xlim(-0.02, 0.02)
    plt.ylim(-0.02, 0.02)
    plt.title('Position of the two 2-tracks system vertex')
    plt.xlabel('x [cm]')
    plt.ylabel('y [cm]')
    plt.plot(xc, yc, '.', color='r')
    plt.arrow(0.02/2.0 * math.cos(phi), 0.02/2.0 * math.sin(phi), 1.0*0.02/4.0 * math.cos(phi), 1.0*0.02/4.0 * math.sin(phi), color='b',  width=0.0001)
    plt.arrow(0.02/2.0 * math.cos(phi+deltaphi), 0.02/2.0 * math.sin(phi+deltaphi), 1.0*0.02/4.0 * math.cos(phi+deltaphi), 1.0*0.02/4.0 * math.sin(phi+deltaphi), color='g', width=0.0001)
    plt.tight_layout()
    plt.savefig("TwoTracksCombined.png")
    """

    fig = plt.figure(figsize = (6,6))
    ax = plt.axes(xlim = (-0.02, 0.02), ylim = (-0.02, 0.02), xlabel = 'x (cm)', ylabel = 'y (cm)')
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
    ax.xaxis.major.formatter._useMathText = True
    ax.yaxis.major.formatter._useMathText = True
    ax.text(0.05, 0.20, '2-Track fitting simulator', horizontalalignment='left', verticalalignment='center', transform=ax.transAxes, weight = 'bold')
    ax.text(0.05, 0.15, 'Number of trials: '+str(options.nevents), horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)
    ax.text(0.05, 0.1, 'Hit resolution: '+str(options.resolution), horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)
    ax.text(0.05, 0.05, r'Angular separation $\Delta\varphi$ = '+str(deltaphi), horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)
    ax.plot(xc, yc, '.', color='r')
    ax.arrow(0.02/2.0 * math.cos(phi), 0.02/2.0 * math.sin(phi), 1.0*0.02/4.0 * math.cos(phi), 1.0*0.02/4.0 * math.sin(phi), color='b',  width=0.0001, head_width = 0.001)
    ax.arrow(0.02/2.0 * math.cos(phi+deltaphi), 0.02/2.0 * math.sin(phi+deltaphi), 1.0*0.02/4.0 * math.cos(phi+deltaphi), 1.0*0.02/4.0 * math.sin(phi+deltaphi), color='g', width=0.0001, head_width = 0.001)
    fig.savefig("TwoTracksCombined_dphi.png")








 
 


