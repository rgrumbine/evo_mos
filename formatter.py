from math import *
import numpy as np
import csv
import matplotlib
import matplotlib.pyplot as plt

######################## ######################## ########################

fout = open("alpha.csv","w")
  
with open('alpha') as fin:
    k = 0
    for line in fin:
      words = line.split()

      day = float(words[0])
      t2m_gfs = float(words[1])
      td_gfs = float(words[2])
      thick_gfs = float(words[3])
      rh_gfs = float(words[4])
      speed = float(words[5])
      obs_t2m= float(words[6])
      obs_td = float(words[7])
      terr = float(words[8])
      tderr = float(words[9])

      print(day,",",t2m_gfs,",", td_gfs,",",thick_gfs,",", rh_gfs,",", speed,",", obs_t2m,",", obs_td,",", terr,",", tderr, file=fout)
      k += 1
fin.close()


