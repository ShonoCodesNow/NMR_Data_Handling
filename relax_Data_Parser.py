import re
import os

file='500_3mM_CPMG.txt'
description='3mM'
vdlist_file='vdlist'
residues={}
spectrometer_frequency='500.53E6'
freq_short='500'

#read in the data
f=open(file,'r')
content=f.read()
content_list=content.splitlines()
f.close()
content_list.pop(0)
#parse into dictionary with residue numbers as keys, list of intensities as 
for line in content_list:
    contents = line.split()
    residue=contents[0]
    residue_stripped=int(re.split(r'\D', residue, maxsplit=1)[0])
    planes=contents[2:]
    residues[residue_stripped]=planes

#prep residue list
residue_list=[]
for key in residues:
    residue_list.append(key)
residue_list.sort()

#prep vdlist from file. make sure it's in the directory
f = open(vdlist_file,'r')
content=f.read()
vdlist=content.splitlines()
f.close()
vdlist=[int(x) for x in vdlist]
data_file=open('data.txt','w')

#write each delay
for index in range(len(vdlist)):
    vd=vdlist[index]
    filename=freq_short+'_'+description+'_'+str(index)+'_' + str(vd)
    filepath=os.path.join('planes',filename)
    if not os.path.isdir('planes'):
        os.mkdir('planes')
        
    f=open(filepath, 'w')

    for item in residue_list:
        #retrieve data from dictionary
        data=residues[item]
        intensity = data[index]
        #write to file
        f.write(str(item)+'\t'+ intensity + '\t' + 'N'+'\n')
    f.close()

    if index == 0: 
        data_file.write("['"+freq_short+'_'+str(vd)+'_'+str(index)+','+'\t'+"'"+filename+"'," + '\t' + 'None,'+'\t'+spectrometer_frequency+'],'+'\n')
    else:
        data_file.write("['"+freq_short+'_'+str(vd)+'_'+str(index)+','+'\t'+"'"+filename+"'," + '\t' + str(vd)+'\t'+spectrometer_frequency+'],'+'\n')

data_file.close()