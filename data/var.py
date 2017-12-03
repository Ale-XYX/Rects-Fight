import pygame
import datetime

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
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'VAR: ' + 'Loaded Colors')
# Restart function
superloop = True

# Determinating things
P1Char = None
P2Char = None
mode = 0
egg = False

# Fonts/Rects
font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 20)
font3 = pygame.font.SysFont(None, 40, True, True)
font4 = pygame.font.SysFont(None, 40, True, False)
font5 = pygame.font.SysFont(None, 20, False, True)
playarea = pygame.Rect(5, 5, 490, 490)
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'VAR: ' + 'Loaded Game Items')
