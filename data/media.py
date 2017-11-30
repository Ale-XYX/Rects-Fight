import pygame
import os
screen = pygame.display.set_mode((500, 600))
pygame.init()
# Blue Medialist
blue = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media','image', 'blue.png')).convert_alpha()
bulletblue = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'bulletblue.png')).convert_alpha()
# Orange Medialist
orange = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'orange.png')).convert_alpha()
bulletorange = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'bulletorange.png')).convert_alpha()
# Green Medialist
green = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'green.png')).convert_alpha()
bulletgreen = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'bulletgreen.png')).convert_alpha()
# Purple Medialist
purple = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'purple.png')).convert_alpha()
bulletpurple = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'bulletpurple.png')).convert_alpha()
# Red Medialist
red = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'red.png')).convert_alpha()
bulletred = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'bulletred.png')).convert_alpha()
# Grey Medialist
grey = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'grey.png')).convert_alpha()
bulletgrey = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'bulletgrey.png')).convert_alpha()
# Yellow Medialist
yellow = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'yellow.png')).convert_alpha()
bulletyellow = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'bulletyellow.png')).convert_alpha()
# HP Medialist
hp1 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'hp1.png')).convert_alpha()
hp2 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'hp2.png')).convert_alpha()
hp3 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'hp3.png')).convert_alpha()
dead = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'dead.png')).convert_alpha()
# Game Medialist
paused = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'paused.png')).convert_alpha()
title = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'title.png')).convert_alpha()
wall = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'wall.png')).convert_alpha()
icon = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'icon.png')).convert_alpha()
etge = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'egtg.png')).convert_alpha()
error = pygame.image.load(os.path.join(os.path.dirname(__file__), 'media', 'image', 'error.png')).convert_alpha()
# Game Soundlist
pause = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'media', 'audio', 'pause.wav'))
fight = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'media', 'audio', 'fight.wav'))
music = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'media', 'audio', 'music.wav'))
select = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'media', 'audio', 'select.wav'))
start = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'media', 'audio', 'start.wav'))
# Player Soundlist
shoot = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'media', 'audio', 'shoot.wav'))
hit = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'media', 'audio', 'hit.wav'))
die = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'media', 'audio', 'die.wav'))
# Screen
pygame.display.set_caption('Rects Fight!')
pygame.display.set_icon(icon)
