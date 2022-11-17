# Phono-Group-velocity-from-band.yaml

Function: Extract phonon frequencies and related data in  band.yaml produced by Phonopy

Usage: Use "phonopy band.conf" command to generate band.yaml

band.conf set shoule be like (of course you can change some parameters if you want): 

ATOM_NAME = Te Sn

DIM = 2 2 2

BAND = 0.3750000000   0.3750000000   0.7500000000 0.0000000000   0.0000000000   0.0000000000  0.5000000000   0.5000000000   0.5000000000 0.5000000000   0.2500000000   0.7500000000 0.5000000000   0.0000000000   0.5000000000

GROUP_VELOCITY = .TRUE.

GV_DELTA_Q = 0.01

       then use "python gv.py" command to get gv.txt
       
       note: # The unit of frequency is the same as that set in phonopy
       
Requirements： Python3 Pandas Numpy PyYaml

Acknowledgment: Liang Yan
