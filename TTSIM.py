################################################################################
# A program for preparing the preparation files needed for molecular dynamics
# simulations.
#

from ttsimprep import Slicer
from ttsimprep import Structure
from ttsimprep import PrepPSF, EditStructure

seq = Slicer("fasta_test.fasta").slice(1, 60)

Structure.buildStructure(seq,"out1.pdb")
Structure.buildStructure(seq,"out2.pdb")

vmd = "/Applications/VMD\ 1.9.4a48-Catalina-Rev7.app/Contents/vmd/vmd_MACOSXX86_64"
prep = PrepPSF(vmd,"out1.pdb")
prep = PrepPSF(vmd,"out2.pdb")

prep.psf_builder()

comb_psf = EditStructure(vmd, "out1.psf","out2.psf", "out_comb.psf")
comb_psf.mergeStructures("PSF")

comb_pdb = EditStructure(vmd, "out1.pdb","out2.pdb", "out_comb.pdb")
comb_pdb.moveApart(10)
comb_pdb.mergeStructures("PDB")