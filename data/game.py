# Game
# Import packages
import pygame
import sys
import datetime
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'GAME: ' + 'Loaded Modules')

# Import data
import media as m
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'GAME: ' + 'Loaded Media')
import var as v
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'GAME: ' + 'Loaded Variables')
import sprites as s
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'GAME: ' + 'Loaded Sprites')
import func as f
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'GAME: ' + 'Loaded Functions')

pygame.init()

# Title Screen
def title():
    loop = True
    time = True
    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000
    timer = 5
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    loop = False
                    m.MEDIA['start'].play()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
        keys = pygame.key.get_pressed()
        if time:
            timer -= dt
        if timer <= 0:
            time = False
        if keys[pygame.K_RSHIFT] and not time:
                v.egg = True
                loop = False
        m.screen.fill(v.black)
        m.screen.blit(m.MEDIA['title'], (0, 0))
        if not time:
            m.screen.blit(m.MEDIA['egtg'], (200, 100))
        pygame.display.flip()
        clock.tick(60)
        
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'GAME: ' + 'Loaded Title')

def mode_select():
    loop = True
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    selectorbig = s.SelectorBig((250, 250))
    mode_choices = ['classic', 'aon', 'inverted']
    all_sprites.add(selectorbig)
    textS1 = v.font.render('Choose Mode', True, v.white)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    v.mode += 1
                    v.mode %= 3
                    print(v.mode)
                    selectorbig.pos[1] -= 100
                if event.key == pygame.K_DOWN:
                    v.mode -= 1
                    v.mode %= 3
                    print(v.mode)
                    selectorbig.pos[1] += 100
                if event.key == pygame.K_SPACE:
                    loop = False
                    if v.mode == 0:
                        m.MEDIA['classicaudio'].play()
                    elif v.mode == 1:
                        m.MEDIA['invertedaudio'].play()
                    elif v.mode == 2:
                        m.MEDIA['aonaudio'].play()
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    if selectorbig.pos[1] == 550:
                        selectorbig.pos[1] = 250
                    elif selectorbig.pos[1] == 150:
                        selectorbig.pos[1] = 450
                    m.MEDIA['select'].play()     
        all_sprites.update()
        m.screen.fill(v.black)
        m.screen.blit(m.MEDIA['classic'], (150, 200))
        m.screen.blit(m.MEDIA['aon'], (150, 300))
        m.screen.blit(m.MEDIA['invertedpic'], (150, 400))
        m.screen.blit(textS1, (155, 100))
        all_sprites.draw(m.screen)
        pygame.display.flip()
        clock.tick(60)

# Character Select [Credit to skrx]
def char_select():
    color_choices = ['Blue', 'Orange', 'Green', 'Purple', 'Red', 'Yellow', 'Grey']
    player1 = 0
    player2 = 1
    textS1 = v.font.render('Choose Your Character', True, v.white)
    textS2 = v.font.render('Space To Continue', True, v.white)
    textS3 = v.font3.render('VS.', True, v.white)
    all_sprites = pygame.sprite.Group()
    player1_image, text1 = f.get('char', color_choices[player1])
    player2_image, text2 = f.get('char', color_choices[player2])
    selectorA = s.Selector((85, 188))
    selectorB = s.Selector((140, 388))
    all_sprites.add(selectorA, selectorB)
    clock = pygame.time.Clock()
    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player1 += 1
                    selectorA.pos[0] += 55
                elif event.key == pygame.K_a:
                    player1 -= 1
                    selectorA.pos[0] -= 55
                if event.key == pygame.K_RIGHT:
                    player2 += 1
                    selectorB.pos[0] += 55
                elif event.key == pygame.K_LEFT:
                    player2 -= 1
                    selectorB.pos[0] -= 55
                if event.key in (pygame.K_d, pygame.K_a, pygame.K_RIGHT, pygame.K_LEFT):
                    player1 %= len(color_choices)
                    player2 %= len(color_choices)
                    player1_image, text1 = f.get('char', color_choices[player1])
                    player2_image, text2 = f.get('char', color_choices[player2])
                    m.MEDIA['select'].play()                    
                if event.key == pygame.K_SPACE:
                    v.P1Char = color_choices[player1]
                    v.P2Char = color_choices[player2]
                    loop = False
        all_sprites.update()
        
        m.screen.fill(v.black)
        m.screen.blit(textS1, (90, 50))
        m.screen.blit(textS2, (120, 500))
        m.screen.blit(textS3, (230, 275))
        m.screen.blit(text1, (f.get('local', player1), 218))
        m.screen.blit(text2, (f.get('local', player2), 330))
        
        m.screen.blit(m.MEDIA['blue'], (60, 163))
        m.screen.blit(m.MEDIA['orange'], (115, 163))
        m.screen.blit(m.MEDIA['green'], (170, 163))
        m.screen.blit(m.MEDIA['purple'], (225, 163))
        m.screen.blit(m.MEDIA['red'], (280, 163))
        m.screen.blit(m.MEDIA['yellow'], (335, 163))
        m.screen.blit(m.MEDIA['grey'], (390, 163))
        
        m.screen.blit(m.MEDIA['blue'], (60, 363))
        m.screen.blit(m.MEDIA['orange'], (115, 363))
        m.screen.blit(m.MEDIA['green'], (170, 363))
        m.screen.blit(m.MEDIA['purple'], (225, 363))
        m.screen.blit(m.MEDIA['red'], (280, 363))
        m.screen.blit(m.MEDIA['yellow'], (335, 363))
        m.screen.blit(m.MEDIA['grey'], (390, 363))
        all_sprites.draw(m.screen)
        m.screen.blit(m.MEDIA['charselborder'], (0, 0))
        
        pygame.display.flip()
        clock.tick(60)
        
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'GAME: ' + 'Loaded Character Select')

