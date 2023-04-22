import pygame

file = ""

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(file)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue