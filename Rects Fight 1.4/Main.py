# Rects Fight V1.4
import pygame
import os
import sys
pygame.init()
screen = pygame.display.set_mode((500, 600))
class Global():
    black = (0, 0, 0)
    grey = (192, 192, 192)
    white = (255, 255, 255)
    blue = (91, 154, 255)
    orange = (247, 157, 66)
    green = (0, 159, 18)
    red = (196, 0, 0)
    purple = (205, 43, 255)
    P1Char = 1
    P2Char = 2
    superloop = True
    font = pygame.font.Font(None, 40)
    font2 = pygame.font.Font(None, 20)
    playarea = pygame.Rect(5, 5, 490, 490)
class Media():
    # Blue Medialist
    blue = pygame.image.load(os.path.join('media', 'blue.png')).convert_alpha()
    bulletblue = pygame.image.load(os.path.join('media', 'bulletblue.png')).convert_alpha()
    # Orange Medialist
    orange = pygame.image.load(os.path.join('media', 'orange.png')).convert_alpha()
    bulletorange = pygame.image.load(os.path.join('media', 'bulletorange.png')).convert_alpha()
    # Green Medialist
    green = pygame.image.load(os.path.join('media', 'green.png')).convert_alpha()
    bulletgreen = pygame.image.load(os.path.join('media', 'bulletgreen.png')).convert_alpha()
    # Purple Medialist
    purple = pygame.image.load(os.path.join('media', 'purple.png')).convert_alpha()
    bulletpurple = pygame.image.load(os.path.join('media', 'bulletpurple.png')).convert_alpha()
    # Red Medialist
    red = pygame.image.load(os.path.join('media', 'red.png')).convert_alpha()
    bulletred = pygame.image.load(os.path.join('media', 'bulletred.png')).convert_alpha()
    # HP Medialist
    hp1 = pygame.image.load(os.path.join('media', 'hp1.png')).convert_alpha()
    hp2 = pygame.image.load(os.path.join('media', 'hp2.png')).convert_alpha()
    hp3 = pygame.image.load(os.path.join('media', 'hp3.png')).convert_alpha()
    hp4 = pygame.image.load(os.path.join('media', 'hp4.png')).convert_alpha()
    hp5 = pygame.image.load(os.path.join('media', 'hp5.png')).convert_alpha()
    dead = pygame.image.load(os.path.join('media', 'dead.png')).convert_alpha()
    # Player Soundlist
    shoot = pygame.mixer.Sound(os.path.join('media', 'shoot.wav'))
    hit = pygame.mixer.Sound(os.path.join('media', 'hit.wav'))
    die = pygame.mixer.Sound(os.path.join('media', 'die.wav'))
    # Game Medialist
    paused = pygame.image.load(os.path.join('media', 'paused.png')).convert_alpha()
    title = pygame.image.load(os.path.join('media', 'title.png')).convert_alpha()
    wall = pygame.image.load(os.path.join('media', 'wall.png')).convert_alpha()
    icon = pygame.image.load(os.path.join('media', 'icon.png')).convert_alpha()
    etge = pygame.image.load(os.path.join('media', 'egtg.png')).convert_alpha()
    # Game Soundlist
    pause = pygame.mixer.Sound(os.path.join('media', 'pause.wav'))
    fight = pygame.mixer.Sound(os.path.join('media', 'fight.wav'))
    music = pygame.mixer.Sound(os.path.join('media', 'music.wav'))
    select = pygame.mixer.Sound(os.path.join('media', 'select.wav'))
    start = pygame.mixer.Sound(os.path.join('media', 'start.wav'))
