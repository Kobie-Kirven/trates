#Combine the individual pdb and psf files into one
package require topotools
set midlist {}
set mol [mol new out1.pdb waitfor all]
lappend midlist $mol
set mol [mol new out2.pdb waitfor all]
lappend midlist $mol

set mol [::TopoTools::mergemols $midlist]
animate write pdb out_comb.pdb $mol

exit