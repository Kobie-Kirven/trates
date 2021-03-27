#Script for plotting the results from the rmsd analysis

#imports
import matplotlib
import matplotlib.pyplot as plt
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

	def plotRMSD(datFile, outFile, smooth=1):
		data = RMSD._getDatData(datFile)
		data = list(data)
		for i in range(len(data[0])):
			data[0][i] = ((data[0][i]*5000)*2)/1000000

		if smooth >1:
			data = Smooth.smoothPlot(data[1],data[0],smooth)
		#Create the plot
		fig, ax = plt.subplots()
		ax.plot(data[0], data[1])

		#label the axies
		ax.set(xlabel='Time (ns)', ylabel='RMSD',
		       title='RMSD Over Time')
		ax.grid()

		#output the figure
		fig.savefig(outFile)

	def _getDatData(datFile):
		with open(datFile) as fn:
			lines = fn.readlines()

		frame, rmsd = [],[]

		#Get the frame and rmsd data
		for line in lines:
			line = line.split('\t')
			frame.append(int(line[0]))
			rmsd.append(float(line[1]))

		return frame, rmsd
