################################################################################
# A program for preparing the preparation files needed for molecular dynamics
# simulations.
#
#!/usr/bin/env python

from .ttsimprep import Slicer
from .ttsimprep import Structure
from .ttsimprep import PrepPSF, EditStructure

import os
import sys
import argparse
import subprocess


def main():
    version = sys.version

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-1", "--input-1", dest="in1", help="First FASTA input file"
    )

    parser.add_argument(
        "-s1",
        "--slice-1",
        dest="s1",
        help="The start and stop residue of the first terminus (start-stop)",
    )

    parser.add_argument(
        "-2", "--input-2", dest="in2", help="Second FASTA input file"
    )

    parser.add_argument(
        "-s2",
        "--slice-2",
        dest="s2",
        help="The start and stop residue of the second terminus (start-stop)",
    )

    parser.add_argument(
        "-o",
        "--output-path",
        dest="out_path",
        help="Path and name of output folder (Ex. ~/Desktop/output",
    )

    parser.add_argument(
        "-nc",
        "--n-and-c",
        dest="nc",
        help="Boolean (T/F) if the simulation is for a combination of the N-terminus and C-terminus",
    )

    parser.add_argument(
        "-vmd", "--vmd-path", dest="vmd", help="Path to VMD"
    )

    parser.add_argument(
        "-n", "--out-name", dest="out_name", help="Name of output files"
    )

    parser.add_argument(
        "-a",
        "--anchoring-residues",
        dest="anchor",
        help="Anchoring residue for each terminus in comma-seperated format",
    )

    parser.add_argument(
        "-d",
        "--distance-apart",
        dest="distance",
        help="Distance between alpha carbons of anchoring residues in angstroms",
    )

    args = parser.parse_args()
    if len(sys.argv)==1:
       parser.print_help(sys.stderr) 

    else:
        try:
            os.system("mkdir " + args.out_path)
        except:
            print("The directory already exists")

        slice1 = args.s1.split("-")
        slice2 = args.s2.split("-")

        if args.nc == "T" or args.nc == "TRUE":
            seq = Slicer(args.in1).sliceNC(int(slice1[0]), int(slice1[1]))
        else:
            seq = Slicer(args.in1).slice(int(slice1[0]), int(slice1[1]))

        seq2 = Slicer(str(args.in2)).slice(int(slice2[0]), int(slice2[1]))

        # Build the structure for each termminus
        Structure.buildStructure(
            seq, args.out_name + "1.pdb", args.out_path
        )
        Structure.buildStructure(
            seq2, args.out_name + "2.pdb", args.out_path
        )

        if args.nc == "T" or args.nc == "TRUE":
            Structure.renumberResiduesBackwards(
                args.out_name + "1.pdb",
                int(slice1[0]),
                int(slice1[1]),
                args.out_path,
            )
        else:
            Structure.renumberResidues(
                args.out_name + "1.pdb",
                int(slice1[0]),
                int(slice1[1]),
                args.out_path,
            )

        Structure.renumberResidues(
            args.out_name + "2.pdb",
            int(slice2[0]),
            int(slice2[1]),
            args.out_path,
        )

        vmd = args.vmd

        prep = PrepPSF(vmd, args.out_name + "1.pdb", args.out_path)
        prep.psf_builder()

        prep = PrepPSF(vmd, args.out_name + "2.pdb", args.out_path)
        prep.psf_builder()

        comb_psf = EditStructure(
            vmd,
            args.out_name + "1.psf",
            args.out_name + "2.psf",
            args.out_name + ".psf",
            args.out_path,
        )
        comb_psf.mergeStructures("PSF")

        comb_pdb = EditStructure(
            vmd,
            args.out_name + "1.pdb",
            args.out_name + "2.pdb",
            args.out_name + ".pdb",
            args.out_path,
        )
        comb_pdb.moveApart(args.distance)
        comb_pdb.mergeStructures("PDB")

        anchor = args.anchor.split(",")
        comb_pdb.anchorResidue(
            int(anchor[0]), int(anchor[1]), args.out_name + ".pdb"
        )

        os.system("rm " + args.out_path + "/*1*")
        os.system("rm " + args.out_path + "/*2*")
        os.system("rm out.txt")

        print("Successfully generated files {}.pdb and {}.psf in {}/".format(args.out_name, args.out_name, args.out_path))


if __name__ == "__main__":
    main()
