# GAME
import pygame
import sys

import GLOBAL as g
import MEDIA as m
import SPRITES as s
import DICT as d

pygame.init()

pygame.display.set_caption('Rects Fight')
pygame.display.set_icon(m.MEDIA['icon'])

# TITLE SCREEN
def TITLE_SCREEN():
    CLOCK = pygame.time.Clock()
    LOOP = True
    TIME = True
    DT = CLOCK.tick(60) / 1000
    TIMER = 10

    while LOOP:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    LOOP = False
                    m.MEDIA['start_sound'].play()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
        keys = pygame.key.get_pressed()
        # Subtract Time/Detect When Timer Ends
        if TIME:
            TIMER -= DT
            if TIMER <= 0:
                TIME = False
        if keys[pygame.K_RSHIFT] and not TIME:
            g.EGG = True
            LOOP = False
            
        # Drawing
        m.SCREEN.fill(g.BLACK)
        m.SCREEN.blit(m.MEDIA['title'], (0, 0))
        if not TIME:
            m.SCREEN.blit(m.MEDIA['egtg'], (200, 100))
        pygame.display.flip()
        CLOCK.tick(60)

# MODE SELECT
def MODE_SELECT():
    CLOCK = pygame.time.Clock()
    LOOP = True
    ALL_SPRITES = pygame.sprite.Group()
    SELECTOR_BIG = s.SELECTOR_BIG((250, 250))
    MODE_CHOICES = ['CLASSIC', 'CHAOS']
    ALL_SPRITES.add(SELECTOR_BIG)
    TEXTS1 = g.FONTNORMAL.render('Choose Mode', True, g.WHITE)
    TEXTS2 = g.FONTNORMAL.render('Space To Continue', True, g.WHITE) 
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
                    g.MODE = MODE_CHOICES[SELECTOR]
                    d.GAME_DICT['MODE'][g.MODE]['SOUND'].play()
                    LOOP = False
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    SELECTOR %= len(MODE_CHOICES)
                    g.MODE = MODE_CHOICES[SELECTOR]
                    m.MEDIA['select_sound'].play()
        ALL_SPRITES.update()

        # Drawing
        m.SCREEN.fill(g.BLACK)
        m.SCREEN.blit(m.MEDIA['classic_card'], (150, 200))
        m.SCREEN.blit(m.MEDIA['chaos_card'], (150, 300))
        m.SCREEN.blit(TEXTS1, (155, 100))
        m.SCREEN.blit(TEXTS2, (120, 500))
        ALL_SPRITES.draw(m.SCREEN)

        pygame.display.flip()
        CLOCK.tick(60)

