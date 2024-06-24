import pygame
pygame.init()
pygame.mixer.music.load('Coisas Aleatórias/AUUU.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
x = input('Digite algo para parar a musica...')