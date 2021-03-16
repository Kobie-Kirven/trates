
#Load the psfgen package and specify the residue /
# atom conversions
package require psfgen
topology {tcl_scripts/top_all36_prot.rtf}
pdbalias residue HIS HSE
pdbalias atom ILE CD1 CD

set PDB file_name
#Create a psf file and pdb file with H's for the N termius
segment pep {pdb $PDB.pdb}
coordpdb $PDB.pdb pep
guesscoord
writepdb $PDB_h.pdb
writepsf $PDB.psf

exit