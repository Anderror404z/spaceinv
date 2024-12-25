import pygame, controls
import os
from gun import Gun
from pygame.sprite import Group
from stats import Stats
import time
from scores import Scores


def restart_game(screen, gun, bullets, inos, stats, sc, music_files3, bg_color, background_image):
    stats.reset_health()
    stats.reset_stats()
    stats.run_game = True

    bullets.empty()
    inos.empty()


    controls.create_army(screen, inos)
    gun.create_gun()
    screen.fill(bg_color)
    screen.blit(background_image, (0, 0))
    controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
    pygame.display.flip()


    current_track = 0
    pygame.mixer.music.load(music_files3[current_track])
    pygame.mixer.music.play(-1)

def blizzard():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Space invaders')
    bg_color = (75, 0, 130)
    base_path = os.path.dirname(__file__)  
    background_image = pygame.image.load(os.path.join(base_path, 'images', 'background.png'))
    gun = Gun(screen)
    bullets = Group()
    music_files3 = [os.path.join(base_path, 'images', 'music1.mp3'),
        os.path.join(base_path, 'images', 'music2.mp3'),
        os.path.join(base_path, 'images', 'music3.mp3') ]

    current_track = 0
    sound_on = True
    last_switch_time = 0
    switch_delay = 200


    pygame.mixer.music.load(music_files3[current_track])
    pygame.mixer.music.play(-1)

    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    game_paused = False
    p_key_pressed = False
    r_key_pressed = False

    while True:
        keys = pygame.key.get_pressed()
        controls.events(screen, gun, bullets)

        if stats.run_game:
            if keys[pygame.K_p]:
                if not p_key_pressed:
                    game_paused = not game_paused
                    if game_paused:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                p_key_pressed = True
            else:
                p_key_pressed = False

            if not game_paused:
                gun.update_gun()
                screen.blit(background_image, (0, 0))
                controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
                controls.update_bullets(screen, stats, sc, inos, bullets)
                controls.update_inos(stats, screen,  sc, gun, inos, bullets)


                current_time = pygame.time.get_ticks()

                if keys[pygame.K_m] and (current_time - last_switch_time > switch_delay):
                    last_switch_time = current_time
                    current_track = (current_track + 1) % len(music_files3)
                    pygame.mixer.music.load(music_files3[current_track])
                    pygame.mixer.music.play(-1)
                if keys[pygame.K_q]:
                    pygame.quit()
                    return
                if keys[pygame.K_n]:
                   if sound_on:
                       pygame.mixer.music.pause()
                if keys[pygame.K_r]:
                    if not r_key_pressed:
                        restart_game(screen, gun, bullets, inos, stats, sc, music_files3, bg_color, background_image)
                    r_key_pressed = True
                else:
                    r_key_pressed = False
            pygame.display.flip()




            this_round_begin = int(round(time.time() * 1000))
            this_round_end = int(round(time.time() * 1000))

        if this_round_end - this_round_begin <= 4:
            time.sleep(0.001 * (4 - (this_round_end - this_round_begin)))
            pygame.display.flip()



blizzard()



