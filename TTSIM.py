################################################################################
# A program for preparing the preparation files needed for molecular dynamics
# simulations.
#

from ttsimprep import Slicer
from ttsimprep import Structure
from ttsimprep import PrepPSF, EditStructure


import os
import sys
import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-1",
        "--input-1",
        dest="in1",
        help="Input first sequence file"
    )

    parser.add_argument(
        "-s1",
        "--slice-1",
        dest="s1",
        help="Start and stop residue inclusive"
    )

    parser.add_argument(
        "-s2",
        "--slice-2",
        dest="s2",
        help="Start and stop residue inclusive"
    )

    parser.add_argument(
        "-2",
        "--input-2",
        dest="in2",
        help="Input second sequence file"
    )

    parser.add_argument(
        "-o",
        "--output-path",
        dest="out_path",
        help="Output path"
    )

    parser.add_argument(
        "-nc", "--n-and-c", dest="nc", help="Boolean (T/F) if the simulation is N and C"
    )

    parser.add_argument(
        "-vmd",
        "--vmd-path",
        dest="vmd",
        help="Output path"
    )

    parser.add_argument(
        "-n",
        "--out-name",
        dest="out_name",
        help="Output pdb name"
    )

    parser.add_argument(
        "-d",
        "--distance-apart",
        dest="distance",
        help="distance"
    )

    parser.add_argument(
        "-a",
        "--anchoring-residues",
        dest="anchor",
        help="Anchoring residues"
    )

    args = parser.parse_args()
    try:
        os.system("mkdir " + args.out_path)
    except:
        print("The directory already exists")

    slice1 = args.s1.split("-")
    slice2 = args.s2.split("-")

    seq = Slicer(args.in1).sliceNC(int(slice1[0]), int(slice1[1]))
    seq2 = Slicer(str(args.in2)).slice(int(slice2[0]), int(slice2[1]))

    Structure.buildStructure(seq, args.out_name + "1.pdb", args.out_path)
    Structure.buildStructure(seq2, args.out_name + "2.pdb", args.out_path)

    Structure.renumberResiduesBackwards(
        args.out_name + "1.pdb", int(slice1[0]), int(slice1[1]), args.out_path)
    Structure.renumberResidues(
        args.out_name + "2.pdb", int(slice2[0]), int(slice2[1]), args.out_path)

    vmd = args.vmd

    prep = PrepPSF(vmd, args.out_name + "1.pdb", args.out_path)
    prep.psf_builder()

    prep = PrepPSF(vmd, args.out_name + "2.pdb", args.out_path)
    prep.psf_builder()

    comb_psf = EditStructure(vmd, args.out_name + "1.psf",
                             args.out_name + "2.psf", args.out_name + ".psf", args.out_path)
    comb_psf.mergeStructures("PSF")

    comb_pdb = EditStructure(vmd, args.out_name + "1.pdb",
                             args.out_name + "2.pdb", args.out_name + ".pdb", args.out_path)
    comb_pdb.moveApart(args.distance)
    comb_pdb.mergeStructures("PDB")

    anchor = args.anchor.split(",")
    comb_pdb.anchorResidue(int(anchor[0]), int(anchor[1]), args.out_name + ".pdb")
    
    os.system("rm " + args.out_path + "/*1*")
    os.system("rm " + args.out_path + "/*1*")

if __name__ == "__main__":
    main()
