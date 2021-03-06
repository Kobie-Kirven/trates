#######################################################################################
# TraTeS is A program for preparing the preparation files needed for molecular dynamics
# simulations.
#
# Author: Kobie Kirven
# 3-21-2020
#######################################################################################
#!/usr/bin/env python

# Imports
from .trates import (
    Slicer,
    Structure,
    PrepPSF,
    EditStructure,
    createConfigFile,
    RMSD,
    Smooth,
    NativeContacts,
    Plot
)
import os
import sys
import argparse
import subprocess
from Bio import SeqIO


def prepare():

    parser = argparse.ArgumentParser(
        description="TRAnsporter TErmani Simulations"
    )
    parser.add_argument(
        "-1",
        "--input-1",
        dest="in1",
        help="First FASTA input file",
        required=True,
    )

    parser.add_argument(
        "-s1",
        "--slice-1",
        dest="s1",
        help="The positons of the start and stop residue (inclusive) for the \
        first terminus seperated by a dash (start-stop)",
        required=True,
    )

    parser.add_argument(
        "-2",
        "--input-2",
        dest="in2",
        help="Second FASTA input file",
        required=True,
    )

    parser.add_argument(
        "-s2",
        "--slice-2",
        dest="s2",
        help="The positons of the start and stop residue (inclusive) for the \
        second terminus seperated by a dash (start-stop)",
        required=True,
    )

    parser.add_argument(
        "-o",
        "--output-path",
        dest="out_path",
        help="Path and name of output folder (Ex. ~/Desktop/output",
        required=True,
    )

    parser.add_argument(
        "-nc",
        "--n-and-c",
        dest="nc",
        help="Boolean (T/F) if the simulation is for a combination of the N-terminus and C-terminus",
        required=True,
    )

    parser.add_argument(
        "-vmd",
        "--vmd-path",
        dest="vmd",
        help="Path to VMD",
        required=True,
    )

    parser.add_argument(
        "-n",
        "--out-name",
        dest="out_name",
        help="Name of output files",
        required=True,
    )

    parser.add_argument(
        "-a",
        "--anchoring-residues",
        dest="anchor",
        help="Anchoring residue for each terminus in comma-seperated format",
        required=True,
    )

    parser.add_argument(
        "-d",
        "--distance-apart",
        dest="distance",
        help="Distance between alpha carbons of anchoring residues in angstroms",
        required=True,
    )

    parser.add_argument(
        "-t",
        "--simulation-time",
        dest="time",
        help="How long to run the simulation in nanoseconds",
    )

    valid = True
    args = parser.parse_args()

    # Input Checks
    if len(sys.argv) > 1:
        try:
            SeqIO.parse(args.in1, "fasta")
            SeqIO.parse(args.in2, "fasta")
        except:
            print(
                "Error: One of the files you entered was not a FASTA file"
            )
            valid = False

        if len(args.s1.split("-")) == 1 or len(args.s2.split("-")) == 1:
            print(
                "Error: The start and stop residue was not formatted correctly"
            )
            valid = False

        try:
            args.anchor.split(",")

        except:
            print("Error: The anchoring residues were not correct")
            valid = False

    # Check to see if the directory already exists
    if valid == True:
        try:
            os.system("mkdir " + args.out_path)
        except:
            print("The directory already exists")

        slice1 = args.s1.split("-")
        slice2 = args.s2.split("-")

        if args.nc == "T" or args.nc == "TRUE":
            seq = Slicer(args.in1).sliceNC(
                int(slice1[0]), int(slice1[1])
            )
        else:
            seq = Slicer(args.in1).slice(int(slice1[0]), int(slice1[1]))

        seq2 = Slicer(str(args.in2)).slice(
            int(slice2[0]), int(slice2[1])
        )

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

        createConfigFile(
            args.out_name + ".pdb",
            args.out_name + ".psf",
            args.out_name,
            args.out_path,
            args.time,
        )

        print(
            "Successfully generated files {}.pdb, {}.psf, and {}.conf in {}/".format(
                args.out_name, args.out_name, args.out_name, args.out_path
            )
        )

