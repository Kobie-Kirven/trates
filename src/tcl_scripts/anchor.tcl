##################################################
# Fix Specified Atoms
##################################################
mol new out_path/file_name

#Set the beta value for all of the atoms to zero
set sel [atomselect top all]
$sel set beta 0

#Set the beta value to 1 for the alpha carbons of each
# of the anchoring residues
set Fix1 [atomselect top "resid residue1 and name CA"]
set Fix2 [atomselect top "resid residue2 and name CA"]
$Fix1 set beta 1
$Fix2 set beta 1

$sel writepdb out_path/file_name

exit