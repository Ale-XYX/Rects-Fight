import pygame
import sys
import globals
import dictionaries
import sprites
import functions

pygame.display.set_caption('Rects Fight! 2.1')
pygame.display.set_icon(dictionaries.MEDIA['icon'])

def title_screen():
    clock = pygame.time.Clock()
    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dictionaries.MEDIA['start_sound'].play()
                    loop = False

        globals.screen.fill(globals.BLACK)
        globals.screen.blit(dictionaries.MEDIA['start_screen'], (0, 0))

        pygame.display.flip()
        clock.tick(60)


def mode_select():
    clock = pygame.time.Clock()
    loop = True
    all_sprites = pygame.sprite.Group()
    selector_big = sprites.SelectorBig((110, 200))
    all_sprites.add(selector_big)
    select_int = 0
    mode_choices = ['Classic', 'Tense', 'Chaos']
    mode_desc = ['Carefree fun for all!', 'Difficulty increased!', 'Its all or nothing!']
    TEXTS1 = globals.FONT_BIG.render('Choose Your Difficulty', True, globals.WHITE)
    TEXTS2 = globals.FONT_BIG.render('Space To Continue', True, globals.WHITE)
    txt = globals.FONT_BIG.render(
        mode_desc[select_int], True, dictionaries.MODE_VALUES[mode_choices[select_int]]['Color']
    )

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Keymap
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    select_int -= 1
                    selector_big.pos[1] -= 100
                if event.key == pygame.K_DOWN:
                    select_int += 1
                    selector_big.pos[1] += 100
                if event.key == pygame.K_SPACE:
                    globals.game_modevalue = mode_choices[select_int]
                    dictionaries.PLAYER_MEDIA['Rainbow'].update({'Parameters': [globals.game_modevalue]})
                    dictionaries.MODE_VALUES[globals.game_modevalue]['Sound'].play()
                    loop = False
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    if select_int == -1:
                        select_int = 2
                    elif select_int == 3:
                        select_int = 0
                    txt = globals.FONT_BIG.render(
                        mode_desc[select_int], True, dictionaries.MODE_VALUES[mode_choices[select_int]]['Color']
                    )
                    dictionaries.MEDIA['select_sound'].play()
        all_sprites.update()

        # Drawing
        globals.screen.fill(globals.BLACK)
        globals.screen.blit(dictionaries.MEDIA['classic_card'], (10, 150))
        globals.screen.blit(dictionaries.MEDIA['tense_card'], (10, 250))
        globals.screen.blit(dictionaries.MEDIA['chaos_card'], (10, 350))
        globals.screen.blit(txt, dictionaries.MODE_VALUES[mode_choices[select_int]]['Location'])
        all_sprites.draw(globals.screen)
        globals.screen.blit(TEXTS1, (100, 50))
        globals.screen.blit(TEXTS2, (120, 500))

        pygame.display.flip()
        clock.tick(60)



