from statistics import mean

class Smooth:

	def smoothPlot(numbersList, frameList, smoothLength):
		smoothList, miniList = [], []
		counter = 0
		for number in numbersList:
			counter += 1
			if counter % smoothLength == 0:
				miniList.append(number)
				smoothList.append(mean(miniList))
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

	def slidingWindow(numbersList, frameList, slidingWindow):
		smoothList = []
		frames = []
		i = 0
		while i <= (len(numbersList) - slidingWindow):
			smoothList.append(mean(numbersList[i:(i + slidingWindow + 1)]))
			frames.append(frameList[i])
			i += 1

		return frames, smoothList


