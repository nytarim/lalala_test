# coding: utf-8

# In[12]:

import glob
import pandas as pd
import numpy as np
from os.path import dirname, splitext, basename, normpath, join as pjoin
from shutil import copyfile
import fileinput

# In[13]:

path_dat = 'T:/data/Archive/processed/Ryan_11315/Pilatus2_1m/0p6_1/reduced/SAXS/profiles/'
path_log = 'T:/data/Archive/processed/Ryan_11315/Pilatus2_1m/0p6_1/reduced/SAXS/'

# In[16]:

log = pjoin(dirname(path_log), 'livelogfile_edit.log')
dats = pjoin(dirname(dirname(path_dat)), 'raw_dats')
print(log, dats)

# In[ ]:

with fileinput.input(log, inplace=True, backup='.bak') as f:
    for line in f:
        line.rstrip('/n')
        if line[(line.find('Energy')) + 10:(line.find('Energy')) + 17] is not '':
            nrg = '{0:.3f}'.format(float(line[(line.find('Energy')) + 10:(line.find('Energy')) + 17])).replace('.', 'p')
            fname = line[:][(line.find('>/')) + 1:-11]
            path_log = dirname(fname)
            filename_log = pjoin(path_log, splitext(basename(fname))[0][:-5] + '_' + nrg + splitext(basename(fname))[0][
                                                                                           -5:] + '.tif').replace('\\',
                                                                                                                  '/')
            filename_dat = splitext(basename(filename_log))[0] + '.dat'
            copyfile(pjoin(dirname(path), splitext(basename(fname))[0] + '.dat'), pjoin(dats, filename_dat))
            line = line.replace(fname, filename_log)
            print(line, end='')

        # In[4]:

        lines = []
        with open(log, 'rt') as file:
            for line in file:
                line.rstrip('/n')
                lines.append(line)

