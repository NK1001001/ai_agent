#!/usr/bin/env python	

class ResultParameters:
	def __init__(self, parameters):
		print 'parameters are: ', parameters 
		self.parameters = parameters
	def getParameters(self, param):
		return self.parameters.get(param,'bad_param')

		
