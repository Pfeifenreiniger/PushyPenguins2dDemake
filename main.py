'''
2D pixelart demake of the glorious Mario Party 5 minigame Pushy Penguins
https://www.mariowiki.com/Pushy_Penguins
Code and graphics by Kevin Spathmann (Pfeifenreiniger on GitHub: https://github.com/Pfeifenreiniger)
Fonts used: "Mario Kart DS" by David (https://www.dafont.com/mario-kart-ds.font)
            "Super Mario 64 DS" by David (https://www.dafont.com/super-mario-64-ds.font)
Musics, SFX, and voices used from Nintendo™ originals (like Mario Party 5, Super Smash Bros. 64 (and Melee) or Super Mario 64)
Original Game (included in Mario Party 5) by Hudson Soft™ and Nintendo™
'''

import pygame, menu, sys, random, time
from background import Background, Wave
from player import Player
from obstacle import Penguins

pygame.init()

## display screen ##
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pushy Penguins 2D Demake")
icon = pygame.image.load("graphics/game_icon.png").convert_alpha()
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
FPS = 30
# fonts #
mario64_font = pygame.font.Font("font/Super-Mario-64-DS.ttf", 20)
marioKart_font = pygame.font.Font("font/Mario-Kart-DS.ttf", 50)
# game music #
game_music = pygame.mixer.Sound("music/mparty5_Bustling_Noisily.mp3")
game_music.set_volume(0.8)

## background graphics ##
bg_sea = Background("sea")
bg_ice_floe = Background("ice_floe")
bg_sea_lower_edge = Background("sea_lower_edge")

## players ##
# testplayers
player1 = Player(1, "yos")
player2 = Player(2, "pea")
player3 = Player(3, "wal")
player4 = Player(4, "mar")

