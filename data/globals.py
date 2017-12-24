# Global Values
# Values used in several functions
import pygame

pygame.init()

# Constants
BLACK = (0, 0, 0)
GREY = (192, 192, 192)
WHITE = (255, 255, 255)
BLUE = (91, 154, 255)
ORANGE = (247, 157, 66)
GREEN = (0, 159, 18)
RED = (196, 0, 0)
YELLOW = (255, 238, 0)
PURPLE = (205, 43, 255)
FONT_BIG = pygame.font.Font(None, 40)
FONT_SMALL = pygame.font.SysFont(None, 20, False, True)
FONT_BOLD = pygame.font.SysFont(None, 40, True, False)
FONT_ITALIC = pygame.font.SysFont(None, 40, False, True)
FONT_BOLD_ITALIC = pygame.font.SysFont(None, 40, True, True)

# Variables
superloop = True
playero_charvalue = None
playert_charvalue = None
game_modevalue = None
screen = pygame.display.set_mode((500, 600))
playarea = pygame.Rect(5, 5, 490, 490)
