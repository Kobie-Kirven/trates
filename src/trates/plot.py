
import matplotlib
import matplotlib.pyplot as plt	
from .smooth import Smooth


class Plot:

	def plotData(datFile, outFile, dataType, smooth=1):
		data = Plot._getDatData(datFile)
		data = list(data)
		for i in range(len(data[0])):
			data[0][i] = ((data[0][i]*5000)*2)/1000000

		if smooth >1:
			data = Smooth.slidingWindow(data[1],data[0],smooth)
		#Create the plot
		fig, ax = plt.subplots()
		ax.plot(data[0], data[1])

		if dataType.lower() == "rmsd": 
			#label the axies
			ax.set(xlabel='Time (ns)', ylabel='RMSD',
			       title='RMSD Over Time')

		elif dataType.lower() == "contacts":
			#label the axies
			ax.set(xlabel='Time (ns)', ylabel='Native Contacts',
			       title='Native Contacts Over Time')
		
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