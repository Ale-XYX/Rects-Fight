# CLIENT
if __name__ == '__main__':
    print('Loading Rects Fight V1.8')
    # Import Modules
    import pygame
    import sys

    sys.path.insert(0, './GAME_DATA')
    # Import Game Module [Which Loads Sprites, Global, Media, etc.]
    import GAME as g

    pygame.init()

    # Game Sequence
    g.TITLE_SCREEN()
    if g.g.EGG:
        g.EGG()
    g.MODE_SELECT()
    g.CHARACTER_SELECT()
    while g.g.SUPERLOOP:
        g.GAME()
    
    pygame.quit()

