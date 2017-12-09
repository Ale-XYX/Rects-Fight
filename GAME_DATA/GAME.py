# GAME
import pygame
import sys
import random

import GLOBAL as G
import SPRITES as S
import DICT as D

pygame.init()

pygame.display.set_caption('Rects Fight')
pygame.display.set_icon(D.MEDIA['icon'])

# TITLE SCREEN
def TITLE_SCREEN():
    CLOCK = pygame.time.Clock()
    LOOP = True
    TIME = True
    TIMER = 10
    DT = CLOCK.tick(60) / 1000

    while LOOP:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    LOOP = False
                    D.MEDIA['start_sound'].play()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
        keys = pygame.key.get_pressed()
        # Subtract Time/Detect When Timer Ends
        if TIME:
            TIMER -= DT
            if TIMER <= 0:
                TIME = False
        if keys[pygame.K_RSHIFT] and not TIME:
            G.EGG = True
            LOOP = False
            
        # Drawing
        G.SCREEN.fill(G.BLACK)
        G.SCREEN.blit(D.MEDIA['title'], (0, 0))
        if not TIME:
            G.SCREEN.blit(D.MEDIA['egtg'], (200, 100))
        pygame.display.flip()
        CLOCK.tick(60)

# MODE SELECT
def MODE_SELECT():
    CLOCK = pygame.time.Clock()
    LOOP = True
    ALL_SPRITES = pygame.sprite.Group()
    SELECTOR_BIG = S.SELECTOR_BIG((250, 250))
    MODE_CHOICES = ['CLASSIC', 'CHAOS']
    ALL_SPRITES.add(SELECTOR_BIG)
    TEXTS1 = G.FONTNORMAL.render('Choose Mode', True, G.WHITE)
    TEXTS2 = G.FONTNORMAL.render('Space To Continue', True, G.WHITE) 
    SELECTOR = 0

    while LOOP:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Keymap
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    SELECTOR += 1
                    SELECTOR_BIG.pos[1] -= 100
                if event.key == pygame.K_DOWN:
                    SELECTOR -= 1
                    SELECTOR_BIG.pos[1] += 100
                if event.key == pygame.K_SPACE:
                    # Load Mode into variable to use later
                    G.MODE = MODE_CHOICES[SELECTOR]
                    D.GAME_DICT['MODE'][G.MODE]['SOUND'].play()
                    LOOP = False
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    SELECTOR %= len(MODE_CHOICES)
                    G.MODE = MODE_CHOICES[SELECTOR]
                    D.MEDIA['select_sound'].play()
        ALL_SPRITES.update()

        # Drawing
        G.SCREEN.fill(G.BLACK)
        G.SCREEN.blit(D.MEDIA['classic_card'], (150, 200))
        G.SCREEN.blit(D.MEDIA['chaos_card'], (150, 300))
        G.SCREEN.blit(TEXTS1, (155, 100))
        G.SCREEN.blit(TEXTS2, (120, 500))
        ALL_SPRITES.draw(G.SCREEN)

        pygame.display.flip()
        CLOCK.tick(60)

