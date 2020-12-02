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
          x.append(float(ppm_shift))
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


##Grabbing Chemical Shift Values from parameters.fit file. 
##Make sure it's in the same directory!


file=open('parameters.fit', 'r')
number = len(residues1)#number of residues

residuelist=[]
cs_a={}
cs_b={}
cs_b_error={}

content=file.read()
content_list=content.splitlines()
file.close()

csa_raw=content_list[8:8+number]

for residue in csa_raw:
    step1=residue.split()
    if not step1:
            continue
    residue=step1[0]
    csa=step1[2]
    cs_a[residue.strip('N')]=float(csa)

csb_raw=content_list[10+number:10+(2*number)]

for residue in csb_raw:
    step1=residue.split()
    if not step1:
        continue
    residue=step1[0]
    csb=step1[2]
    cs_b[residue.strip('N')]=float(csb)
    err=step1[4]
    cs_b_error[residue.strip('N')]=float(err)



##Hey, If you wanted to put something to select only certain residues to print,
##here would be a great place to put it


##plotting each residue##

xlabels=x[::8]

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

    cs_a_line=cs_a[key]
    cs_b_line=cs_b[key]
    cs_b_err=cs_b_error[key]
    cs_b_err_upper=cs_b_line-cs_b_err
    cs_b_err_lower=cs_b_line+cs_b_err

    #Actually plotting the shizz

    plt.scatter(x, y1acorr, color=low, label='10 hz')
    plt.plot(x, y1bcorr, color=low)
    plt.scatter(x, y2acorr, color=med, label='25 hz')
    plt.plot(x, y2bcorr, color=med)
    plt.scatter(x, y3acorr, color=high, label='50 hz')
    plt.plot(x, y3bcorr, color=high)

    plt.axvspan(cs_b_err_lower,cs_b_err_upper, facecolor='grey', alpha=0.2)#these keep plotting to the far right of all the data for some reason... if I change to floats it smushes the data to the left. putting in a static number works though
    plt.axvline(x=cs_a_line, color='black')
    plt.axvline(x=cs_b_line, color='black', linestyle='--')
    
    plt.xticks(xlabels,xlabels)  
    plt.xlabel('B1 position (ppm)', labelpad=15, fontsize=12)
    plt.ylabel('I/Io', labelpad=15, fontsize=12)
    plt.suptitle(key)

    plt.savefig(key, dpi=300, bbox_inches='tight', pad_inches=.1)
    plt.close()    




