# CLIENT
if __name__ == '__main__':
    print('Loading Rects Fight V2.0')
    # Import Modules
    import pygame
    import sys

    # Import Game Module [Which Loads Sprites, Global, Media, etc.]
    sys.path.insert(0, './GAME_DATA')
    import GAME as G

    pygame.init()

    # Game Sequence
    G.TITLE_SCREEN()
    if G.G.EGG:
        G.EGG()
    G.MODE_SELECT()
    G.CHARACTER_SELECT()
    while G.G.SUPERLOOP:
        G.GAME()
    
    pygame.quit()