def char_select():
    def get(insert):
        color = dictionaries.PLAYER_MEDIA[insert[0]]['Color']
        img = dictionaries.PLAYER_MEDIA[insert[0]]['Image']
        txt = globals.FONT_BIG.render(insert[0], True, color)
        abiltxt = globals.FONT_BIG.render('Ability: ' + str(insert[1]), True, color)
        return img, txt, abiltxt
    clock = pygame.time.Clock()
    loop = True
    color_choices = [
        ('Blue', 'Big Bullet'),
        ('Orange', 'Big Bullet'),
        ('Green', 'Split Bullet'),
        ('Yellow', 'Split Bullet'),
        ('Red', 'Beam'),
        ('Purple', 'Beam'),
        ('Grey', 'Reverse Bullet'),
        ('White', 'Reverse Bullet'),
        ('Rainbow', 'Multi bullet')
    ]
    TEXTS1 = globals.FONT_BIG.render('Choose Your Character', True, globals.WHITE)
    TEXTS2 = globals.FONT_BIG.render('Space To Continue', True, globals.WHITE)
    TEXTS3 = globals.FONT_BOLD_ITALIC.render('VS.', True, globals.WHITE)
    playero_int = 0
    playert_int = 1
    playero_image, chartxto, abiltxto = get(color_choices[playero_int])
    playert_image, chartxtt, abiltxtt = get(color_choices[playert_int])
    selector_a = sprites.Selector((30, 188))
    selector_b = sprites.Selector((85, 388))
    all_sprites = pygame.sprite.Group()
    all_sprites.add(selector_a, selector_b)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # Keymap
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    playero_int += 1
                    selector_a.pos[0] += 55
                elif event.key == pygame.K_a:
                    playero_int -= 1
                    selector_a.pos[0] -= 55
                if event.key == pygame.K_RIGHT:
                    playert_int += 1
                    selector_b.pos[0] += 55
                elif event.key == pygame.K_LEFT:
                    playert_int -= 1
                    selector_b.pos[0] -= 55
                if event.key == pygame.K_SPACE:
                    # Loads character values based on Player 1 and Player 2's choices.
                    globals.playero_charvalue = color_choices[playero_int][0]
                    globals.playert_charvalue = color_choices[playert_int][0]
                    if globals.playero_charvalue == 'Grey' and globals.playert_charvalue == 'White':
                        globals.mem_activate = True
                    loop = False
                if event.key in (pygame.K_d, pygame.K_a, pygame.K_RIGHT, pygame.K_LEFT):
                    playero_int %= len(color_choices)
                    playert_int %= len(color_choices)
                    playero_image, chartxto, abiltxto = get(color_choices[playero_int])
                    playert_image, chartxtt, abiltxtt = get(color_choices[playert_int])
                    dictionaries.MEDIA['select_sound'].play()
        all_sprites.update(470, 30)

        globals.screen.fill(globals.BLACK)
        globals.screen.blit(TEXTS1, (90, 50))
        globals.screen.blit(TEXTS2, (120, 500))
        globals.screen.blit(TEXTS3, (230, 275))
        globals.screen.blit(chartxto, (dictionaries.PLAYER_MEDIA[color_choices[playero_int][0]]['Location'][0], 218))
        globals.screen.blit(chartxtt, (dictionaries.PLAYER_MEDIA[color_choices[playert_int][0]]['Location'][0], 300))
        globals.screen.blit(abiltxto, (dictionaries.PLAYER_MEDIA[color_choices[playero_int][0]]['Location'][1], 248))
        globals.screen.blit(abiltxtt, (dictionaries.PLAYER_MEDIA[color_choices[playert_int][0]]['Location'][1], 330))
        globals.screen.blit(dictionaries.MEDIA['charsel_bar'], (0, 158))
        globals.screen.blit(dictionaries.MEDIA['charsel_bar'], (0, 358))
        all_sprites.draw(globals.screen)

        pygame.display.flip()
        clock.tick(60)


