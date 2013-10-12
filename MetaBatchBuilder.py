import numpy

class MetaBatchBuilder:
	def __init__(self, serializer):
		self.serializer = serializer
	
	def build(self, imgList, classNames, fileToSave):
		meta = {}
		imgSize = imgList[0].getArray().shape[0]
		meta['num_vis'] = imgSize
		meta['data_in_rows'] = True
		meta['label_names'] = classNames
		meta['data_mean'] = self.calculateMean(imgList, imgSize).reshape(-1,1)
		self.serializer.write(fileToSave, meta)
	
	def calculateMean(self, imgList, imgSize):
		total = numpy.zeros(imgSize)
		for img in imgList:
			total += img.getArray()
		return total / len(imgList)
