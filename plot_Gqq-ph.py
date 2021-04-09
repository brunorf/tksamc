#!/usr/bin/env python
#coding: utf8

import matplotlib.pyplot as plt
__description__ = \
    """
Charge-charge energy calculation in python
"""

__author__ = "Dr. Vinícius Contessoto"
__date__ = "21/12/2016"

################################################################
# TKSA em python - faz tudo sem precisar do bash
#
# Try to rewrite in python way by Vinícius Contessoto
# start 30/09/2015
#
# Nesta versão, faz a leitura em python mas roda em c++
#
# python pulo_do_gato.py PDB.pdb
#
# Need to install some bib from python
################################################################

import sys
import numpy as np
import scipy as sc
import subprocess
import os
import argparse
import time
import matplotlib
matplotlib.use('agg')

parser = argparse.ArgumentParser(description='Plot dGqq vs pH in python')
parser.add_argument('-f', metavar='input-file-Gqq-ph',
                    help='insert dGqq-ph file', type=argparse.FileType('rt'))

try:
    arguments = parser.parse_args()

except IOError as msg:
    parser.error(str(msg))


def main():

    file_plot = arguments.f

    plot_data = []
    for line in file_plot:  # Calculando a SASA
        list1 = line.split()
        plot_data.append(list1)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    X = np.asarray([i[0] for i in plot_data]).astype(np.float)
    Y = np.asarray([i[1] for i in plot_data]).astype(np.float)

    plt.plot(X, Y, '-o', markersize=10, linewidth=2.5)
    ax.tick_params('both', length=5, width=2.5, which='major', labelsize=15)
    plt.setp(ax.spines.values(), linewidth=2)
    plt.xticks(np.arange(min(X)-1.0, max(X)+2.0, 1.0))

    plt.xlabel(r'pH', fontsize=20)
    plt.ylabel(r'$\Delta G_{elec}$(kJ/mol)', fontsize=20)
    plt.subplots_adjust(left=0.16, right=0.84, bottom=0.2, top=0.95)
    fig.savefig('Fig_Gqq-pH_' + os.path.splitext(arguments.f.name)
                [0]+'.jpg', dpi=300)


if __name__ == "__main__":
    main()
