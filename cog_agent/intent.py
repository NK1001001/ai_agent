#!/usr/bin/env python
from play_music import playMusic
import json
from intent_result import IntentResult
from intent_status import IntentStatus

class Intent:
    def __init__(self, data):
        print 'Json response is: ', data
        json_obj = json.loads(data)
        self.UUID = 0
        self.Action = "none"
        self.Object = " "
        self.intentResult = IntentResult(json_obj['result'])
        self.intentStatus = IntentStatus()
        self.intentStatus.createIntentStatus(json_obj['status'])
        self.intentName = self.intentResult.getIntentName()
    def getUUID(self):
        return self.UUID
    def handleIntent(self):
        print 'handling intent: ', self.intentName
        if self.intentName == 'playMusic':
            print 'intent: playMusic'
            musicArtist = self.intentResult.getParam('music-artist')
            playMusic(musicArtist)
            # if musicArtist == 'Guns N\' Roses':
            #     print 'music Artist is: Guns N Roses'
            #     print ' playing Guns N Roses!!!'
            #     #playMusic('Guns.mp3')
            #     playMusic(musicArtist)


    def getIntentName(self):
        #return self.intentResult.getIntentName()
        return self.intentName