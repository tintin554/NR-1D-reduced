# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:43:29 2021

@author: Adam
"""


'''
Plotting NR data from ILL 1D data Jun21

'''



import numpy as np
import matplotlib.pyplot as plt
import pickle

import refnx
from refnx.analysis import Objective


filename_unox = '731130_731129.dat'
filename_ox = '731150_731151.dat'

data_unox = np.genfromtxt(filename_unox)
data_ox = np.genfromtxt(filename_ox)

plt.figure(figsize=(6,4))
plt.errorbar(data_unox[:,0],data_unox[:,1],yerr=data_unox[:,2],linestyle='none',marker='o',ms=5,mfc='w',label='Unoxidised\n82 % RH')
plt.errorbar(data_ox[:,0],data_ox[:,1],yerr=data_ox[:,2],linestyle='none',marker='o',ms=5,mfc='w',mec='r',label='Oxidised\n82 % RH')
plt.yscale('log')
plt.xscale('log')
plt.legend(fancybox=False,framealpha=1,edgecolor='k',loc='lower left')
plt.ylabel('R(Q)',fontsize='large')
plt.xlabel('Q / Å$^{-1}$',fontsize='large')
plt.tight_layout()
#plt.savefig('1D_NR_highRH_ox_unox.svg')
plt.show()