# CHARACTER SELECT
def CHARACTER_SELECT():
    def GET(INSERT):
        IMAGE = D.GAME_DICT[INSERT.upper()]['PLAYER_IMAGE']
        COLOR = D.GAME_DICT[INSERT.upper()]['COLOR']
        TEXT = G.FONTNORMAL.render(INSERT, True, COLOR)
        return IMAGE, TEXT
    COLOR_CHOICES = ['Blue', 'Orange', 'Green', 'Yellow', 'Red', 'Purple', 'Grey', 'White', 'Rainbow']
    PLAYER1 = 0
    PLAYER2 = 1
    TEXTS1 = G.FONTNORMAL.render('Choose Your Character', True, G.WHITE)
    TEXTS2 = G.FONTNORMAL.render('Space To Continue', True, G.WHITE)
    TEXTS3 = G.FONTIB.render('VS.', True, G.WHITE)
    ALL_SPRITES = pygame.sprite.Group()
    PLAYER1_IMAGE, TEXT1 = GET(COLOR_CHOICES[PLAYER1])
    PLAYER2_IMAGE, TEXT2 = GET(COLOR_CHOICES[PLAYER2])
    SELECTORA = S.SELECTOR((30, 188))
    SELECTORB = S.SELECTOR((85, 388))
    ALL_SPRITES.add(SELECTORA, SELECTORB)
    CLOCK = pygame.time.Clock()
    LOOP = True

    while LOOP:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # Keymap
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    PLAYER1 += 1
                    SELECTORA.pos[0] += 55
                elif event.key == pygame.K_a:
                    PLAYER1 -= 1
                    SELECTORA.pos[0] -= 55
                if event.key == pygame.K_RIGHT:
                    PLAYER2 += 1
                    SELECTORB.pos[0] += 55
                elif event.key == pygame.K_LEFT:
                    PLAYER2 -= 1
                    SELECTORB.pos[0] -= 55
                if event.key == pygame.K_SPACE:
                    # Load Character choice into variable to use later
                    G.P1CHAR = COLOR_CHOICES[PLAYER1]
                    G.P2CHAR = COLOR_CHOICES[PLAYER2]
                    LOOP = False
                if event.key in (pygame.K_d, pygame.K_a, pygame.K_RIGHT, pygame.K_LEFT):
                    PLAYER1 %= len(COLOR_CHOICES)
                    PLAYER2 %= len(COLOR_CHOICES)
                    PLAYER1_IMAGE, TEXT1 = GET(COLOR_CHOICES[PLAYER1])
                    PLAYER2_IMAGE, TEXT2 = GET(COLOR_CHOICES[PLAYER2])
                    D.MEDIA['select_sound'].play()
        ALL_SPRITES.update()

        # Drawing GUI
        G.SCREEN.fill(G.BLACK)
        G.SCREEN.blit(TEXTS1, (90, 50))
        G.SCREEN.blit(TEXTS2, (120, 500))
        G.SCREEN.blit(TEXTS3, (230, 275))
        G.SCREEN.blit(TEXT1, (D.GAME_DICT[COLOR_CHOICES[PLAYER1].upper()]['LOCAL'], 218))
        G.SCREEN.blit(TEXT2, (D.GAME_DICT[COLOR_CHOICES[PLAYER2].upper()]['LOCAL'], 330))
        
        G.SCREEN.blit(D.MEDIA['blue_face'], (5, 163))
        G.SCREEN.blit(D.MEDIA['orange_face'], (60, 163))
        G.SCREEN.blit(D.MEDIA['green_face'], (115, 163))
        G.SCREEN.blit(D.MEDIA['yellow_face'], (170, 163))
        G.SCREEN.blit(D.MEDIA['red_face'], (225, 163))
        G.SCREEN.blit(D.MEDIA['purple_face'], (280, 163))
        G.SCREEN.blit(D.MEDIA['grey_face'], (335, 163))
        G.SCREEN.blit(D.MEDIA['white_face'], (390, 163))
        G.SCREEN.blit(D.MEDIA['rainbow_face'], (445, 163))
        
        G.SCREEN.blit(D.MEDIA['blue_face'], (60 - 55, 363))
        G.SCREEN.blit(D.MEDIA['orange_face'], (115 - 55, 363))
        G.SCREEN.blit(D.MEDIA['green_face'], (170 - 55, 363))
        G.SCREEN.blit(D.MEDIA['yellow_face'], (225 - 55, 363))
        G.SCREEN.blit(D.MEDIA['red_face'], (280 - 55, 363))
        G.SCREEN.blit(D.MEDIA['purple_face'], (335 - 55, 363))
        G.SCREEN.blit(D.MEDIA['grey_face'], (390 - 55, 363))
        G.SCREEN.blit(D.MEDIA['white_face'], (390, 363))
        G.SCREEN.blit(D.MEDIA['rainbow_face'], (445, 363))
        
        ALL_SPRITES.draw(G.SCREEN)
        
        pygame.display.flip()
        CLOCK.tick(60)

