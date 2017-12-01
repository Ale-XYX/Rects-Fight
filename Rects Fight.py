# Import packages
import pygame
import sys

# Import data
sys.path.insert(0, './data')
from fetch import *
import media32 as m32
import var as v
import sprites as s

pygame.init()

# Title Screen
def title():
    loop = True
    time = True
    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000
    timer = 20
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    loop = False
                    m32.MEDIA[32].play()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
        if time:
            timer -= dt
        if timer <= 0:
            time = False
        m32.screen.fill(v.black)
        m32.screen.blit(m32.MEDIA[22], (0, 0))
        if not time:
            m32.screen.blit(m32.MEDIA[10], (200, 100))
        pygame.display.flip()
        clock.tick(60)

# Character Select       
def charselect():
    loop = True
    clock = pygame.time.Clock()
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    v.P1Char += 1
                    if not v.P1Char == 8:
                        m32.MEDIA[30].play()
                elif event.key == pygame.K_s:
                    v.P1Char -= 1
                    if not v.P2Char == 0:
                        m32.MEDIA[30].play()
                if event.key == pygame.K_UP:
                    v.P2Char += 1
                    if not v.P2Char == 8:
                        m32.MEDIA[30].play()
                elif event.key == pygame.K_DOWN:
                    v.P2Char -= 1
                    if not v.P2Char == 0:
                        m32.MEDIA[30].play()
                if event.key == pygame.K_SPACE:
                    loop = False
        if v.P1Char == 8:
            v.P1Char -= 1
        elif v.P1Char == 0:
            v.P1Char += 1
        if v.P2Char == 8:
            v.P2Char -= 1
        elif v.P2Char == 0:
            v.P2Char += 1
        text1 = Fetch('text', 'player', 'player1', None, None)
        text2 = Fetch('text', 'player', 'player2', None, None)
        textS1 = v.font.render('Choose Your Character', True, v.white)
        textS2 = v.font.render('Space To Continue', True, v.white)
        textS3 = v.font.render('Player 1: ', True, v.white)
        textS4 = v.font.render('Player 2: ', True, v.white)
        m32.screen.fill(v.black)
        m32.screen.blit(textS1, (100, 50))
        m32.screen.blit(textS2, (125, 500))
        m32.screen.blit(textS3, (115, 225))
        m32.screen.blit(textS4, (115, 325))
        m32.screen.blit(text1, (240, 225))
        m32.screen.blit(text2, (240, 325))
        m32.screen.blit(Fetch('player', 'player1', 'image', None, None), (355, 210))
        m32.screen.blit(Fetch('player', 'player2', 'image', None, None), (355, 310))
        pygame.display.flip()
        clock.tick(60)