numb_of_players = menu.numb_of_players
player_collision_bounce = 20
def player_collision():
    if numb_of_players > 1:
        # 1 vs 2 player
        if pygame.sprite.collide_rect(player1, player2):  ## top-bottom p1
            if player1.fall_l != True and player2.fall_l != True and player1.fall_u != True and player2.fall_u != True and player1.fall_d != True and player2.fall_d != True:
                if player1.rect.bottom >= player2.rect.top and player1.rect.bottom <= player2.rect.bottom:
                    player1.y -= player_collision_bounce
                    player1.crash_sfx.play()
                    player2.y += player_collision_bounce
                    player2.crash_sfx.play()
        if pygame.sprite.collide_rect(player2, player1):  ## top-bottom p2
            if player2.fall_l != True and player1.fall_l != True and player1.fall_u != True and player2.fall_u != True and player1.fall_d != True and player2.fall_d != True:
                if player2.rect.bottom >= player1.rect.top and player2.rect.bottom <= player1.rect.bottom:
                    player2.y -= player_collision_bounce
                    player2.crash_sfx.play()
                    player1.y += player_collision_bounce
                    player1.crash_sfx.play()
        if numb_of_players > 2:
            # 3 vs 1 and 2 player
            if pygame.sprite.collide_rect(player3, player1):  ## top-bottom p3 vs p1
                if player3.fall_l != True and player1.fall_l != True and player1.fall_u != True and player3.fall_u != True and player1.fall_d != True and player3.fall_d != True:
                    if player3.rect.bottom >= player1.rect.top and player3.rect.bottom <= player1.rect.bottom:
                        player3.y -= player_collision_bounce
                        player3.crash_sfx.play()
                        player1.y += player_collision_bounce
                        player1.crash_sfx.play()
            if pygame.sprite.collide_rect(player1, player3):  ## top-bottom p1 vs p3
                if player1.fall_l != True and player3.fall_l != True and player1.fall_u != True and player3.fall_u != True and player1.fall_d != True and player3.fall_d != True:
                    if player1.rect.bottom >= player3.rect.top and player1.rect.bottom <= player3.rect.bottom:
                        player1.y -= player_collision_bounce
                        player1.crash_sfx.play()
                        player3.y += player_collision_bounce
                        player3.crash_sfx.play()
            if pygame.sprite.collide_rect(player3, player2):  ## top-bottom p3 vs p2
                if player3.fall_l != True and player2.fall_l != True and player2.fall_u != True and player3.fall_u != True and player2.fall_d != True and player3.fall_d != True:
                    if player3.rect.bottom >= player2.rect.top and player3.rect.bottom <= player2.rect.bottom:
                        player3.y -= player_collision_bounce
                        player3.crash_sfx.play()
                        player2.y += player_collision_bounce
                        player2.crash_sfx.play()
            if pygame.sprite.collide_rect(player2, player3):  ## top-bottom p2 vs p3
                if player2.fall_l != True and player3.fall_l != True and player2.fall_u != True and player3.fall_u != True and player2.fall_d != True and player3.fall_d != True:
                    if player2.rect.bottom >= player3.rect.top and player2.rect.bottom <= player3.rect.bottom:
                        player2.y -= player_collision_bounce
                        player2.crash_sfx.play()
                        player3.y += player_collision_bounce
                        player3.crash_sfx.play()
            if numb_of_players > 3:
                # 4 vs 1, 2, and 3 player
                if pygame.sprite.collide_rect(player4, player1):  ## top-bottom p4 vs p1
                    if player4.fall_l != True and player1.fall_l != True and player1.fall_u != True and player4.fall_u != True and player1.fall_d != True and player4.fall_d != True:
                        if player4.rect.bottom >= player1.rect.top and player4.rect.bottom <= player1.rect.bottom:
                            player4.y -= player_collision_bounce
                            player4.crash_sfx.play()
                            player1.y += player_collision_bounce
                            player1.crash_sfx.play()
                if pygame.sprite.collide_rect(player1, player4):  ## top-bottom p1 vs p4
                    if player1.fall_l != True and player4.fall_l != True and player1.fall_u != True and player4.fall_u != True and player1.fall_d != True and player4.fall_d != True:
                        if player1.rect.bottom >= player4.rect.top and player1.rect.bottom <= player4.rect.bottom:
                            player1.y -= player_collision_bounce
                            player1.crash_sfx.play()
                            player4.y += player_collision_bounce
                            player4.crash_sfx.play()
                if pygame.sprite.collide_rect(player4, player2):  ## top-bottom p4 vs p2
                    if player4.fall_l != True and player2.fall_l != True and player2.fall_u != True and player4.fall_u != True and player2.fall_d != True and player4.fall_d != True:
                        if player4.rect.bottom >= player2.rect.top and player4.rect.bottom <= player2.rect.bottom:
                            player4.y -= player_collision_bounce
                            player4.crash_sfx.play()
                            player2.y += player_collision_bounce
                            player2.crash_sfx.play()
                if pygame.sprite.collide_rect(player2, player4):  ## top-bottom p2 vs p4
                    if player2.fall_l != True and player4.fall_l != True and player2.fall_u != True and player4.fall_u != True and player2.fall_d != True and player4.fall_d != True:
                        if player2.rect.bottom >= player4.rect.top and player2.rect.bottom <= player4.rect.bottom:
                            player2.y -= player_collision_bounce
                            player2.crash_sfx.play()
                            player4.y += player_collision_bounce
                            player4.crash_sfx.play()
                if pygame.sprite.collide_rect(player4, player3):  ## top-bottom p4 vs p3
                    if player4.fall_l != True and player3.fall_l != True and player3.fall_u != True and player4.fall_u != True and player3.fall_d != True and player4.fall_d != True:
                        if player4.rect.bottom >= player3.rect.top and player4.rect.bottom <= player3.rect.bottom:
                            player4.y -= player_collision_bounce
                            player4.crash_sfx.play()
                            player3.y += player_collision_bounce
                            player3.crash_sfx.play()
                if pygame.sprite.collide_rect(player3, player4):  ## top-bottom p3 vs p4
                    if player3.fall_l != True and player4.fall_l != True and player3.fall_u != True and player4.fall_u != True and player3.fall_d != True and player4.fall_d != True:
                        if player3.rect.bottom >= player4.rect.top and player3.rect.bottom <= player4.rect.bottom:
                            player3.y -= player_collision_bounce
                            player3.crash_sfx.play()
                            player4.y += player_collision_bounce
                            player4.crash_sfx.play()


## groups ##
wave_grp = pygame.sprite.Group()
penguin_grp1 = pygame.sprite.Group()
penguin_grp2 = pygame.sprite.Group()
penguin_grp3 = pygame.sprite.Group()
penguin_grp4 = pygame.sprite.Group()
penguin_grp5 = pygame.sprite.Group()
penguin_grp6 = pygame.sprite.Group()
penguin_grp7 = pygame.sprite.Group()
penguin_grp8 = pygame.sprite.Group()
penguin_grp9 = pygame.sprite.Group()
penguin_grp10 = pygame.sprite.Group()
penguin_grp11 = pygame.sprite.Group()

#time.sleep(2)
## timers ##
wave_timer = pygame.USEREVENT + 1
pygame.time.set_timer(wave_timer, 2500)
penguin_timer = pygame.USEREVENT + 2
pygame.time.set_timer(penguin_timer, 2000)

## functions ##

def game_restart():
    global game_active, limit_time, menu
    menu.title_music.stop()
    menu.score_music.stop()
    menu.title_music_played = False
    menu.score_music_played = False
    menu.menu_change()
    menu.sfx_score_screen_played = False
    wave_grp.empty()
    penguin_grp1.empty()
    penguin_grp2.empty()
    penguin_grp3.empty()
    penguin_grp4.empty()
    penguin_grp5.empty()
    penguin_grp6.empty()
    penguin_grp7.empty()
    penguin_grp8.empty()
    penguin_grp9.empty()
    penguin_grp10.empty()
    penguin_grp11.empty()
    game_active = True
    limit_time = (pygame.time.get_ticks() / 1000)
    player1.player_reset()
    if numb_of_players > 1:
        player2.player_reset()
    if numb_of_players > 2:
        player3.player_reset()
    if numb_of_players > 3:
        player4.player_reset()
    pygame.time.set_timer(wave_timer, 2500)
    pygame.time.set_timer(penguin_timer, 2000)

