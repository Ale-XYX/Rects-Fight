import pygame
import os
screen = pygame.display.set_mode((500, 600))
pygame.init()
# Blue Medialist
blue = pygame.image.load(os.path.join('media', 'blue.png')).convert_alpha()
bulletblue = pygame.image.load(os.path.join('media', 'bulletblue.png')).convert_alpha()
# Orange Medialist
orange = pygame.image.load(os.path.join('media', 'orange.png')).convert_alpha()
bulletorange = pygame.image.load(os.path.join('media', 'bulletorange.png')).convert_alpha()
# Green Medialist
green = pygame.image.load(os.path.join('media', 'green.png')).convert_alpha()
bulletgreen = pygame.image.load(os.path.join('media', 'bulletgreen.png')).convert_alpha()
# Purple Medialist
purple = pygame.image.load(os.path.join('media', 'purple.png')).convert_alpha()
bulletpurple = pygame.image.load(os.path.join('media', 'bulletpurple.png')).convert_alpha()
# Red Medialist
red = pygame.image.load(os.path.join('media', 'red.png')).convert_alpha()
bulletred = pygame.image.load(os.path.join('media', 'bulletred.png')).convert_alpha()
# Grey Medialist
grey = pygame.image.load(os.path.join('media', 'grey.png')).convert_alpha()
bulletgrey = pygame.image.load(os.path.join('media', 'bulletgrey.png')).convert_alpha()
# Yellow Medialist
yellow = pygame.image.load(os.path.join('media', 'yellow.png')).convert_alpha()
bulletyellow = pygame.image.load(os.path.join('media', 'bulletyellow.png')).convert_alpha()
# HP Medialist
hp1 = pygame.image.load(os.path.join('media', 'hp1.png')).convert_alpha()
hp2 = pygame.image.load(os.path.join('media', 'hp2.png')).convert_alpha()
hp3 = pygame.image.load(os.path.join('media', 'hp3.png')).convert_alpha()
dead = pygame.image.load(os.path.join('media', 'dead.png')).convert_alpha()
# Player Soundlist
shoot = pygame.mixer.Sound(os.path.join('media', 'shoot.wav'))
hit = pygame.mixer.Sound(os.path.join('media', 'hit.wav'))
die = pygame.mixer.Sound(os.path.join('media', 'die.wav'))
# Game Medialist
paused = pygame.image.load(os.path.join('media', 'paused.png')).convert_alpha()
title = pygame.image.load(os.path.join('media', 'title.png')).convert_alpha()
wall = pygame.image.load(os.path.join('media', 'wall.png')).convert_alpha()
icon = pygame.image.load(os.path.join('media', 'icon.png')).convert_alpha()
etge = pygame.image.load(os.path.join('media', 'egtg.png')).convert_alpha()
error = pygame.image.load(os.path.join('media', 'error.png')).convert_alpha()
# Game Soundlist
pause = pygame.mixer.Sound(os.path.join('media', 'pause.wav'))
fight = pygame.mixer.Sound(os.path.join('media', 'fight.wav'))
music = pygame.mixer.Sound(os.path.join('media', 'music.wav'))
select = pygame.mixer.Sound(os.path.join('media', 'select.wav'))
start = pygame.mixer.Sound(os.path.join('media', 'start.wav'))
# Screen
pygame.display.set_caption('Rects Fight!')
pygame.display.set_icon(icon)
