#!/usr/bin/env python
from intent_result_parameters import ResultParameters


class IntentResult:
    def __init__(self, resultObject):
        self.Result = resultObject
        self.Parameters = ResultParameters(resultObject.get('parameters', 'no_param'))
        self.Action = resultObject.get('action', 'no_action')
        self.MetaData = self.Result.get('metadata', 'no_meta_data')
        self.IntentName = self.MetaData.get('intentName', 'no_intent_name')

    # self.Action = resultObject['action']
    # self.Parameters = resultObject['parameters']
    def createIntentResult(self, resultObject):
        self.Result = resultObject

    #		self.Action = resultObject['action']
    def getAction(self):
        return self.Action

	def getResult(self):
		return self.Result

    def getParam(self, param):
        return self.Parameters.getParameters(param)

    def getIntentName(self):
        return self.IntentName
