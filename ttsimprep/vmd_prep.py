import os
from pathlib import Path

class PrepPSF:
	'''A class for generating protein structure files'''
	def __init__(self, vmd_path, molName):
		self.vmd_path = vmd_path
		self.molName = molName


	def psf_builder(self):
		'''Build the Protein Structure File for a 
			given squence'''
		with open(os.path.abspath("tcl_scripts/psf.tcl")) as fn:
			lines = fn.readlines()

		with open("psf_temp.tcl", "w") as tcl:
			for line in lines:
				if "file_name" in line:
					line = line.replace("file_name", self.molName.strip(".pdb"))
				tcl.write(line)

		os.system(self.vmd_path + " -dispdev text -e psf_temp.tcl")
		os.system("rm psf_temp.tcl")


class EditStructure:

	'''A class for merging 2 structure files'''

	def __init__(self, vmd_path, file1, file2, outFile):
		self.vmd_path = vmd_path
		self.file1 = file1
		self.file2 = file2
		self.outFile = outFile

	def anchorResidues(self, resid1, resid2):
		pass

	def moveApart(self, distance):
		'''Move the alpha carbons of the anchoring residues a certian distance apart'''
		replaceDict = dict({"file_name":self.file1, "distance":distance})
		EditStructure.makeAndRunTclFile("move.tcl", replaceDict, self.vmd_path)

	def mergeStructures(self, fileType):
		'''Merge 2 structure files together'''
		replaceDict = dict({"file_1":str(self.file1),"file_2":str(self.file2),
			"out_file":str(self.outFile), "TYPE":str(fileType).lower()})

		EditStructure.makeAndRunTclFile("merge.tcl", replaceDict, self.vmd_path)


	def runTclFile(vmdPath, fileName):
		os.system(vmdPath + " -dispdev text -e " + fileName)
		# os.system("rm " + fileName)

	def createTclFile(templateFileName, replaceDict):
		with open("temp.tcl","w") as merge:
			lines = EditStructure.readTemplateFile(templateFileName)
			for line in lines:
				for i in replaceDict:
					if i in line:
						line = line.replace(i, str(replaceDict[i]))
				merge.write(line)

	def readTemplateFile(templateFileName):
		with open(os.path.abspath("tcl_scripts/" + templateFileName)) as fn:
			return fn.readlines()

	def makeAndRunTclFile(templateFileName, replaceDict, vmdPath):
		EditStructure.createTclFile(templateFileName, replaceDict)
		EditStructure.runTclFile(vmdPath, "temp.tcl")
