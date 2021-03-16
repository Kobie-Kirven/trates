#Combine the individual pdb and psf files into one
package require topotools
set midlist {}
set mol [mol new file_1 waitfor all]
lappend midlist $mol
set mol [mol new file_2 waitfor all]
lappend midlist $mol

set mol [::TopoTools::mergemols $midlist]
animate write TYPE out_file $mol

exit