# CHARACTER SELECT
def CHARACTER_SELECT():
    def GET(INSERT):
        IMAGE = d.GAME_DICT[INSERT.upper()]['PLAYER_IMAGE']
        COLOR = d.GAME_DICT[INSERT.upper()]['COLOR']
        TEXT = g.FONTNORMAL.render(INSERT, True, COLOR)
        return IMAGE, TEXT
    COLOR_CHOICES = ['Blue', 'Orange', 'Green', 'Yellow', 'Red', 'Purple', 'Grey', 'White', 'Rainbow']
    PLAYER1 = 0
    PLAYER2 = 1
    TEXTS1 = g.FONTNORMAL.render('Choose Your Character', True, g.WHITE)
    TEXTS2 = g.FONTNORMAL.render('Space To Continue', True, g.WHITE)
    TEXTS3 = g.FONTIB.render('VS.', True, g.WHITE)
    ALL_SPRITES = pygame.sprite.Group()
    PLAYER1_IMAGE, TEXT1 = GET(COLOR_CHOICES[PLAYER1])
    PLAYER2_IMAGE, TEXT2 = GET(COLOR_CHOICES[PLAYER2])
    SELECTORA = s.SELECTOR((30, 188))
    SELECTORB = s.SELECTOR((85, 388))
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
                    g.P1CHAR = COLOR_CHOICES[PLAYER1]
                    g.P2CHAR = COLOR_CHOICES[PLAYER2]
                    LOOP = False
                if event.key in (pygame.K_d, pygame.K_a, pygame.K_RIGHT, pygame.K_LEFT):
                    PLAYER1 %= len(COLOR_CHOICES)
                    PLAYER2 %= len(COLOR_CHOICES)
                    PLAYER1_IMAGE, TEXT1 = GET(COLOR_CHOICES[PLAYER1])
                    PLAYER2_IMAGE, TEXT2 = GET(COLOR_CHOICES[PLAYER2])
                    m.MEDIA['select_sound'].play()
        ALL_SPRITES.update()

        # Drawing GUI
        m.SCREEN.fill(g.BLACK)
        m.SCREEN.blit(TEXTS1, (90, 50))
        m.SCREEN.blit(TEXTS2, (120, 500))
        m.SCREEN.blit(TEXTS3, (230, 275))
        m.SCREEN.blit(TEXT1, (d.GAME_DICT[COLOR_CHOICES[PLAYER1].upper()]['LOCAL'], 218))
        m.SCREEN.blit(TEXT2, (d.GAME_DICT[COLOR_CHOICES[PLAYER2].upper()]['LOCAL'], 330))
        
        m.SCREEN.blit(m.MEDIA['blue_face'], (5, 163))
        m.SCREEN.blit(m.MEDIA['orange_face'], (60, 163))
        m.SCREEN.blit(m.MEDIA['green_face'], (115, 163))
        m.SCREEN.blit(m.MEDIA['yellow_face'], (170, 163))
        m.SCREEN.blit(m.MEDIA['red_face'], (225, 163))
        m.SCREEN.blit(m.MEDIA['purple_face'], (280, 163))
        m.SCREEN.blit(m.MEDIA['grey_face'], (335, 163))
        m.SCREEN.blit(m.MEDIA['white_face'], (390, 163))
        m.SCREEN.blit(m.MEDIA['rainbow_face'], (445, 163))
        
        m.SCREEN.blit(m.MEDIA['blue_face'], (60 - 55, 363))
        m.SCREEN.blit(m.MEDIA['orange_face'], (115 - 55, 363))
        m.SCREEN.blit(m.MEDIA['green_face'], (170 - 55, 363))
        m.SCREEN.blit(m.MEDIA['yellow_face'], (225 - 55, 363))
        m.SCREEN.blit(m.MEDIA['red_face'], (280 - 55, 363))
        m.SCREEN.blit(m.MEDIA['purple_face'], (335 - 55, 363))
        m.SCREEN.blit(m.MEDIA['grey_face'], (390 - 55, 363))
        m.SCREEN.blit(m.MEDIA['white_face'], (390, 363))
        m.SCREEN.blit(m.MEDIA['rainbow_face'], (445, 363))
        
        ALL_SPRITES.draw(m.SCREEN)
        
        pygame.display.flip()
        CLOCK.tick(60)

