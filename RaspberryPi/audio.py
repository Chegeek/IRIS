'''
This file contains algorithms related to audio output. During navigation, the user receives audio feedback (turn-by-turn
navigation information) over the earphone.

@author: chen-zhuo
'''

'''
Plays an audio file over the earphone. The audio file is specified by 'fileNameWithPath'.

@param fileNameWithPath
           e.g. '~/Desktop/IRIS/RaspberryPi/Audio Files/Go Straight.mp3'
'''
import pygame.mixer
from pygame.mixer import Sound
from threading import Thread
import random

pygame.mixer.init()

#fileDir = '/home/pi/Documents/sound.mp3'

#turnR.play()

def playNum(fileDir):
    if fileDir == '/home/pi/Documents/sound.mp3':
        Thread(target = loadBGM).start()
    else:
        num = Sound(fileDir)
        pygame.mixer.music.set_volume(0.5)
        num.play()

musicList = ['sound.mp3']

def loadBGM():
    bgm = random.choice(musicList)
    pygame.mixer.music.set_volume(0.9)

    pygame.mixer.music.load('/home/pi/Documents/sound.mp3')
    playBGM()

def playBGM():
    pygame.mixer.music.play()

#while the user is waiting
#def playMusic():
#Thread(target = loadBGM).start()
Thread(target = playNum(fileDir)).start()
print "music end"


if __name__ == '__main__':
    pass