pygame.display.set_caption('Rects Fight!')
pygame.display.set_icon(Media.icon)
def Fetch(typeOfFetch, playerType, toReturn):
    if typeOfFetch == 'player':
        if playerType == 'player1':
            if toReturn == 'image':
                if Global.P1Char == 1:
                    return Media.blue
                elif Global.P1Char == 2:
                    return Media.orange
                elif Global.P1Char == 3:
                    return Media.green
                elif Global.P1Char == 4:
                    return Media.purple
                elif Global.P1Char == 5:
                    return Media.red
            elif toReturn == 'bullet':
                if Global.P1Char == 1:
                    return Media.bulletblue
                elif Global.P1Char == 2:
                    return Media.bulletorange
                elif Global.P1Char == 3:
                    return Media.bulletgreen
                elif Global.P1Char == 4:
                    return Media.bulletpurple
                elif Global.P1Char == 5:
                    return Media.bulletred
        elif playerType == 'player2':
            if toReturn == 'image':
                if Global.P2Char == 1:
                    return Media.blue
                elif Global.P2Char == 2:
                    return Media.orange
                elif Global.P2Char == 3:
                    return Media.green
                elif Global.P2Char == 4:
                    return Media.purple
                elif Global.P2Char == 5:
                    return Media.red
            elif toReturn == 'bullet':
                if Global.P2Char == 1:
                    return Media.bulletblue
                elif Global.P2Char == 2:
                    return Media.bulletorange
                elif Global.P2Char == 3:
                    return Media.bulletgreen
                elif Global.P2Char == 4:
                    return Media.bulletpurple
                elif Global.P2Char == 5:
                    return Media.bulletred
    elif typeOfFetch == 'text':
        if playerType == 'player1':
            if Global.P1Char == 1:
                return Global.font.render('Blue', True, Global.blue)
            elif Global.P1Char == 2:
                return Global.font.render('Orange', True, Global.orange)
            elif Global.P1Char == 3:
                return Global.font.render('Green', True, Global.green)
            elif Global.P1Char == 4:
                return Global.font.render('Purple', True, Global.purple)
            elif Global.P1Char == 5:
                return Global.font.render('Red', True, Global.red)
        elif playerType == 'player2':
            if Global.P2Char == 1:
                return Global.font.render('Blue', True, Global.blue)
            elif Global.P2Char == 2:
                return Global.font.render('Orange', True, Global.orange)
            elif Global.P2Char == 3:
                return Global.font.render('Green', True, Global.green)
            elif Global.P2Char == 4:
                return Global.font.render('Purple', True, Global.purple)
            elif Global.P2Char == 5:
                return Global.font.render('Red', True, Global.red)
# Sprites
class Sprites():
    # Player Sprite
    class Player(pygame.sprite.Sprite):
        def __init__(self, pos, enemy_bullets, image, direction, *groups):
            super().__init__(*groups)
            self.image = image
            self.rect = self.image.get_rect(center = pos)
            self.vel = pygame.math.Vector2(0, 0)
            self.pos = pygame.math.Vector2(pos)
            self.fire_direction = pygame.math.Vector2(direction)
            self.health = 3
            self.enemy_bullets = enemy_bullets
            self.toggle = False
        def update(self):
            self.pos += self.vel
            self.rect.center = self.pos
            self.rect.clamp_ip(Global.playarea)
            collided = pygame.sprite.spritecollide(self, self.enemy_bullets, True)
            for bullet in collided:
                self.health -= 1
                Media.hit.play()
                if self.health <= 0:
                    self.kill()
                    self.toggle = True
                    Media.die.play()
    # Bullet Sprite
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, pos, vel, image):
            super().__init__()
            self.image = image
            self.rect = self.image.get_rect(center = pos)
            self.vel = pygame.math.Vector2(vel)
            self.pos = pygame.math.Vector2(pos)
            self.toggle = False
        def update(self):
            if self.toggle == False:
                self.pos += self.vel
                self.rect.center = self.pos
                if not Global.playarea.contains(self):
                    self.kill()
