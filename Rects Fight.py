# Import packages
import pygame
import sys

# Import data
sys.path.insert(0, './data')
from fetch import *
import media
import gamewide
import sprites

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
                    media.start.play()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
        if time:
            timer -= dt
        if timer <= 0:
            time = False
        media.screen.fill(gamewide.black)
        media.screen.blit(media.title, (0, 0))
        if not time:
            media.screen.blit(media.etge, (200, 100))
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
                    gamewide.P1Char += 1
                    if not gamewide.P1Char == 8:
                        media.select.play()
                elif event.key == pygame.K_s:
                    gamewide.P1Char -= 1
                    if not gamewide.P2Char == 0:
                        media.select.play()
                if event.key == pygame.K_UP:
                    gamewide.P2Char += 1
                    if not gamewide.P2Char == 8:
                        media.select.play()
                elif event.key == pygame.K_DOWN:
                    gamewide.P2Char -= 1
                    if not gamewide.P2Char == 0:
                        media.select.play()
                if event.key == pygame.K_SPACE:
                    loop = False
        if gamewide.P1Char == 8:
            gamewide.P1Char -= 1
        elif gamewide.P1Char == 0:
            gamewide.P1Char += 1
        if gamewide.P2Char == 8:
            gamewide.P2Char -= 1
        elif gamewide.P2Char == 0:
            gamewide.P2Char += 1
        text1 = Fetch('text', 'player', 'player1', None, None)
        text2 = Fetch('text', 'player', 'player2', None, None)
        textS1 = gamewide.font.render('Choose Your Character', True, gamewide.white)
        textS2 = gamewide.font.render('Space To Continue', True, gamewide.white)
        textS3 = gamewide.font.render('Player 1: ', True, gamewide.white)
        textS4 = gamewide.font.render('Player 2: ', True, gamewide.white)
        media.screen.fill(gamewide.black)
        media.screen.blit(textS1, (100, 50))
        media.screen.blit(textS2, (125, 500))
        media.screen.blit(textS3, (115, 225))
        media.screen.blit(textS4, (115, 325))
        media.screen.blit(text1, (240, 225))
        media.screen.blit(text2, (240, 325))
        media.screen.blit(Fetch('player', 'player1', 'image', None, None), (355, 210))
        media.screen.blit(Fetch('player', 'player2', 'image', None, None), (355, 310))
        pygame.display.flip()
        clock.tick(60)

# Game
def main():
    # Game Variables
    all_sprites = pygame.sprite.Group()
    bullets1 = pygame.sprite.Group()
    bullets2 = pygame.sprite.Group()
    player1 = sprites.Player((35, 35), bullets2, Fetch('player', 'player1', 'image', None, None), (8, 0), all_sprites)
    player2 = sprites.Player((465, 465), bullets1, Fetch('player', 'player2', 'image', None, None), (-8, 0), all_sprites)
    clock = pygame.time.Clock()
    textstatic1 = gamewide.font2.render('Player 1', True, gamewide.white)
    textstatic2 = gamewide.font2.render('Player 2', True, gamewide.white)
    textstatic3 = gamewide.font2.render('Escape to leave', True, gamewide.white)
    textstatic4 = gamewide.font2.render('Enter to restart', True, gamewide.white)
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
                gamewide.superloop = False
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and player1.toggle == False:
                    bullet = sprites.Bullet(player1.rect.center, pygame.math.Vector2(player1.fire_direction), Fetch('player', 'player1', 'bullet', None, None))
                    media.shoot.play()
                    bullets1.add(bullet)
                    all_sprites.add(bullet)
                if event.key == pygame.K_SPACE and player2.toggle == False:
                    bullet = sprites.Bullet(player2.rect.center, pygame.math.Vector2(player2.fire_direction), Fetch('player', 'player2', 'bullet', None, None))
                    media.shoot.play()
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
            media.fight.play()
            media.music.play()
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
            media.pause.play()
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
            media.pause.play()
        elif keys[pygame.K_ESCAPE] and confirm:
            gamewide.superloop = False
            loop = False
        elif keys[pygame.K_RETURN] and confirm:
            media.music.stop()
            loop = False
        if time:
            timer -= dt
            txt = gamewide.font.render(str(round(timer, 1)), True, Fetch('text', 'timer', None, timer, None))
            if timer <= 0:
                player1.toggle = True
                player2.toggle = True
                for bullet in bullets1:
                    bullet.toggle = True
                for bullet in bullets2:
                    bullet.toggle = True
                media.die.play()
                media.music.stop()
                time = False
                onEnd = False
                textlocal = (190, 530)
                txt = gamewide.font.render('Times Up!', True, gamewide.grey)
        if not time and keys[pygame.K_ESCAPE]:
            gamewide.superloop = False
            loop = False
        elif not time and keys[pygame.K_RETURN] and not confirm:
            media.music.stop()
            loop = False
        if player1.health == 0:
            txt = gamewide.font.render('Player 2 Wins!', True, Fetch('text', 'playerColor', None, player2, player1))
            textlocal = (155, 530)
            time = False
            onEnd = False
            media.music.stop()
            if keys[pygame.K_ESCAPE] and not confirm:
                gamewide.superloop = False
                loop = False
            elif keys[pygame.K_RETURN] and not confirm:
                media.music.stop()
                loop = False
            # Player 2 Outcome
        if player2.health == 0:
            txt = gamewide.font.render('Player 1 Wins!', True, Fetch('text', 'playerColor', None, player2, player1))
            textlocal = (155, 530)
            time = False
            onEnd = False
            media.music.stop()
            if keys[pygame.K_ESCAPE] and not confirm:
                gamewide.superloop = False
                loop = False
            if keys[pygame.K_RETURN] and not confirm:
                media.music.stop()
                loop = False
        # Draw Outcome
        if player1.health == 0 and player2.health == 0:
            txt = gamewide.font.render('Draw!', True, gamewide.grey)
            textlocal = (210, 530)
            time = False
            onEnd = False
            media.music.stop()
            if keys[pygame.K_ESCAPE] and not confirm:
                gamewide.superloop = False
                loop = False
            elif keys[pygame.K_RETURN] and not confirm:
                media.music.stop()
                loop = False
        # Drawing
        all_sprites.update()
        media.screen.fill(gamewide.black)
        media.screen.blit(media.wall, (0, 0))
        media.screen.blit(Fetch('player', 'player1', 'hp', player1, player2), (20, 530))
        media.screen.blit(Fetch('player', 'player2', 'hp', player1, player2), (380, 530))
        media.screen.blit(txt, textlocal)
        media.screen.blit(textstatic1, (19, 515))
        media.screen.blit(textstatic2, (429, 515))
        all_sprites.draw(media.screen)
        if not onEnd:
            media.screen.blit(textstatic3, (395, 10))
            media.screen.blit(textstatic4, (10, 10))
        if confirm:
            media.screen.blit(media.paused, (154, 165))
        pygame.display.flip()
        clock.tick(60)

# Game Sequence        
if __name__ == '__main__':
    title()
    charselect()
    while gamewide.superloop:
        main()
    pygame.quit()
    
            
            
                
                    
                    
                
                
        
