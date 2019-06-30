import pygame

def PlayBeep(soundFile):
    pygame.mixer.init()
    pygame.mixer.music.load('sounds/{0}'.format(soundFile))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
