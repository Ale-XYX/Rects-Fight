# CLIENT
if __name__ == '__main__':
    import sys
    import subprocess
    import time

    print('Loading Rects Fight V2.0...', end='', flush=True)
    # Check if pygame is installed, if not install pygame
    # If os is not windows, then tell to manually install
    if str(sys.platform) == 'win32':
        try:
            import pygame
        except ModuleNotFoundError:
            print('X')
            print('Pygame is not installed! Installing...')
            subprocess.call(['py', '-m', 'pip', 'install', 'pygame'])
            print('Finished, continuing...')
            import pygame
    else:
        try:
            import pygame
        except ModuleNotFoundError:
            print('YOU ARE USING LINUX/MAC, PLEASE INSTALL PYGAME MANUALLY')
            time.sleep(3)
            sys.exit()

    # Import Game Module [Which Loads Sprites, Global, Media, etc.]
    sys.path.insert(0, './data')
    import game

    print('Done')

    pygame.init()

    pygame.init()
    game.title_screen()
    game.mode_select()
    game.char_select()
    game.main()
    pygame.quit()