def rmsd():
    parser = argparse.ArgumentParser(
        description="RMSD calculations"
    )
    parser.add_argument(
        "-psf",
        "--psf-file",
        dest="psf",
        help="PSF file",
    )

    parser.add_argument(
        "-dcd",
        "--dcd-file",
        dest="dcd",
        help="DCD file",
    )

    parser.add_argument(
        "-o",
        "--out-file",
        dest="out",
        help="Output Data File",
    )


    parser.add_argument(
        "-vmd",
        "--vmd-path",
        dest="vmd",
        help="Path to vmd",
    )


    args = parser.parse_args()

    r = RMSD(args.psf, args.dcd, args.vmd)
    r.getRMSD(args.out)


def native_contacts():
    parser = argparse.ArgumentParser(
        description="Calculate native contacts"
    )
    parser.add_argument(
        "-psf",
        "--psf-file",
        dest="psf",
        help="Protein structure (PSF) file",
    )

    parser.add_argument(
        "-dcd",
        "--dcd-file",
        dest="dcd",
        help="Trajectory (DCD) file",
    )

    parser.add_argument(
        "-vmd",
        "--vmd-path",
        dest="vmd",
        help="Path to vmd",
    )

    parser.add_argument(
        "-o",
        "--out-file",
        dest="out",
        help="Name of output file (.txt)",
    )

    parser.add_argument(
        "-f",
        "--frame-span",
        dest="frame",
        help="Begining and ending frame of simulation",
    )

    parser.add_argument(
        "-d",
        "--contact-distance",
        dest="distance",
        help="Cutoff distance in angstroms for native contacts",
    )

    parser.add_argument(
        "-t",
        "--contact-type",
        dest="type",
        help="Type of native coontact (options: inter, intra, all)",
    )

    parser.add_argument(
        "-r",
        "--residue-cut-off",
        dest="cutoff",
        help="Intramolecular: Cutoff for native contacts (only interactions more than a specified \
                distance apart",
    )

    parser.add_argument(
        "-c",
        "--chain-number",
        dest="chain",
        help="Intramolecular: Chain number (1 or 2)",
    )

    args = parser.parse_args()

    replaceDict = {"psf_file":args.psf, "dcd_file": args.dcd,
     "frame_number":0}

    fn = open(args.out, "w")
    counts = []
    frames = args.frame.split("-")
    fn.write('Frame\tContacts\n')
    for i in range(int(frames[0]), int(frames[1])):
        percent = (100 / (int(frames[1]) - int(frames[0]))) *(i +1)
        replaceDict["frame_number"] = i
        EditStructure.makeAndRunTclFile("getPDBfromDCD.tcl", replaceDict, args.vmd)

        if args.type.lower() == "inter":
             count = NativeContacts("frame.pdb").getIntermolecularContacts(int(args.distance))

        elif args.type.lower() == "intra":
            count = NativeContacts("frame.pdb").getIntramolecularContacts(int(args.distance), 
                int(args.cutoff), (int(args.chain)-1))

        elif args.type.lower() == "all":
            count = NativeContacts.getAllContacts(int(args.distance), 
                int(args.cutoff))

        print("{} % done".format(percent))

        fn.write(str(i) + '\t' + str(count) + "\n")
    fn.close()
    os.system("rm frame.pdb")

def plot():

    parser = argparse.ArgumentParser(
        description="Plot the output data"
    )

    parser.add_argument(
        "-i",
        "--input-file",
        dest="input",
        help="Input data file",
    )

    parser.add_argument(
        "-o",
        "--image-file",
        dest="image",
        help="Output image",
    )

    parser.add_argument(
        "-s",
        "--sliding-widow",
        dest="smooth",
        help="Sliding window length for smoothing",
    )

    parser.add_argument(
        "-d",
        "--data-type",
        dest="type",
        help="Data type (rmsd, conacts)",
    )

    args = parser.parse_args()
    Plot.plotData(args.input,args.image, args.type, int(args.smooth))









