set psfFile psf_file
set trajFile dcd_file

#Load the protein structure file
mol new $psfFile type psf

#Load the trajectory file
mol addfile $trajFile type dcd first first_step last last_step step 1 waitfor all

#Set a reference frame for the rmsd calculation
set reference [atomselect top "protein and backbone" frame 0]

#Set the frame to compare to
set compare [atomselect top "protein and backbone"]

#Get the number of frames in the trajectory file
set num_steps [molinfo top get numframes]

#Set output file
set outfile [open rmsd_output w]

for {set frame 0} {$frame < $num_steps} {incr frame} {
			#get the correct frame
			$compare frame $frame

			set trans_mat [measure fit $compare $reference]

			$compare move $trans_mat

			set rmsd [measure rmsd $compare $reference]
	puts $outfile "$frame 	$rmsd"
}

close $outfile

exit

