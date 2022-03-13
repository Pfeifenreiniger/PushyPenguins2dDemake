
import pygame

screen = pygame.display.set_mode((800, 600))

class Player(pygame.sprite.Sprite):

    def __init__(self, numb, char):
        super().__init__()
        self.numb = numb
        self.char = char
        self.player_reset()

    def player_imgs_stand_down(self):
        self.stand_down_imgs = [
            pygame.image.load("graphics/game/player/" + self.char + "/stand_down/" + self.char +"_stand_down_f1.png").convert_alpha(),
            pygame.image.load("graphics/game/player/" + self.char + "/stand_down/" + self.char + "_stand_down_f2.png").convert_alpha()]

    def player_imgs_stand_up(self):
        self.stand_up_imgs = [
                pygame.image.load("graphics/game/player/" + self.char + "/stand_up/" + self.char + "_stand_up_f1.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/stand_up/" + self.char + "_stand_up_f2.png").convert_alpha()]

    def player_imgs_stand_left(self):
        self.stand_left_imgs = [
                pygame.image.load("graphics/game/player/" + self.char + "/stand_left/" + self.char + "_stand_left_f1.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/stand_left/" + self.char + "_stand_left_f2.png").convert_alpha()]

    def player_imgs_stand_right(self):
        self.stand_right_imgs = [
                pygame.image.load("graphics/game/player/" + self.char + "/stand_right/" + self.char + "_stand_right_f1.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/stand_right/" + self.char + "_stand_right_f2.png").convert_alpha()]

    def player_imgs_run_down(self):
        self.run_down_imgs = [
                pygame.image.load("graphics/game/player/" + self.char + "/run_down/" + self.char + "_run_down_f1.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/run_down/" + self.char + "_run_down_f2.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/run_down/" + self.char + "_run_down_f3.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/run_down/" + self.char + "_run_down_f4.png").convert_alpha()]

    def player_imgs_run_up(self):
        self.run_up_imgs = [
                pygame.image.load("graphics/game/player/" + self.char + "/run_up/" + self.char + "_run_up_f1.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/run_up/" + self.char + "_run_up_f2.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/run_up/" + self.char + "_run_up_f3.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/run_up/" + self.char + "_run_up_f4.png").convert_alpha()]

    def player_imgs_run_right(self):
        self.run_right_imgs = [
                pygame.image.load("graphics/game/player/" + self.char + "/run_right/" + self.char + "_run_right_f1.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/run_right/" + self.char + "_run_right_f2.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/run_right/" + self.char + "_run_right_f3.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/run_right/" + self.char + "_run_right_f4.png").convert_alpha()]

    def player_imgs_run_left(self):
        self.run_left_imgs = [
                pygame.image.load("graphics/game/player/" + self.char + "/run_left/" + self.char + "_run_left_f1.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/run_left/" + self.char + "_run_left_f2.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/run_left/" + self.char + "_run_left_f3.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/run_left/" + self.char + "_run_left_f4.png").convert_alpha()]

    def player_imgs_fall_down(self):
        self.fall_down_imgs = [
                pygame.image.load("graphics/game/player/" + self.char + "/fall_down/" + self.char + "_fall_down_f1.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/fall_down/" + self.char + "_fall_down_f2.png").convert_alpha()]

    def player_imgs_fall_up(self):
        self.fall_up_imgs = [
                pygame.image.load("graphics/game/player/" + self.char + "/fall_up/" + self.char + "_fall_up_f1.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/fall_up/" + self.char + "_fall_up_f2.png").convert_alpha()]

    def player_imgs_fall_left(self):
        self.fall_left_imgs = [
                pygame.image.load("graphics/game/player/" + self.char + "/fall_left/" + self.char + "_fall_left_f1.png").convert_alpha(),
                pygame.image.load("graphics/game/player/" + self.char + "/fall_left/" + self.char + "_fall_left_f2.png").convert_alpha()]

    def player_imgs_hit(self):
        self.hit_img = pygame.image.load("graphics/game/player/" + self.char + "/hit/" + self.char + "_hit.png").convert_alpha()

    def player_imgs_shadow(self):
        self.shadow_img = pygame.image.load("graphics/game/player/" + self.char + "/shadow.png").convert_alpha()
        self.shadow_img.set_alpha(128)

    def player_imgs_splash(self):
        self.splash_img = pygame.image.load("graphics/game/player/player_splash.png").convert_alpha()

    def player_imgs(self):
        """loading images (images depend on character)"""
        self.player_imgs_stand_down()
        self.player_imgs_stand_up()
        self.player_imgs_stand_left()
        self.player_imgs_stand_right()
        self.player_imgs_run_down()
        self.player_imgs_run_up()
        self.player_imgs_run_left()
        self.player_imgs_run_right()
        self.player_imgs_fall_down()
        self.player_imgs_fall_up()
        self.player_imgs_fall_left()
        self.player_imgs_hit()
        self.player_imgs_shadow()
        self.player_imgs_splash()

    def player_sfx(self):
        if self.char == "wal":
            self.fall_sfx = pygame.mixer.Sound("voices/waluigi/mparty5_waluigi_whahoahoa_(fall).wav")
            self.crash_sfx = pygame.mixer.Sound("voices/waluigi/mparty5_waluigi_woua_(crash).wav")
        elif self.char == "pea":
            self.fall_sfx = pygame.mixer.Sound("voices/peach/mparty5_peach_nooo_(fall).wav")
            self.crash_sfx = pygame.mixer.Sound("voices/peach/mparty5_peach_oh_(crash).wav")
        elif self.char == "yos":
            self.fall_sfx = pygame.mixer.Sound("voices/yoshi/mparty5_yoshi_auauau_(fall).wav")
            self.crash_sfx = pygame.mixer.Sound("voices/yoshi/mparty5_yoshi_hou_(crash).wav")
        elif self.char == "mar":
            self.fall_sfx = pygame.mixer.Sound("voices/mario/sm64_mario_scream_(fall).wav")
            self.crash_sfx = pygame.mixer.Sound("voices/mario/mparty5_mario_ouuu_(crash).wav")
        self.fall_sfx.set_volume(0.8)
        self.crash_sfx.set_volume(0.7)

    def player_imgs_scale(self):
        """scales the player image based on the current location of the player and the sprite(s) used"""
        if self.rect.bottom <= 68:
            if self.fall_l != True or self.fall_u != True:
                self.shadow_scale = (57, 14)
                self.player_imgs_shadow()
                self.shadow_img = pygame.transform.smoothscale(self.shadow_img, self.shadow_scale)
            if self.stand_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_d_scale = (57, 64)
                self.player_imgs_stand_down()
                self.stand_down_imgs[0] = pygame.transform.smoothscale(self.stand_down_imgs[0], self.stand_d_scale)
                self.stand_down_imgs[1] = pygame.transform.smoothscale(self.stand_down_imgs[1], self.stand_d_scale)
            elif self.stand_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_u_scale = (57, 64)
                self.player_imgs_stand_up()
                self.stand_up_imgs[0] = pygame.transform.smoothscale(self.stand_up_imgs[0], self.stand_u_scale)
                self.stand_up_imgs[1] = pygame.transform.smoothscale(self.stand_up_imgs[1], self.stand_u_scale)
            elif self.stand_l:
                if self.char == "wal":
                    self.stand_l_scale = (23, 64)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_l_scale = (57, 64)
                self.player_imgs_stand_left()
                self.stand_left_imgs[0] = pygame.transform.smoothscale(self.stand_left_imgs[0], self.stand_l_scale)
                self.stand_left_imgs[1] = pygame.transform.smoothscale(self.stand_left_imgs[1], self.stand_l_scale)
            elif self.stand_r:
                if self.char == "wal":
                    self.stand_r_scale = (23, 64)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_r_scale = (57, 64)
                self.player_imgs_stand_right()
                self.stand_right_imgs[0] = pygame.transform.smoothscale(self.stand_right_imgs[0], self.stand_r_scale)
                self.stand_right_imgs[1] = pygame.transform.smoothscale(self.stand_right_imgs[1], self.stand_r_scale)
            elif self.run_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_d_scale = (57, 64)
                self.player_imgs_run_down()
                self.run_down_imgs[0] = pygame.transform.smoothscale(self.run_down_imgs[0], self.run_d_scale)
                self.run_down_imgs[1] = pygame.transform.smoothscale(self.run_down_imgs[1], self.run_d_scale)
                self.run_down_imgs[2] = pygame.transform.smoothscale(self.run_down_imgs[2], self.run_d_scale)
                self.run_down_imgs[3] = pygame.transform.smoothscale(self.run_down_imgs[3], self.run_d_scale)
            elif self.run_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_u_scale = (57, 64)
                self.player_imgs_run_up()
                self.run_up_imgs[0] = pygame.transform.smoothscale(self.run_up_imgs[0], self.run_u_scale)
                self.run_up_imgs[1] = pygame.transform.smoothscale(self.run_up_imgs[1], self.run_u_scale)
                self.run_up_imgs[2] = pygame.transform.smoothscale(self.run_up_imgs[2], self.run_u_scale)
                self.run_up_imgs[3] = pygame.transform.smoothscale(self.run_up_imgs[3], self.run_u_scale)
            elif self.run_l:
                if self.char == "wal":
                    self.run_l_scale = (62, 64)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_l_scale = (57, 64)
                self.player_imgs_run_left()
                self.run_left_imgs[0] = pygame.transform.smoothscale(self.run_left_imgs[0], self.run_l_scale)
                self.run_left_imgs[1] = pygame.transform.smoothscale(self.run_left_imgs[1], self.run_l_scale)
                self.run_left_imgs[2] = pygame.transform.smoothscale(self.run_left_imgs[2], self.run_l_scale)
                self.run_left_imgs[3] = pygame.transform.smoothscale(self.run_left_imgs[3], self.run_l_scale)
            elif self.run_r:
                if self.char == "wal":
                    self.run_r_scale = (62, 64)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                        self.run_r_scale = (57, 64)
                self.player_imgs_run_right()
                self.run_right_imgs[0] = pygame.transform.smoothscale(self.run_right_imgs[0], self.run_r_scale)
                self.run_right_imgs[1] = pygame.transform.smoothscale(self.run_right_imgs[1], self.run_r_scale)
                self.run_right_imgs[2] = pygame.transform.smoothscale(self.run_right_imgs[2], self.run_r_scale)
                self.run_right_imgs[3] = pygame.transform.smoothscale(self.run_right_imgs[3], self.run_r_scale)
            elif self.fall_u:
                if self.char == "wal":
                    self.fall_u_scale = (67,64)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.fall_u_scale = (57, 64)
                self.player_imgs_fall_up()
                self.fall_up_imgs[0] = pygame.transform.smoothscale(self.fall_up_imgs[0], self.fall_u_scale)
                self.fall_up_imgs[1] = pygame.transform.smoothscale(self.fall_up_imgs[1], self.fall_u_scale)
                self.splash_scale = (80, 89)
                self.splash_img = pygame.transform.smoothscale(self.splash_img, self.splash_scale)
            elif self.fall_l:
                if self.char == "wal":
                    self.fall_l_scale = (41,64)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.fall_l_scale = (57, 64)
                self.player_imgs_fall_left()
                self.fall_left_imgs[0] = pygame.transform.smoothscale(self.fall_left_imgs[0], self.fall_l_scale)
                self.fall_left_imgs[1] = pygame.transform.smoothscale(self.fall_left_imgs[1], self.fall_l_scale)
                self.splash_scale = (80, 89)
                self.player_imgs_splash()
                self.splash_img = pygame.transform.smoothscale(self.splash_img, self.splash_scale)
            elif self.hitted:
                if self.char == "wal":
                    self.hit_scale = (31, 64)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.hit_scale = (57, 64)
                self.player_imgs_hit()
                self.hit_img = pygame.transform.smoothscale(self.hit_img, self.hit_scale)
        elif self.rect.bottom <= 98:
            if self.fall_l != True:
                self.shadow_scale = (58, 15)
                self.player_imgs_shadow()
                self.shadow_img = pygame.transform.smoothscale(self.shadow_img, self.shadow_scale)
            if self.stand_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_d_scale = (58, 65)
                self.player_imgs_stand_down()
                self.stand_down_imgs[0] = pygame.transform.smoothscale(self.stand_down_imgs[0], self.stand_d_scale)
                self.stand_down_imgs[1] = pygame.transform.smoothscale(self.stand_down_imgs[1], self.stand_d_scale)
            elif self.stand_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_u_scale = (58, 65)
                self.player_imgs_stand_up()
                self.stand_up_imgs[0] = pygame.transform.smoothscale(self.stand_up_imgs[0], self.stand_u_scale)
                self.stand_up_imgs[1] = pygame.transform.smoothscale(self.stand_up_imgs[1], self.stand_u_scale)
            elif self.stand_l:
                if self.char == "wal":
                    self.stand_l_scale = (24, 65)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_l_scale = (58, 65)
                self.player_imgs_stand_left()
                self.stand_left_imgs[0] = pygame.transform.smoothscale(self.stand_left_imgs[0], self.stand_l_scale)
                self.stand_left_imgs[1] = pygame.transform.smoothscale(self.stand_left_imgs[1], self.stand_l_scale)
            elif self.stand_r:
                if self.char == "wal":
                    self.stand_r_scale = (24, 65)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_r_scale = (58, 65)
                self.player_imgs_stand_right()
                self.stand_right_imgs[0] = pygame.transform.smoothscale(self.stand_right_imgs[0], self.stand_r_scale)
                self.stand_right_imgs[1] = pygame.transform.smoothscale(self.stand_right_imgs[1], self.stand_r_scale)
            elif self.run_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_d_scale = (58, 65)
                self.player_imgs_run_down()
                self.run_down_imgs[0] = pygame.transform.smoothscale(self.run_down_imgs[0], self.run_d_scale)
                self.run_down_imgs[1] = pygame.transform.smoothscale(self.run_down_imgs[1], self.run_d_scale)
                self.run_down_imgs[2] = pygame.transform.smoothscale(self.run_down_imgs[2], self.run_d_scale)
                self.run_down_imgs[3] = pygame.transform.smoothscale(self.run_down_imgs[3], self.run_d_scale)
            elif self.run_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_u_scale = (58, 65)
                self.player_imgs_run_up()
                self.run_up_imgs[0] = pygame.transform.smoothscale(self.run_up_imgs[0], self.run_u_scale)
                self.run_up_imgs[1] = pygame.transform.smoothscale(self.run_up_imgs[1], self.run_u_scale)
                self.run_up_imgs[2] = pygame.transform.smoothscale(self.run_up_imgs[2], self.run_u_scale)
                self.run_up_imgs[3] = pygame.transform.smoothscale(self.run_up_imgs[3], self.run_u_scale)
            elif self.run_l:
                if self.char == "wal":
                    self.run_l_scale = (63, 65)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_l_scale = (58, 65)
                self.player_imgs_run_left()
                self.run_left_imgs[0] = pygame.transform.smoothscale(self.run_left_imgs[0], self.run_l_scale)
                self.run_left_imgs[1] = pygame.transform.smoothscale(self.run_left_imgs[1], self.run_l_scale)
                self.run_left_imgs[2] = pygame.transform.smoothscale(self.run_left_imgs[2], self.run_l_scale)
                self.run_left_imgs[3] = pygame.transform.smoothscale(self.run_left_imgs[3], self.run_l_scale)
            elif self.run_r:
                if self.char == "wal":
                    self.run_r_scale = (63, 65)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_r_scale = (58, 65)
                self.player_imgs_run_right()
                self.run_right_imgs[0] = pygame.transform.smoothscale(self.run_right_imgs[0], self.run_r_scale)
                self.run_right_imgs[1] = pygame.transform.smoothscale(self.run_right_imgs[1], self.run_r_scale)
                self.run_right_imgs[2] = pygame.transform.smoothscale(self.run_right_imgs[2], self.run_r_scale)
                self.run_right_imgs[3] = pygame.transform.smoothscale(self.run_right_imgs[3], self.run_r_scale)
            elif self.fall_l:
                if self.char == "wal":
                    self.fall_l_scale = (42,65)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.fall_l_scale = (58, 65)
                self.player_imgs_fall_left()
                self.fall_left_imgs[0] = pygame.transform.smoothscale(self.fall_left_imgs[0], self.fall_l_scale)
                self.fall_left_imgs[1] = pygame.transform.smoothscale(self.fall_left_imgs[1], self.fall_l_scale)
                self.splash_scale = (81, 90)
                self.player_imgs_splash()
                self.splash_img = pygame.transform.smoothscale(self.splash_img, self.splash_scale)
            elif self.hitted:
                if self.char == "wal":
                    self.hit_scale = (32, 65)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.hit_scale = (58, 65)
                self.player_imgs_hit()
                self.hit_img = pygame.transform.smoothscale(self.hit_img, self.hit_scale)
        elif self.rect.bottom <= 130:
            if self.fall_l != True:
                self.shadow_scale = (59, 16)
                self.player_imgs_shadow()
                self.shadow_img = pygame.transform.smoothscale(self.shadow_img, self.shadow_scale)
            if self.stand_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_d_scale = (59, 66)
                self.player_imgs_stand_down()
                self.stand_down_imgs[0] = pygame.transform.smoothscale(self.stand_down_imgs[0], self.stand_d_scale)
                self.stand_down_imgs[1] = pygame.transform.smoothscale(self.stand_down_imgs[1], self.stand_d_scale)
            elif self.stand_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_u_scale = (59, 66)
                self.player_imgs_stand_up()
                self.stand_up_imgs[0] = pygame.transform.smoothscale(self.stand_up_imgs[0], self.stand_u_scale)
                self.stand_up_imgs[1] = pygame.transform.smoothscale(self.stand_up_imgs[1], self.stand_u_scale)
            elif self.stand_l:
                if self.char == "wal":
                    self.stand_l_scale = (25, 66)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_l_scale = (59, 66)
                self.player_imgs_stand_left()
                self.stand_left_imgs[0] = pygame.transform.smoothscale(self.stand_left_imgs[0], self.stand_l_scale)
                self.stand_left_imgs[1] = pygame.transform.smoothscale(self.stand_left_imgs[1], self.stand_l_scale)
            elif self.stand_r:
                if self.char == "wal":
                    self.stand_r_scale = (25, 66)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_r_scale = (59, 66)
                self.player_imgs_stand_right()
                self.stand_right_imgs[0] = pygame.transform.smoothscale(self.stand_right_imgs[0], self.stand_r_scale)
                self.stand_right_imgs[1] = pygame.transform.smoothscale(self.stand_right_imgs[1], self.stand_r_scale)
            elif self.run_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_d_scale = (59, 66)
                self.player_imgs_run_down()
                self.run_down_imgs[0] = pygame.transform.smoothscale(self.run_down_imgs[0], self.run_d_scale)
                self.run_down_imgs[1] = pygame.transform.smoothscale(self.run_down_imgs[1], self.run_d_scale)
                self.run_down_imgs[2] = pygame.transform.smoothscale(self.run_down_imgs[2], self.run_d_scale)
                self.run_down_imgs[3] = pygame.transform.smoothscale(self.run_down_imgs[3], self.run_d_scale)
            elif self.run_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_u_scale = (59, 66)
                self.player_imgs_run_up()
                self.run_up_imgs[0] = pygame.transform.smoothscale(self.run_up_imgs[0], self.run_u_scale)
                self.run_up_imgs[1] = pygame.transform.smoothscale(self.run_up_imgs[1], self.run_u_scale)
                self.run_up_imgs[2] = pygame.transform.smoothscale(self.run_up_imgs[2], self.run_u_scale)
                self.run_up_imgs[3] = pygame.transform.smoothscale(self.run_up_imgs[3], self.run_u_scale)
            elif self.run_l:
                if self.char == "wal":
                    self.run_l_scale = (64, 66)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_l_scale = (59, 66)
                self.player_imgs_run_left()
                self.run_left_imgs[0] = pygame.transform.smoothscale(self.run_left_imgs[0], self.run_l_scale)
                self.run_left_imgs[1] = pygame.transform.smoothscale(self.run_left_imgs[1], self.run_l_scale)
                self.run_left_imgs[2] = pygame.transform.smoothscale(self.run_left_imgs[2], self.run_l_scale)
                self.run_left_imgs[3] = pygame.transform.smoothscale(self.run_left_imgs[3], self.run_l_scale)
            elif self.run_r:
                if self.char == "wal":
                    self.run_r_scale = (64, 66)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_r_scale = (59, 66)
                self.player_imgs_run_right()
                self.run_right_imgs[0] = pygame.transform.smoothscale(self.run_right_imgs[0], self.run_r_scale)
                self.run_right_imgs[1] = pygame.transform.smoothscale(self.run_right_imgs[1], self.run_r_scale)
                self.run_right_imgs[2] = pygame.transform.smoothscale(self.run_right_imgs[2], self.run_r_scale)
                self.run_right_imgs[3] = pygame.transform.smoothscale(self.run_right_imgs[3], self.run_r_scale)
            elif self.fall_l:
                if self.char == "wal":
                    self.fall_l_scale = (43,66)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.fall_l_scale = (59, 66)
                self.player_imgs_fall_left()
                self.fall_left_imgs[0] = pygame.transform.smoothscale(self.fall_left_imgs[0], self.fall_l_scale)
                self.fall_left_imgs[1] = pygame.transform.smoothscale(self.fall_left_imgs[1], self.fall_l_scale)
                self.splash_scale = (82, 91)
                self.player_imgs_splash()
                self.splash_img = pygame.transform.smoothscale(self.splash_img, self.splash_scale)
            elif self.hitted:
                if self.char == "wal":
                    self.hit_scale = (33, 66)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.hit_scale = (59, 66)
                self.player_imgs_hit()
                self.hit_img = pygame.transform.smoothscale(self.hit_img, self.hit_scale)
        elif self.rect.bottom <= 164:
            if self.fall_l != True:
                self.shadow_scale = (60, 17)
                self.player_imgs_shadow()
                self.shadow_img = pygame.transform.smoothscale(self.shadow_img, self.shadow_scale)
            if self.stand_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_d_scale = (60, 67)
                self.player_imgs_stand_down()
                self.stand_down_imgs[0] = pygame.transform.smoothscale(self.stand_down_imgs[0], self.stand_d_scale)
                self.stand_down_imgs[1] = pygame.transform.smoothscale(self.stand_down_imgs[1], self.stand_d_scale)
            elif self.stand_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_u_scale = (60, 67)
                self.player_imgs_stand_up()
                self.stand_up_imgs[0] = pygame.transform.smoothscale(self.stand_up_imgs[0], self.stand_u_scale)
                self.stand_up_imgs[1] = pygame.transform.smoothscale(self.stand_up_imgs[1], self.stand_u_scale)
            elif self.stand_l:
                if self.char == "wal":
                    self.stand_l_scale = (26, 67)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_l_scale = (60, 67)
                self.player_imgs_stand_left()
                self.stand_left_imgs[0] = pygame.transform.smoothscale(self.stand_left_imgs[0], self.stand_l_scale)
                self.stand_left_imgs[1] = pygame.transform.smoothscale(self.stand_left_imgs[1], self.stand_l_scale)
            elif self.stand_r:
                if self.char == "wal":
                    self.stand_r_scale = (26, 67)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_r_scale = (60, 67)
                self.player_imgs_stand_right()
                self.stand_right_imgs[0] = pygame.transform.smoothscale(self.stand_right_imgs[0], self.stand_r_scale)
                self.stand_right_imgs[1] = pygame.transform.smoothscale(self.stand_right_imgs[1], self.stand_r_scale)
            elif self.run_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_d_scale = (60, 67)
                self.player_imgs_run_down()
                self.run_down_imgs[0] = pygame.transform.smoothscale(self.run_down_imgs[0], self.run_d_scale)
                self.run_down_imgs[1] = pygame.transform.smoothscale(self.run_down_imgs[1], self.run_d_scale)
                self.run_down_imgs[2] = pygame.transform.smoothscale(self.run_down_imgs[2], self.run_d_scale)
                self.run_down_imgs[3] = pygame.transform.smoothscale(self.run_down_imgs[3], self.run_d_scale)
            elif self.run_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_u_scale = (60, 67)
                self.player_imgs_run_up()
                self.run_up_imgs[0] = pygame.transform.smoothscale(self.run_up_imgs[0], self.run_u_scale)
                self.run_up_imgs[1] = pygame.transform.smoothscale(self.run_up_imgs[1], self.run_u_scale)
                self.run_up_imgs[2] = pygame.transform.smoothscale(self.run_up_imgs[2], self.run_u_scale)
                self.run_up_imgs[3] = pygame.transform.smoothscale(self.run_up_imgs[3], self.run_u_scale)
            elif self.run_l:
                if self.char == "wal":
                    self.run_l_scale = (65, 67)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_l_scale = (60, 67)
                self.player_imgs_run_left()
                self.run_left_imgs[0] = pygame.transform.smoothscale(self.run_left_imgs[0], self.run_l_scale)
                self.run_left_imgs[1] = pygame.transform.smoothscale(self.run_left_imgs[1], self.run_l_scale)
                self.run_left_imgs[2] = pygame.transform.smoothscale(self.run_left_imgs[2], self.run_l_scale)
                self.run_left_imgs[3] = pygame.transform.smoothscale(self.run_left_imgs[3], self.run_l_scale)
            elif self.run_r:
                if self.char == "wal":
                    self.run_r_scale = (65, 67)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_r_scale = (60, 67)
                self.player_imgs_run_right()
                self.run_right_imgs[0] = pygame.transform.smoothscale(self.run_right_imgs[0], self.run_r_scale)
                self.run_right_imgs[1] = pygame.transform.smoothscale(self.run_right_imgs[1], self.run_r_scale)
                self.run_right_imgs[2] = pygame.transform.smoothscale(self.run_right_imgs[2], self.run_r_scale)
                self.run_right_imgs[3] = pygame.transform.smoothscale(self.run_right_imgs[3], self.run_r_scale)
            elif self.fall_l:
                if self.char == "wal":
                    self.fall_l_scale = (44,67)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.fall_l_scale = (60, 67)
                self.player_imgs_fall_left()
                self.fall_left_imgs[0] = pygame.transform.smoothscale(self.fall_left_imgs[0], self.fall_l_scale)
                self.fall_left_imgs[1] = pygame.transform.smoothscale(self.fall_left_imgs[1], self.fall_l_scale)
                self.splash_scale = (83, 92)
                self.splash_img = pygame.transform.smoothscale(self.splash_img, self.splash_scale)
            elif self.hitted:
                if self.char == "wal":
                    self.hit_scale = (34, 67)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.hit_scale = (60, 67)
                self.player_imgs_hit()
                self.hit_img = pygame.transform.smoothscale(self.hit_img, self.hit_scale)
        elif self.rect.bottom <= 200:
            if self.fall_l != True:
                self.shadow_scale = (61, 18)
                self.player_imgs_shadow()
                self.shadow_img = pygame.transform.smoothscale(self.shadow_img, self.shadow_scale)
            if self.stand_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_d_scale = (61, 68)
                self.player_imgs_stand_down()
                self.stand_down_imgs[0] = pygame.transform.smoothscale(self.stand_down_imgs[0], self.stand_d_scale)
                self.stand_down_imgs[1] = pygame.transform.smoothscale(self.stand_down_imgs[1], self.stand_d_scale)
            elif self.stand_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_u_scale = (61, 68)
                self.player_imgs_stand_up()
                self.stand_up_imgs[0] = pygame.transform.smoothscale(self.stand_up_imgs[0], self.stand_u_scale)
                self.stand_up_imgs[1] = pygame.transform.smoothscale(self.stand_up_imgs[1], self.stand_u_scale)
            elif self.stand_l:
                if self.char == "wal":
                    self.stand_l_scale = (27, 68)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_l_scale = (61, 68)
                self.player_imgs_stand_left()
                self.stand_left_imgs[0] = pygame.transform.smoothscale(self.stand_left_imgs[0], self.stand_l_scale)
                self.stand_left_imgs[1] = pygame.transform.smoothscale(self.stand_left_imgs[1], self.stand_l_scale)
            elif self.stand_r:
                if self.char == "wal":
                    self.stand_r_scale = (27, 68)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_r_scale = (61, 68)
                self.player_imgs_stand_right()
                self.stand_right_imgs[0] = pygame.transform.smoothscale(self.stand_right_imgs[0], self.stand_r_scale)
                self.stand_right_imgs[1] = pygame.transform.smoothscale(self.stand_right_imgs[1], self.stand_r_scale)
            elif self.run_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_d_scale = (61, 68)
                self.player_imgs_run_down()
                self.run_down_imgs[0] = pygame.transform.smoothscale(self.run_down_imgs[0], self.run_d_scale)
                self.run_down_imgs[1] = pygame.transform.smoothscale(self.run_down_imgs[1], self.run_d_scale)
                self.run_down_imgs[2] = pygame.transform.smoothscale(self.run_down_imgs[2], self.run_d_scale)
                self.run_down_imgs[3] = pygame.transform.smoothscale(self.run_down_imgs[3], self.run_d_scale)
            elif self.run_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_u_scale = (61, 68)
                self.player_imgs_run_up()
                self.run_up_imgs[0] = pygame.transform.smoothscale(self.run_up_imgs[0], self.run_u_scale)
                self.run_up_imgs[1] = pygame.transform.smoothscale(self.run_up_imgs[1], self.run_u_scale)
                self.run_up_imgs[2] = pygame.transform.smoothscale(self.run_up_imgs[2], self.run_u_scale)
                self.run_up_imgs[3] = pygame.transform.smoothscale(self.run_up_imgs[3], self.run_u_scale)
            elif self.run_l:
                if self.char == "wal":
                    self.run_l_scale = (66, 68)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_l_scale = (61, 68)
                self.player_imgs_run_left()
                self.run_left_imgs[0] = pygame.transform.smoothscale(self.run_left_imgs[0], self.run_l_scale)
                self.run_left_imgs[1] = pygame.transform.smoothscale(self.run_left_imgs[1], self.run_l_scale)
                self.run_left_imgs[2] = pygame.transform.smoothscale(self.run_left_imgs[2], self.run_l_scale)
                self.run_left_imgs[3] = pygame.transform.smoothscale(self.run_left_imgs[3], self.run_l_scale)
            elif self.run_r:
                if self.char == "wal":
                    self.run_r_scale = (66, 68)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_r_scale = (61, 68)
                self.player_imgs_run_right()
                self.run_right_imgs[0] = pygame.transform.smoothscale(self.run_right_imgs[0], self.run_r_scale)
                self.run_right_imgs[1] = pygame.transform.smoothscale(self.run_right_imgs[1], self.run_r_scale)
                self.run_right_imgs[2] = pygame.transform.smoothscale(self.run_right_imgs[2], self.run_r_scale)
                self.run_right_imgs[3] = pygame.transform.smoothscale(self.run_right_imgs[3], self.run_r_scale)
            elif self.fall_l:
                if self.char == "wal":
                    self.fall_l_scale = (45,68)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.fall_l_scale = (61, 68)
                self.player_imgs_fall_left()
                self.fall_left_imgs[0] = pygame.transform.smoothscale(self.fall_left_imgs[0], self.fall_l_scale)
                self.fall_left_imgs[1] = pygame.transform.smoothscale(self.fall_left_imgs[1], self.fall_l_scale)
                self.splash_scale = (84, 93)
                self.player_imgs_splash()
                self.splash_img = pygame.transform.smoothscale(self.splash_img, self.splash_scale)
            elif self.hitted:
                if self.char == "wal":
                    self.hit_scale = (35, 68)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.hit_scale = (61, 68)
                self.player_imgs_hit()
                self.hit_img = pygame.transform.smoothscale(self.hit_img, self.hit_scale)
        elif self.rect.bottom <= 238:
            if self.fall_l != True:
                self.shadow_scale = (62, 19)
                self.player_imgs_shadow()
                self.shadow_img = pygame.transform.smoothscale(self.shadow_img, self.shadow_scale)
            if self.stand_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_d_scale = (62, 69)
                self.player_imgs_stand_down()
                self.stand_down_imgs[0] = pygame.transform.smoothscale(self.stand_down_imgs[0], self.stand_d_scale)
                self.stand_down_imgs[1] = pygame.transform.smoothscale(self.stand_down_imgs[1], self.stand_d_scale)
            elif self.stand_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_u_scale = (62, 69)
                self.player_imgs_stand_up()
                self.stand_up_imgs[0] = pygame.transform.smoothscale(self.stand_up_imgs[0], self.stand_u_scale)
                self.stand_up_imgs[1] = pygame.transform.smoothscale(self.stand_up_imgs[1], self.stand_u_scale)
            elif self.stand_l:
                if self.char == "wal":
                    self.stand_l_scale = (28, 69)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_l_scale = (62, 69)
                self.player_imgs_stand_left()
                self.stand_left_imgs[0] = pygame.transform.smoothscale(self.stand_left_imgs[0], self.stand_l_scale)
                self.stand_left_imgs[1] = pygame.transform.smoothscale(self.stand_left_imgs[1], self.stand_l_scale)
            elif self.stand_r:
                if self.char == "wal":
                    self.stand_r_scale = (28, 69)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_r_scale = (62, 69)
                self.player_imgs_stand_right()
                self.stand_right_imgs[0] = pygame.transform.smoothscale(self.stand_right_imgs[0], self.stand_r_scale)
                self.stand_right_imgs[1] = pygame.transform.smoothscale(self.stand_right_imgs[1], self.stand_r_scale)
            elif self.run_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_d_scale = (62, 69)
                self.player_imgs_run_down()
                self.run_down_imgs[0] = pygame.transform.smoothscale(self.run_down_imgs[0], self.run_d_scale)
                self.run_down_imgs[1] = pygame.transform.smoothscale(self.run_down_imgs[1], self.run_d_scale)
                self.run_down_imgs[2] = pygame.transform.smoothscale(self.run_down_imgs[2], self.run_d_scale)
                self.run_down_imgs[3] = pygame.transform.smoothscale(self.run_down_imgs[3], self.run_d_scale)
            elif self.run_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_u_scale = (62, 69)
                self.player_imgs_run_up()
                self.run_up_imgs[0] = pygame.transform.smoothscale(self.run_up_imgs[0], self.run_u_scale)
                self.run_up_imgs[1] = pygame.transform.smoothscale(self.run_up_imgs[1], self.run_u_scale)
                self.run_up_imgs[2] = pygame.transform.smoothscale(self.run_up_imgs[2], self.run_u_scale)
                self.run_up_imgs[3] = pygame.transform.smoothscale(self.run_up_imgs[3], self.run_u_scale)
            elif self.run_l:
                if self.char == "wal":
                    self.run_l_scale = (67, 69)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_l_scale = (62, 69)
                self.player_imgs_run_left()
                self.run_left_imgs[0] = pygame.transform.smoothscale(self.run_left_imgs[0], self.run_l_scale)
                self.run_left_imgs[1] = pygame.transform.smoothscale(self.run_left_imgs[1], self.run_l_scale)
                self.run_left_imgs[2] = pygame.transform.smoothscale(self.run_left_imgs[2], self.run_l_scale)
                self.run_left_imgs[3] = pygame.transform.smoothscale(self.run_left_imgs[3], self.run_l_scale)
            elif self.run_r:
                if self.char == "wal":
                    self.run_r_scale = (67, 69)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_r_scale = (62, 69)
                self.player_imgs_run_right()
                self.run_right_imgs[0] = pygame.transform.smoothscale(self.run_right_imgs[0], self.run_r_scale)
                self.run_right_imgs[1] = pygame.transform.smoothscale(self.run_right_imgs[1], self.run_r_scale)
                self.run_right_imgs[2] = pygame.transform.smoothscale(self.run_right_imgs[2], self.run_r_scale)
                self.run_right_imgs[3] = pygame.transform.smoothscale(self.run_right_imgs[3], self.run_r_scale)
            elif self.fall_l:
                if self.char == "wal":
                    self.fall_l_scale = (46,69)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.fall_l_scale = (62, 69)
                self.player_imgs_fall_left()
                self.fall_left_imgs[0] = pygame.transform.smoothscale(self.fall_left_imgs[0], self.fall_l_scale)
                self.fall_left_imgs[1] = pygame.transform.smoothscale(self.fall_left_imgs[1], self.fall_l_scale)
                self.splash_scale = (85, 94)
                self.player_imgs_splash()
                self.splash_img = pygame.transform.smoothscale(self.splash_img, self.splash_scale)
            elif self.hitted:
                if self.char == "wal":
                    self.hit_scale = (36, 69)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.hit_scale = (62, 69)
                self.player_imgs_hit()
                self.hit_img = pygame.transform.smoothscale(self.hit_img, self.hit_scale)
        elif self.rect.bottom <= 278:
            if self.fall_l != True:
                self.shadow_scale = (63, 20)
                self.player_imgs_shadow()
                self.shadow_img = pygame.transform.smoothscale(self.shadow_img, self.shadow_scale)
            if self.stand_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_d_scale = (63, 70)
                self.player_imgs_stand_down()
                self.stand_down_imgs[0] = pygame.transform.smoothscale(self.stand_down_imgs[0], self.stand_d_scale)
                self.stand_down_imgs[1] = pygame.transform.smoothscale(self.stand_down_imgs[1], self.stand_d_scale)
            elif self.stand_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_u_scale = (63, 70)
                self.player_imgs_stand_up()
                self.stand_up_imgs[0] = pygame.transform.smoothscale(self.stand_up_imgs[0], self.stand_u_scale)
                self.stand_up_imgs[1] = pygame.transform.smoothscale(self.stand_up_imgs[1], self.stand_u_scale)
            elif self.stand_l:
                if self.char == "wal":
                    self.stand_l_scale = (29, 70)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_l_scale = (63, 70)
                self.player_imgs_stand_left()
                self.stand_left_imgs[0] = pygame.transform.smoothscale(self.stand_left_imgs[0], self.stand_l_scale)
                self.stand_left_imgs[1] = pygame.transform.smoothscale(self.stand_left_imgs[1], self.stand_l_scale)
            elif self.stand_r:
                if self.char == "wal":
                    self.stand_r_scale = (29, 70)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_r_scale = (63, 70)
                self.player_imgs_stand_right()
                self.stand_right_imgs[0] = pygame.transform.smoothscale(self.stand_right_imgs[0], self.stand_r_scale)
                self.stand_right_imgs[1] = pygame.transform.smoothscale(self.stand_right_imgs[1], self.stand_r_scale)
            elif self.run_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_d_scale = (63, 70)
                self.player_imgs_run_down()
                self.run_down_imgs[0] = pygame.transform.smoothscale(self.run_down_imgs[0], self.run_d_scale)
                self.run_down_imgs[1] = pygame.transform.smoothscale(self.run_down_imgs[1], self.run_d_scale)
                self.run_down_imgs[2] = pygame.transform.smoothscale(self.run_down_imgs[2], self.run_d_scale)
                self.run_down_imgs[3] = pygame.transform.smoothscale(self.run_down_imgs[3], self.run_d_scale)
            elif self.run_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_u_scale = (63, 70)
                self.player_imgs_run_up()
                self.run_up_imgs[0] = pygame.transform.smoothscale(self.run_up_imgs[0], self.run_u_scale)
                self.run_up_imgs[1] = pygame.transform.smoothscale(self.run_up_imgs[1], self.run_u_scale)
                self.run_up_imgs[2] = pygame.transform.smoothscale(self.run_up_imgs[2], self.run_u_scale)
                self.run_up_imgs[3] = pygame.transform.smoothscale(self.run_up_imgs[3], self.run_u_scale)
            elif self.run_l:
                if self.char == "wal":
                    self.run_l_scale = (68, 70)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_l_scale = (63, 70)
                self.player_imgs_run_left()
                self.run_left_imgs[0] = pygame.transform.smoothscale(self.run_left_imgs[0], self.run_l_scale)
                self.run_left_imgs[1] = pygame.transform.smoothscale(self.run_left_imgs[1], self.run_l_scale)
                self.run_left_imgs[2] = pygame.transform.smoothscale(self.run_left_imgs[2], self.run_l_scale)
                self.run_left_imgs[3] = pygame.transform.smoothscale(self.run_left_imgs[3], self.run_l_scale)
            elif self.run_r:
                if self.char == "wal":
                    self.run_r_scale = (68, 70)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_r_scale = (63, 70)
                self.player_imgs_run_right()
                self.run_right_imgs[0] = pygame.transform.smoothscale(self.run_right_imgs[0], self.run_r_scale)
                self.run_right_imgs[1] = pygame.transform.smoothscale(self.run_right_imgs[1], self.run_r_scale)
                self.run_right_imgs[2] = pygame.transform.smoothscale(self.run_right_imgs[2], self.run_r_scale)
                self.run_right_imgs[3] = pygame.transform.smoothscale(self.run_right_imgs[3], self.run_r_scale)
            elif self.fall_l:
                if self.char == "wal":
                    self.fall_l_scale = (47,70)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.fall_l_scale = (63, 70)
                self.player_imgs_fall_left()
                self.fall_left_imgs[0] = pygame.transform.smoothscale(self.fall_left_imgs[0], self.fall_l_scale)
                self.fall_left_imgs[1] = pygame.transform.smoothscale(self.fall_left_imgs[1], self.fall_l_scale)
                self.splash_scale = (86, 95)
                self.player_imgs_splash()
                self.splash_img = pygame.transform.smoothscale(self.splash_img, self.splash_scale)
            elif self.hitted:
                if self.char == "wal":
                    self.hit_scale = (37, 70)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.hit_scale = (63, 70)
                self.player_imgs_hit()
                self.hit_img = pygame.transform.smoothscale(self.hit_img, self.hit_scale)
        elif self.rect.bottom <= 320:
            if self.fall_l != True:
                self.shadow_scale = (64, 21)
                self.player_imgs_shadow()
                self.shadow_img = pygame.transform.smoothscale(self.shadow_img, self.shadow_scale)
            if self.stand_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_d_scale = (64, 71)
                self.player_imgs_stand_down()
                self.stand_down_imgs[0] = pygame.transform.smoothscale(self.stand_down_imgs[0], self.stand_d_scale)
                self.stand_down_imgs[1] = pygame.transform.smoothscale(self.stand_down_imgs[1], self.stand_d_scale)
            elif self.stand_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_u_scale = (64, 71)
                self.player_imgs_stand_up()
                self.stand_up_imgs[0] = pygame.transform.smoothscale(self.stand_up_imgs[0], self.stand_u_scale)
                self.stand_up_imgs[1] = pygame.transform.smoothscale(self.stand_up_imgs[1], self.stand_u_scale)
            elif self.stand_l:
                if self.char == "wal":
                    self.stand_l_scale = (30, 71)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_l_scale = (64, 71)
                self.player_imgs_stand_left()
                self.stand_left_imgs[0] = pygame.transform.smoothscale(self.stand_left_imgs[0], self.stand_l_scale)
                self.stand_left_imgs[1] = pygame.transform.smoothscale(self.stand_left_imgs[1], self.stand_l_scale)
            elif self.stand_r:
                if self.char == "wal":
                    self.stand_r_scale = (30, 71)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_r_scale = (64, 71)
                self.player_imgs_stand_right()
                self.stand_right_imgs[0] = pygame.transform.smoothscale(self.stand_right_imgs[0], self.stand_r_scale)
                self.stand_right_imgs[1] = pygame.transform.smoothscale(self.stand_right_imgs[1], self.stand_r_scale)
            elif self.run_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_d_scale = (64, 71)
                self.player_imgs_run_down()
                self.run_down_imgs[0] = pygame.transform.smoothscale(self.run_down_imgs[0], self.run_d_scale)
                self.run_down_imgs[1] = pygame.transform.smoothscale(self.run_down_imgs[1], self.run_d_scale)
                self.run_down_imgs[2] = pygame.transform.smoothscale(self.run_down_imgs[2], self.run_d_scale)
                self.run_down_imgs[3] = pygame.transform.smoothscale(self.run_down_imgs[3], self.run_d_scale)
            elif self.run_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_u_scale = (64, 71)
                self.player_imgs_run_up()
                self.run_up_imgs[0] = pygame.transform.smoothscale(self.run_up_imgs[0], self.run_u_scale)
                self.run_up_imgs[1] = pygame.transform.smoothscale(self.run_up_imgs[1], self.run_u_scale)
                self.run_up_imgs[2] = pygame.transform.smoothscale(self.run_up_imgs[2], self.run_u_scale)
                self.run_up_imgs[3] = pygame.transform.smoothscale(self.run_up_imgs[3], self.run_u_scale)
            elif self.run_l:
                if self.char == "wal":
                    self.run_l_scale = (69, 71)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_l_scale = (64, 71)
                self.player_imgs_run_left()
                self.run_left_imgs[0] = pygame.transform.smoothscale(self.run_left_imgs[0], self.run_l_scale)
                self.run_left_imgs[1] = pygame.transform.smoothscale(self.run_left_imgs[1], self.run_l_scale)
                self.run_left_imgs[2] = pygame.transform.smoothscale(self.run_left_imgs[2], self.run_l_scale)
                self.run_left_imgs[3] = pygame.transform.smoothscale(self.run_left_imgs[3], self.run_l_scale)
            elif self.run_r:
                if self.char == "wal":
                    self.run_r_scale = (69, 71)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_r_scale = (64, 71)
                self.player_imgs_run_right()
                self.run_right_imgs[0] = pygame.transform.smoothscale(self.run_right_imgs[0], self.run_r_scale)
                self.run_right_imgs[1] = pygame.transform.smoothscale(self.run_right_imgs[1], self.run_r_scale)
                self.run_right_imgs[2] = pygame.transform.smoothscale(self.run_right_imgs[2], self.run_r_scale)
                self.run_right_imgs[3] = pygame.transform.smoothscale(self.run_right_imgs[3], self.run_r_scale)
            elif self.fall_l:
                if self.char == "wal":
                    self.fall_l_scale = (48,71)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.fall_l_scale = (64, 71)
                self.player_imgs_fall_left()
                self.fall_left_imgs[0] = pygame.transform.smoothscale(self.fall_left_imgs[0], self.fall_l_scale)
                self.fall_left_imgs[1] = pygame.transform.smoothscale(self.fall_left_imgs[1], self.fall_l_scale)
                self.splash_scale = (87, 96)
                self.player_imgs_splash()
                self.splash_img = pygame.transform.smoothscale(self.splash_img, self.splash_scale)
            elif self.hitted:
                if self.char == "wal":
                    self.hit_scale = (38, 71)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.hit_scale = (64, 71)
                self.player_imgs_hit()
                self.hit_img = pygame.transform.smoothscale(self.hit_img, self.hit_scale)
        elif self.rect.bottom <= 364:
            if self.fall_l != True:
                self.shadow_scale = (65, 22)
                self.player_imgs_shadow()
                self.shadow_img = pygame.transform.smoothscale(self.shadow_img, self.shadow_scale)
            if self.stand_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_d_scale = (65, 72)
                self.player_imgs_stand_down()
                self.stand_down_imgs[0] = pygame.transform.smoothscale(self.stand_down_imgs[0], self.stand_d_scale)
                self.stand_down_imgs[1] = pygame.transform.smoothscale(self.stand_down_imgs[1], self.stand_d_scale)
            elif self.stand_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_u_scale = (65, 72)
                self.player_imgs_stand_up()
                self.stand_up_imgs[0] = pygame.transform.smoothscale(self.stand_up_imgs[0], self.stand_u_scale)
                self.stand_up_imgs[1] = pygame.transform.smoothscale(self.stand_up_imgs[1], self.stand_u_scale)
            elif self.stand_l:
                if self.char == "wal":
                    self.stand_l_scale = (31, 72)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_l_scale = (65, 72)
                self.player_imgs_stand_left()
                self.stand_left_imgs[0] = pygame.transform.smoothscale(self.stand_left_imgs[0], self.stand_l_scale)
                self.stand_left_imgs[1] = pygame.transform.smoothscale(self.stand_left_imgs[1], self.stand_l_scale)
            elif self.stand_r:
                if self.char == "wal":
                    self.stand_r_scale = (31, 72)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_r_scale = (65, 72)
                self.player_imgs_stand_right()
                self.stand_right_imgs[0] = pygame.transform.smoothscale(self.stand_right_imgs[0], self.stand_r_scale)
                self.stand_right_imgs[1] = pygame.transform.smoothscale(self.stand_right_imgs[1], self.stand_r_scale)
            elif self.run_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_d_scale = (65, 72)
                self.player_imgs_run_down()
                self.run_down_imgs[0] = pygame.transform.smoothscale(self.run_down_imgs[0], self.run_d_scale)
                self.run_down_imgs[1] = pygame.transform.smoothscale(self.run_down_imgs[1], self.run_d_scale)
                self.run_down_imgs[2] = pygame.transform.smoothscale(self.run_down_imgs[2], self.run_d_scale)
                self.run_down_imgs[3] = pygame.transform.smoothscale(self.run_down_imgs[3], self.run_d_scale)
            elif self.run_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_u_scale = (65, 72)
                self.player_imgs_run_up()
                self.run_up_imgs[0] = pygame.transform.smoothscale(self.run_up_imgs[0], self.run_u_scale)
                self.run_up_imgs[1] = pygame.transform.smoothscale(self.run_up_imgs[1], self.run_u_scale)
                self.run_up_imgs[2] = pygame.transform.smoothscale(self.run_up_imgs[2], self.run_u_scale)
                self.run_up_imgs[3] = pygame.transform.smoothscale(self.run_up_imgs[3], self.run_u_scale)
            elif self.run_l:
                if self.char == "wal":
                    self.run_l_scale = (70, 72)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_l_scale = (65, 72)
                self.player_imgs_run_left()
                self.run_left_imgs[0] = pygame.transform.smoothscale(self.run_left_imgs[0], self.run_l_scale)
                self.run_left_imgs[1] = pygame.transform.smoothscale(self.run_left_imgs[1], self.run_l_scale)
                self.run_left_imgs[2] = pygame.transform.smoothscale(self.run_left_imgs[2], self.run_l_scale)
                self.run_left_imgs[3] = pygame.transform.smoothscale(self.run_left_imgs[3], self.run_l_scale)
            elif self.run_r:
                if self.char == "wal":
                    self.run_r_scale = (70, 72)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_r_scale = (65, 72)
                self.player_imgs_run_right()
                self.run_right_imgs[0] = pygame.transform.smoothscale(self.run_right_imgs[0], self.run_r_scale)
                self.run_right_imgs[1] = pygame.transform.smoothscale(self.run_right_imgs[1], self.run_r_scale)
                self.run_right_imgs[2] = pygame.transform.smoothscale(self.run_right_imgs[2], self.run_r_scale)
                self.run_right_imgs[3] = pygame.transform.smoothscale(self.run_right_imgs[3], self.run_r_scale)
            elif self.fall_l:
                if self.char == "wal":
                    self.fall_l_scale = (49,72)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.fall_l_scale = (65, 72)
                self.player_imgs_fall_left()
                self.fall_left_imgs[0] = pygame.transform.smoothscale(self.fall_left_imgs[0], self.fall_l_scale)
                self.fall_left_imgs[1] = pygame.transform.smoothscale(self.fall_left_imgs[1], self.fall_l_scale)
                self.splash_scale = (88, 97)
                self.player_imgs_splash()
                self.splash_img = pygame.transform.smoothscale(self.splash_img, self.splash_scale)
            elif self.hitted:
                if self.char == "wal":
                    self.hit_scale = (39, 72)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.hit_scale = (65, 72)
                self.player_imgs_hit()
                self.hit_img = pygame.transform.smoothscale(self.hit_img, self.hit_scale)
        elif self.rect.bottom <= 410:
            if self.fall_l != True:
                self.shadow_scale = (66, 23)
                self.player_imgs_shadow()
                self.shadow_img = pygame.transform.smoothscale(self.shadow_img, self.shadow_scale)
            if self.stand_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_d_scale = (66, 73)
                self.player_imgs_stand_down()
                self.stand_down_imgs[0] = pygame.transform.smoothscale(self.stand_down_imgs[0], self.stand_d_scale)
                self.stand_down_imgs[1] = pygame.transform.smoothscale(self.stand_down_imgs[1], self.stand_d_scale)
            elif self.stand_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_u_scale = (66, 73)
                self.player_imgs_stand_up()
                self.stand_up_imgs[0] = pygame.transform.smoothscale(self.stand_up_imgs[0], self.stand_u_scale)
                self.stand_up_imgs[1] = pygame.transform.smoothscale(self.stand_up_imgs[1], self.stand_u_scale)
            elif self.stand_l:
                if self.char == "wal":
                    self.stand_l_scale = (32, 73)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_l_scale = (66, 73)
                self.player_imgs_stand_left()
                self.stand_left_imgs[0] = pygame.transform.smoothscale(self.stand_left_imgs[0], self.stand_l_scale)
                self.stand_left_imgs[1] = pygame.transform.smoothscale(self.stand_left_imgs[1], self.stand_l_scale)
            elif self.stand_r:
                if self.char == "wal":
                    self.stand_r_scale = (32, 73)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_r_scale = (66, 73)
                self.player_imgs_stand_right()
                self.stand_right_imgs[0] = pygame.transform.smoothscale(self.stand_right_imgs[0], self.stand_r_scale)
                self.stand_right_imgs[1] = pygame.transform.smoothscale(self.stand_right_imgs[1], self.stand_r_scale)
            elif self.run_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_d_scale = (66, 73)
                self.player_imgs_run_down()
                self.run_down_imgs[0] = pygame.transform.smoothscale(self.run_down_imgs[0], self.run_d_scale)
                self.run_down_imgs[1] = pygame.transform.smoothscale(self.run_down_imgs[1], self.run_d_scale)
                self.run_down_imgs[2] = pygame.transform.smoothscale(self.run_down_imgs[2], self.run_d_scale)
                self.run_down_imgs[3] = pygame.transform.smoothscale(self.run_down_imgs[3], self.run_d_scale)
            elif self.run_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_u_scale = (66, 73)
                self.player_imgs_run_up()
                self.run_up_imgs[0] = pygame.transform.smoothscale(self.run_up_imgs[0], self.run_u_scale)
                self.run_up_imgs[1] = pygame.transform.smoothscale(self.run_up_imgs[1], self.run_u_scale)
                self.run_up_imgs[2] = pygame.transform.smoothscale(self.run_up_imgs[2], self.run_u_scale)
                self.run_up_imgs[3] = pygame.transform.smoothscale(self.run_up_imgs[3], self.run_u_scale)
            elif self.run_l:
                if self.char == "wal":
                    self.run_l_scale = (71, 73)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_l_scale = (66, 73)
                self.player_imgs_run_left()
                self.run_left_imgs[0] = pygame.transform.smoothscale(self.run_left_imgs[0], self.run_l_scale)
                self.run_left_imgs[1] = pygame.transform.smoothscale(self.run_left_imgs[1], self.run_l_scale)
                self.run_left_imgs[2] = pygame.transform.smoothscale(self.run_left_imgs[2], self.run_l_scale)
                self.run_left_imgs[3] = pygame.transform.smoothscale(self.run_left_imgs[3], self.run_l_scale)
            elif self.run_r:
                if self.char == "wal":
                    self.run_r_scale = (71, 73)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_r_scale = (66, 73)
                self.player_imgs_run_right()
                self.run_right_imgs[0] = pygame.transform.smoothscale(self.run_right_imgs[0], self.run_r_scale)
                self.run_right_imgs[1] = pygame.transform.smoothscale(self.run_right_imgs[1], self.run_r_scale)
                self.run_right_imgs[2] = pygame.transform.smoothscale(self.run_right_imgs[2], self.run_r_scale)
                self.run_right_imgs[3] = pygame.transform.smoothscale(self.run_right_imgs[3], self.run_r_scale)
            elif self.fall_l:
                if self.char == "wal":
                    self.fall_l_scale = (50,73)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.fall_l_scale = (66, 73)
                self.player_imgs_fall_left()
                self.fall_left_imgs[0] = pygame.transform.smoothscale(self.fall_left_imgs[0], self.fall_l_scale)
                self.fall_left_imgs[1] = pygame.transform.smoothscale(self.fall_left_imgs[1], self.fall_l_scale)
                self.splash_scale = (89, 98)
                self.player_imgs_splash()
                self.splash_img = pygame.transform.smoothscale(self.splash_img, self.splash_scale)
            elif self.hitted:
                if self.char == "wal":
                    self.hit_scale = (40, 73)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.hit_scale = (66, 73)
                self.player_imgs_hit()
                self.hit_img = pygame.transform.smoothscale(self.hit_img, self.hit_scale)
        elif self.rect.bottom <= 458:
            if self.fall_l != True:
                self.shadow_scale = (67, 24)
                self.player_imgs_shadow()
                self.shadow_img = pygame.transform.smoothscale(self.shadow_img, self.shadow_scale)
            if self.stand_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_d_scale = (67, 74)
                self.player_imgs_stand_down()
                self.stand_down_imgs[0] = pygame.transform.smoothscale(self.stand_down_imgs[0], self.stand_d_scale)
                self.stand_down_imgs[1] = pygame.transform.smoothscale(self.stand_down_imgs[1], self.stand_d_scale)
            elif self.stand_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_u_scale = (67, 74)
                self.player_imgs_stand_up()
                self.stand_up_imgs[0] = pygame.transform.smoothscale(self.stand_up_imgs[0], self.stand_u_scale)
                self.stand_up_imgs[1] = pygame.transform.smoothscale(self.stand_up_imgs[1], self.stand_u_scale)
            elif self.stand_l:
                if self.char == "wal":
                    self.stand_l_scale = (33, 74)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_l_scale = (67, 74)
                self.player_imgs_stand_left()
                self.stand_left_imgs[0] = pygame.transform.smoothscale(self.stand_left_imgs[0], self.stand_l_scale)
                self.stand_left_imgs[1] = pygame.transform.smoothscale(self.stand_left_imgs[1], self.stand_l_scale)
            elif self.stand_r:
                if self.char == "wal":
                    self.stand_r_scale = (33, 74)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.stand_r_scale = (67, 74)
                self.player_imgs_stand_right()
                self.stand_right_imgs[0] = pygame.transform.smoothscale(self.stand_right_imgs[0], self.stand_r_scale)
                self.stand_right_imgs[1] = pygame.transform.smoothscale(self.stand_right_imgs[1], self.stand_r_scale)
            elif self.run_d:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_d_scale = (67, 74)
                self.player_imgs_run_down()
                self.run_down_imgs[0] = pygame.transform.smoothscale(self.run_down_imgs[0], self.run_d_scale)
                self.run_down_imgs[1] = pygame.transform.smoothscale(self.run_down_imgs[1], self.run_d_scale)
                self.run_down_imgs[2] = pygame.transform.smoothscale(self.run_down_imgs[2], self.run_d_scale)
                self.run_down_imgs[3] = pygame.transform.smoothscale(self.run_down_imgs[3], self.run_d_scale)
            elif self.run_u:
                if self.char == "wal" or self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_u_scale = (67, 74)
                self.player_imgs_run_up()
                self.run_up_imgs[0] = pygame.transform.smoothscale(self.run_up_imgs[0], self.run_u_scale)
                self.run_up_imgs[1] = pygame.transform.smoothscale(self.run_up_imgs[1], self.run_u_scale)
                self.run_up_imgs[2] = pygame.transform.smoothscale(self.run_up_imgs[2], self.run_u_scale)
                self.run_up_imgs[3] = pygame.transform.smoothscale(self.run_up_imgs[3], self.run_u_scale)
            elif self.run_l:
                if self.char == "wal":
                    self.run_l_scale = (72, 74)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_l_scale = (67, 74)
                self.player_imgs_run_left()
                self.run_left_imgs[0] = pygame.transform.smoothscale(self.run_left_imgs[0], self.run_l_scale)
                self.run_left_imgs[1] = pygame.transform.smoothscale(self.run_left_imgs[1], self.run_l_scale)
                self.run_left_imgs[2] = pygame.transform.smoothscale(self.run_left_imgs[2], self.run_l_scale)
                self.run_left_imgs[3] = pygame.transform.smoothscale(self.run_left_imgs[3], self.run_l_scale)
            elif self.run_r:
                if self.char == "wal":
                    self.run_r_scale = (72, 74)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.run_r_scale = (67, 74)
                self.player_imgs_run_right()
                self.run_right_imgs[0] = pygame.transform.smoothscale(self.run_right_imgs[0], self.run_r_scale)
                self.run_right_imgs[1] = pygame.transform.smoothscale(self.run_right_imgs[1], self.run_r_scale)
                self.run_right_imgs[2] = pygame.transform.smoothscale(self.run_right_imgs[2], self.run_r_scale)
                self.run_right_imgs[3] = pygame.transform.smoothscale(self.run_right_imgs[3], self.run_r_scale)
            elif self.fall_l:
                if self.char == "wal":
                    self.fall_l_scale = (51,74)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.fall_l_scale = (67, 74)
                self.player_imgs_fall_left()
                self.fall_left_imgs[0] = pygame.transform.smoothscale(self.fall_left_imgs[0], self.fall_l_scale)
                self.fall_left_imgs[1] = pygame.transform.smoothscale(self.fall_left_imgs[1], self.fall_l_scale)
                self.splash_scale = (90, 99)
                self.player_imgs_splash()
                self.splash_img = pygame.transform.smoothscale(self.splash_img, self.splash_scale)
            elif self.hitted:
                if self.char == "wal":
                    self.hit_scale = (41, 74)
                elif self.char == "yos" or self.char == "pea" or self.char == "mar":
                    self.hit_scale = (67, 74)
                self.player_imgs_hit()
                self.hit_img = pygame.transform.smoothscale(self.hit_img, self.hit_scale)

        elif self.rect.bottom > 458:
            if self.stand_d:
                self.player_imgs_stand_down()
                self.player_imgs_shadow()
            elif self.stand_u:
                self.player_imgs_stand_up()
                self.player_imgs_shadow()
            elif self.stand_l:
                self.player_imgs_stand_left()
                self.player_imgs_shadow()
            elif self.stand_r:
                self.player_imgs_stand_right()
                self.player_imgs_shadow()
            elif self.run_d:
                self.player_imgs_run_down()
                self.player_imgs_shadow()
            elif self.run_u:
                self.player_imgs_run_up()
                self.player_imgs_shadow()
            elif self.run_l:
                self.player_imgs_run_left()
                self.player_imgs_shadow()
            elif self.run_r:
                self.player_imgs_run_right()
                self.player_imgs_shadow()
            elif self.fall_d:
                self.player_imgs_fall_down()
                self.player_imgs_splash()
            elif self.fall_l:
                self.player_imgs_fall_left()
                self.player_imgs_splash()
            elif self.hitted:
                self.player_imgs_hit()
                self.player_imgs_shadow()

    def player_rects(self):
        """player rect depends on sprite currently used"""
        if self.stand_d:
            if self.char == "wal":
                self.rect = pygame.Rect(round(self.x + (self.stand_d_scale[0] / 5.5)), self.y+(round(self.stand_d_scale[1]/1.5)), round(self.stand_d_scale[0] / 1.5), round(self.stand_d_scale[1]/3))
            elif self.char == "yos":
                self.rect = pygame.Rect(round(self.x + (self.stand_d_scale[0] / 4)), self.y + (round(self.stand_d_scale[1] / 1.5)), round(self.stand_d_scale[0] / 2), round(self.stand_d_scale[1] / 3))
            elif self.char == "pea":
                self.rect = pygame.Rect(round(self.x + (self.stand_d_scale[0] / 5)), self.y + (round(self.stand_d_scale[1] / 1.5)), round(self.stand_d_scale[0] / 1.8), round(self.stand_d_scale[1] / 3))
            elif self.char == "mar":
                self.rect = pygame.Rect(round(self.x + (self.stand_d_scale[0] / 4)), self.y + (round(self.stand_d_scale[1] / 1.4)), round(self.stand_d_scale[0] / 2.2), round(self.stand_d_scale[1] / 3))
        elif self.stand_u:
            if self.char == "wal":
                self.rect = pygame.Rect(round(self.x + (self.stand_u_scale[0] / 5.5)), self.y + (round(self.stand_u_scale[1] / 1.5)), round(self.stand_u_scale[0] / 1.5), round(self.stand_u_scale[1]/3))
            elif self.char == "yos":
                self.rect = pygame.Rect(round(self.x + (self.stand_u_scale[0] / 4)), self.y + (round(self.stand_u_scale[1] / 1.5)), round(self.stand_u_scale[0] / 2), round(self.stand_u_scale[1] / 3))
            elif self.char == "pea":
                self.rect = pygame.Rect(round(self.x + (self.stand_u_scale[0] / 5)), self.y + (round(self.stand_u_scale[1] / 1.5)), round(self.stand_u_scale[0] / 1.8), round(self.stand_u_scale[1] / 3))
            elif self.char == "mar":
                self.rect = pygame.Rect(round(self.x + (self.stand_u_scale[0] / 4)), self.y + (round(self.stand_u_scale[1] / 1.4)), round(self.stand_u_scale[0] / 2.2), round(self.stand_u_scale[1] / 3))
        elif self.stand_l:
            if self.char == "wal":
                self.rect = pygame.Rect(self.x, self.y + (round(self.stand_l_scale[1] / 1.5)), self.stand_l_scale[0], round(self.stand_l_scale[1]/3))
            elif self.char == "yos":
                self.rect = pygame.Rect(round(self.x + (self.stand_l_scale[0] / 4)), self.y + (round(self.stand_l_scale[1] / 1.5)), round(self.stand_l_scale[0] / 2), round(self.stand_l_scale[1] / 3))
            elif self.char == "pea":
                self.rect = pygame.Rect(round(self.x + (self.stand_l_scale[0] / 5)), self.y + (round(self.stand_l_scale[1] / 1.5)), round(self.stand_l_scale[0] / 1.8), round(self.stand_l_scale[1] / 3))
            elif self.char == "mar":
                self.rect = pygame.Rect(round(self.x + (self.stand_l_scale[0] / 3)), self.y + (round(self.stand_l_scale[1] / 1.4)), round(self.stand_l_scale[0] / 2.5), round(self.stand_l_scale[1] / 3))
        elif self.stand_r:
            if self.char == "wal":
                self.rect = pygame.Rect(self.x, self.y + (round(self.stand_r_scale[1] / 1.5)), self.stand_r_scale[0], round(self.stand_r_scale[1]/3))
            elif self.char == "yos":
                self.rect = pygame.Rect(round(self.x + (self.stand_r_scale[0] / 4)), self.y + (round(self.stand_r_scale[1] / 1.5)), round(self.stand_r_scale[0] / 2), round(self.stand_r_scale[1] / 3))
            elif self.char == "pea":
                self.rect = pygame.Rect(round(self.x + (self.stand_r_scale[0] / 5)), self.y + (round(self.stand_r_scale[1] / 1.5)), round(self.stand_r_scale[0] / 1.8), round(self.stand_r_scale[1] / 3))
            elif self.char == "mar":
                self.rect = pygame.Rect(round(self.x + (self.stand_r_scale[0] / 4)), self.y + (round(self.stand_r_scale[1] / 1.4)), round(self.stand_r_scale[0] / 2.5), round(self.stand_r_scale[1] / 3))
        elif self.run_d:
            if self.char == "wal":
                self.rect = pygame.Rect(round(self.x + (self.run_d_scale[0] / 5.5)), self.y + (round(self.run_d_scale[1] / 1.5)), round(self.run_d_scale[0] / 1.5), round(self.run_d_scale[1]/3))
            elif self.char == "yos":
                self.rect = pygame.Rect(round(self.x + (self.run_d_scale[0] / 4)), self.y + (round(self.run_d_scale[1] / 1.5)), round(self.run_d_scale[0] / 2), round(self.run_d_scale[1] / 3))
            elif self.char == "pea":
                self.rect = pygame.Rect(round(self.x + (self.run_d_scale[0] / 5)), self.y + (round(self.run_d_scale[1] / 1.5)), round(self.run_d_scale[0] / 1.8), round(self.run_d_scale[1] / 3))
            elif self.char == "mar":
                self.rect = pygame.Rect(round(self.x + (self.run_d_scale[0] / 4)), self.y + (round(self.run_d_scale[1] / 1.4)), round(self.run_d_scale[0] / 2.2), round(self.run_d_scale[1] / 3))
        elif self.run_u:
            if self.char == "wal":
                self.rect = pygame.Rect(round(self.x + (self.run_u_scale[0] / 5.5)), self.y + (round(self.run_u_scale[1] / 1.5)), round(self.run_u_scale[0] / 1.5), round(self.run_u_scale[1]/3))
            elif self.char == "yos":
                self.rect = pygame.Rect(round(self.x + (self.run_u_scale[0] / 4)), self.y + (round(self.run_u_scale[1] / 1.5)), round(self.run_u_scale[0] / 2), round(self.run_u_scale[1] / 3))
            elif self.char == "pea":
                self.rect = pygame.Rect(round(self.x + (self.run_u_scale[0] / 5)), self.y + (round(self.run_u_scale[1] / 1.5)), round(self.run_u_scale[0] / 1.8), round(self.run_u_scale[1] / 3))
            elif self.char == "mar":
                self.rect = pygame.Rect(round(self.x + (self.run_u_scale[0] / 4)), self.y + (round(self.run_u_scale[1] / 1.4)), round(self.run_u_scale[0] / 2.2), round(self.run_u_scale[1] / 3))
        elif self.run_l:
            if self.char == "wal":
                self.rect = pygame.Rect(round(self.x + (self.run_l_scale[0] / 12)), self.y + (round(self.run_l_scale[1] / 1.5)), round(self.run_l_scale[0] / 1.2), round(self.run_l_scale[1] / 3))
            elif self.char == "yos":
                self.rect = pygame.Rect(round(self.x + (self.run_l_scale[0] / 4)), self.y + (round(self.run_l_scale[1] / 1.5)), round(self.run_l_scale[0] / 2), round(self.run_l_scale[1] / 3))
            elif self.char == "pea":
                self.rect = pygame.Rect(round(self.x + (self.run_l_scale[0] / 5)), self.y + (round(self.run_l_scale[1] / 1.5)), round(self.run_l_scale[0] / 1.8), round(self.run_l_scale[1] / 3))
            elif self.char == "mar":
                self.rect = pygame.Rect(round(self.x + (self.run_l_scale[0] / 4)), self.y + (round(self.run_l_scale[1] / 1.4)), round(self.run_l_scale[0] / 1.8), round(self.run_l_scale[1] / 3))
        elif self.run_r:
            if self.char == "wal":
                self.rect = pygame.Rect(round(self.x + (self.run_r_scale[0] / 12)), self.y + (round(self.run_r_scale[1] / 1.5)), round(self.run_r_scale[0] / 1.2), round(self.run_r_scale[1] / 3))
            elif self.char == "yos":
                self.rect = pygame.Rect(round(self.x + (self.run_r_scale[0] / 4)), self.y + (round(self.run_r_scale[1] / 1.5)), round(self.run_r_scale[0] / 2), round(self.run_r_scale[1] / 3))
            elif self.char == "pea":
                self.rect = pygame.Rect(round(self.x + (self.run_r_scale[0] / 5)), self.y + (round(self.run_r_scale[1] / 1.5)), round(self.run_r_scale[0] / 1.8), round(self.run_r_scale[1] / 3))
            elif self.char == "mar":
                self.rect = pygame.Rect(round(self.x + (self.run_r_scale[0] / 5)), self.y + (round(self.run_r_scale[1] / 1.4)), round(self.run_r_scale[0] / 1.8), round(self.run_r_scale[1] / 3))
        elif self.fall_d:
            self.rect = self.fall_down_imgs[0].get_rect(topleft=(self.x, self.y))
        elif self.fall_u:
            self.rect = self.fall_up_imgs[0].get_rect(topleft=(self.x, self.y))
        elif self.fall_l:
            self.rect = self.fall_left_imgs[0].get_rect(topleft=(self.x, self.y))
        elif self.hitted:
            if self.char == "wal":
                self.rect = pygame.Rect(round(self.x + (self.hit_scale[0] / 12)), self.y + (round(self.hit_scale[1] / 1.5)), round(self.hit_scale[0] / 1.2), round(self.hit_scale[1] / 3))
            elif self.char == "yos":
                self.rect = pygame.Rect(round(self.x + (self.hit_scale[0] / 4)), self.y + (round(self.hit_scale[1] / 1.5)), round(self.hit_scale[0] / 2), round(self.hit_scale[1] / 3))
            elif self.char == "pea":
                self.rect = pygame.Rect(round(self.x + (self.hit_scale[0] / 5)), self.y + (round(self.hit_scale[1] / 1.5)), round(self.hit_scale[0] / 1.8), round(self.hit_scale[1] / 3))
            elif self.char == "mar":
                self.rect = pygame.Rect(round(self.x + (self.hit_scale[0] / 5)), self.y + (round(self.hit_scale[1] / 1.4)), round(self.hit_scale[0] / 1.8), round(self.hit_scale[1] / 3))

    def create_frame_counter(self):
        self.stand_frame_counter = 0
        self.run_frame_counter = 0
        self.stand_frame_change = 0.1
        self.run_frame_change = 0.2
        self.run_frame_up = True
        self.fall_frame_counter = 0
        self.fall_frame_change = 0.1
        self.falling_rounds = 0
        self.hit_rounds = 0

    def stand_frame_counting(self):
        if round(self.stand_frame_counter + self.stand_frame_change) > 1:
            self.stand_frame_counter = 0
        else:
            self.stand_frame_counter += self.stand_frame_change

    def run_frame_counting(self):
        if self.run_frame_up:
            if round(self.run_frame_counter + self.run_frame_change) > 3:
                self.run_frame_up = False
            else:
                self.run_frame_counter += self.run_frame_change
        else:
            if round(self.run_frame_counter - self.run_frame_change) < 0:
                self.run_frame_up = True
            else:
                self.run_frame_counter -= self.run_frame_change

    def player_start_pos(self):
        """start y coord depends on player number"""
        if self.numb == 1:
            self.y = 400
        if self.numb == 2:
            self.y = 300
        if self.numb == 3:
            self.y = 200
        if self.numb == 4:
            self.y = 100
        self.x = 450

    def reset_direction(self):
        self.run_r = False
        self.run_l = False
        self.run_u = False
        self.run_d = False
        self.stand_r = False
        self.stand_l = False
        self.stand_u = False
        self.stand_d = False

    def player_input(self):
        # player keyboard inputs for up to 4 players
        self.keys = pygame.key.get_pressed()
        # controls only if the player's not falling or got hitten by an obstacle
        if self.fall_d != True and self.fall_u != True and self.fall_l != True and self.hitted != True:
            # player 1: w a s d
            if self.numb == 1:
                if self.keys[pygame.K_w] and self.button_u and self.button_d != True and self.button_l != True and self.button_r != True:
                    self.reset_direction()
                    self.run_u = True
                    self.y -= self.move_speed
                elif self.keys[pygame.K_a] and self.button_l and self.button_d != True and self.button_u != True and self.button_r != True:
                    self.reset_direction()
                    self.run_l = True
                    self.x -= self.move_speed
                elif self.keys[pygame.K_s] and self.button_d and self.button_u != True and self.button_l != True and self.button_r != True:
                    self.reset_direction()
                    self.run_d = True
                    self.y += self.move_speed
                elif self.keys[pygame.K_d] and self.button_r and self.button_d != True and self.button_l != True and self.button_u != True:
                    self.reset_direction()
                    self.run_r = True
                    self.x += self.move_speed
            # player 2: i j k l
            elif self.numb == 2:
                if self.keys[pygame.K_i] and self.button_u and self.button_d != True and self.button_l != True and self.button_r != True:
                    self.reset_direction()
                    self.run_u = True
                    self.y -= self.move_speed
                elif self.keys[pygame.K_j] and self.button_l and self.button_d != True and self.button_u != True and self.button_r != True:
                    self.reset_direction()
                    self.run_l = True
                    self.x -= self.move_speed
                elif self.keys[pygame.K_k] and self.button_d and self.button_u != True and self.button_l != True and self.button_r != True:
                    self.reset_direction()
                    self.run_d = True
                    self.y += self.move_speed
                elif self.keys[pygame.K_l] and self.button_r and self.button_d != True and self.button_l != True and self.button_u != True:
                    self.reset_direction()
                    self.run_r = True
                    self.x += self.move_speed
            # player 3: arrow keys
            elif self.numb == 3:
                if self.keys[pygame.K_UP] and self.button_u and self.button_d != True and self.button_l != True and self.button_r != True:
                    self.reset_direction()
                    self.run_u = True
                    self.y -= self.move_speed
                elif self.keys[pygame.K_LEFT] and self.button_l and self.button_d != True and self.button_u != True and self.button_r != True:
                    self.reset_direction()
                    self.run_l = True
                    self.x -= self.move_speed
                elif self.keys[pygame.K_DOWN] and self.button_d and self.button_u != True and self.button_l != True and self.button_r != True:
                    self.reset_direction()
                    self.run_d = True
                    self.y += self.move_speed
                elif self.keys[pygame.K_RIGHT] and self.button_r and self.button_d != True and self.button_l != True and self.button_u != True:
                    self.reset_direction()
                    self.run_r = True
                    self.x += self.move_speed
            # player 4: numpad 8 4 5 6
            elif self.numb == 4:
                if self.keys[pygame.K_KP8] and self.button_u and self.button_d != True and self.button_l != True and self.button_r != True:
                    self.reset_direction()
                    self.run_u = True
                    self.y -= self.move_speed
                elif self.keys[pygame.K_KP4] and self.button_l and self.button_d != True and self.button_u != True and self.button_r != True:
                    self.reset_direction()
                    self.run_l = True
                    self.x -= self.move_speed
                elif self.keys[pygame.K_KP5] and self.button_d and self.button_u != True and self.button_l != True and self.button_r != True:
                    self.reset_direction()
                    self.run_d = True
                    self.y += self.move_speed
                elif self.keys[pygame.K_KP6] and self.button_r and self.button_d != True and self.button_l != True and self.button_u != True:
                    self.reset_direction()
                    self.run_r = True
                    self.x += self.move_speed

    def player_fall(self):
        if self.fall_d != True and self.fall_l != True and self.fall_u != True:
            if self.rect.bottom < 68:
                self.reset_direction()
                self.fall_u = True
                self.fall_sfx.play()
            elif self.rect.bottom > 508:
                self.reset_direction()
                self.fall_d = True
                self.fall_sfx.play()
            elif self.rect.bottom > 266 and self.rect.left < 97:
                self.reset_direction()
                self.fall_l = True
                self.fall_sfx.play()
            elif self.rect.bottom > 223 and self.rect.left < 107:
                self.reset_direction()
                self.fall_l = True
                self.fall_sfx.play()
            elif self.rect.bottom <= 223 and self.rect.left < 119:
                self.reset_direction()
                self.fall_sfx.play()
                self.fall_l = True
        if self.fall_d or self.fall_u or self.fall_l:
            if round(self.fall_frame_counter + self.fall_frame_change) > 1:
                self.fall_frame_counter = 1
            else:
                self.fall_frame_counter += self.fall_frame_change
            if self.fall_l:
                if self.fall_swing_l > 0:
                    self.fall_swing_l -= 0.2
                self.x -= round(self.fall_swing_l)
            self.y += self.fall_gravity_d
            if self.falling_rounds >= 30:
                self.fallen = True
            self.falling_rounds += 1

    def player_obstacle_hit(self):
        if self.hitted:
            if self.hit_rounds < 6:
                self.x -= self.obstacle_bounce
                self.hit_rounds += 1
            else:
                self.hit_rounds = 0
                self.hitted = False

    def player_draw(self):
        """blits the player"""
        # fall animation
        if self.fall_d or self.fall_u or self.fall_l:
            if self.fall_d:
                screen.blit(self.fall_down_imgs[round(self.fall_frame_counter)], (self.x, self.y))
            elif self.fall_u:
                screen.blit(self.fall_up_imgs[round(self.fall_frame_counter)], (self.x, self.y))
            else:
                screen.blit(self.fall_left_imgs[round(self.fall_frame_counter)], (self.x, self.y))
            if self.falling_rounds > 20:
                screen.blit(self.splash_img, (self.x - 10, self.y))
        elif self.hitted:
            if self.char == "pea":
                screen.blit(self.shadow_img, (self.x, self.y + 57))
            else:
                screen.blit(self.shadow_img, (self.x - 5, self.y + 60))
            screen.blit(self.hit_img, (self.x, self.y))
        # idle animation
        elif (self.numb == 1 and self.keys[pygame.K_w] != True and self.keys[pygame.K_a] != True and self.keys[pygame.K_s] != True and self.keys[pygame.K_d] != True) or\
                (self.numb == 2 and self.keys[pygame.K_i] != True and self.keys[pygame.K_j] != True and self.keys[pygame.K_k] != True and self.keys[pygame.K_l] != True) or\
                (self.numb == 3 and self.keys[pygame.K_UP] != True and self.keys[pygame.K_LEFT] != True and self.keys[pygame.K_DOWN] != True and self.keys[pygame.K_RIGHT] != True) or \
                (self.numb == 4 and self.keys[pygame.K_KP8] != True and self.keys[pygame.K_KP4] != True and self.keys[pygame.K_KP5] != True and self.keys[pygame.K_KP6] != True):
            if self.run_r or self.stand_r:
                self.run_r = False
                self.stand_r = True
                if self.char == "wal":
                    screen.blit(self.shadow_img, (self.x-15 , self.y+60))
                elif self.char == "yos":
                    screen.blit(self.shadow_img, (self.x + 1, self.y + 60))
                elif self.char == "pea":
                    screen.blit(self.shadow_img, (self.x, self.y + 57))
                elif self.char == "mar":
                    screen.blit(self.shadow_img, (self.x, self.y + 60))
                screen.blit(self.stand_right_imgs[round(self.stand_frame_counter)], (self.x, self.y))
            elif self.run_l or self.stand_l:
                self.run_l = False
                self.stand_l = True
                if self.char == "wal":
                    screen.blit(self.shadow_img, (self.x - 15, self.y + 60))
                elif self.char == "yos":
                    screen.blit(self.shadow_img, (self.x + 1, self.y + 60))
                elif self.char == "pea":
                    screen.blit(self.shadow_img, (self.x, self.y + 57))
                elif self.char == "mar":
                    screen.blit(self.shadow_img, (self.x, self.y + 60))
                screen.blit(self.stand_left_imgs[round(self.stand_frame_counter)], (self.x, self.y))
            elif self.run_u or self.stand_u:
                self.run_u = False
                self.stand_u = True
                if self.char == "pea":
                    screen.blit(self.shadow_img, (self.x, self.y + 57))
                elif self.char == "mar":
                    screen.blit(self.shadow_img, (self.x-1 , self.y + 60))
                else:
                    screen.blit(self.shadow_img, (self.x+1, self.y + 60))
                screen.blit(self.stand_up_imgs[round(self.stand_frame_counter)], (self.x, self.y))
            elif self.run_d or self.stand_d:
                self.run_d = False
                self.stand_d = True
                if self.char == "pea":
                    screen.blit(self.shadow_img, (self.x, self.y + 57))
                elif self.char == "mar":
                    screen.blit(self.shadow_img, (self.x-1 , self.y + 60))
                else:
                    screen.blit(self.shadow_img, (self.x+1, self.y + 60))
                screen.blit(self.stand_down_imgs[round(self.stand_frame_counter)], (self.x, self.y))
        # run animation
        else:
            if self.run_r:
                if self.char == "pea":
                    screen.blit(self.shadow_img, (self.x, self.y + 57))
                else:
                    screen.blit(self.shadow_img, (self.x + 1, self.y + 60))
                screen.blit(self.run_right_imgs[round(self.run_frame_counter)], (self.x, self.y))
            elif self.run_l:
                if self.char == "pea":
                    screen.blit(self.shadow_img, (self.x, self.y + 57))
                else:
                    screen.blit(self.shadow_img, (self.x + 1, self.y + 60))
                screen.blit(self.run_left_imgs[round(self.run_frame_counter)], (self.x, self.y))
            elif self.run_u:
                if self.char == "pea":
                    screen.blit(self.shadow_img, (self.x, self.y + 57))
                elif self.char == "mar":
                    screen.blit(self.shadow_img, (self.x-1 , self.y + 60))
                else:
                    screen.blit(self.shadow_img, (self.x + 1, self.y + 60))
                screen.blit(self.run_up_imgs[round(self.run_frame_counter)], (self.x, self.y))
            elif self.run_d:
                if self.char == "pea":
                    screen.blit(self.shadow_img, (self.x, self.y + 57))
                elif self.char == "mar":
                    screen.blit(self.shadow_img, (self.x-1 , self.y + 60))
                else:
                    screen.blit(self.shadow_img, (self.x + 1, self.y + 60))
                screen.blit(self.run_down_imgs[round(self.run_frame_counter)], (self.x, self.y))
        #pygame.draw.rect(screen, (000,000,000), self.rect)    # for help with rect based meethods

    def player_reset(self):
        self.score = 0
        self.stand_d = False  # stands down
        self.stand_u = False  # stands up
        self.stand_l = False  # stands left
        self.stand_r = True  # stands right
        self.run_d = False  # runs down
        self.run_u = False  # runs up
        self.run_l = False  # runs left
        self.run_r = False  # runs right
        self.fallen = False  # if fallen, player is defeated
        self.fall_u = False  # falls over the upper ledge
        self.fall_d = False  # falls over the down ledge
        self.fall_l = False  # falls over the left ledge
        self.hitted = False  # got hitted by an obstacle
        self.stand_r_scale = (0, 0)
        self.stand_l_scale = (0, 0)
        self.stand_u_scale = (0, 0)
        self.stand_d_scale = (0, 0)
        self.run_r_scale = (0, 0)
        self.run_l_scale = (0, 0)
        self.run_u_scale = (0, 0)
        self.run_d_scale = (0, 0)
        self.fall_u_scale = (0, 0)
        self.fall_l_scale = (0, 0)
        self.fall_gravity_d = 5
        self.fall_swing_l = 7
        self.player_imgs()
        self.player_sfx()
        self.player_start_pos()
        self.rect = self.stand_right_imgs[0].get_rect(topleft=(self.x, self.y))
        self.player_imgs_scale()
        self.create_frame_counter()
        if self.char == "wal":
            self.move_speed = 7
            self.obstacle_bounce = 12
        elif self.char == "yos":
            self.move_speed = 6
            self.obstacle_bounce = 10
        elif self.char == "pea":
            self.move_speed = 6
            self.obstacle_bounce = 11
        elif self.char == "mar":
            self.move_speed = 5
            self.obstacle_bounce = 9
        self.button_l = False  # attributes to check if and which run-button is currently pressed
        self.button_r = False
        self.button_u = False
        self.button_d = False

    def player_update(self):
        if self.fallen != True:
            self.player_obstacle_hit()
            self.stand_frame_counting()
            self.run_frame_counting()
            self.player_input()
            self.player_fall()
            self.player_imgs_scale()
            self.player_rects()
            self.player_draw()