def two_point_five_d():
    """blitting the player(s), obstacles, and background (ice floe) in 2.5 D"""
    p1_updated = False
    if numb_of_players > 1:
        p2_updated = False
        if numb_of_players > 2:
            p3_updated = False
            if numb_of_players > 3:
                p4_updated = False

    if player1.fall_u:
        player1.player_update()
        p1_updated = True
    if numb_of_players > 1:
        if player2.fall_u:
            player2.player_update()
            p2_updated = True
        if numb_of_players > 2:
            if player3.fall_u:
                player3.player_update()
                p3_updated = True
            if numb_of_players > 3:
                if player4.fall_u:
                    player4.player_update()
                    p4_updated = True
    bg_ice_floe.draw()
    if player1.rect.bottom <= 83 and p1_updated != True:
        if player1.fall_u != True:
            player1.player_update()
            p1_updated = True
    if numb_of_players > 1:
        if player2.rect.bottom <= 83 and p2_updated != True:
            if player2.fall_u != True:
                player2.player_update()
                p2_updated = True
        if numb_of_players > 2:
            if player3.rect.bottom <= 83 and p3_updated != True:
                if player3.fall_u != True:
                    player3.player_update()
                    p3_updated = True
            if numb_of_players > 3:
                if player4.rect.bottom <= 83 and p4_updated != True:
                    if player4.fall_u != True:
                        player4.player_update()
                        p4_updated = True
    penguin_grp11.update()
    if player1.rect.bottom <= 117 and p1_updated != True:
        if player1.fall_u != True:
            player1.player_update()
            p1_updated = True
    if numb_of_players > 1:
        if player2.rect.bottom <= 117 and p2_updated != True:
            if player2.fall_u != True:
                player2.player_update()
                p2_updated = True
        if numb_of_players > 2:
            if player3.rect.bottom <= 117 and p3_updated != True:
                if player3.fall_u != True:
                    player3.player_update()
                    p3_updated = True
            if numb_of_players > 3:
                if player4.rect.bottom <= 117 and p4_updated != True:
                    if player4.fall_u != True:
                        player4.player_update()
                        p4_updated = True
    penguin_grp10.update()
    if player1.rect.bottom <= 150 and p1_updated != True:
        if player1.fall_u != True:
            player1.player_update()
            p1_updated = True
    if numb_of_players > 1:
        if player2.rect.bottom <= 150 and p2_updated != True:
            if player2.fall_u != True:
                player2.player_update()
                p2_updated = True
        if numb_of_players > 2:
            if player3.rect.bottom <= 150 and p3_updated != True:
                if player3.fall_u != True:
                    player3.player_update()
                    p3_updated = True
            if numb_of_players > 3:
                if player4.rect.bottom <= 150 and p4_updated != True:
                    if player4.fall_u != True:
                        player4.player_update()
                        p4_updated = True
    penguin_grp9.update()
    if player1.rect.bottom <= 185 and p1_updated != True:
        if player1.fall_u != True:
            player1.player_update()
            p1_updated = True
    if numb_of_players > 1:
        if player2.rect.bottom <= 185 and p2_updated != True:
            if player2.fall_u != True:
                player2.player_update()
                p2_updated = True
        if numb_of_players > 2:
            if player3.rect.bottom <= 185 and p3_updated != True:
                if player3.fall_u != True:
                    player3.player_update()
                    p3_updated = True
            if numb_of_players > 3:
                if player4.rect.bottom <= 185 and p4_updated != True:
                    if player4.fall_u != True:
                        player4.player_update()
                        p4_updated = True
    penguin_grp8.update()
    if player1.rect.bottom <= 222 and p1_updated != True:
        if player1.fall_u != True:
            player1.player_update()
            p1_updated = True
    if numb_of_players > 1:
        if player2.rect.bottom <= 222 and p2_updated != True:
            if player2.fall_u != True:
                player2.player_update()
                p2_updated = True
        if numb_of_players > 2:
            if player3.rect.bottom <= 222 and p3_updated != True:
                if player3.fall_u != True:
                    player3.player_update()
                    p3_updated = True
            if numb_of_players > 3:
                if player4.rect.bottom <= 222 and p4_updated != True:
                    if player4.fall_u != True:
                        player4.player_update()
                        p4_updated = True
    penguin_grp7.update()
    if player1.rect.bottom <= 301 and p1_updated != True:
        player1.player_update()
        p1_updated = True
    if numb_of_players > 1:
        if player2.rect.bottom <= 302 and p2_updated != True:
            player2.player_update()
            p2_updated = True
        if numb_of_players > 2:
            if player3.rect.bottom <= 302 and p3_updated != True:
                player3.player_update()
                p3_updated = True
            if numb_of_players > 3:
                if player4.rect.bottom <= 302 and p4_updated != True:
                    player4.player_update()
                    p4_updated = True
    penguin_grp6.update()
    if player1.rect.bottom <= 301 and p1_updated != True:
        player1.player_update()
        p1_updated = True
    if numb_of_players > 1:
        if player2.rect.bottom <= 302 and p2_updated != True:
            player2.player_update()
            p2_updated = True
        if numb_of_players > 2:
            if player3.rect.bottom <= 302 and p3_updated != True:
                player3.player_update()
                p3_updated = True
            if numb_of_players > 3:
                if player4.rect.bottom <= 302 and p4_updated != True:
                    player4.player_update()
                    p4_updated = True
    penguin_grp5.update()
    if player1.rect.bottom <= 345 and p1_updated != True:
        player1.player_update()
        p1_updated = True
    if numb_of_players > 1:
        if player2.rect.bottom <= 345 and p2_updated != True:
            player2.player_update()
            p2_updated = True
        if numb_of_players > 2:
            if player3.rect.bottom <= 345 and p3_updated != True:
                player3.player_update()
                p3_updated = True
            if numb_of_players > 3:
                if player4.rect.bottom <= 345 and p4_updated != True:
                    player4.player_update()
                    p4_updated = True
    penguin_grp4.update()
    if player1.rect.bottom <= 390 and p1_updated != True:
        player1.player_update()
        p1_updated = True
    if numb_of_players > 1:
        if player2.rect.bottom <= 390 and p2_updated != True:
            player2.player_update()
            p2_updated = True
        if numb_of_players > 2:
            if player3.rect.bottom <= 390 and p3_updated != True:
                player3.player_update()
                p3_updated = True
            if numb_of_players > 3:
                if player4.rect.bottom <= 390 and p4_updated != True:
                    player4.player_update()
                    p4_updated = True
    penguin_grp3.update()
    if player1.rect.bottom <= 437 and p1_updated != True:
        player1.player_update()
        p1_updated = True
    if numb_of_players > 1:
        if player2.rect.bottom <= 437 and p2_updated != True:
            player2.player_update()
            p2_updated = True
        if numb_of_players > 2:
            if player3.rect.bottom <= 437 and p3_updated != True:
                player3.player_update()
                p3_updated = True
            if numb_of_players > 3:
                if player4.rect.bottom <= 437 and p4_updated != True:
                    player4.player_update()
                    p4_updated = True
    penguin_grp2.update()
    if player1.rect.bottom <= 486 and p1_updated != True:
        player1.player_update()
        p1_updated = True
    if numb_of_players > 1:
        if player2.rect.bottom <= 486 and p2_updated != True:
            player2.player_update()
            p2_updated = True
        if numb_of_players > 2:
            if player3.rect.bottom <= 486 and p3_updated != True:
                player3.player_update()
                p3_updated = True
            if numb_of_players > 3:
                if player4.rect.bottom <= 486 and p4_updated != True:
                    player4.player_update()
                    p4_updated = True
    penguin_grp1.update()
    if player1.rect.bottom > 486 and p1_updated != True:
        player1.player_update()
        p1_updated = True
    if numb_of_players > 1:
        if player2.rect.bottom > 486 and p2_updated != True:
            player2.player_update()
            p2_updated = True
        if numb_of_players > 2:
            if player3.rect.bottom > 486 and p3_updated != True:
                player3.player_update()
                p3_updated = True
            if numb_of_players > 3:
                if player4.rect.bottom > 486 and p4_updated != True:
                    player4.player_update()
                    p4_updated = True


