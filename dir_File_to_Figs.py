import re
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
import os


ten_hz_file='cest_x_ip_10hz_400ms_800mhz_30c.txt'
twentyfive_hz_file='cest_x_ip_25hz_400ms_800mhz_30c.txt'
fifty_hz_file='cest_x_ip_50hz_400ms_800mhz_30c.txt'


###color scheme###
high='#404787'  #50 hz
med='#267D8F'   #25 hz
low='#29B080'   #10 hz


#prep the data

#set up offset list in ppm using fq3list from experiment folder. Make sure it's in the same folder!
x=[]
f=open('fq3list', 'r')
for line in f:
      if 'ppm' not in line:
          ppm_shift = line.strip('\n')
          x.append(ppm_shift)
f.close()


###open 10 hz data###
data1=open(ten_hz_file, 'r')

residues1={}
experimental_vals1=[]
fit_vals1=[]
error1=[]

for line in data1:
    if '[' in line:
        residue1=line.strip('[').replace('N-HN]','')
        residue_strip1=residue1.strip('\n')
    elif '#' in line:
        pass        
    else:
        splitline=line.split()
        if not splitline:
            continue
        experimental_vals1.append(float(splitline[2]))
        error1.append(float(splitline[3]))
        fit_vals1.append(float(splitline[4]))
        

    if len(experimental_vals1) == 64:
        residues1[residue_strip1]=[experimental_vals1,error1,fit_vals1]
        experimental_vals1=[]
        error1=[]
        fit_vals1=[]
    else:
        continue
data1.close()

####open 25 hz data####    
data2=open(twentyfive_hz_file, 'r')

residues2={}
experimental_vals2=[]
fit_vals2=[]
error2=[]

for line in data2:
    if '[' in line:
        residue2=line.strip('[').replace('N-HN]','')
        residue_strip2=residue2.strip('\n')
    elif '#' in line:
        pass        
    else:
        splitline=line.split()
        if not splitline:
            continue
        experimental_vals2.append(float(splitline[2]))
        error2.append(float(splitline[3]))
        fit_vals2.append(float(splitline[4]))
    

    if len(experimental_vals2) == 64:
        residues2[residue_strip2]=[experimental_vals2,error2,fit_vals2]
        experimental_vals2=[]
        error2=[]
        fit_vals2=[]
    else:
        continue
data2.close()


####open 50 hz data####    
data3=open(fifty_hz_file, 'r')

residues3={}
experimental_vals3=[]
fit_vals3=[]
error3=[]

for line in data3:
    if '[' in line:
        residue3=line.strip('[').replace('N-HN]','')
        residue_strip3=residue3.strip('\n')
    elif '#' in line:
        pass        
    else:
        splitline=line.split()
        if not splitline:
            continue
        experimental_vals3.append(float(splitline[2]))
        error3.append(float(splitline[3]))
        fit_vals3.append(float(splitline[4]))
        

    if len(experimental_vals3) == 64:
        residues3[residue_strip3]=[experimental_vals3,error3,fit_vals3]
        experimental_vals3=[]
        error3=[]
        fit_vals3=[]
    else:
        continue
data3.close()



##plotting each residue##
for key in residues1:
    #pull data from dict for residue
    ten_hz_ys=residues1[key]
    twentyfive_hz_ys=residues2[key]
    fifty_hz_ys=residues3[key]

    #normalize to first entry
    y1a=ten_hz_ys[0]
    y1acorr=[x/y1a[0] for x in y1a]
    y1acorr.pop(0)

    y1b=ten_hz_ys[2]
    y1bcorr=[x/y1b[0] for x in y1b]
    y1bcorr.pop(0)

    y2a=twentyfive_hz_ys[0]
    y2acorr=[x/y2a[0] for x in y2a]
    y2acorr.pop(0)

    y2b=twentyfive_hz_ys[2]
    y2bcorr=[x/y2b[0] for x in y2b]
    y2bcorr.pop(0)

    y3a=fifty_hz_ys[0]
    y3acorr=[x/y3a[0] for x in y3a]
    y3acorr.pop(0)

    y3b=fifty_hz_ys[2]
    y3bcorr=[x/y3b[0] for x in y3b]
    y3bcorr.pop(0)

    #Actually plotting the shizz

    tick_spacing = 6 #change this if you want x labels closer or further apart

    fig, ax = plt.subplots(1,1)

    ax.scatter(x, y1acorr, color=low, label='10 hz')
    ax.plot(x, y1bcorr, color=low)
    ax.scatter(x, y2acorr, color=med, label='25 hz')
    ax.plot(x, y2bcorr, color=med)
    ax.scatter(x, y3acorr, color=high, label='50 hz')
    ax.plot(x, y3bcorr, color=high)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.set_xlabel('Offset (ppm)', labelpad=15, fontsize=12)
    ax.set_ylabel('I/Io', labelpad=15, fontsize=12)
    fig.suptitle(key)
    plt.savefig(key)
    plt.close()





