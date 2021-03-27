class Smooth:

	def smoothPlot(numbersList, frameList, smoothLength):
		smoothList = []
		miniList = []
		counter = 0
		for number in numbersList:
			counter += 1
			if counter % smoothLength == 0:
				miniList.append(number)
				average = sum(miniList) / len(miniList)
				smoothList.append(average)
				miniList = []
				counter = 0

			else:
				miniList.append(number)

		frames = []
		counter = 0
		for frame in frameList:
			counter += 1
			if counter % smoothLength == 0:
				frames.append(frame)


		return frames, smoothList
