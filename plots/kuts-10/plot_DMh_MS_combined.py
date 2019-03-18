#!/usr/bin/env python
#python plotting script for Fig 2: individual sources of uncertainty in HSSUSY

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import matplotlib.patches as patches
import scipy.interpolate

def plot(datafile, datafile2, datafile3, outfile, title, label_y, range_y, range_x):
    plt.rcParams['text.usetex'] = True
    plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

    try:
        data = np.genfromtxt(datafile)
        data2 = np.genfromtxt(datafile2)
        data3 = np.genfromtxt(datafile3)
    except:
        print "Error: could not load numerical data from file"
        exit

    MS          = data[:,0]
    Mh          = data[:,1]
    DMhQpole    = data[:,2]
    DMhQmatch   = data[:,3]
    DMhytSM     = data[:,4]
    DMhytMSSM   = data[:,5]
    DMhEFT      = data[:,6]
    FSpH        = data2[:,1]
    SSpH        = data3[:,1]
    DSS         = data3[:,2]

    DMh = DMhQpole + DMhytSM + DMhEFT + DMhQmatch + DMhytMSSM

    MhpDMh = Mh + DMh
    MhmDMh = Mh - DMh

    SSpDFS = SSpH + DSS
    SSmDFS = SSpH - DSS

    Mhplus = 125.41
    Mhminus =124.77

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif', weight='normal')
    fig = plt.figure(figsize=(4,4))
    plt.gcf().subplots_adjust(bottom=0.15, left=0.15) # room for xlabel
    ax = plt.gca()
    ax.set_axisbelow(False)
    ax.xaxis.set_major_formatter(tck.FormatStrFormatter(r'$%g$'))
    ax.yaxis.set_major_formatter(tck.FormatStrFormatter(r'$%g$'))
    ax.get_yaxis().set_tick_params(which='both',direction='in')
    ax.get_xaxis().set_tick_params(which='both',direction='in')
    ax.text(540, 125.8, r'ATLAS/CMS $\pm 1 \sigma$', fontsize=7)
    plt.grid(color='0.5', linestyle='-', linewidth=0.2, dashes=(5,15))

    plt.xscale('log')
    plt.xlabel(r'$M_S\,/\,\mathrm{GeV}$')
    plt.ylabel(label_y)
    plt.title(title)

    plt.plot(MS, SSpH, 'r-' , linewidth=1.0)
    plt.plot(MS, FSpH, 'b--' , linewidth=1.0)
    plt.plot(MS, Mh, 'k:' , linewidth=1.0)
    plt.fill_between(MS, Mhplus, Mhminus, facecolor='darkorange', alpha=0.5)
    plt.fill_between(MS, SSpDFS, SSmDFS, facecolor='palevioletred', alpha=0.5)
    plt.fill_between(MS, MhmDMh, MhpDMh, facecolor='grey', alpha=0.5)
    # plt.plot(MS, DMhQmatch , 'b-.', linewidth=1.0)
    # plt.plot(MS, DMhytSM   , 'g:' , linewidth=1.0)
    # plt.plot(MS, DMhytMSSM , 'g:' , linewidth=1.0)
    # plt.plot(MS, DMhEFT    , 'g:' , linewidth=1.0)
    # plt.plot(MS, DMhytMSSM , linewidth=1.0, color='orange', dashes=(2,1,2,3))
    # plt.plot(MS, DMhEFT    , linewidth=1.0, color='darkred', dashes=(1,1,1,1,3,1))

    leg = plt.legend([r'\texttt{SS+H}',
                      r'\texttt{FS+H}',
                      r'\texttt{HSSUSY}'],
                     loc='lower right', fontsize=10, fancybox=None, framealpha=None)
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
arg3 = sys.argv[3]
arg4 = sys.argv[4]

plot(arg1, arg2, arg3, arg4, r'$X_t = -\sqrt{6}M_S, \tan\beta = 20$', r'$M_h\,/\,\mathrm{GeV}$', [112,135], [500,10000])
