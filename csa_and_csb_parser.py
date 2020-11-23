import os
import re
import numpy as np

file=open('parameters.fit', 'r')
number = 38#number of residues will pull from residue list##
##line 9-9+number will be CS_A

residuelist=[]
cs_a={}
cs_b={}
cs_b_error={}

content=file.read()
content_list=content.splitlines()
file.close()

csa_raw=content_list[9:9+number]

for residue in csa_raw:
    step1=residue.split()
    if not step1:
            continue
    residue=step1[0]
    csa=step1[2]
    cs_a[residue.strip('N')]=csa

csb_raw=content_list[10+number:10+(2*number)]

for residue in csb_raw:
    step1=residue.split()
    if not step1:
        continue
    residue=step1[0]
    csb=step1[2]
    cs_b[residue.strip('N')]=csb
    err=step1[4]
    cs_b_error[residue.strip('N')]=err

