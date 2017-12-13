# CLIENT
if __name__ == '__main__':
    import sys
    import subprocess
    import time

    print('Loading Rects Fight V2.0...')
    print('|', end='', flush=True)
    
    # Check if pygame is installed, if not install pygame
    # If os is not windows, then tell to manually install
    if str(sys.platform) == 'win32':
        try:
            import pygame
        except ModuleNotFoundError:
            print('X')
            print('Pygame is not installed! Installing...')
            
            subprocess.call(['py', '-m', 'pip', 'install', 'pygame'])       
            print('Finished, continuing load...')
            
            import pygame
    else:
        try:
            import pygame
        except ModuleNotFoundError:
            print('YOU ARE USING LINUX/MAC, PLEASE INSTALL PYGAME MANUALLY')
            
            time.sleep(3)
            sys.exit()
    
    # Import Game Module [Which Loads Sprites, Global, Media, etc.]
    sys.path.insert(0, './GAME_DATA')
    import GAME as G
    print('█|', end='', flush=True)
    
    pygame.init()

    # Game sequence [Runs all parts of the game in order
    G.TITLE_SCREEN()
    if G.G.EGG:
        G.EGG()
    G.MODE_SELECT()
    G.CHARACTER_SELECT()
    while G.G.SUPERLOOP:
        G.GAME()
    
    pygame.quit()

