#!/usr/bin/env python
class IntentStatus:
		StatusErrorType = ""
		def getStatusErrorType(self):
				return self.StatusErrorType
		def createIntentStatus(self, statusObject):
			self.statusErrorType = statusObject['errorType']
		def getErrorType(self):
			print'errorType is: ' , self.statusErrorType
			return self.statusErrorType
