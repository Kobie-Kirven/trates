mol new file_name
set molecule [atomselect top "all"]

# #Move the C-terminus by the specified values
$molecule moveby {0 0 distance}

#Output the pdb with the fixed atoms
$molecule writepdb file_name

exit