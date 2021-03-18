################################################################################
# A program for preparing the preparation files needed for molecular dynamics
# simulations.
#

from ttsimprep import Slicer
from ttsimprep import Structure
from ttsimprep import PrepPSF, EditStructure
import os

seq = Slicer("fasta_test.fasta").slice(1, 60)
seq2 = Slicer("fasta_test.fasta").slice(480, 540)

out_path = "output_files" 

try:
	os.system("mkdir " + out_path)

except:
	pass
Structure.buildStructure(seq,"out1.pdb", out_path)
Structure.buildStructure(seq2,"out2.pdb", out_path)
Structure.renumberResidues("out2.pdb", 480, 540, out_path)

vmd = "/Applications/VMD\ 1.9.4a48-Catalina-Rev7.app/Contents/vmd/vmd_MACOSXX86_64"

prep = PrepPSF(vmd,"out1.pdb", out_path)
prep.psf_builder()

prep = PrepPSF(vmd,"out2.pdb", out_path)
prep.psf_builder()

comb_psf = EditStructure(vmd, "out1.psf","out2.psf", "out_comb_1.psf", out_path)
comb_psf.mergeStructures("PSF")

comb_pdb = EditStructure(vmd, "out1.pdb","out2.pdb", "out_comb_1.pdb",out_path)
comb_pdb.moveApart(10)
comb_pdb.mergeStructures("PDB")
comb_pdb.anchorResidue(60, "out_comb_1.pdb")