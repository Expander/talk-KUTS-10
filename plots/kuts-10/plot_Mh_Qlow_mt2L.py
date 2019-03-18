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

    Qlow             = data[:,0]
    mt       		 = data[:,1]
    mtasat    	     = data[:,2]
    mtat2      		 = data[:,3]
    mtasatat2        = data[:,4]
    # DMhQmatch   = data[:,5]
    # DMhytMSSM   = data[:,6]

    # DMh = DMhQpole + DMhytSM + DMhEFT + DMhQmatch + DMhytMSSM

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

    plt.plot(Qlow, mt, 'k:', linewidth=1.0)
    plt.plot(Qlow, mtasat, 'b-.', linewidth=1.0)
    plt.plot(Qlow, mtat2, 'g--' , linewidth=1.0)
    plt.plot(Qlow, mtasatat2, 'r-' , linewidth=1.0)
    # plt.plot(MS, DMhytMSSM , 'g:' , linewidth=1.0)
    # plt.plot(MS, DMhEFT    , 'g:' , linewidth=1.0)
    # plt.plot(MS, DMhytSMflvsSp , linewidth=1.0, color='orange', dashes=(2,1,2,3))
    # plt.plot(MS, DMhEFT    , linewidth=1.0, color='darkred', dashes=(1,1,1,1,3,1))

    leg = plt.legend([r'$\mathcal{O}(\alpha_s^2)$',
                      r'$\mathcal{O}(\alpha_s^2+\alpha_s\alpha_t)$',
                      r'$\mathcal{O}(\alpha_s^2+\alpha_t^2)$',
                      r'$\mathcal{O}(\alpha_s^2+\alpha_s\alpha_t+\alpha_t^2)$'],
                     loc='best', fontsize=9, fancybox=None, framealpha=None)
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

plot(arg1, arg2, r'$M_S=5\, \mathrm{TeV}, X_t = -\sqrt{6}M_S, \tan\beta = 20$', r'$M_h(m_t(Q_\text{low}))/\,\mathrm{GeV}$', [126.4,127], [45,176])