# Game
def main():
    # Game Variables
    all_sprites = pygame.sprite.Group()
    bullets1 = pygame.sprite.Group()
    bullets2 = pygame.sprite.Group()
    if v.mode == 0:
        timer = 30
        bvel = 8
        pvel = 5
    elif v.mode == 1:
        timer = 30
        pvel = -5
        bvel = -8
    elif v.mode == 2:
        timer = 10
        bvel = 15
    player1 = s.Player((35, 35), bullets2, (bvel, 0), v.P1Char, all_sprites)
    player2 = s.Player((465, 465), bullets1, (-bvel, 0), v.P2Char, all_sprites)
    clock = pygame.time.Clock()
    textstatic1 = v.font5.render('Player 1', True, v.white)
    textstatic2 = v.font5.render('Player 2', True, v.white)
    textstatic3 = v.font2.render('Escape to leave', True, v.white)
    textstatic4 = v.font2.render('Enter to restart', True, v.white)
    if v.mode == 2:
        player1.health = 1
        player2.health = 1    
    # Conditionals
    loop = True
    time = True
    onStart = True
    onEnd = True
    confirm = False
    # Integers
    vel_reset = 0
    dt = clock.tick(60) / 1000
    textlocal = (222, 520)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                v.superloop = False
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and player1.toggle == False:
                    bullet = s.Bullet(player1.rect.center, pygame.math.Vector2(player1.fire_direction), player1.bullet_image)
                    m.MEDIA['shoot'].play()
                    bullets1.add(bullet)
                    all_sprites.add(bullet)
                if event.key == pygame.K_SPACE and player2.toggle == False:
                    bullet = s.Bullet(player2.rect.center, pygame.math.Vector2(player2.fire_direction), player2.bullet_image)
                    m.MEDIA['shoot'].play()
                    bullets2.add(bullet)
                    all_sprites.add(bullet)
                if event.key == pygame.K_d and player1.toggle == False:
                    player1.vel.x = pvel
                    player1.fire_direction = pygame.math.Vector2(bvel, 0)
                if event.key == pygame.K_a and player1.toggle == False:
                    player1.vel.x = -pvel
                    player1.fire_direction = pygame.math.Vector2(-bvel, 0)
                if event.key == pygame.K_s and player1.toggle == False:
                    player1.vel.y = pvel
                    player1.fire_direction = pygame.math.Vector2(0, bvel)
                if event.key == pygame.K_w and player1.toggle == False:
                    player1.vel.y = -pvel
                    player1.fire_direction = pygame.math.Vector2(0, -bvel)
                if event.key == pygame.K_RIGHT and player2.toggle == False:
                    player2.vel.x = pvel
                    player2.fire_direction = pygame.math.Vector2(bvel, 0)
                if event.key == pygame.K_LEFT and player2.toggle == False:
                    player2.vel.x = -pvel
                    player2.fire_direction = pygame.math.Vector2(-bvel, 0)
                if event.key == pygame.K_DOWN and player2.toggle == False:
                    player2.vel.y = pvel
                    player2.fire_direction = pygame.math.Vector2(0, bvel)
                if event.key == pygame.K_UP and player2.toggle == False:
                    player2.vel.y = -pvel
                    player2.fire_direction = pygame.math.Vector2(0, -bvel)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player1.vel.x = vel_reset
                if event.key == pygame.K_a:
                    player1.vel.x = vel_reset
                if event.key == pygame.K_s:
                    player1.vel.y = vel_reset
                if event.key == pygame.K_w:
                    player1.vel.y = vel_reset
                if event.key == pygame.K_RIGHT:
                    player2.vel.x = vel_reset
                if event.key == pygame.K_LEFT:
                    player2.vel.x = vel_reset
                if event.key == pygame.K_DOWN:
                    player2.vel.y = vel_reset
                if event.key == pygame.K_UP:
                    player2.vel.y = vel_reset
        keys = pygame.key.get_pressed()
        if onStart:
            m.MEDIA['fight'].play()
            if v.mode == 0:
                m.MEDIA['music'].play()
            elif v.mode == 1:
                m.MEDIA['inverted'].play()
            elif v.mode == 2:
                m.MEDIA['panic'].play()
            else:
                m.MEDIA['music'].play()
            onStart = False
        if keys[pygame.K_TAB] and not confirm and onEnd:
            player1.toggle = True
            player2.toggle = True
            confirm = True
            time = False
            for bullet in bullets1:
                bullet.toggle = True
            for bullet in bullets2:
                bullet.toggle = True
            pygame.mixer.pause()
            m.MEDIA['pause'].play()
        elif keys[pygame.K_LSHIFT] and confirm:
            player1.toggle = False
            player2.toggle = False
            confirm = False
            time = True
            for bullet in bullets1:
                bullet.toggle = False
            for bullet in bullets2:
                bullet.toggle = False
            pygame.mixer.unpause()
            m.MEDIA['pause'].play()
        elif keys[pygame.K_ESCAPE] and confirm:
            v.superloop = False
            loop = False
        elif keys[pygame.K_RETURN] and confirm:
            if v.mode == 0:
                m.MEDIA['music'].stop()
            elif v.mode == 1:
                m.MEDIA['inverted'].stop()
            elif v.mode == 2:
                m.MEDIA['panic'].stop()
            else:
                m.MEDIA['music'].stop()
            loop = False
        if time:
            timer -= dt
            txt = f.get('time', timer)
            if timer <= 0:
                player1.toggle = True
                player2.toggle = True
                for bullet in bullets1:
                    bullet.toggle = True
                for bullet in bullets2:
                    bullet.toggle = True
                m.MEDIA['die'].play()
                if v.mode == 0:
                    m.MEDIA['music'].stop()
                elif v.mode == 1:
                    m.MEDIA['inverted'].stop()
                elif v.mode == 2:
                    m.MEDIA['panic'].stop()
                else:
                    m.MEDIA['music'].stop()
                time = False
                onEnd = False
                textlocal = (190, 530)
                txt = v.font.render('Times Up!', True, v.grey)
        if not time and keys[pygame.K_ESCAPE]:
            v.superloop = False
            loop = False
        elif not time and keys[pygame.K_RETURN] and not confirm:
            pygame.mixer.pause()
            loop = False
        if player1.health == 0:
            txt = v.font.render('Player 2 Wins!', True, player2.color)
            textlocal = (155, 530)
            time = False
            onEnd = False
            if v.mode == 0:
                m.MEDIA['music'].stop()
            elif v.mode == 1:
                m.MEDIA['inverted'].stop()
            elif v.mode == 2:
                m.MEDIA['panic'].stop()
            else:
                m.MEDIA['music'].stop()
            if keys[pygame.K_ESCAPE] and not confirm:
                v.superloop = False
                loop = False
            elif keys[pygame.K_RETURN] and not confirm:
                loop = False
            # Player 2 Outcome
        if player2.health == 0:
            txt = v.font.render('Player 1 Wins!', True, player1.color)
            textlocal = (155, 530)
            time = False
            onEnd = False
            if v.mode == 0:
                m.MEDIA['music'].stop()
            elif v.mode == 1:
                m.MEDIA['inverted'].stop()
            elif v.mode == 2:
                m.MEDIA['panic'].stop()
            else:
                m.MEDIA['music'].stop()
            if keys[pygame.K_ESCAPE] and not confirm:
                v.superloop = False
                loop = False
            if keys[pygame.K_RETURN] and not confirm:
                loop = False
        # Draw Outcome
        if player1.health == 0 and player2.health == 0:
            txt = v.font.render('Draw!', True, v.grey)
            textlocal = (210, 530)
            time = False
            onEnd = False
            if v.mode == 0:
                m.MEDIA['music'].stop()
            elif v.mode == 1:
                m.MEDIA['inverted'].play()
            elif v.mode == 2:
                m.MEDIA['panic'].stop()
            else:
                m.MEDIA['music'].stop()
            if keys[pygame.K_ESCAPE] and not confirm:
                v.superloop = False
                loop = False
            elif keys[pygame.K_RETURN] and not confirm:
                loop = False
        # Drawing
        all_sprites.update()
        m.screen.fill(v.black)
        m.screen.blit(m.MEDIA['wall'], (0, 0))
        m.screen.blit(f.get('hp1', player1), (20, 530))
        m.screen.blit(f.get('hp2', player2), (380, 530))
        m.screen.blit(txt, textlocal)
        m.screen.blit(textstatic1, (19, 515))
        m.screen.blit(textstatic2, (429, 515))
        all_sprites.draw(m.screen)
        if not onEnd:
            m.screen.blit(textstatic3, (395, 10))
            m.screen.blit(textstatic4, (10, 10))
        if confirm:
            m.screen.blit(m.MEDIA['paused'], (154, 165))
        pygame.display.flip()
        clock.tick(60)
def egg():
    loop = True
    clock = pygame.time.Clock()
    fontS1 = v.font.render('All Sounds from freesound.org', True, v.white)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        m.screen.fill(v.black)
        m.screen.blit(m.MEDIA['egg'], (0, 100))
        m.screen.blit(fontS1, (40, 10))
        
        pygame.display.flip()
        clock.tick(60)
        
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'GAME: ' + 'Loaded Main')
