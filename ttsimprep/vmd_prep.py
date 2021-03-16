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


class Merge:

	'''A class for merging 2 structure files'''

	def __init__(self, vmd_path, file1, file2, outFile):
		self.vmd_path = vmd_path
		self.file1 = file1
		self.file2 = file2
		self.outFile = outFile

	def mergePSF(self):
		'''Merge 2 PSF files together'''
		with open(os.path.abspath("tcl_scripts/psf_merge.tcl")) as fn:
			lines = fn.readlines()

		with open("psf_merge_temp.tcl","w") as merge:
			replaceList = dict({"file_1":str(self.file1),"file_2":str(self.file2),"out_file":str(self.outFile)})
			for line in lines:
				for i in replaceList:
					if i in line:
						line = line.replace(i, replaceList[i])
				merge.write(line)

		os.system(self.vmd_path + " -dispdev text -e psf_merge_temp.tcl")
		os.system("rm psf_merge_temp.tcl")


	def mergePDB(self):
		pass
