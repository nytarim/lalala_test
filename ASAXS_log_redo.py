from os.path import dirname, splitext, basename, join as pjoin
from shutil import copyfile
import fileinput
import re

def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys1(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split('(\d+)', text[-23:-20])]

# In[13]:

path_dat = 'T:/data/Archive/processed/Ryan_11315/Pilatus2_1m/0p6_1/reduced/SAXS/profiles/'
path_log = 'T:/data/Archive/Cycle_2016_3/Ryan_11315/Pilatus2_1m/0p6_1/images/'
# In[16]:

log = pjoin(dirname(path_log), 'livelogfile_edit.log')
dats = pjoin(dirname(dirname(path_dat)), 'raw_dats')

# In[ ]:

with fileinput.input(log, inplace=True, backup='.bak') as f:
    for line in f:
        line.rstrip('/n')
        if line[(line.find('Energy')) + 10:(line.find('Energy')) + 17] is not '':
            nrg = '{0:.3f}'.format(float(line[(line.find('Energy')) + 10:(line.find('Energy')) + 17])).replace('.', 'p')
            fname = line[:][(line.find('>/')) + 1:-11]
            path_log = dirname(fname)
            filename_log = pjoin(path_log, splitext(basename(fname))[0][:-5] + '_' + nrg + splitext(basename(fname))[0][
                                                                                           -5:] + '.tif')
            filename_dat = splitext(basename(filename_log))[0] + '.dat'
            copyfile(pjoin(dirname(path), splitext(basename(fname))[0] + '.dat'), pjoin(dats, filename_dat))
            line = line.replace(fname, filename_log)
            print line, ''

# In[4]:

#lines = []
#with open(log, 'rt') as file:
#    for line in file:
#        line.rstrip('/n')
#        lines.append(line)

# In[6]:





# In[7]:

#print(natural_keys2(lines[30]))

# In[10]:

#lines_sorted = sorted(lines, key=natural_keys1)
#if lines_sorted is None:
#    print('failed')

# In[11]:

#with open(dirname(path_log) + '/livelogfile_sorted.log', 'w') as file:
#    file.writelines(lines_sorted)


# In[ ]:



