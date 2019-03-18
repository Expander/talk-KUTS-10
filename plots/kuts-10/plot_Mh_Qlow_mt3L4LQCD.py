#!/usr/bin/env python
#python plotting script for Fig 2: individual sources of uncertainty in HSSUSY

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import matplotlib.patches as patches
import scipy.interpolate

def plot(datafile, outfile, title, label_y, range_y, range_x):
    plt.rcParams['text.usetex'] = True
    plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

    try:
        data  = np.genfromtxt(datafile)
    except:
        print "Error: could not load numerical data from file"
        exit

    Qlow              = data[:,0]
    mtas2             = data[:,1]
    mtas2as3          = data[:,2]
    mtas2as4    	  = data[:,3]
    mtas2as3as4       = data[:,4]


    plt.rc('text', usetex=True)
    plt.rc('font', family='serif', weight='normal')
    fig = plt.figure(figsize=(7,4))
    plt.gcf().subplots_adjust(bottom=0.15, left=0.15) # room for xlabel
    ax = plt.gca()
    ax.set_axisbelow(True)
    ax.xaxis.set_major_formatter(tck.FormatStrFormatter(r'$%g$'))
    ax.yaxis.set_major_formatter(tck.FormatStrFormatter(r'$%g$'))
    ax.get_yaxis().set_tick_params(which='both',direction='in')
    ax.get_xaxis().set_tick_params(which='both',direction='in')
    plt.grid(color='0.5', linestyle=':', linewidth=0.2, dashes=(0.5,1.5))

    #plt.xscale('log')
    plt.xlabel(r'$Q_\text{low}\,/\,\mathrm{GeV}$')
    plt.ylabel(label_y)
    plt.title(title)

    plt.plot(Qlow, mtas2, 'k:', linewidth=1.0)
    plt.plot(Qlow, mtas2as3, 'b-.', linewidth=1.0)
    plt.plot(Qlow, mtas2as4, 'g--', linewidth=1.0)
    plt.plot(Qlow, mtas2as3as4, 'r-', linewidth=1.0)

    leg = plt.legend([r'$\mathcal{O}(\alpha_s^2)$',
                      r'$\mathcal{O}(\alpha_s^2+\alpha_s^3)$',
                      r'$\mathcal{O}(\alpha_s^2+\alpha_s^4)$',
                      r'$\mathcal{O}(\alpha_s^2+\alpha_s^3+\alpha_s^4)$'],
                     loc='lower right', fontsize=9, fancybox=None, framealpha=None)
    leg.get_frame().set_alpha(1.0)
    leg.get_frame().set_edgecolor('black')
    plt.ylim(range_y)
    plt.xlim(range_x)

    plt.savefig(outfile)
    print "saved plot in ", outfile
    plt.close(fig)



import sys
arg1 = sys.argv[1]
arg2 = sys.argv[2]

# plot(datafile, outfile, title, label_y, range_y, range_x):

plot(arg1, arg2, r'$M_S=5\, \mathrm{TeV}, X_t = -\sqrt{6}M_S, \tan\beta = 20$', r'$M_h(m_t(Q_\text{low}))/\,\mathrm{GeV}$', [125.8,127], [45.59,182.38])
