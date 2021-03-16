################################################################################
# A program for preparing the preparation files needed for molecular dynamics
# simulations.
#

from tsimprep import Slicer
from tsimprep import Structure
from tsimprep import PrepPSF, Merge

seq = Slicer("fasta_test.fasta").slice(1, 60)

Structure.buildStructure(seq,"out.pdb")

vmd = "/Applications/VMD\ 1.9.4a48-Catalina-Rev7.app/Contents/vmd/vmd_MACOSXX86_64"
# prep = PrepPSF(vmd,"out.pdb")

# prep.psf_builder()

comb = Merge(vmd, "out.psf","out.psf", "out_comb.psf")
comb.mergePSF()