#!/usr/bin/env python
#python plotting script for Fig 2: individual sources of uncertainty in HSSUSY

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import matplotlib.patches as patches
import scipy.interpolate

def plot(datafile, datafile2, outfile, title, label_y, range_y, range_x):
    plt.rcParams['text.usetex'] = True
    plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

    try:
        data  = np.genfromtxt(datafile)
        data2 = np.genfromtxt(datafile2)
    except:
        print "Error: could not load numerical data from file"
        exit

    MS               = data[:,0]
    DMhytrepr        = data[:,1]
    DMhytkorr        = data[:,2]
    DMhytSMfull      = data[:,3]
    DMhytSM4l        = data2[:,1]
    # DMhQmatch   = data[:,5]
    # DMhytMSSM   = data[:,6]

    # DMh = DMhQpole + DMhytSM + DMhEFT + DMhQmatch + DMhytMSSM

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif', weight='normal')
    fig = plt.figure(figsize=(4,4))
    plt.gcf().subplots_adjust(bottom=0.15, left=0.15) # room for xlabel
    ax = plt.gca()
    ax.set_axisbelow(True)
    ax.xaxis.set_major_formatter(tck.FormatStrFormatter(r'$%g$'))
    ax.yaxis.set_major_formatter(tck.FormatStrFormatter(r'$%g$'))
    ax.get_yaxis().set_tick_params(which='both',direction='in')
    ax.get_xaxis().set_tick_params(which='both',direction='in')
    plt.grid(color='0.5', linestyle=':', linewidth=0.2, dashes=(0.5,1.5))

    plt.xscale('log')
    plt.xlabel(r'$M_S\,/\,\mathrm{GeV}$')
    plt.ylabel(label_y)
    plt.title(title)

    plt.plot(MS, DMhytrepr , 'r-', linewidth=1.0)
    plt.plot(MS, DMhytkorr , 'b-.', linewidth=1.0)
    plt.plot(MS, DMhytSMfull   , 'g:' , linewidth=1.0)
    plt.plot(MS, DMhytSM4l       , 'b--' , linewidth=1.2)
    # plt.plot(MS, DMhytMSSM , 'g:' , linewidth=1.0)
    # plt.plot(MS, DMhEFT    , 'g:' , linewidth=1.0)
    # plt.plot(MS, DMhytSMflvsSp , linewidth=1.0, color='orange', dashes=(2,1,2,3))
    # plt.plot(MS, DMhEFT    , linewidth=1.0, color='darkred', dashes=(1,1,1,1,3,1))

    leg = plt.legend([r'2l-QCD vs. 3l-QCD',
                      r'2l-QCD vs. 3l-QCD-SM',
                      r'2l-complete vs. 3l-QCD-SM',
                      r'3l-QCD-SM vs. 4l-QCD-SM'],
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
arg3 = sys.argv[3]

# plot(datafile, outfile, title, label_y, range_y, range_x):

plot(arg1, arg2, arg3, r'$X_t = -\sqrt{6}M_S, \tan\beta = 20$', r'$\Delta M_h(y_t^\text{SM})/\,\mathrm{GeV}$', [0.269250,0.27], [500,505])
