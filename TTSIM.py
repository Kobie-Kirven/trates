################################################################################
# A program for preparing the preparation files needed for molecular dynamics
# simulations.
#

from ttsimprep import Slicer
from ttsimprep import Structure
from ttsimprep import PrepPSF, Merge

seq = Slicer("fasta_test.fasta").slice(1, 60)

Structure.buildStructure(seq,"out.pdb")

vmd = "/Applications/VMD\ 1.9.4a48-Catalina-Rev7.app/Contents/vmd/vmd_MACOSXX86_64"
prep = PrepPSF(vmd,"out.pdb")

prep.psf_builder()

comb_psf = Merge(vmd, "out.psf","out.psf", "out_comb.psf")
comb_psf.merge("PSF")

comb_pdb = Merge(vmd, "out.pdb","out.pdb", "out_comb.pdb")
comb_pdb.merge("PDB")