#Script for plotting the results from the rmsd analysis

#imports
from .vmd_prep import EditStructure
from .smooth import Smooth



class RMSD:
	'''Calculate and plot RMSD for simulation'''
	def __init__(self,psfFile, dcdFile, vmdPath):
		self.psfFile = psfFile
		self.dcdFile = dcdFile
		self.vmdPath = vmdPath


	def getRMSD(self, outDatFile, firstFrame=0, lastFrame=-1):

		replaceDict = {"psf_file":self.psfFile, "dcd_file":self.dcdFile,
		"first_step":firstFrame, "last_step":lastFrame, "rmsd_output":outDatFile}
		EditStructure.makeAndRunTclFile("rmsd.tcl", replaceDict, 
			self.vmdPath)
