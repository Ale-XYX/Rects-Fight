# GLOBAL
import pygame

pygame.init()

# Colors
BLACK = (0, 0, 0)
GREY = (192, 192, 192)
WHITE = (255, 255, 255)
BLUE = (91, 154, 255)
ORANGE = (247, 157, 66)
GREEN = (0, 159, 18)
RED = (196, 0, 0)
YELLOW = (255, 238, 0)
PURPLE = (205, 43, 255)

# Game
SUPERLOOP = True
P1CHAR = None
P2CHAR = None
MODE = None
EGG = False

# Fonts and other game items
FONTNORMAL = pygame.font.Font(None, 40)
FONTSMALL = pygame.font.SysFont(None, 20, False, True)
FONTB = pygame.font.SysFont(None, 40, True, False)
FONTI = pygame.font.SysFont(None, 40, False, True)
FONTIB = pygame.font.SysFont(None, 40, True, True)
PLAY_AREA = pygame.Rect(5, 5, 490, 490)
SCREEN = pygame.display.set_mode((500, 600))

print('█', end='', flush=True)


