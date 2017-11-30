import pygame
import media

pygame.init()

# Colors
black = (0, 0, 0)
grey = (192, 192, 192)
white = (255, 255, 255)
blue = (91, 154, 255)
orange = (247, 157, 66)
green = (0, 159, 18)
red = (196, 0, 0)
yellow = (255, 238, 0)
purple = (205, 43, 255)

# Character Determining Variables
P1Char = 1
P2Char = 2

# Restart function
superloop = True

# Fonts/Rects
font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 20)
playarea = pygame.Rect(5, 5, 490, 490)
