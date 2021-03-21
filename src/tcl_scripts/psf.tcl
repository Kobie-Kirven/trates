
#Load the psfgen package and specify the residue /
# atom conversions
package require psfgen
topology {/usr/local/lib/python3.7/site-packages/src/tcl_scripts/top_all36_prot.rtf}
pdbalias residue HIS HSE
pdbalias atom ILE CD1 CD

set PDB out_path/file_name
#Create a psf file and pdb file with H's for the N termius
segment pep {pdb $PDB.pdb}
coordpdb $PDB.pdb pep
guesscoord
writepdb $PDB.pdb
writepsf $PDB.psf

exit