def main():
    # Game Variables
    ABIL = {
        'Blue': functions.big_bullet,
        'Orange': functions.big_bullet,
        'Green': functions.split_bullet,
        'Yellow': functions.split_bullet,
        'Red': functions.beam,
        'Purple': functions.beam,
        'Grey': functions.reverse_bullet,
        'White': functions.reverse_bullet,
        'Rainbow': functions.multi_bullet

    }
    all_sprites = pygame.sprite.Group()
    bullets_o = pygame.sprite.Group()
    bullets_t = pygame.sprite.Group()
    clock = pygame.time.Clock()
    TEXTS1 = globals.FONT_SMALL.render('Player 1', True, dictionaries.PLAYER_MEDIA[globals.playero_charvalue]['Color'])
    TEXTS2 = globals.FONT_SMALL.render('Player 2', True, dictionaries.PLAYER_MEDIA[globals.playert_charvalue]['Color'])
    TEXTS3 = globals.FONT_SMALL.render('Escape to leave', True, globals.WHITE)
    TEXTS4 = globals.FONT_SMALL.render('Enter to restart', True, globals.WHITE)
    # Using G.MODE, selects attributes to use for game
    game_music = dictionaries.MODE_VALUES[globals.game_modevalue]['Music']
    timer = dictionaries.MODE_VALUES[globals.game_modevalue]['Timer']
    player_velocity = dictionaries.MODE_VALUES[globals.game_modevalue]['Player_Velocity']
    bullet_velocity = dictionaries.MODE_VALUES[globals.game_modevalue]['Bullet_Velocity']
    player_o = sprites.RectPlayer((35, 35), bullets_t, (bullet_velocity, 0), globals.playero_charvalue, ABIL[globals.playero_charvalue],  all_sprites)
    player_t = sprites.RectPlayer((465, 465), bullets_o, (-bullet_velocity, 0), globals.playert_charvalue, ABIL[globals.playert_charvalue], all_sprites)
    player_o.health = dictionaries.MODE_VALUES[globals.game_modevalue]['Health']
    player_t.health = dictionaries.MODE_VALUES[globals.game_modevalue]['Health']
    cooldown_o = dictionaries.MODE_VALUES[globals.game_modevalue]['Cooldown']
    cooldown_t = dictionaries.MODE_VALUES[globals.game_modevalue]['Cooldown']
    # Bools
    loop = True
    time = True
    ability_o = False
    ability_t = False
    time_o = True
    time_t = True
    on_start = True
    on_end = False
    confirm = False
    draw = False
    # Integers
    velocity_reset = 0
    dt = clock.tick(60) / 1000
    text_location = (222, 520)

    while loop:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globals.superloop = False
                loop = False
            # Keymap
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and not player_o.toggle:
                    BULLET = sprites.Bullet(player_o.rect.center, (player_o.fire_direction), player_o.bullet_image, 'Bullet')
                    bullets_o.add(BULLET)
                    all_sprites.add(BULLET)
                    dictionaries.MEDIA['shoot_sound'].play()
                if event.key == pygame.K_SPACE and not player_t.toggle:
                    BULLET = sprites.Bullet(player_t.rect.center, (player_t.fire_direction), player_t.bullet_image, 'Bullet')
                    bullets_t.add(BULLET)
                    all_sprites.add(BULLET)
                    dictionaries.MEDIA['shoot_sound'].play()
                if event.key == pygame.K_e and not player_o.toggle and ability_o:
                    player_o.ability(bullets_o, all_sprites, player_o.rect.center, (player_o.fire_direction), *player_o.params)
                    time_o = True
                    ability_o = False
                    cooldown_o = dictionaries.MODE_VALUES[globals.game_modevalue]['Cooldown']
                if event.key == pygame.K_RCTRL and not player_t.toggle and ability_t:
                    player_t.ability(bullets_t, all_sprites, player_t.rect.center, (player_t.fire_direction), *player_t.params)
                    time_t = True
                    ability_t = False
                    cooldown_t = dictionaries.MODE_VALUES[globals.game_modevalue]['Cooldown']
                if event.key == pygame.K_d and not player_o.toggle and player_o.vel.x == 0:
                    player_o.vel.x = player_velocity
                    player_o.fire_direction = (bullet_velocity, 0)
                if event.key == pygame.K_a and not player_o.toggle and player_o.vel.x == 0:
                    player_o.vel.x = -player_velocity
                    player_o.fire_direction = (-bullet_velocity, 0)
                if event.key == pygame.K_s and not player_o.toggle and player_o.vel.y == 0:
                    player_o.vel.y = player_velocity
                    player_o.fire_direction = (0, bullet_velocity)
                if event.key == pygame.K_w and not player_o.toggle and player_o.vel.y == 0:
                    player_o.vel.y = -player_velocity
                    player_o.fire_direction = (0, -bullet_velocity)
                if event.key == pygame.K_RIGHT and not player_t.toggle and player_t.vel.x == 0:
                    player_t.vel.x = player_velocity
                    player_t.fire_direction = (bullet_velocity, 0)
                if event.key == pygame.K_LEFT and not player_t.toggle and player_t.vel.x == 0:
                    player_t.vel.x = -player_velocity
                    player_t.fire_direction = (-bullet_velocity, 0)
                if event.key == pygame.K_DOWN and not player_t.toggle and player_t.vel.y == 0:
                    player_t.vel.y = player_velocity
                    player_t.fire_direction = (0, bullet_velocity)
                if event.key == pygame.K_UP and not player_t.toggle and player_t.vel.y == 0:
                    player_t.vel.y = -player_velocity
                    player_t.fire_direction = (0, -bullet_velocity)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player_o.vel.x = velocity_reset
                if event.key == pygame.K_a:
                    player_o.vel.x = velocity_reset
                if event.key == pygame.K_s:
                    player_o.vel.y = velocity_reset
                if event.key == pygame.K_w:
                    player_o.vel.y = velocity_reset
                if event.key == pygame.K_RIGHT:
                    player_t.vel.x = velocity_reset
                if event.key == pygame.K_LEFT:
                    player_t.vel.x = velocity_reset
                if event.key == pygame.K_DOWN:
                    player_t.vel.y = velocity_reset
                if event.key == pygame.K_UP:
                    player_t.vel.y = velocity_reset

        # Code that runs on first iteration, runs music and the "FIGHT!" announcer but only once
        if on_start:
            dictionaries.MEDIA['fight_sound'].play()
            game_music.play()
            on_start = False

        # On TAB keypress, all game functions cease and pause screen appears until LSHIFT/ESC/ENTER is pressed
        # ESC: Game leaves, both superloop and loop are declared false as the game ends
        # ENTER: Restarts, only loop ends, restarting the game
        # LSHIFT: Continues operation of game
        if keys[pygame.K_TAB] and not confirm and not on_end:
            confirm = True
            time = False
            time_o = False
            time_t = False
            for sprite in all_sprites:
                sprite.toggle = True
            pygame.mixer.pause()
            dictionaries.MEDIA['pause_sound'].play()

        elif keys[pygame.K_LSHIFT] and confirm:
            confirm = False
            time = True
            time_o = True
            time_t = True
            for sprite in all_sprites:
                sprite.toggle = False
            pygame.mixer.unpause()
            dictionaries.MEDIA['pause_sound'].play()

        elif keys[pygame.K_ESCAPE] and confirm:
            globals.superloop = False
            loop = False

        elif keys[pygame.K_RETURN] and confirm:
            game_music.stop()
            loop = False

        # Time code, subtracts timer and cooldown, detects when time is @0 and does according actions, and contains more action code
        if time:
            timer -= dt
            txt = dictionaries.TIMER_DICT[timer < 10][1].render(str(round(timer, 1)), True, dictionaries.TIMER_DICT[timer < 10][0])
            if timer <= 0:
                for sprite in all_sprites:
                    sprite.toggle = True
                game_music.stop()
                time = False
                time_o = False
                time_t = False
                on_end = True
                text_location = (190, 530)
                txt = globals.FONT_BIG.render('Times Up!', True, globals.GREY)
                dictionaries.MEDIA['die_sound'].play()

        if not time and keys[pygame.K_ESCAPE]:
            globals.superloop = False
            loop = False
        elif not time and keys[pygame.K_RETURN] and not confirm:
            game_music.stop()
            loop = False

        if time_o:
            cooldown_o -= dt
            if cooldown_o <= 0:
                time_o = False
                ability_o = True
        if time_t:
            cooldown_t -= dt
            if cooldown_t <= 0:
                time_t = False
                ability_t = True

        # Outcome code, when health of a player(s) is at 0, code is run that shows outcome on timer area, stops time, and also contains key actions
        if player_o.health <= 0 and not draw:
            txt = globals.FONT_BIG.render('Player 2 Wins!', True, player_t.color)
            text_location = (155, 530)
            time = False
            time_o = False
            time_t = False
            on_end = True
            game_music.stop()
            if keys[pygame.K_ESCAPE] and not confirm:
                globals.superloop = False
                loop = False
            elif keys[pygame.K_RETURN] and not confirm:
                loop = False
                if globals.mem_activate:
                    globals.mem.append(1)
                    print(globals.mem)
                    if globals.mem == globals.mem_ideal:
                        pygame.display.set_caption('Regg fitte')

        if player_t.health <= 0 and not draw:
            txt = globals.FONT_BIG.render('Player 1 Wins!', True, player_o.color)
            text_location = (155, 530)
            time = False
            time_o = False
            time_t = False
            on_end = True
            game_music.stop()
            if keys[pygame.K_ESCAPE] and not confirm:
                globals.superloop = False
                loop = False
            elif keys[pygame.K_RETURN] and not confirm:
                loop = False
                if globals.mem_activate:
                    globals.mem.append(0)
                    print(globals.mem)
                    if globals.mem == globals.mem_ideal:
                        pygame.display.set_caption('Regg fitte')

        if player_o.health <= 0 and player_t.health <= 0:
            txt = globals.FONT_BIG.render('Draw!', True, globals.GREY)
            text_location = (210, 530)
            time = False
            time_o = False
            time_t = False
            on_end = True
            draw = True
            game_music.stop()
            if keys[pygame.K_ESCAPE] and not confirm:
                globals.superloop = False
                loop = False
            elif keys[pygame.K_RETURN] and not confirm:
                loop = False
                if globals.mem_activate:
                    globals.mem.append(' ')
                    print(globals.mem)
                    if globals.mem == globals.mem_ideal:
                        pygame.display.set_caption('Regg fitte')

        all_sprites.update()

        # Drawing code, draws media, hp bars, text, sprites, etc.
        globals.screen.fill(globals.BLACK)
        globals.screen.blit(dictionaries.MEDIA['wall'], (0, 0))
        globals.screen.blit(pygame.transform.flip(dictionaries.HP_MEDIA[player_o.health], True, False), (20, 530))
        globals.screen.blit(dictionaries.HP_MEDIA[player_t.health], (380, 530))
        globals.screen.blit(txt, text_location)
        globals.screen.blit(TEXTS1, (19, 515))
        globals.screen.blit(TEXTS2, (429, 515))
        DRAWPARAMS1 = [functions.get_cooldown_img(globals.game_modevalue, cooldown_o), (100, 515)]
        DRAWPARAMS2 = [functions.get_cooldown_img(globals.game_modevalue, cooldown_t), (380, 515)]
        globals.screen.blit(*DRAWPARAMS1)
        globals.screen.blit(*DRAWPARAMS2)

        all_sprites.draw(globals.screen)

        if on_end:
            globals.screen.blit(TEXTS3, (395, 10))
            globals.screen.blit(TEXTS4, (10, 10))
        if confirm:
            globals.screen.blit(dictionaries.MEDIA['paused'], (154, 165))

        pygame.display.flip()
        clock.tick(60)