# GAME
def GAME():
    # Game Variables
    ALL_SPRITES = pygame.sprite.Group()
    BULLETS1 = pygame.sprite.Group()
    BULLETS2 = pygame.sprite.Group()
    CLOCK = pygame.time.Clock()
    TEXTS1 = g.FONTSMALL.render('Player 1', True, d.GAME_DICT[g.P1CHAR.upper()]['COLOR'])
    TEXTS2 = g.FONTSMALL.render('Player 2', True, d.GAME_DICT[g.P2CHAR.upper()]['COLOR'])
    TEXTS3 = g.FONTSMALL.render('Escape to leave', True, g.WHITE)
    TEXTS4 = g.FONTSMALL.render('Enter to restart', True, g.WHITE)        
    # Using the variable where mode is stored to set game conditions
    GAME_MUSIC = d.GAME_DICT['MODE'][g.MODE]['MUSIC']
    g.TIMER = d.GAME_DICT['MODE'][g.MODE]['TIMER']
    PLAYER_VELOCITY = d.GAME_DICT['MODE'][g.MODE]['PLAYER_VELOCITY']
    BULLET_VELOCITY = d.GAME_DICT['MODE'][g.MODE]['BULLET_VELOCITY']
    PLAYER1 = s.RECT((35, 35), BULLETS2, (BULLET_VELOCITY, 0), g.P1CHAR, ALL_SPRITES)
    PLAYER2 = s.RECT((465, 465), BULLETS1, (-BULLET_VELOCITY, 0), g.P2CHAR, ALL_SPRITES)
    PLAYER1.health = d.GAME_DICT['MODE'][g.MODE]['HEALTH']
    PLAYER2.health = d.GAME_DICT['MODE'][g.MODE]['HEALTH']
    DT_COOLDOWN = d.GAME_DICT['MODE'][g.MODE]['DT']
    # Bools
    LOOP = True
    TIME = True
    ABILITY1 = False
    ABILITY2 = False
    COOLDOWN1 = 3
    COOLDOWN2 = 3
    TIME1 = True
    TIME2 = True
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
                'PLAYER1': [BULLETS1, ALL_SPRITES, PLAYER1.rect.center, pygame.math.Vector2(PLAYER1.fire_direction), m.MEDIA['blue_big_bullet']],
                'PLAYER2': [BULLETS2, ALL_SPRITES, PLAYER2.rect.center, pygame.math.Vector2(PLAYER2.fire_direction), m.MEDIA['blue_big_bullet']]},
            'ORANGE': {
                'PLAYER1': [BULLETS1, ALL_SPRITES, PLAYER1.rect.center, pygame.math.Vector2(PLAYER1.fire_direction), m.MEDIA['orange_big_bullet']],
                'PLAYER2': [BULLETS2, ALL_SPRITES, PLAYER2.rect.center, pygame.math.Vector2(PLAYER2.fire_direction), m.MEDIA['orange_big_bullet']]},
            'GREEN': {
                'PLAYER1': [BULLETS1, ALL_SPRITES, PLAYER1.rect.center, pygame.math.Vector2(PLAYER1.fire_direction), m.MEDIA['green_split_bullet'], 'GREEN'],
                'PLAYER2': [BULLETS2, ALL_SPRITES, PLAYER2.rect.center, pygame.math.Vector2(PLAYER2.fire_direction), m.MEDIA['green_split_bullet'], 'GREEN']},
            'PURPLE': {
                'PLAYER1': [BULLETS1, ALL_SPRITES, PLAYER1.rect.center, pygame.math.Vector2(PLAYER1.fire_direction), 'PURPLE'],
                'PLAYER2': [BULLETS2, ALL_SPRITES, PLAYER2.rect.center, pygame.math.Vector2(PLAYER2.fire_direction), 'PURPLE']},
            'RED': {
                'PLAYER1': [BULLETS1, ALL_SPRITES, PLAYER1.rect.center, pygame.math.Vector2(PLAYER1.fire_direction), 'RED'],
                'PLAYER2': [BULLETS2, ALL_SPRITES, PLAYER2.rect.center, pygame.math.Vector2(PLAYER2.fire_direction), 'RED']},
            'YELLOW': {
                'PLAYER1': [BULLETS1, ALL_SPRITES, PLAYER1.rect.center, pygame.math.Vector2(PLAYER1.fire_direction), m.MEDIA['yellow_split_bullet'], 'YELLOW'],
                'PLAYER2': [BULLETS2, ALL_SPRITES, PLAYER2.rect.center, pygame.math.Vector2(PLAYER2.fire_direction), m.MEDIA['yellow_split_bullet'], 'YELLOW']},
            'GREY': {
                'PLAYER1': [BULLETS1, ALL_SPRITES, PLAYER1.rect.center, pygame.math.Vector2(PLAYER1.fire_direction), m.MEDIA['grey_boomerang_bullet']],
                'PLAYER2': [BULLETS2, ALL_SPRITES, PLAYER2.rect.center, pygame.math.Vector2(PLAYER2.fire_direction), m.MEDIA['grey_boomerang_bullet']]},
            'RAINBOW': {
                'PLAYER1': [BULLETS1, ALL_SPRITES, PLAYER1.rect.center],
                'PLAYER2': [BULLETS2, ALL_SPRITES, PLAYER2.rect.center]},
            'WHITE': {
                'PLAYER1': [BULLETS1, ALL_SPRITES, PLAYER1.rect.center, pygame.math.Vector2(PLAYER1.fire_direction), m.MEDIA['white_boomerang_bullet']],
                'PLAYER2': [BULLETS2, ALL_SPRITES, PLAYER2.rect.center, pygame.math.Vector2(PLAYER2.fire_direction), m.MEDIA['white_boomerang_bullet']]},
        }
        P1PARAMS = ARGS_DICT[g.P1CHAR.upper()]['PLAYER1']
        P2PARAMS = ARGS_DICT[g.P2CHAR.upper()]['PLAYER2']
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g.SUPERLOOP = False
                LOOP = False
            # Keymap
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and not PLAYER1.toggle:
                    BULLET = s.BULLET(PLAYER1.rect.center, pygame.math.Vector2(PLAYER1.fire_direction), PLAYER1.bullet_image)
                    BULLETS1.add(BULLET)
                    ALL_SPRITES.add(BULLET)
                    m.MEDIA['shoot_sound'].play()
                if event.key == pygame.K_SPACE and not PLAYER2.toggle:
                    BULLET = s.BULLET(PLAYER2.rect.center, pygame.math.Vector2(PLAYER2.fire_direction), PLAYER2.bullet_image)
                    BULLETS2.add(BULLET)
                    ALL_SPRITES.add(BULLET)
                    m.MEDIA['shoot_sound'].play()
                if event.key == pygame.K_RCTRL and not PLAYER2.toggle and ABILITY2:
                    d.GAME_DICT[g.P2CHAR.upper()]['ABILITY'](*P2PARAMS)
                    COOLDOWN2 = 3
                    TIME2 = True
                    ABILITY2 = False
                if event.key == pygame.K_g and not PLAYER1.toggle and ABILITY1:
                    d.GAME_DICT[g.P1CHAR.upper()]['ABILITY'](*P1PARAMS)
                    COOLDOWN1 = 3
                    TIME1 = True
                    ABILITY1 = False
                if event.key == pygame.K_d and PLAYER1.toggle == False:
                    PLAYER1.vel.x = PLAYER_VELOCITY
                    PLAYER1.fire_direction = pygame.math.Vector2(BULLET_VELOCITY, 0)
                if event.key == pygame.K_a and PLAYER1.toggle == False:
                    PLAYER1.vel.x = -PLAYER_VELOCITY
                    PLAYER1.fire_direction = pygame.math.Vector2(-BULLET_VELOCITY, 0)
                if event.key == pygame.K_s and PLAYER1.toggle == False:
                    PLAYER1.vel.y = PLAYER_VELOCITY
                    PLAYER1.fire_direction = pygame.math.Vector2(0, BULLET_VELOCITY)
                if event.key == pygame.K_w and PLAYER1.toggle == False:
                    PLAYER1.vel.y = -PLAYER_VELOCITY
                    PLAYER1.fire_direction = pygame.math.Vector2(0, -BULLET_VELOCITY)
                if event.key == pygame.K_RIGHT and PLAYER2.toggle == False:
                    PLAYER2.vel.x = PLAYER_VELOCITY
                    PLAYER2.fire_direction = pygame.math.Vector2(BULLET_VELOCITY, 0)
                if event.key == pygame.K_LEFT and PLAYER2.toggle == False:
                    PLAYER2.vel.x = -PLAYER_VELOCITY
                    PLAYER2.fire_direction = pygame.math.Vector2(-BULLET_VELOCITY, 0)                   
                if event.key == pygame.K_DOWN and PLAYER2.toggle == False:
                    PLAYER2.vel.y = PLAYER_VELOCITY
                    PLAYER2.fire_direction = pygame.math.Vector2(0, BULLET_VELOCITY)
                if event.key == pygame.K_UP and PLAYER2.toggle == False:
                    PLAYER2.vel.y = -PLAYER_VELOCITY
                    PLAYER2.fire_direction = pygame.math.Vector2(0, -BULLET_VELOCITY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    PLAYER1.vel.x = VELOCITY_RESET
                if event.key == pygame.K_a:
                    PLAYER1.vel.x = VELOCITY_RESET
                if event.key == pygame.K_s:
                    PLAYER1.vel.y = VELOCITY_RESET
                if event.key == pygame.K_w:
                    PLAYER1.vel.y = VELOCITY_RESET
                if event.key == pygame.K_RIGHT:
                    PLAYER2.vel.x = VELOCITY_RESET
                if event.key == pygame.K_LEFT:
                    PLAYER2.vel.x = VELOCITY_RESET
                if event.key == pygame.K_DOWN:
                    PLAYER2.vel.y = VELOCITY_RESET
                if event.key == pygame.K_UP:
                    PLAYER2.vel.y = VELOCITY_RESET
        # Code that runs on first iteration
        if ON_START:
            m.MEDIA['fight_sound'].play()
            GAME_MUSIC.play()
            ON_START = False
            
        # Pause Function, stops all game movement
        if keys[pygame.K_TAB] and not CONFIRM and ON_END:
            PLAYER1.toggle = True
            PLAYER2.toggle = True
            CONFIRM = True
            TIME = False
            for BULLET in BULLETS1:
                BULLET.toggle = True
            for BULLET in BULLETS2:
                BULLET.toggle = True
            pygame.mixer.pause()
            m.MEDIA['pause_sound'].play()

        # Cancel Pause
        elif keys[pygame.K_LSHIFT] and CONFIRM:
            PLAYER1.toggle = False
            PLAYER2.toggle = False
            CONFIRM = False
            TIME = True
            for BULLET in BULLETS1:
                BULLET.toggle = False
            for BULLET in BULLETS2:
                BULLET.toggle = False
            pygame.mixer.unpause()
            m.MEDIA['pause_sound'].play()

        # Exit Game
        elif keys[pygame.K_ESCAPE] and CONFIRM:
            g.SUPERLOOP = False
            LOOP = False

        # Restarting Game
        elif keys[pygame.K_RETURN] and CONFIRM:
            GAME_MUSIC.stop()
            LOOP = False

        # Subtracting time, setting text, checking if timer has run out, more leaving/restart functions
        if TIME:
            g.TIMER -= DT
            TXT = d.GAME_DICT['TIMER'][g.TIMER < 10][1].render(str(round(g.TIMER, 1)), True, d.GAME_DICT['TIMER'][g.TIMER < 10][0])
            if g.TIMER <= 0:
                PLAYER1.toggle = True
                PLAYER2.toggle = True
                for BULLET in BULLETS1:
                    BULLET.toggle = True
                for BULLET in BULLETS2:
                    BULLET.toggle = True
                GAME_MUSIC.stop()
                TIME = False
                ON_END = False
                TEXT_LOCAL = (190, 530)
                TXT = g.FONTNORMAL.render('Times Up!', True, g.GREY)
                m.MEDIA['die_sound'].play()
            if not TIME and keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            elif not TIME and keys[pygame.K_RETURN] and not CONFIRM:
                pygame.mixer.pause()
                LOOP = False
                
        # Subtracts cooldown/detects when cooldown is 0       
        if TIME1:
            COOLDOWN1 -= DT_COOLDOWN
            if COOLDOWN1 <= 0:
                TIME1 = False
                ABILITY1 = True
                
        if TIME2:
            COOLDOWN2 -= DT_COOLDOWN
            if COOLDOWN2 <= 0:
                TIME2 = False
                ABILITY2 = True
        
        # Outcome is Player 2 Wins
        if PLAYER1.health <= 0:
            TXT = g.FONTNORMAL.render('Player 2 Wins!', True, PLAYER2.color)
            TEXT_LOCAL = (155, 530)
            TIME = False
            TIME1 = False
            TIME2 = False
            ON_END = False
            GAME_MUSIC.stop()
            if keys[pygame.K_ESCAPE] and not CONFIRM:
                g.SUPERLOOP = False
                LOOP = False
            elif keys[pygame.K_RETURN] and not CONFIRM:
                LOOP = False
                
        # Outcome if Player 1 Wins
        if PLAYER2.health <= 0:
            TXT = g.FONTNORMAL.render('Player 1 Wins!', True, PLAYER1.color)
            TEXT_LOCAL = (155, 530)
            TIME = False
            TIME1 = False
            TIME2 = False
            ON_END = False
            GAME_MUSIC.stop()
            if keys[pygame.K_ESCAPE] and not CONFIRM:
                g.SUPERLOOP = False
                LOOP = False
            elif keys[pygame.K_RETURN] and not CONFIRM:
                LOOP = False

        # Outcome of draw
        if PLAYER1.health <= 0 and PLAYER2.health <= 0:
            TXT = g.FONTNORMAL.render('Draw!', True, v.GREY)
            TEXT_LOCAL = (210, 530)
            TIME = False
            TIME1 = False
            TIME2 = False
            ON_END = False
            GAME_MUSIC.stop()
            if keys[pygame.K_ESCAPE] and not CONFIRM:
                g.SUPERLOOP = False
                LOOP = False
            elif keys[pygame.K_RETURN] and not CONFIRM:
                LOOP = False
        ALL_SPRITES.update()
        
        # Drawing Sprites/Bullets/GUI
        m.SCREEN.fill(g.BLACK)
        m.SCREEN.blit(m.MEDIA['wall'], (0, 0))
        m.SCREEN.blit(pygame.transform.flip(d.GAME_DICT['HP'][PLAYER1.health], True, False), (20, 530))
        m.SCREEN.blit(d.GAME_DICT['HP'][PLAYER2.health], (380, 530))
        m.SCREEN.blit(TXT, TEXT_LOCAL)
        m.SCREEN.blit(TEXTS1, (19, 515))
        m.SCREEN.blit(TEXTS2, (429, 515))
        # Cooldown blitting [Probaly Will Optimize with GAME_DICT]
        if COOLDOWN1 <= 3 and COOLDOWN1 >= 2:
            m.SCREEN.blit(m.MEDIA['cooldown3'], (100, 515))
        elif COOLDOWN1 <= 2 and COOLDOWN1 >= 1:
            m.SCREEN.blit(m.MEDIA['cooldown2'], (100, 515))
        elif COOLDOWN1 <= 1 and COOLDOWN1 >= 0:
            m.SCREEN.blit(m.MEDIA['cooldown1'], (100, 515))
        elif COOLDOWN1 <= 0:
            m.SCREEN.blit(m.MEDIA['cooldown0'], (100, 515))
            
        if COOLDOWN2 <= 3 and COOLDOWN2 >= 2:
            m.SCREEN.blit(m.MEDIA['cooldown3'], (380, 515))
        elif COOLDOWN2 <= 2 and COOLDOWN2 >= 1:
            m.SCREEN.blit(m.MEDIA['cooldown2'], (380, 515))
        elif COOLDOWN2 <= 1 and COOLDOWN2 >= 0:
            m.SCREEN.blit(m.MEDIA['cooldown1'], (380, 515))
        elif COOLDOWN2 <= 0:
            m.SCREEN.blit(m.MEDIA['cooldown0'], (380, 515))
        ALL_SPRITES.draw(m.SCREEN)
        if not ON_END:
            m.SCREEN.blit(TEXTS3, (395, 10))
            m.SCREEN.blit(TEXTS4, (10, 10))
        if CONFIRM:
            m.SCREEN.blit(m.MEDIA['paused'], (154, 165))
                
        pygame.display.flip()
        CLOCK.tick(60)

# Easter egg page :)            
def EGG():
    LOOP = True
    CLOCK = pygame.time.Clock()
    FONTS1 = g.FONTNORMAL.render('All Sounds from freesound.org', True, g.WHITE)
    while LOOP:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        m.SCREEN.fill(g.BLACK)
        m.SCREEN.blit(m.MEDIA['egg'], (0, 100))
        m.SCREEN.blit(FONTS1, (40, 10))
        
        pygame.display.flip()
        CLOCK.tick(60)            
            
            
            
    
                    
    
    
                
                
                    
    
        
