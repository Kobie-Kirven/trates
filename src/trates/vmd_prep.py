import os
from pathlib import Path
import pkg_resources


class PrepPSF:
    """A class for generating protein structure files"""

    def __init__(self, vmd_path, molName, outPath):
        self.vmd_path = vmd_path
        self.molName = molName
        self.outPath = outPath

    def psf_builder(self):
        """Build the Protein Structure File for a
        given squence"""
        replaceDict = dict(
            {
                "file_name": self.molName.strip(".pdb"),
                "out_path": self.outPath,
                "in_path": pkg_resources.resource_filename(
                    "src", "tcl_scripts"
                ),
            }
        )
        EditStructure.makeAndRunTclFile(
            "/psf.tcl", replaceDict, self.vmd_path
        )


class EditStructure:

    """A class for merging 2 structure files"""

    def __init__(self, vmd_path, file1, file2, outFile, outPath):
        self.vmd_path = vmd_path
        self.file1 = file1
        self.file2 = file2
        self.outFile = outFile
        self.outPath = outPath

    def moveApart(self, distance):
        """Move the alpha carbons of the anchoring residues a certian distance apart"""
        replaceDict = dict(
            {
                "file_name": self.file1,
                "distance": distance,
                "out_path": self.outPath,
            }
        )
        EditStructure.makeAndRunTclFile(
            "move.tcl", replaceDict, self.vmd_path
        )

    def mergeStructures(self, fileType):
        """Merge 2 structure files together"""
        replaceDict = dict(
            {
                "file_1": str(self.file1),
                "file_2": str(self.file2),
                "out_file": str(self.outFile),
                "TYPE": str(fileType).lower(),
                "out_path": self.outPath,
            }
        )

        EditStructure.makeAndRunTclFile(
            "merge.tcl", replaceDict, self.vmd_path
        )

    def rotateStructure(self):
        replaceDict = dict(
            {
                "file_name": str(self.file2),
                "out_file": str(self.outFile),
                "out_path": self.outPath,
            }
        )

        EditStructure.makeAndRunTclFile(
            "rotate.tcl", replaceDict, self.vmd_path
        )

    def runTclFile(vmdPath, fileName):
        os.system(
            vmdPath + " -dispdev text -e " + fileName + " > out.txt"
        )
        os.system("rm " + fileName)

    def createTclFile(templateFileName, replaceDict):
        with open("temp.tcl", "w") as merge:
            lines = EditStructure.readTemplateFile(templateFileName)
            for line in lines:
                for i in replaceDict:
                    if i in line:
                        line = line.replace(i, str(replaceDict[i]))
                merge.write(line)

    def anchorResidue(self, resid1, resid2, fileName):
        replaceDict = dict(
            {
                "file_name": fileName,
                "residue1": resid1,
                "residue2": resid2,
                "out_path": self.outPath,
            }
        )
        EditStructure.makeAndRunTclFile(
            "anchor.tcl", replaceDict, self.vmd_path
        )

    def readTemplateFile(templateFileName):
        with open(
            pkg_resources.resource_filename("src", "tcl_scripts")
            + "/"
            + templateFileName
        ) as fn:
            return fn.readlines()

    def makeAndRunTclFile(templateFileName, replaceDict, vmdPath):
        EditStructure.createTclFile(templateFileName, replaceDict)
        EditStructure.runTclFile(vmdPath, "temp.tcl")