# Game
def main():
    # Game Variables
    all_sprites = pygame.sprite.Group()
    bullets1 = pygame.sprite.Group()
    bullets2 = pygame.sprite.Group()
    player1 = s.Player((35, 35), bullets2, Fetch('player', 'player1', 'image', None, None), (8, 0), all_sprites)
    player2 = s.Player((465, 465), bullets1, Fetch('player', 'player2', 'image', None, None), (-8, 0), all_sprites)
    clock = pygame.time.Clock()
    textstatic1 = v.font2.render('Player 1', True, v.white)
    textstatic2 = v.font2.render('Player 2', True, v.white)
    textstatic3 = v.font2.render('Escape to leave', True, v.white)
    textstatic4 = v.font2.render('Enter to restart', True, v.white)
    # Conditionals
    loop = True
    time = True
    onStart = True
    onEnd = True
    confirm = False
    # Integers
    vel = 8
    vel_reset = 0
    timer = 30
    dt = clock.tick(60) / 1000
    textlocal = (222, 520)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                v.superloop = False
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and player1.toggle == False:
                    bullet = s.Bullet(player1.rect.center, pygame.math.Vector2(player1.fire_direction), Fetch('player', 'player1', 'bullet', None, None))
                    m32.MEDIA[31].play()
                    bullets1.add(bullet)
                    all_sprites.add(bullet)
                if event.key == pygame.K_SPACE and player2.toggle == False:
                    bullet = s.Bullet(player2.rect.center, pygame.math.Vector2(player2.fire_direction), Fetch('player', 'player2', 'bullet', None, None))
                    m32.MEDIA[31].play()
                    bullets2.add(bullet)
                    all_sprites.add(bullet)
                if event.key == pygame.K_d and player1.toggle == False:
                    player1.vel.x = 5
                    player1.fire_direction = pygame.math.Vector2(vel, 0)
                if event.key == pygame.K_a and player1.toggle == False:
                    player1.vel.x = -5
                    player1.fire_direction = pygame.math.Vector2(-vel, 0)
                if event.key == pygame.K_s and player1.toggle == False:
                    player1.vel.y = 5
                    player1.fire_direction = pygame.math.Vector2(0, vel)
                if event.key == pygame.K_w and player1.toggle == False:
                    player1.vel.y = -5
                    player1.fire_direction = pygame.math.Vector2(0, -vel)
                if event.key == pygame.K_RIGHT and player2.toggle == False:
                    player2.vel.x = 5
                    player2.fire_direction = pygame.math.Vector2(vel, 0)
                if event.key == pygame.K_LEFT and player2.toggle == False:
                    player2.vel.x = -5
                    player2.fire_direction = pygame.math.Vector2(-vel, 0)
                if event.key == pygame.K_DOWN and player2.toggle == False:
                    player2.vel.y = 5
                    player2.fire_direction = pygame.math.Vector2(0, vel)
                if event.key == pygame.K_UP and player2.toggle == False:
                    player2.vel.y = -5
                    player2.fire_direction = pygame.math.Vector2(0, -vel)
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
            m32.MEDIA[26].play()
            m32.MEDIA[28].play()
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
            m32.MEDIA[29].play()
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
            m32.MEDIA[29].play()
        elif keys[pygame.K_ESCAPE] and confirm:
            v.superloop = False
            loop = False
        elif keys[pygame.K_RETURN] and confirm:
            m32.MEDIA[28].stop()
            loop = False
        if time:
            timer -= dt
            txt = v.font.render(str(round(timer, 1)), True, Fetch('text', 'timer', None, timer, None))
            if timer <= 0:
                player1.toggle = True
                player2.toggle = True
                for bullet in bullets1:
                    bullet.toggle = True
                for bullet in bullets2:
                    bullet.toggle = True
                m32.MEDIA[25].play()
                m32.MEDIA[28].stop()
                time = False
                onEnd = False
                textlocal = (190, 530)
                txt = v.font.render('Times Up!', True, v.grey)
        if not time and keys[pygame.K_ESCAPE]:
            v.superloop = False
            loop = False
        elif not time and keys[pygame.K_RETURN] and not confirm:
            m32.MEDIA[28].stop()
            loop = False
        if player1.health == 0:
            txt = v.font.render('Player 2 Wins!', True, Fetch('text', 'playerColor', None, player2, player1))
            textlocal = (155, 530)
            time = False
            onEnd = False
            m32.MEDIA[28].stop()
            if keys[pygame.K_ESCAPE] and not confirm:
                v.superloop = False
                loop = False
            elif keys[pygame.K_RETURN] and not confirm:
                loop = False
            # Player 2 Outcome
        if player2.health == 0:
            txt = v.font.render('Player 1 Wins!', True, Fetch('text', 'playerColor', None, player2, player1))
            textlocal = (155, 530)
            time = False
            onEnd = False
            m32.MEDIA[28].stop()
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
            m32.MEDIA[28].stop()
            if keys[pygame.K_ESCAPE] and not confirm:
                v.superloop = False
                loop = False
            elif keys[pygame.K_RETURN] and not confirm:
                loop = False
        # Drawing
        all_sprites.update()
        m32.screen.fill(v.black)
        m32.screen.blit(m32.MEDIA[23], (0, 0))
        m32.screen.blit(Fetch('player', 'player1', 'hp', player1, player2), (20, 530))
        m32.screen.blit(Fetch('player', 'player2', 'hp', player1, player2), (380, 530))
        m32.screen.blit(txt, textlocal)
        m32.screen.blit(textstatic1, (19, 515))
        m32.screen.blit(textstatic2, (429, 515))
        all_sprites.draw(m32.screen)
        if not onEnd:
            m32.screen.blit(textstatic3, (395, 10))
            m32.screen.blit(textstatic4, (10, 10))
        if confirm:
            m32.screen.blit(m32.MEDIA[19], (154, 165))
        pygame.display.flip()
        clock.tick(60)

# Game Sequence        
if __name__ == '__main__':
    title()
    charselect()
    while v.superloop:
        main()
    pygame.quit()
    
            
            
                
                    
                    
                
                
        