# Game
class Game():
    def Title():
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
                        Media.start.play()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
            if time:
                timer -= dt
            if timer <= 0:
                time = False
            screen.fill(Global.black)
            screen.blit(Media.title, (0, 0))
            if not time:
                screen.blit(Media.etge, (200, 100))
            pygame.display.flip()
            clock.tick(60)
    def CharSelect():
        loop = True
        clock = pygame.time.Clock()
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        Global.P1Char += 1
                        if Global.P1Char <= 5:
                            Media.select.play()
                    elif event.key == pygame.K_s:
                        Global.P1Char -= 1
                        if Global.P1Char >= 1:
                            Media.select.play()
                    if event.key == pygame.K_UP:
                        Global.P2Char += 1
                        if Global.P2Char <= 5:
                            Media.select.play()
                    elif event.key == pygame.K_DOWN:
                        Global.P2Char -= 1
                        if Global.P2Char >= 1:
                            Media.select.play()
                    if event.key == pygame.K_SPACE:
                        loop = False
            if Global.P1Char == 6:
                Global.P1Char -= 1
            elif Global.P1Char == 0:
                Global.P1Char += 1
            if Global.P2Char == 6:
                Global.P2Char -= 1
            elif Global.P2Char == 0:
                Global.P2Char += 1
            text1 = Fetch('text', 'player1', None)
            text2 = Fetch('text', 'player2', None)
            textS1 = Global.font.render('Choose Your Character', True, Global.white)
            textS2 = Global.font.render('Space To Continue', True, Global.white)
            textS3 = Global.font.render('Player 1: ', True, Global.white)
            textS4 = Global.font.render('Player 2: ', True, Global.white)
            screen.fill(Global.black)
            screen.blit(textS1, (100, 50))
            screen.blit(textS2, (125, 500))
            screen.blit(textS3, (115, 225))
            screen.blit(textS4, (115, 325))
            screen.blit(text1, (240, 225))
            screen.blit(text2, (240, 325))
            screen.blit(Fetch('player', 'player1', 'image'), (355, 210))
            screen.blit(Fetch('player', 'player2', 'image'), (355, 310))
            pygame.display.flip()
            clock.tick(60)
    def Main():
        # Functions
        def MainFetch(typeOf, player):
            if typeOf == 'time':
                if timer < 10:
                    return (196, 0, 0)
                else:
                    return (255, 255, 255)
            elif typeOf == 'player':
                if player2.health == 0:
                    if Global.P1Char == 1:
                        return (91, 154, 255)
                    if Global.P1Char == 2:
                        return (247, 157, 66)
                    if Global.P1Char == 3:
                        return (0, 159, 18)
                    if Global.P1Char == 4:
                        return (205, 43, 255)
                    if Global.P1Char == 5:
                        return (196, 0, 0)
                if player1.health == 0:
                    if Global.P2Char == 1:
                        return (91, 154, 255)
                    if Global.P2Char == 2:
                        return (247, 157, 66)
                    if Global.P2Char == 3:
                        return (0, 159, 18)
                    if Global.P2Char == 4:
                        return (205, 43, 255)
                    if Global.P2Char == 5:
                        return (196, 0, 0)
            elif typeOf == 'hp':
                if player == 'player1':
                    if player1.health == 3:
                        return Media.hp1
                    if player1.health == 2:
                        return Media.hp4
                    if player1.health == 1:
                        return Media.hp5
                    if player1.health == 0:
                        return Media.dead
                if player == 'player2':
                    if player2.health == 3:
                        return Media.hp1
                    if player2.health == 2:
                        return Media.hp2
                    if player2.health == 1:
                        return Media.hp3
                    if player2.health == 0:
                        return Media.dead
        # Game Variables
        all_sprites = pygame.sprite.Group()
        bullets1 = pygame.sprite.Group()
        bullets2 = pygame.sprite.Group()
        player1 = Sprites.Player((35, 35), bullets2, Fetch('player', 'player1', 'image'), (8, 0), all_sprites)
        player2 = Sprites.Player((465, 465), bullets1, Fetch('player', 'player2', 'image'), (-8, 0), all_sprites)
        clock = pygame.time.Clock()
        textstatic1 = Global.font2.render('Player 1', True, Global.white)
        textstatic2 = Global.font2.render('Player 2', True, Global.white)
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
        textlocal = (215, 520)
        # Game Variables
        all_sprites = pygame.sprite.Group()
        bullets1 = pygame.sprite.Group()
        bullets2 = pygame.sprite.Group()
        player1 = Sprites.Player((35, 35), bullets2, Fetch('player', 'player1', 'image'), (8, 0), all_sprites)
        player2 = Sprites.Player((465, 465), bullets1, Fetch('player', 'player2', 'image'), (-8, 0), all_sprites)
        clock = pygame.time.Clock()
        textstatic1 = Global.font2.render('Player 1', True, Global.white)
        textstatic2 = Global.font2.render('Player 2', True, Global.white)
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
        textlocal = (217, 520)
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e and player1.toggle == False:
                        bullet = Sprites.Bullet(player1.rect.center, pygame.math.Vector2(player1.fire_direction), Fetch('player', 'player1', 'bullet'))
                        Media.shoot.play()
                        bullets1.add(bullet)
                        all_sprites.add(bullet)
                    if event.key == pygame.K_SPACE and player2.toggle == False:
                        bullet = Sprites.Bullet(player2.rect.center, pygame.math.Vector2(player2.fire_direction), Fetch('player', 'player2', 'bullet'))
                        Media.shoot.play()
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
                Media.fight.play()
                Media.music.play()
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
                Media.pause.play()
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
                Media.pause.play()
            elif keys[pygame.K_ESCAPE] and confirm:
                Global.superloop = False
                loop = False
            elif keys[pygame.K_SPACE] and confirm:
                loop = False
            if time:
                timer -= dt
                txt = Global.font.render(str(round(timer, 1)), True, MainFetch('time', None))
                if timer <= 0:
                    player1.toggle = True
                    player2.toggle = True
                    for bullet in bullets1:
                        bullet.toggle = True
                    for bullet in bullets2:
                        bullet.toggle = True
                    Media.die.play()
                    Media.music.stop()
                    time = False
                    onEnd = False
                    textlocal = (190, 520)
                    txt = Global.font.render('Times Up!', True, Global.grey)
            if not time and keys[pygame.K_ESCAPE]:
                Global.superloop = False
                loop = False
            elif not time and keys[pygame.K_SPACE] and not confirm:
                    loop = False
            # Player 1 Outcome
            if player1.health == 0:
                txt = Global.font.render('Player 2 Wins!', True, MainFetch('player', None))
                textlocal = (155, 520)
                time = False
                onEnd = False
                Media.music.stop()
                if keys[pygame.K_ESCAPE] and not confirm:
                    Global.superloop = False
                    loop = False
                elif keys[pygame.K_SPACE] and not confirm:
                    loop = False
            # Player 2 Outcome
            if player2.health == 0:
                txt = Global.font.render('Player 1 Wins!', True, MainFetch('player', None))
                textlocal = (155, 520)
                time = False
                onEnd = False
                Media.music.stop()
                if keys[pygame.K_ESCAPE] and not confirm:
                    Global.superloop = False
                    loop = False
                elif keys[pygame.K_SPACE] and not confirm:
                    loop = False
            # Draw Outcome
            if player1.health == 0 and player2.health == 0:
                txt = Global.font.render('Draw!', True, Global.grey)
                textlocal = (210, 520)
                time = False
                onEnd = False
                Media.music.stop()
                if keys[pygame.K_ESCAPE] and not confirm:
                    Global.superloop = False
                    loop = False
                elif keys[pygame.K_SPACE] and not confirm:
                    loop = False
            # Drawing
            all_sprites.update()
            screen.fill(Global.black)
            if confirm:
                screen.blit(Media.paused, (145, 210))
            screen.blit(Media.wall,(0, 0))
            screen.blit(MainFetch('hp', 'player1'), (20, 520))
            screen.blit(MainFetch('hp', 'player2'), (380, 520))
            screen.blit(txt, (textlocal))
            screen.blit(textstatic1, (20, 505))
            screen.blit(textstatic2, (429, 505))
            all_sprites.draw(screen)
            pygame.display.flip()
            clock.tick(60)
if __name__ == '__main__':
    Game.Title()
    Game.CharSelect()
    while Global.superloop == True:
        Game.Main()
    pygame.quit()
