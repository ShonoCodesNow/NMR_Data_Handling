# NMR_Data_Handling
Miscellaneous Code for prepping and plotting NMR Data


CEST_Data_Parser.py:

Instensity Values (xlsx) & Error -> Text files for each residue to load into ChemEx, also
prepopulates cs_a, dw_ab input files with residue names, and the residue->file table that's 
a pain to type out in the experiment.cfg files. 

Input is an excel file, each hz in a different tab. First column=the offset, 
subsequent columns are residue intensity data with residue number as headers.

Make sure fq3list from run folder is in the same directory.


dir_File_to_Figs.py:

3 .dir files & parameters.fit from ChemEx CEST analysis + fq3list -> lovely plots for each residue, each with experimental 
and calculated I/Io values for the 3 frequencies. CS A, CS B, and CS B error also plotted.


relax_Data_Parser.py:

Intensity values (txt table) & vdlist -> text files for each CPMG frequency populated with residues and corresponding intensities

Preps data table that's a pain to type out by hand for input into relax code.


