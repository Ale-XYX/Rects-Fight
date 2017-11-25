# Rects Fight V1.3
import pygame
import os
from pygame.math import Vector2
pygame.init()
screen = pygame.display.set_mode((500, 500))
# Game Class
class Game():
    playarea = pygame.Rect(5, 5, 490, 490)
    black = (0, 0, 0)
    grey = (192, 192, 192)
    white = (255, 255, 255)
    blue = (91, 154, 255)
    orange = (247, 157, 66)
    green = (0, 159, 18)
    P1Char = 1
    P2Char = 2
    # Media  
    class Media():
        # Blue Medialist
        blue1 = pygame.image.load(os.path.join('media', 'blue1.png')).convert_alpha()
        blue2 = pygame.image.load(os.path.join('media', 'blue2.png')).convert_alpha()
        blue3 = pygame.image.load(os.path.join('media', 'blue3.png')).convert_alpha()
        bulletblue = pygame.image.load(os.path.join('media', 'bulletblue.png')).convert_alpha()
        # Orange Medialist
        orange1 = pygame.image.load(os.path.join('media', 'orange1.png')).convert_alpha()
        orange2 = pygame.image.load(os.path.join('media', 'orange2.png')).convert_alpha()
        orange3 = pygame.image.load(os.path.join('media', 'orange3.png')).convert_alpha()
        bulletorange = pygame.image.load(os.path.join('media', 'bulletorange.png')).convert_alpha()
        # Green Medialist
        green1 = pygame.image.load(os.path.join('media', 'green1.png')).convert_alpha()
        green2 = pygame.image.load(os.path.join('media', 'green2.png')).convert_alpha()
        green3 = pygame.image.load(os.path.join('media', 'green3.png')).convert_alpha()
        bulletgreen = pygame.image.load(os.path.join('media', 'bulletgreen.png')).convert_alpha()
        # Game Medialist
        paused = pygame.image.load(os.path.join('media', 'paused.png')).convert_alpha()
        title = pygame.image.load(os.path.join('media', 'title.png')).convert_alpha()
        wall = pygame.image.load(os.path.join('media', 'wall.png')).convert_alpha()
        icon = pygame.image.load(os.path.join('media', 'icon.png')).convert_alpha()
        # Game Soundlist
        shoot = pygame.mixer.Sound(os.path.join('media', 'shoot.wav'))
        hit = pygame.mixer.Sound(os.path.join('media', 'hit.wav'))
        die = pygame.mixer.Sound(os.path.join('media', 'die.wav'))
        pause = pygame.mixer.Sound(os.path.join('media', 'pause.wav'))
        fight = pygame.mixer.Sound(os.path.join('media', 'fight.wav'))
        music = pygame.mixer.Sound(os.path.join('media', 'music.wav'))
    pygame.display.set_caption('Rects Fight!')
    pygame.display.set_icon(Media.icon)
    # Sprites
    class Sprites():
        # Player Sprite
        class Player(pygame.sprite.Sprite):
            def __init__(self, pos, enemy_bullets, image, direction, *groups):
                super().__init__(*groups)
                self.image = image
                self.rect = self.image.get_rect(center = pos)
                self.vel = Vector2(0, 0)
                self.pos = Vector2(pos)
                self.fire_direction = Vector2(direction)
                self.health = 3
                self.enemy_bullets = enemy_bullets
                self.toggle = False
            def update(self):
                self.pos += self.vel
                self.rect.center = self.pos
                self.rect.clamp_ip(Game.playarea)
                collided = pygame.sprite.spritecollide(self, self.enemy_bullets, True)
                for bullet in collided:
                    self.health -= 1
                    Game.Media.hit.play()
                    if self.health <= 0:
                        self.kill()
                        self.toggle = True
                        Game.Media.die.play()
        # Bullet Sprite
        class Bullet(pygame.sprite.Sprite):
            def __init__(self, pos, vel, image):
                super().__init__()
                self.image = image
                self.rect = self.image.get_rect(center = pos)
                self.vel = vel
                self.pos = pos
                self.toggle = False
            def update(self):
                if self.toggle == False:
                    self.pos += self.vel
                    self.rect.center = self.pos
                    if not Game.playarea.contains(self):
                        self.kill()
    # Main game
    class Engine():
        # Title Screen
        def Title():
            endScreen = True
            while endScreen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            endScreen = False
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                screen.fill(Game.black)
                screen.blit(Game.Media.title, (0, 0))
                pygame.display.flip()
        # Character Select
        def Char():
            def ReturnP1():
                if Game.P1Char == 1:
                    return font.render('Blue', True, Game.blue)
                elif Game.P1Char == 2:
                    return font.render('Orange', True, Game.orange)
                elif Game.P1Char == 3:
                    return font.render('Green', True, Game.green)
            def ReturnP2():
                if Game.P2Char == 1:
                    return font.render('Blue', True, Game.blue)
                elif Game.P2Char == 2:
                    return font.render('Orange', True, Game.orange)
                elif Game.P2Char == 3:
                    return font.render('Green', True, Game.green)
            font = pygame.font.Font(None, 40)    
            char = True
            clock = pygame.time.Clock()
            while char:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            Game.P1Char += 1
                        elif event.key == pygame.K_s:
                            Game.P1Char -= 1
                        if event.key == pygame.K_UP:
                            Game.P2Char += 1
                        elif event.key == pygame.K_DOWN:
                            Game.P2Char -= 1
                        if event.key == pygame.K_SPACE:
                            char = False
                if Game.P1Char == 4:
                    Game.P1Char -= 1
                elif Game.P2Char == 4:
                    Game.P2Char -= 1
                if Game.P1Char == 0:
                    Game.P1Char += 1
                elif Game.P2Char == 0:
                    Game.P2Char += 1
                txt1 = ReturnP1()
                txt2 = ReturnP2()
                textS1 = font.render('Choose Your Character', True, Game.white)
                textS2 = font.render('Space To Continue', True, Game.white)
                textS3 = font.render('Player 1: ', True, Game.white)
                textS4 = font.render('Player 2: ', True, Game.white)
                screen.fill(Game.black)
                screen.blit(textS1, (100, 50))
                screen.blit(textS3, (135, 150))
                screen.blit(txt1, (260, 150))
                screen.blit(textS4, (135, 250))
                screen.blit(txt2, (260, 250))
                screen.blit(textS2, (125, 400))
                pygame.display.flip()
                clock.tick(60)                
        # Main Game
        def Main():
            def P1Return(toReturn):
                if toReturn == 'image':
                    if Game.P1Char == 1:
                        return Game.Media.blue1
                    elif Game.P1Char == 2:
                        return Game.Media.orange1
                    elif Game.P1Char == 3:
                        return Game.Media.green1
                elif toReturn == 'bullet':
                    if Game.P1Char == 1:
                        return Game.Media.bulletblue
                    elif Game.P1Char == 2:
                        return Game.Media.bulletorange
                    elif Game.P1Char == 3:
                        return Game.Media.bulletgreen
                elif toReturn == 'stage2':
                    if Game.P1Char == 1:
                        return Game.Media.blue2
                    elif Game.P1Char == 2:
                        return Game.Media.orange2
                    elif Game.P1Char == 3:
                        return Game.Media.green2
                elif toReturn == 'stage3':
                    if Game.P1Char == 1:
                        return Game.Media.blue3
                    elif Game.P1Char == 2:
                        return Game.Media.orange3
                    elif Game.P1Char == 3:
                        return Game.Media.green3
            def P2Return(toReturn):
                if toReturn == 'image':
                    if Game.P2Char == 1:
                        return Game.Media.blue1
                    elif Game.P2Char == 2:
                        return Game.Media.orange1
                    elif Game.P2Char == 3:
                        return Game.Media.green1
                elif toReturn == 'bullet':
                    if Game.P2Char == 1:
                        return Game.Media.bulletblue
                    elif Game.P2Char == 2:
                        return Game.Media.bulletorange
                    elif Game.P2Char == 3:
                        return Game.Media.bulletgreen
                elif toReturn == 'stage2':
                    if Game.P2Char == 1:
                        return Game.Media.blue2
                    elif Game.P2Char == 2:
                        return Game.Media.orange2
                    elif Game.P2Char == 3:
                        return Game.Media.green2
                elif toReturn == 'stage3':
                    if Game.P2Char == 1:
                        return Game.Media.blue3
                    elif Game.P2Char == 2:
                        return Game.Media.orange3
                    elif Game.P2Char == 3:
                        return Game.Media.green3
            def ReturnColor():
                if player1.health == 0:
                    if Game.P2Char == 1:
                        return (91, 154, 255)
                    if Game.P2Char == 2:
                        return (247, 157, 66)
                    if Game.P2Char == 3:
                        return (0, 159, 18)
                if player2.health == 0:
                    if Game.P1Char == 1:
                        return (91, 154, 255)
                    if Game.P1Char == 2:
                        return (247, 157, 66)
                    if Game.P1Char == 3:
                        return (0, 159, 18)
            # Game Stuff
            all_sprites = pygame.sprite.Group()
            bullets1 = pygame.sprite.Group()
            bullets2 = pygame.sprite.Group()
            player1 = Game.Sprites.Player((35, 35), bullets2, P1Return('image'), (8, 0), all_sprites)
            player2 = Game.Sprites.Player((465, 465), bullets1, P2Return('image'), (-8, 0), all_sprites)
            clock = pygame.time.Clock()
            font = pygame.font.Font(None, 40)
            # Conditionals
            onStart = True
            loop = True
            time = True
            onEnd = True
            confirm = False
            # Numericals
            vel = 8
            vel_reset = 0 
            timer = 30 # Max Is 51
            dt = clock.tick(60) / 1000
            textlocal = (215, 20)
            # Game loop
            while loop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e and player1.toggle == False:
                            bullet = Game.Sprites.Bullet(player1.rect.center, Vector2(player1.fire_direction), P1Return('bullet'))
                            Game.Media.shoot.play()
                            bullets1.add(bullet)
                            all_sprites.add(bullet)
                        if event.key == pygame.K_SPACE and player2.toggle == False:
                            bullet = Game.Sprites.Bullet(player2.rect.center, Vector2(player2.fire_direction), P2Return('bullet'))
                            Game.Media.shoot.play()
                            bullets2.add(bullet)
                            all_sprites.add(bullet)
                        if event.key == pygame.K_d and player1.toggle == False:
                            player1.vel.x = 5
                            player1.fire_direction = Vector2(vel, 0)
                        if event.key == pygame.K_a and player1.toggle == False:
                            player1.vel.x = -5
                            player1.fire_direction = Vector2(-vel, 0)
                        if event.key == pygame.K_s and player1.toggle == False:
                            player1.vel.y = 5
                            player1.fire_direction = Vector2(0, vel)
                        if event.key == pygame.K_w and player1.toggle == False:
                            player1.vel.y = -5
                            player1.fire_direction = Vector2(0, -vel)                             
                        if event.key == pygame.K_RIGHT and player2.toggle == False:
                            player2.vel.x = 5
                            player2.fire_direction = Vector2(vel, 0)
                        if event.key == pygame.K_LEFT and player2.toggle == False:
                            player2.vel.x = -5
                            player2.fire_direction = Vector2(-vel, 0)
                        if event.key == pygame.K_DOWN and player2.toggle == False:
                            player2.vel.y = 5
                            player2.fire_direction = Vector2(0, vel)
                        if event.key == pygame.K_UP and player2.toggle == False:
                            player2.vel.y = -5
                            player2.fire_direction = Vector2(0, -vel)
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
                # Logic
                if onStart:
                    Game.Media.fight.play()
                    Game.Media.music.play()
                    onStart = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_TAB] and confirm == False:
                    player1.toggle = True
                    player2.toggle = True
                    confirm = True
                    time = False
                    for bullet in bullets1:
                        bullet.toggle = True
                    for bullet in bullets2:
                        bullet.toggle = True
                    pygame.mixer.pause()
                    Game.Media.pause.play()
                if keys[pygame.K_ESCAPE] and confirm:
                    loop = False
                elif keys[pygame.K_LSHIFT] and confirm:
                    confirm = False
                    player1.toggle = False
                    player2.toggle = False
                    confirm = False
                    time = True
                    for bullet in bullets1:
                        bullet.toggle = False
                    for bullet in bullets2:
                        bullet.toggle = False
                    pygame.mixer.unpause()
                    Game.Media.pause.play()
                if time:
                    timer -= dt
                    txt = font.render(str(round(timer, 1)), True, Game.white)
                    if timer <= 0:
                        txt = font.render('Times Up!', True, Game.white)
                        player1.toggle = True
                        player2.toggle = True
                        for bullet in bullets1:
                            bullet.toggle = True
                        for bullet in bullets2:
                            bullet.toggle = True
                        Game.Media.die.play()
                        Game.Media.music.stop()
                        time = False
                        textlocal = (185, 20)
                if time == False and keys[pygame.K_ESCAPE]:
                    loop = False
                if player1.health == 2:
                    player1.image = P1Return('stage2')
                elif player1.health == 1:
                    player1.image = P1Return('stage3')
                elif player1.health == 0:
                    txt = font.render('Player 2 Wins!', True, ReturnColor())
                    textlocal = (140, 20)
                    time = False
                    Game.Media.music.stop()
                    if keys[pygame.K_ESCAPE] and confirm == False:
                        loop = False
                if player2.health == 2:
                    player2.image = P2Return('stage2')
                elif player2.health == 1:
                    player2.image = P2Return('stage3')
                elif player2.health == 0:
                    txt = font.render('Player 1 Wins!', True, ReturnColor())
                    textlocal = (140, 20)
                    time = False
                    Game.Media.music.stop()
                    if keys[pygame.K_ESCAPE] and confirm == False:
                        loop = False
                if player1.health == 0 and player2.health == 0:
                    txt = font.render('Draw!', True, Game.grey)
                    textlocal = (205, 20)
                    time = False
                    Game.Media.music.stop()
                    if keys[pygame.K_ESCAPE] and confirm == False:
                        loop = False
                # Drawing
                all_sprites.update()
                screen.fill(Game.black)
                if confirm:
                    screen.blit(Game.Media.paused, (145, 210))
                screen.blit(Game.Media.wall, (0, 0))
                screen.blit(txt, (textlocal))
                all_sprites.draw(screen)
                pygame.display.flip()
                clock.tick(60)
# Game Sequence
if __name__ == '__main__':
    Game.Engine.Title()
    Game.Engine.Char()
    Game.Engine.Main()
    pygame.quit()
# SnivyDroid
