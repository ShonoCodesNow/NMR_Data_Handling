import os
import re
import matplotlib.pyplot as plt
import numpy as np


#will create dictionary with key=residue number (int)
#and value = [[Field_strength],[x],[y1],[y2],[yerr]]
residue_level_data={}

filelist = os.listdir()
for i in filelist:
    if i.endswith('.out') and i.startswith('disp_'):
        #grab residue from file name
        pre_residue=i.split('_')
        residue=pre_residue[2]
        #read in data
        f=open(i, 'r')
        content=f.read()
        content_list=content.splitlines()
        f.close()
        #trim header
        content_list.pop(0)
        #parse into dictionary with residue numbers as keys
        Hz_list_800=[]
        R2eff_measured_list_800=[]
        R2eff_calc_list_800=[]
        R2eff_error_list_800=[]

        Hz_list_500=[]
        R2eff_measured_list_500=[]
        R2eff_calc_list_500=[]
        R2eff_error_list_500=[]
        for line in content_list:
            contents=line.split()
            if '799' in contents[2]:
                Hz=float(contents[3])
                Hz_list_800.append(Hz)
                R2eff_measured=float(contents[4])
                R2eff_measured_list_800.append(R2eff_measured)
                R2eff_calc=float(contents[5])
                R2eff_calc_list_800.append(R2eff_calc)
                R2eff_error=float(contents[6])
                R2eff_error_list_800.append(R2eff_error)
            if '500' in contents[2]:
                Hz=float(contents[3])
                Hz_list_500.append(Hz)
                R2eff_measured=(contents[4])
                R2eff_measured_list_500.append(R2eff_measured)
                R2eff_calc=float(contents[5])
                R2eff_calc_list_500.append(R2eff_calc)
                R2eff_error=float(contents[6])
                R2eff_error_list_500.append(R2eff_error)
        data=[]
        data.append(Hz_list_800)
        data.append(R2eff_measured_list_800)
        data.append(R2eff_calc_list_800)
        data.append(R2eff_error_list_800)
        data.append(Hz_list_500)
        data.append(R2eff_measured_list_500)
        data.append(R2eff_calc_list_500)
        data.append(R2eff_error_list_500)

        residue_level_data[residue]=data



for key in residue_level_data:
    data=residue_level_data[key]
    x1=data[0]
    y1a=data[1]
    y1b=data[2]

    x2=data[4]
    y2a=data[5]
    y2b=data[7]



    plt.figure()
    plt.scatter(x1,y1a)
    plt.plot(x1,y1b)
    plt.scatter(x2,y2a)
    plt.plot(x2,y2b)
    plt.suptitle(key)
    plt.ylabel('R2eff', labelpad=15, fontsize=12)
    plt.xlabel('CPMG Frequency (Hz)', labelpad=15, fontsize=12)

    plt.savefig(key, dpi=300, bbox_inches='tight', pad_inches=.1)
    plt.close()