def player_collisions_with_obstacles():
    if player1.fall_l != True and player1.fall_u != True and player1.fall_d != True:
        if pygame.sprite.spritecollideany(player1, penguin_grp1) or pygame.sprite.spritecollideany(player1, penguin_grp2) \
            or pygame.sprite.spritecollideany(player1, penguin_grp3) or pygame.sprite.spritecollideany(player1, penguin_grp4) \
            or pygame.sprite.spritecollideany(player1, penguin_grp5) or pygame.sprite.spritecollideany(player1, penguin_grp6) \
            or pygame.sprite.spritecollideany(player1, penguin_grp7) or pygame.sprite.spritecollideany(player1, penguin_grp8) \
            or pygame.sprite.spritecollideany(player1, penguin_grp9) or pygame.sprite.spritecollideany(player1, penguin_grp10) \
            or pygame.sprite.spritecollideany(player1, penguin_grp11):
            player1.hitted = True
            player1.crash_sfx.play()
    if numb_of_players > 1:
        if player2.fall_l != True and player2.fall_u != True and player2.fall_d != True:
            if pygame.sprite.spritecollideany(player2, penguin_grp1) or pygame.sprite.spritecollideany(player2, penguin_grp2) \
                or pygame.sprite.spritecollideany(player2, penguin_grp3) or pygame.sprite.spritecollideany(player2, penguin_grp4) \
                or pygame.sprite.spritecollideany(player2, penguin_grp5) or pygame.sprite.spritecollideany(player2, penguin_grp6) \
                or pygame.sprite.spritecollideany(player2, penguin_grp7) or pygame.sprite.spritecollideany(player2, penguin_grp8) \
                or pygame.sprite.spritecollideany(player2, penguin_grp9) or pygame.sprite.spritecollideany(player2, penguin_grp10) \
                or pygame.sprite.spritecollideany(player2, penguin_grp11):
                player2.hitted = True
                player2.crash_sfx.play()
        if numb_of_players > 2:
            if player3.fall_l != True and player3.fall_u != True and player3.fall_d != True:
                if pygame.sprite.spritecollideany(player3, penguin_grp1) or pygame.sprite.spritecollideany(player3, penguin_grp2) \
                        or pygame.sprite.spritecollideany(player3, penguin_grp3) or pygame.sprite.spritecollideany(player3, penguin_grp4) \
                        or pygame.sprite.spritecollideany(player3, penguin_grp5) or pygame.sprite.spritecollideany(player3, penguin_grp6) \
                        or pygame.sprite.spritecollideany(player3, penguin_grp7) or pygame.sprite.spritecollideany(player3, penguin_grp8) \
                        or pygame.sprite.spritecollideany(player3, penguin_grp9) or pygame.sprite.spritecollideany(player3, penguin_grp10) \
                        or pygame.sprite.spritecollideany(player3, penguin_grp11):
                    player3.hitted = True
                    player3.crash_sfx.play()
            if numb_of_players > 3:
                if player4.fall_l != True and player4.fall_u != True and player4.fall_d != True:
                    if pygame.sprite.spritecollideany(player4, penguin_grp1) or pygame.sprite.spritecollideany(player4,penguin_grp2) \
                            or pygame.sprite.spritecollideany(player4, penguin_grp3) or pygame.sprite.spritecollideany(player4, penguin_grp4) \
                            or pygame.sprite.spritecollideany(player4, penguin_grp5) or pygame.sprite.spritecollideany(player4, penguin_grp6) \
                            or pygame.sprite.spritecollideany(player4, penguin_grp7) or pygame.sprite.spritecollideany(player4, penguin_grp8) \
                            or pygame.sprite.spritecollideany(player4, penguin_grp9) or pygame.sprite.spritecollideany(player4, penguin_grp10) \
                            or pygame.sprite.spritecollideany(player4, penguin_grp11):
                        player4.hitted = True
                        player4.crash_sfx.play()

