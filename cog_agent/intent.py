#!/usr/bin/env python
from play_music import playMusic
import json
from intent_result import IntentResult
from intent_status import IntentStatus

class Intent():
    def __init__(self, data):
        print 'Json response is: ', data
        json_obj = json.loads(data)
        self.UUID = 0
        self.Action = None
        self.Object = None
        self.PromptToUser = None

        self.Fulfillment = json_obj.get('fulfillment')
        self.intentResult = IntentResult(json_obj['result'])
        self.Action = self.intentResult.Result.get('action')
        self.intentStatus = IntentStatus()
        self.intentStatus.createIntentStatus(json_obj['status'])
        self.intentName = self.intentResult.getIntentName()
    def getUUID(self):
        return self.UUID
    def handleIntent(self):
        print 'handling intent: ', self.intentName
        if self.Action is not None:
            if self.Action == 'play-music':

                print 'intent: playMusic'
                musicArtist = self.intentResult.getParam('music-artist')
                intentResultFulfillment = self.intentResult.getResultFulfillment()
                if intentResultFulfillment is not None:
                    self.PromptToUser = intentResultFulfillment.get('speech')
                    self.PromptToUser += ' ' + musicArtist
                    print 'Prompt to user: ' , self.PromptToUser
                else:
                    print 'No Fulfillment object found in response'
                playMusic(musicArtist)
                # if musicArtist == 'Guns N\' Roses':
                #     print 'music Artist is: Guns N Roses'
                #     print ' playing Guns N Roses!!!'
                #     #playMusic('Guns.mp3')
                #     playMusic(musicArtist)


    def getIntentName(self):
        #return self.intentResult.getIntentName()
        return self.intentName