# GAME
def GAME():
    # Game Variables
    ALL_SPRITES = pygame.sprite.Group()
    BULLETS_1 = pygame.sprite.Group()
    BULLETS_2 = pygame.sprite.Group()
    CLOCK = pygame.time.Clock()
    TEXTS1 = G.FONTSMALL.render('Player 1', True, D.GAME_DICT[G.P1CHAR.upper()]['COLOR'])
    TEXTS2 = G.FONTSMALL.render('Player 2', True, D.GAME_DICT[G.P2CHAR.upper()]['COLOR'])
    TEXTS3 = G.FONTSMALL.render('Escape to leave', True, G.WHITE)
    TEXTS4 = G.FONTSMALL.render('Enter to restart', True, G.WHITE)        
    # Using the variable where mode is stored to set game conditions
    GAME_MUSIC = D.GAME_DICT['MODE'][G.MODE]['MUSIC']
    TIMER = D.GAME_DICT['MODE'][G.MODE]['TIMER']
    PLAYER_VELOCITY = D.GAME_DICT['MODE'][G.MODE]['PLAYER_VELOCITY']
    BULLET_VELOCITY = D.GAME_DICT['MODE'][G.MODE]['BULLET_VELOCITY']
    PLAYER_1 = S.RECT((35, 35), BULLETS_2, (BULLET_VELOCITY, 0), G.P1CHAR, ALL_SPRITES)
    PLAYER_2 = S.RECT((465, 465), BULLETS_1, (-BULLET_VELOCITY, 0), G.P2CHAR, ALL_SPRITES)
    PLAYER_1.health = D.GAME_DICT['MODE'][G.MODE]['HEALTH']
    PLAYER_2.health = D.GAME_DICT['MODE'][G.MODE]['HEALTH']
    DT_COOLDOWN = D.GAME_DICT['MODE'][G.MODE]['DT']
    # Bools
    LOOP = True
    TIME = True
    ABILITY_1 = False
    ABILITY_2 = False
    COOLDOWN_1 = 3
    COOLDOWN_2 = 3
    TIME_1 = True
    TIME_2 = True
    ON_START = True
    ON_END = True
    CONFIRM = False
    # Integers
    VELOCITY_RESET = 0
    DT = CLOCK.tick(60) / 1000
    TEXT_LOCAL = (222, 520)
    
    while LOOP:
        keys = pygame.key.get_pressed()
        # PARAMS [NEEDS TO BE REFRESHED
        ARGS_DICT = {
            'BLUE': {
                'PLAYER1': [BULLETS_1, ALL_SPRITES, PLAYER_1.rect.center, (PLAYER_1.fire_direction), D.MEDIA['blue_big_bullet'], 'BIG_BULLET', D.GAME_DICT],
                'PLAYER2': [BULLETS_2, ALL_SPRITES, PLAYER_2.rect.center, (PLAYER_2.fire_direction), D.MEDIA['blue_big_bullet'], 'BIG_BULLET', D.GAME_DICT]},
            'ORANGE': {
                'PLAYER1': [BULLETS_1, ALL_SPRITES, PLAYER_1.rect.center, (PLAYER_1.fire_direction), D.MEDIA['orange_big_bullet'], 'BIG_BULLET', D.GAME_DICT],
                'PLAYER2': [BULLETS_2, ALL_SPRITES, PLAYER_2.rect.center, (PLAYER_2.fire_direction), D.MEDIA['orange_big_bullet'], 'BIG_BULLET', D.GAME_DICT]},
            'GREEN': {
                'PLAYER1': [BULLETS_1, ALL_SPRITES, PLAYER_1.rect.center, (PLAYER_1.fire_direction), D.MEDIA['green_split_bullet'], 'GREEN'],
                'PLAYER2': [BULLETS_2, ALL_SPRITES, PLAYER_2.rect.center, (PLAYER_2.fire_direction), D.MEDIA['green_split_bullet'], 'GREEN']},
            'PURPLE': {
                'PLAYER1': [BULLETS_1, ALL_SPRITES, PLAYER_1.rect.center, (PLAYER_1.fire_direction), 'PURPLE'],
                'PLAYER2': [BULLETS_2, ALL_SPRITES, PLAYER_2.rect.center, (PLAYER_2.fire_direction), 'PURPLE']},
            'RED': {
                'PLAYER1': [BULLETS_1, ALL_SPRITES, PLAYER_1.rect.center, (PLAYER_1.fire_direction), 'RED'],
                'PLAYER2': [BULLETS_2, ALL_SPRITES, PLAYER_2.rect.center, (PLAYER_2.fire_direction), 'RED']},
            'YELLOW': {
                'PLAYER1': [BULLETS_1, ALL_SPRITES, PLAYER_1.rect.center, (PLAYER_1.fire_direction), D.MEDIA['yellow_split_bullet'], 'YELLOW'],
                'PLAYER2': [BULLETS_2, ALL_SPRITES, PLAYER_2.rect.center, (PLAYER_2.fire_direction), D.MEDIA['yellow_split_bullet'], 'YELLOW']},
            'GREY': {
                'PLAYER1': [BULLETS_1, ALL_SPRITES, PLAYER_1.rect.center, (PLAYER_1.fire_direction), D.MEDIA['grey_boomerang_bullet'], 'GREY', D.GAME_DICT],
                'PLAYER2': [BULLETS_2, ALL_SPRITES, PLAYER_2.rect.center, (PLAYER_2.fire_direction), D.MEDIA['grey_boomerang_bullet'], 'GREY', D.GAME_DICT]},
            'RAINBOW': {
                'PLAYER1': [BULLETS_1, ALL_SPRITES, PLAYER_1.rect.center],
                'PLAYER2': [BULLETS_2, ALL_SPRITES, PLAYER_2.rect.center]},
            'WHITE': {
                'PLAYER1': [BULLETS_1, ALL_SPRITES, PLAYER_1.rect.center, (PLAYER_1.fire_direction), D.MEDIA['white_boomerang_bullet'], 'WHITE', D.GAME_DICT],
                'PLAYER2': [BULLETS_2, ALL_SPRITES, PLAYER_2.rect.center, (PLAYER_2.fire_direction), D.MEDIA['white_boomerang_bullet'], 'WHITE', D.GAME_DICT]},
        }
        P1_PARAMS = ARGS_DICT[G.P1CHAR.upper()]['PLAYER1']
        P2_PARAMS = ARGS_DICT[G.P2CHAR.upper()]['PLAYER2']
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                G.SUPERLOOP = False
                LOOP = False
            # Keymap
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and not PLAYER_1.toggle:
                    BULLET = S.BULLET(PLAYER_1.rect.center, (PLAYER_1.fire_direction), PLAYER_1.bullet_image, 'BULLET')
                    BULLETS_1.add(BULLET)
                    ALL_SPRITES.add(BULLET)
                    D.MEDIA['shoot_sound'].play()
                if event.key == pygame.K_SPACE and not PLAYER_2.toggle:
                    BULLET = S.BULLET(PLAYER_2.rect.center, (PLAYER_2.fire_direction), PLAYER_2.bullet_image, 'BULLET')
                    BULLETS_2.add(BULLET)
                    ALL_SPRITES.add(BULLET)
                    D.MEDIA['shoot_sound'].play()
                if event.key == pygame.K_e and not PLAYER_1.toggle and ABILITY_1:
                    D.GAME_DICT[G.P1CHAR.upper()]['ABILITY'](*P1_PARAMS)
                    TIME_1 = True
                    ABILITY_1 = False
                    COOLDOWN_1 = 3
                if event.key == pygame.K_RCTRL and not PLAYER_2.toggle and ABILITY_2:
                    D.GAME_DICT[G.P2CHAR.upper()]['ABILITY'](*P2_PARAMS)
                    TIME_2 = True
                    ABILITY_2 = False
                    COOLDOWN_2 = 3
                if event.key == pygame.K_d and PLAYER_1.toggle == False:
                    PLAYER_1.vel.x = PLAYER_VELOCITY
                    PLAYER_1.fire_direction = (BULLET_VELOCITY, 0)
                if event.key == pygame.K_a and PLAYER_1.toggle == False:
                    PLAYER_1.vel.x = -PLAYER_VELOCITY
                    PLAYER_1.fire_direction = (-BULLET_VELOCITY, 0)
                if event.key == pygame.K_s and PLAYER_1.toggle == False:
                    PLAYER_1.vel.y = PLAYER_VELOCITY
                    PLAYER_1.fire_direction = (0, BULLET_VELOCITY)
                if event.key == pygame.K_w and PLAYER_1.toggle == False:
                    PLAYER_1.vel.y = -PLAYER_VELOCITY
                    PLAYER_1.fire_direction = (0, -BULLET_VELOCITY)
                if event.key == pygame.K_RIGHT and PLAYER_2.toggle == False:
                    PLAYER_2.vel.x = PLAYER_VELOCITY
                    PLAYER_2.fire_direction = (BULLET_VELOCITY, 0)
                if event.key == pygame.K_LEFT and PLAYER_2.toggle == False:
                    PLAYER_2.vel.x = -PLAYER_VELOCITY
                    PLAYER_2.fire_direction = (-BULLET_VELOCITY, 0)                   
                if event.key == pygame.K_DOWN and PLAYER_2.toggle == False:
                    PLAYER_2.vel.y = PLAYER_VELOCITY
                    PLAYER_2.fire_direction = (0, BULLET_VELOCITY)
                if event.key == pygame.K_UP and PLAYER_2.toggle == False:
                    PLAYER_2.vel.y = -PLAYER_VELOCITY
                    PLAYER_2.fire_direction = (0, -BULLET_VELOCITY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    PLAYER_1.vel.x = VELOCITY_RESET
                if event.key == pygame.K_a:
                    PLAYER_1.vel.x = VELOCITY_RESET
                if event.key == pygame.K_s:
                    PLAYER_1.vel.y = VELOCITY_RESET
                if event.key == pygame.K_w:
                    PLAYER_1.vel.y = VELOCITY_RESET
                if event.key == pygame.K_RIGHT:
                    PLAYER_2.vel.x = VELOCITY_RESET
                if event.key == pygame.K_LEFT:
                    PLAYER_2.vel.x = VELOCITY_RESET
                if event.key == pygame.K_DOWN:
                    PLAYER_2.vel.y = VELOCITY_RESET
                if event.key == pygame.K_UP:
                    PLAYER_2.vel.y = VELOCITY_RESET
        # Code that runs on first iteration
        if ON_START:
            D.MEDIA['fight_sound'].play()
            GAME_MUSIC.play()
            ON_START = False
            
        # Pause Function, stops all game movement
        if keys[pygame.K_TAB] and not CONFIRM and ON_END:
            PLAYER_1.toggle = True
            PLAYER_2.toggle = True
            CONFIRM = True
            TIME = False
            for SPRITE in ALL_SPRITES:
                SPRITE.toggle = True
            pygame.mixer.pause()
            D.MEDIA['pause_sound'].play()

        # Cancel Pause
        elif keys[pygame.K_LSHIFT] and CONFIRM:
            PLAYER_1.toggle = False
            PLAYER_2.toggle = False
            CONFIRM = False
            TIME = True
            TIME_1 = False
            TIME_2 = False
            for SPRITE in ALL_SPRITES:
                SPRITE.toggle = False
            pygame.mixer.unpause()
            D.MEDIA['pause_sound'].play()

        # Exit Game
        elif keys[pygame.K_ESCAPE] and CONFIRM:
            G.SUPERLOOP = False
            LOOP = False

        # Restarting Game
        elif keys[pygame.K_RETURN] and CONFIRM:
            GAME_MUSIC.stop()
            LOOP = False

        # Subtracting time, setting text, checking if timer has run out, more leaving/restart functions
        if TIME:
            TIMER -= DT
            TXT = D.GAME_DICT['TIMER'][TIMER < 10][1].render(str(round(TIMER, 1)), True, D.GAME_DICT['TIMER'][TIMER < 10][0])
            if TIMER <= 0:
                for SPRITE in ALL_SPRITES:
                    SPRITE.toggle = True
                GAME_MUSIC.stop()
                TIME = False
                TIME_1 = False
                TIME_2 = False
                ON_END = False
                TEXT_LOCAL = (190, 530)
                TXT = G.FONTNORMAL.render('Times Up!', True, G.GREY)
                D.MEDIA['die_sound'].play()
        if not TIME and keys[pygame.K_ESCAPE]:
            G.SUPERLOOP = False
            LOOP = False
        elif not TIME and keys[pygame.K_RETURN] and not CONFIRM:
            GAME_MUSIC.stop()
            LOOP = False
                
        # Subtracts cooldown/detects when cooldown is 0       
        if TIME_1:
            COOLDOWN_1 -= DT_COOLDOWN
            if COOLDOWN_1 <= 0:
                TIME_1 = False
                ABILITY_1 = True         
        if TIME_2:
            COOLDOWN_2 -= DT_COOLDOWN
            if COOLDOWN_2 <= 0:
                TIME_2 = False
                ABILITY_2 = True
            
        # Outcome is Player 2 Wins
        if PLAYER_1.health <= 0:
            TXT = G.FONTNORMAL.render('Player 2 Wins!', True, PLAYER_2.color)
            TEXT_LOCAL = (155, 530)
            TIME = False
            TIME_1 = False
            TIME_2 = False
            ON_END = False
            GAME_MUSIC.stop()
            if keys[pygame.K_ESCAPE] and not CONFIRM:
                G.SUPERLOOP = False
                LOOP = False
            elif keys[pygame.K_RETURN] and not CONFIRM:
                LOOP = False
                
        # Outcome if Player 1 Wins
        if PLAYER_2.health <= 0:
            TXT = G.FONTNORMAL.render('Player 1 Wins!', True, PLAYER_1.color)
            TEXT_LOCAL = (155, 530)
            TIME = False
            TIME_1 = False
            TIME_2 = False
            ON_END = False
            GAME_MUSIC.stop()
            if keys[pygame.K_ESCAPE] and not CONFIRM:
                G.SUPERLOOP = False
                LOOP = False
            elif keys[pygame.K_RETURN] and not CONFIRM:
                LOOP = False

        # Outcome of draw
        if PLAYER_1.health <= 0 and PLAYER_2.health <= 0:
            TXT = G.FONTNORMAL.render('Draw!', True, v.GREY)
            TEXT_LOCAL = (210, 530)
            TIME = False
            TIME_1 = False
            TIME_2 = False
            ON_END = False
            GAME_MUSIC.stop()
            if keys[pygame.K_ESCAPE] and not CONFIRM:
                G.SUPERLOOP = False
                LOOP = False
            elif keys[pygame.K_RETURN] and not CONFIRM:
                LOOP = False
            
        ALL_SPRITES.update()
        
        # Drawing Sprites/Bullets/GUI
        G.SCREEN.fill(G.BLACK)
        G.SCREEN.blit(D.MEDIA['wall'], (0, 0))
        G.SCREEN.blit(pygame.transform.flip(D.GAME_DICT['HP'][PLAYER_1.health], True, False), (20, 530))
        G.SCREEN.blit(D.GAME_DICT['HP'][PLAYER_2.health], (380, 530))
        G.SCREEN.blit(TXT, TEXT_LOCAL)
        G.SCREEN.blit(TEXTS1, (19, 515))
        G.SCREEN.blit(TEXTS2, (429, 515))
        
        # Cooldown drawing
        if COOLDOWN_1 <= 3 and COOLDOWN_1 >= 2:
            G.SCREEN.blit(D.MEDIA['cooldown4'], (100, 515))
        elif COOLDOWN_1 <= 2 and COOLDOWN_1 >= 1:
            G.SCREEN.blit(D.MEDIA['cooldown3'], (100, 515))
        elif COOLDOWN_1 <= 1 and COOLDOWN_1 >= 0:
            G.SCREEN.blit(D.MEDIA['cooldown2'], (100, 515))
        elif COOLDOWN_1 <= 0:
            G.SCREEN.blit(D.MEDIA['cooldown1'], (100, 515))
            
        if COOLDOWN_2 <= 3 and COOLDOWN_2 >= 2:
            G.SCREEN.blit(D.MEDIA['cooldown4'], (380, 515))
        elif COOLDOWN_2 <= 2 and COOLDOWN_2 >= 1:
            G.SCREEN.blit(D.MEDIA['cooldown3'], (380, 515))
        elif COOLDOWN_2 <= 1 and COOLDOWN_2 >= 0:
            G.SCREEN.blit(D.MEDIA['cooldown2'], (380, 515))
        elif COOLDOWN_2 <= 0:
            G.SCREEN.blit(D.MEDIA['cooldown1'], (380, 515))

        ALL_SPRITES.draw(G.SCREEN)
        
        if not ON_END:
            G.SCREEN.blit(TEXTS3, (395, 10))
            G.SCREEN.blit(TEXTS4, (10, 10))
        if CONFIRM:
            G.SCREEN.blit(D.MEDIA['paused'], (154, 165))
                
        pygame.display.flip()
        CLOCK.tick(60)

# Easter egg page :)            
def EGG():
    LOOP = True
    CLOCK = pygame.time.Clock()
    FONTS1 = G.FONTNORMAL.render('All Sounds from freesound.org', True, G.WHITE)
    while LOOP:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        G.SCREEN.fill(G.BLACK)
        G.SCREEN.blit(D.MEDIA['egg'], (0, 100))
        G.SCREEN.blit(FONTS1, (40, 10))
        
        pygame.display.flip()
        CLOCK.tick(60)            
            
            
            
    
                    
    
    
                
                
                    
    
        