def obstacle_collisions():
    """collision between the obstacles"""
    if len(penguin_grp1) > 1:
        for penguin1 in penguin_grp1:
            p1 = penguin1
            for penguin2 in penguin_grp1:
                p2 = penguin2
                if p1.rect.left != p2.rect.left:
                    if pygame.sprite.collide_rect(p1, p2):
                        if p1.rect.left < p2.rect.left:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
                        else:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
    if len(penguin_grp2) > 1:
        for penguin1 in penguin_grp2:
            p1 = penguin1
            for penguin2 in penguin_grp2:
                p2 = penguin2
                if p1.rect.left != p2.rect.left:
                    if pygame.sprite.collide_rect(p1, p2):
                        if p1.rect.left < p2.rect.left:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
                        else:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
    if len(penguin_grp3) > 1:
        for penguin1 in penguin_grp3:
            p1 = penguin1
            for penguin2 in penguin_grp3:
                p2 = penguin2
                if p1.rect.left != p2.rect.left:
                    if pygame.sprite.collide_rect(p1, p2):
                        if p1.rect.left < p2.rect.left:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
                        else:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
    if len(penguin_grp4) > 1:
        for penguin1 in penguin_grp4:
            p1 = penguin1
            for penguin2 in penguin_grp4:
                p2 = penguin2
                if p1.rect.left != p2.rect.left:
                    if pygame.sprite.collide_rect(p1, p2):
                        if p1.rect.left < p2.rect.left:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
                        else:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
    if len(penguin_grp5) > 1:
        for penguin1 in penguin_grp5:
            p1 = penguin1
            for penguin2 in penguin_grp5:
                p2 = penguin2
                if p1.rect.left != p2.rect.left:
                    if pygame.sprite.collide_rect(p1, p2):
                        if p1.rect.left < p2.rect.left:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
                        else:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
    if len(penguin_grp6) > 1:
        for penguin1 in penguin_grp6:
            p1 = penguin1
            for penguin2 in penguin_grp6:
                p2 = penguin2
                if p1.rect.left != p2.rect.left:
                    if pygame.sprite.collide_rect(p1, p2):
                        if p1.rect.left < p2.rect.left:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
                        else:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
    if len(penguin_grp7) > 1:
        for penguin1 in penguin_grp7:
            p1 = penguin1
            for penguin2 in penguin_grp7:
                p2 = penguin2
                if p1.rect.left != p2.rect.left:
                    if pygame.sprite.collide_rect(p1, p2):
                        if p1.rect.left < p2.rect.left:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
                        else:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
    if len(penguin_grp8) > 1:
        for penguin1 in penguin_grp8:
            p1 = penguin1
            for penguin2 in penguin_grp8:
                p2 = penguin2
                if p1.rect.left != p2.rect.left:
                    if pygame.sprite.collide_rect(p1, p2):
                        if p1.rect.left < p2.rect.left:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
                        else:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
    if len(penguin_grp9) > 1:
        for penguin1 in penguin_grp9:
            p1 = penguin1
            for penguin2 in penguin_grp9:
                p2 = penguin2
                if p1.rect.left != p2.rect.left:
                    if pygame.sprite.collide_rect(p1, p2):
                        if p1.rect.left < p2.rect.left:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
                        else:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
    if len(penguin_grp10) > 1:
        for penguin1 in penguin_grp10:
            p1 = penguin1
            for penguin2 in penguin_grp10:
                p2 = penguin2
                if p1.rect.left != p2.rect.left:
                    if pygame.sprite.collide_rect(p1, p2):
                        if p1.rect.left < p2.rect.left:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
                        else:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
    if len(penguin_grp11) > 1:
        for penguin1 in penguin_grp11:
            p1 = penguin1
            for penguin2 in penguin_grp11:
                p2 = penguin2
                if p1.rect.left != p2.rect.left:
                    if pygame.sprite.collide_rect(p1, p2):
                        if p1.rect.left < p2.rect.left:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3
                        else:
                            if p1.movespeed_updated:
                                p1.movespeed = 4
                            else:
                                p1.movespeed = 2
                            if p2.movespeed_updated:
                                p2.movespeed = 6
                            else:
                                p2.movespeed = 3


