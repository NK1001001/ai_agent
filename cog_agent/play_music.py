#!/usr/bin/env python

import pygame as pg
import os
from os import listdir
from os.path import isfile, join
import re

currentMusicFile = None
def playMusic(filename, volume=0.8):
    freq = 44100
    bitsize = 16
    channels = 2
    buffer = 2048
    pg.mixer.init(freq,bitsize, channels, buffer)
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        foundMusicFile = findFile(filename, '/home/roscon/Music')
        print 'Found Music File: ', foundMusicFile
        #print 'Guns: ', foundMusicFile['Guns']
        #if any(filename in string for string in foundMusicFile):
       # print [s for s in foundMusicFile if filename in s]
        #print 'list of music files', foundMusicFile
        #pg.mixer.music.load(filename)
        if foundMusicFile == None:
            print 'could not find the requested file'
            return
        pg.mixer.music.load('/home/roscon/Music/'+foundMusicFile)
        print 'Music file {} loaded', format(foundMusicFile)
        global currentMusicFile
        currentMusicFile= foundMusicFile
    except pg.error:
        print 'File {} not found ', format(foundMusicFile)
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        clock.tick(30)
def findFile(fileName, path):
    #onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print 'file name to find is: \n', fileName

    cleanName = re.sub('[^A-Za-z0-9]+', ' ', fileName)
    cleanName = cleanName.lower()
    print 'name after cleaning: ', cleanName
    for file in os.listdir(path):
        cleanFile = re.sub('[^A-Za-z0-9]+',' ', file)
        cleanFile = cleanFile.lower()
        print 'cleanFile name is: ' ,cleanFile
        if cleanName in cleanFile:
            print cleanFile

            return file
        #print '\t file is: ', file



  #  print 'here is the list of files: ', onlyfiles
    return None


#filename = "~/Music/Guns\ N\ Roses\ -\ Sweet\ Child\ O\ Mine.mp3"
filename = "Guns.mp3"
#print 'file in: ', findFile(filename, '/home/roscon/Music')
if __name__ == '__play_music__':
    playMusic(filename)