# time limit #
def display_timelimit():
    global game_active
    current_time = int(time_limit - ((pygame.time.get_ticks() / 1000) - limit_time))
    font = marioKart_font
    if current_time <= 10:
        time_color = (255, 0, 0)
    else:
        time_color = (51, 255, 255)
    time_surf = font.render(str(current_time), False, time_color)
    time_rect = time_surf.get_rect(center = (750, 50))
    time_bg = pygame.Surface((76, 56))
    time_bg.fill((0, 0, 0,))
    time_bg.set_alpha(128)
    screen.blit(time_bg, time_bg.get_rect(center = (750, 50)))
    pygame.draw.rect(screen, (204, 204, 0), pygame.Rect(710, 20, 80, 60), 6, 6, 6, 6)
    screen.blit(time_surf, time_rect)
    if current_time <= 0:
        game_active = False
    return current_time     # return time in case a player falls from a ledge (timestamp of game over)
time_limit = 31
limit_time = 0


rows = [1,2,3,4,5,6,7,8,9,10,11]
big_rows = []

if __name__ == "__main__":
    game_active = False
    first_start = True
    running = True
    ### gameloop ###
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        player1.button_u = True
                    elif event.key == pygame.K_a:
                        player1.button_l = True
                    elif event.key == pygame.K_s:
                        player1.button_d = True
                    elif event.key == pygame.K_d:
                        player1.button_r = True
                    if numb_of_players > 1:
                        if event.key == pygame.K_i:
                            player2.button_u = True
                        elif event.key == pygame.K_j:
                            player2.button_l = True
                        elif event.key == pygame.K_k:
                            player2.button_d = True
                        elif event.key == pygame.K_l:
                            player2.button_r = True
                        if numb_of_players > 2:
                            if event.key == pygame.K_UP:
                                player3.button_u = True
                            elif event.key == pygame.K_LEFT:
                                player3.button_l = True
                            elif event.key == pygame.K_DOWN:
                                player3.button_d = True
                            elif event.key == pygame.K_RIGHT:
                                player3.button_r = True
                            if numb_of_players > 3:
                                if event.key == pygame.K_KP8:
                                    player4.button_u = True
                                elif event.key == pygame.K_KP4:
                                    player4.button_l = True
                                elif event.key == pygame.K_KP5:
                                    player4.button_d = True
                                elif event.key == pygame.K_KP6:
                                    player4.button_r = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        player1.button_u = False
                    elif event.key == pygame.K_a:
                        player1.button_l = False
                    elif event.key == pygame.K_s:
                        player1.button_d = False
                    elif event.key == pygame.K_d:
                        player1.button_r = False
                    if numb_of_players > 1:
                        if event.key == pygame.K_i:
                            player2.button_u = False
                        elif event.key == pygame.K_j:
                            player2.button_l = False
                        elif event.key == pygame.K_k:
                            player2.button_d = False
                        elif event.key == pygame.K_l:
                            player2.button_r = False
                        if numb_of_players > 2:
                            if event.key == pygame.K_UP:
                                player3.button_u = False
                            elif event.key == pygame.K_LEFT:
                                player3.button_l = False
                            elif event.key == pygame.K_DOWN:
                                player3.button_d = False
                            elif event.key == pygame.K_RIGHT:
                                player3.button_r = False
                            if numb_of_players > 3:
                                if event.key == pygame.K_KP8:
                                    player4.button_u = False
                                elif event.key == pygame.K_KP4:
                                    player4.button_l = False
                                elif event.key == pygame.K_KP5:
                                    player4.button_d = False
                                elif event.key == pygame.K_KP6:
                                    player4.button_r = False
                if event.type == wave_timer:
                    if random.randint(1,10) > 3:
                        wave_grp.add(Wave(random.randint(1,3)))
                if event.type == penguin_timer:
                    penguins_started = True
                    if display_timelimit() <= 15:      # bei nur noch 15 sekunden timelimit mehr pinguine und schnellere spawnrate
                        spawns_at_rows = random.sample(rows, k=6)
                        pygame.time.set_timer(penguin_timer, 1000)
                    else:
                        spawns_at_rows = random.sample(rows, k=4)
                    spawns_at_rows.sort(reverse=True)
                    if random.randint(1,10) > 5:    # 40% chance auf big-penguin spawn. Spawned dahin, wo eine Doppelreihe frei ist
                        if 1 not in spawns_at_rows and 2 not in spawns_at_rows:
                            big_rows.append(1)
                        if 3 not in spawns_at_rows and 4 not in spawns_at_rows:
                            big_rows.append(3)
                        if 5 not in spawns_at_rows and 6 not in spawns_at_rows:
                            big_rows.append(5)
                        if 7 not in spawns_at_rows and 8 not in spawns_at_rows:
                            big_rows.append(7)
                        if 9 not in spawns_at_rows and 10 not in spawns_at_rows:
                            big_rows.append(9)
                    if 11 in spawns_at_rows:
                        penguin_grp11.add(Penguins("small", 11))
                    if 10 in spawns_at_rows:
                        penguin_grp10.add(Penguins("small", 10))
                    if 9 in spawns_at_rows:
                        penguin_grp9.add(Penguins("small", 9))
                    elif 9 in big_rows:
                        penguin_grp9.add(Penguins("big", 9))
                    if 8 in spawns_at_rows:
                        penguin_grp8.add(Penguins("small", 8))
                    if 7 in spawns_at_rows:
                        penguin_grp7.add(Penguins("small", 7))
                    elif 7 in big_rows:
                        penguin_grp7.add(Penguins("big", 7))
                    if 6 in spawns_at_rows:
                        penguin_grp6.add(Penguins("small", 6))
                    if 5 in spawns_at_rows:
                        penguin_grp5.add(Penguins("small", 5))
                    elif 5 in big_rows:
                        penguin_grp5.add(Penguins("big", 5))
                    if 4 in spawns_at_rows:
                        penguin_grp4.add(Penguins("small", 4))
                    if 3 in spawns_at_rows:
                        penguin_grp3.add(Penguins("small", 3))
                    elif 3 in big_rows:
                        penguin_grp3.add(Penguins("big", 3))
                    if 2 in spawns_at_rows:
                        penguin_grp2.add(Penguins("small", 2))
                    if 1 in spawns_at_rows:
                        penguin_grp1.add(Penguins("small", 1))
                    elif 1 in big_rows:
                        penguin_grp1.add(Penguins("big", 1))
                    if len(big_rows) > 0:
                        big_rows = []
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and menu.which_menu == "numb_of_players":
                        menu.menu_cursor.menu_update()
                        numb_of_players = menu.menu_cursor.number_of_players
                    elif event.key == pygame.K_RETURN and (menu.which_menu == "control_mapping" or menu.which_menu == "score_screen"):  # game retry
                        game_restart()
                        first_start = False
                        game_music.play(loops=-1)
                    elif event.key == pygame.K_SPACE and menu.which_menu == "score_screen":  # full game restart
                        game_restart()
                        menu.char_selected_reset()
                        first_start = True
                        game_active = False
                    if menu.which_menu == "numb_of_players":
                        menu.menu_cursor.pressed = False
                    elif menu.which_menu == "char_select":
                        menu.p1_char_select.pressed = False
                        if numb_of_players > 1:
                            menu.p2_char_select.pressed = False
                            if numb_of_players > 2:
                                menu.p3_char_select.pressed = False
                                if numb_of_players > 3:
                                    menu.p4_char_select.pressed = False

        if game_active:     # the actual game

            if numb_of_players == 1:
                if player1.fallen:
                    game_active = False
            elif numb_of_players == 2:
                if player1.fallen and player2.fallen:
                    game_active = False
            elif numb_of_players == 3:
                if player1.fallen and player2.fallen and player3.fallen:
                    game_active = False
            elif numb_of_players == 4:
                if player1.fallen and player2.fallen and player3.fallen:
                    game_active = False

            bg_sea.draw()
            bg_sea_lower_edge.animation()
            bg_sea_lower_edge.draw()
            wave_grp.update()

            player_collision()
            obstacle_collisions()
            player_collisions_with_obstacles()

            two_point_five_d()

            current_time = display_timelimit()

            if player1.fallen != True:
                player1.score = current_time
            if numb_of_players > 1:
                if player2.fallen != True:
                    player2.score = current_time
                if numb_of_players > 2:
                    if player3.fallen != True:
                        player3.score = current_time
                    if numb_of_players > 3:
                        if player4.fallen != True:
                            player4.score = current_time

        else:   # menu screens
            if first_start:
                if menu.title_music_played != True:
                    game_music.stop()
                    menu.title_music.play(loops=-1)
                    menu.title_music_played = True
                if menu.which_menu == "numb_of_players":
                    menu.display_menu_numb_of_players()
                    menu.menu_cursor.menu_update()
                elif menu.which_menu == "char_select":
                    menu.display_char_select()
                    menu.char_select_rect()
                    menu.p1_char_select.menu_update()
                    if menu.p1_char:
                        player1 = Player(1, menu.p1_char_select.character[:3])
                        if numb_of_players == 1 and menu.p1_char:
                            menu.menu_change()
                    if numb_of_players > 1:
                        menu.p2_char_select.menu_update()
                        if menu.p2_char:
                            player2 = Player(2, menu.p2_char_select.character[:3])
                            if numb_of_players == 2 and menu.p1_char and menu.p2_char:
                                menu.menu_change()
                        if numb_of_players > 2:
                            menu.p3_char_select.menu_update()
                            if menu.p3_char:
                                player3 = Player(3, menu.p3_char_select.character[:3])
                                if numb_of_players == 3 and menu.p1_char and menu.p2_char and menu.p3_char:
                                    menu.menu_change()
                            if numb_of_players > 3:
                                menu.p4_char_select.menu_update()
                                if menu.p4_char:
                                    player4 = Player(4, menu.p4_char_select.character[:3])
                                    if numb_of_players == 4 and menu.p1_char and menu.p2_char and menu.p3_char and menu.p4_char:
                                        menu.menu_change()
                elif menu.which_menu == "control_mapping":
                    menu.display_control_mapping()

            else:

                if menu.score_music_played != True:
                    game_music.stop()
                    menu.score_music.play(loops=-1)
                    menu.score_music_played = True

                if player1.score > 0:
                    score_message_surf_p1 = mario64_font.render("P1, what a pitty! " + str(player1.score) + " seconds left.", False, (25, 25, 25))
                else:
                    score_message_surf_p1 = mario64_font.render("P1 made it - Congratulations!", False, (25, 25, 25))
                score_message_rect_p1 = score_message_surf_p1.get_rect(midleft=(200, 60))
                if numb_of_players > 1:
                    if player2.score > 0:
                        score_message_surf_p2 = mario64_font.render("P2, what a pitty! " + str(player2.score) + " seconds left.", False, (25, 25, 25))
                    else:
                        score_message_surf_p2 = mario64_font.render("P2 made it - Congratulations!", False, (25, 25, 25))
                    score_message_rect_p2 = score_message_surf_p2.get_rect(midleft=(200, 130))
                if numb_of_players > 2:
                    if player3.score > 0:
                        score_message_surf_p3 = mario64_font.render("P3, what a pitty! " + str(player3.score) + " seconds left.", False, (25, 25, 25))
                    else:
                        score_message_surf_p3 = mario64_font.render("P3 made it - Congratulations!", False, (25, 25, 25))
                    score_message_rect_p3 = score_message_surf_p3.get_rect(midleft=(200, 200))
                if numb_of_players > 3:
                    if player4.score > 0:
                        score_message_surf_p4 = mario64_font.render("P4, what a pitty!  " + str(player4.score) + " seconds left.", False, (25, 25, 25))
                    else:
                        score_message_surf_p4 = mario64_font.render("P4 made it - Congratulations!", False, (25, 25, 25))
                    score_message_rect_p4 = score_message_surf_p4.get_rect(midleft=(200, 270))

                menu.display_score_screen()

                screen.blit(score_message_surf_p1, score_message_rect_p1)
                if numb_of_players > 1:
                    screen.blit(score_message_surf_p2, score_message_rect_p2)
                if numb_of_players > 2:
                    screen.blit(score_message_surf_p3, score_message_rect_p3)
                if numb_of_players > 3:
                    screen.blit(score_message_surf_p4, score_message_rect_p4)

        pygame.display.set_caption("Pushy Penguins 2D Demake | " + str(round(clock.get_fps())) + " FPS")
        pygame.display.update()
        clock.tick(FPS)