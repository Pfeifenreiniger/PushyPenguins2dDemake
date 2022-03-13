
import pygame, random

screen = pygame.display.set_mode((800, 600))

class Penguins(pygame.sprite.Sprite):
    def __init__(self, size, row):        # y pos and sprite-scaling depends on row
        super().__init__()
        self.size = size
        self.row = row
        self.walk_animation_counter = 0
        self.walk_animation_counter_plus = 0.2
        self.jump_animation_counter = 2
        self.jump_animation_counter_plus = 0.1
        self.jump = False
        self.x = 800
        if self.size == "small":
            self.img_walk1 = pygame.image.load("graphics/game/obstacles/penguins_small/small_pengu1.png").convert_alpha()
            self.img_walk2 = pygame.image.load("graphics/game/obstacles/penguins_small/small_pengu2.png").convert_alpha()
            self.img_jump1 = pygame.image.load("graphics/game/obstacles/penguins_small/small_pengu_jump1.png").convert_alpha()
            self.img_jump2 = pygame.image.load("graphics/game/obstacles/penguins_small/small_pengu_jump2.png").convert_alpha()
            self.img_splash = pygame.image.load("graphics/game/obstacles/penguins_small/small_pengu_splash.png").convert_alpha()
            self.img_swimming = pygame.image.load("graphics/game/obstacles/penguins_small/small_pengu_swimming.png").convert_alpha()
            if self.row == 1:
                self.y = 458
                self.penguin_rects()
            elif self.row == 2:
                self.y = 410
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (40,48))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (40, 48))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (40, 48))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (40, 48))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (45, 50))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (45, 50))
            elif self.row == 3:
                self.y = 364
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (39, 47))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (39, 47))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (39, 47))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (39, 47))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (44, 49))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (44, 49))
            elif self.row == 4:
                self.y = 320
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (38, 46))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (38, 46))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (38, 46))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (38, 46))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (43, 49))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (43, 49))
            elif self.row == 5:
                self.y = 278
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (37, 45))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (37, 45))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (37, 45))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (37, 45))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (42, 48))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (42, 48))
            elif self.row == 6:
                self.y = 238
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (36, 44))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (36, 44))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (36, 44))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (36, 44))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (41, 47))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (41, 47))
            elif self.row == 7:
                self.y = 200
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (35, 43))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (35, 43))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (35, 43))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (35, 43))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (40, 46))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (40, 46))
            elif self.row == 8:
                self.y = 164
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (34, 42))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (34, 42))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (34, 42))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (34, 42))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (39, 45))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (39, 45))
            elif self.row == 9:
                self.y = 130
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (33, 41))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (33, 41))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (33, 41))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (33, 41))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (38, 44))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (38, 44))
            elif self.row == 10:
                self.y = 98
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (32, 40))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (32, 40))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (32, 40))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (32, 40))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (37, 43))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (37, 43))
            elif self.row == 11:
                self.y = 68
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (31, 39))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (31, 39))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (31, 39))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (31, 39))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (36, 42))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (36, 42))
        else:
            self.img_walk1 = pygame.image.load("graphics/game/obstacles/penguins_big/big_pengu1.png").convert_alpha()
            self.img_walk2 = pygame.image.load("graphics/game/obstacles/penguins_big/big_pengu2.png").convert_alpha()
            self.img_jump1 = pygame.image.load("graphics/game/obstacles/penguins_big/big_pengu_jump1.png").convert_alpha()
            self.img_jump2 = pygame.image.load("graphics/game/obstacles/penguins_big/big_pengu_jump2.png").convert_alpha()
            self.img_splash = pygame.image.load("graphics/game/obstacles/penguins_big/big_pengu_splash.png").convert_alpha()
            self.img_swimming = pygame.image.load("graphics/game/obstacles/penguins_big/big_pengu_swimming.png").convert_alpha()
            if self.row == 1:
                self.y = 410
                self.penguin_rects()
            elif self.row == 3:
                self.y = 320
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (80, 96))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (80, 96))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (80, 96))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (80, 96))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (89, 98))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (89, 98))
            elif self.row == 5:
                self.y = 238
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (78, 94))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (78, 94))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (78, 94))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (78, 94))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (87, 96))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (87, 96))
            elif self.row == 7:
                self.y = 164
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (75, 91))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (75, 91))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (75, 91))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (75, 91))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (84, 93))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (84, 93))
            elif self.row == 9:
                self.y = 98
                self.img_walk1 = pygame.transform.smoothscale(self.img_walk1, (73, 89))
                self.img_walk2 = pygame.transform.smoothscale(self.img_walk2, (73, 89))
                self.img_jump1 = pygame.transform.smoothscale(self.img_jump1, (73, 89))
                self.img_jump2 = pygame.transform.smoothscale(self.img_jump2, (73, 89))
                self.penguin_rects()
                self.img_splash = pygame.transform.smoothscale(self.img_splash, (82, 91))
                self.img_swimming = pygame.transform.smoothscale(self.img_swimming, (82, 91))
        self.imgs = [self.img_walk1, self.img_walk2, self.img_jump1, self.img_jump2]
        self.movespeed = random.randint(2,3)
        self.movespeed_updated = False
        self.step_sfx = pygame.mixer.Sound("sfx/game/penguins/ssbm_wong_sfx.wav")
        self.baby_cry_sfx = pygame.mixer.Sound("sfx/game/penguins/sm64_penguin_baby.wav")
        self.setup_sfx()
    def moving(self):
        if self.x <= 310 and self.movespeed_updated != True:
            self.movespeed = self.movespeed * 2
            self.movespeed_updated = True
        self.x -= self.movespeed
    def jumping(self):
        self.jump = True
        if round(self.jump_animation_counter + self.jump_animation_counter_plus) > 3:
            self.jump_animation_counter = 3
        else:
            self.jump_animation_counter += self.jump_animation_counter_plus
    def animation(self):
        if self.size == "small":
            if self.y > 265 and self.x <= 97:                                                       # jump from the ledge
                self.jumping()
            elif self.y <= 265 and self.x <= 116:
                self.jumping()
            elif round(self.walk_animation_counter + self.walk_animation_counter_plus) > 1:         # walking animation
                self.walk_animation_counter = 0
        else:
            if self.y > 265 and self.x <= 57:                                                       # jump from the ledge
                self.jumping()
            elif self.y <= 265 and self.x <= 76:
                self.jumping()
            elif round(self.walk_animation_counter + self.walk_animation_counter_plus) > 1:         # walking animation
                self.walk_animation_counter = 0
        self.walk_animation_counter += self.walk_animation_counter_plus

    def setup_sfx(self):
        self.step_sfx.set_volume(0.3)
        self.baby_cry_sfx.set_volume(0.2)

    def sfx(self):
        if random.randint(0,50) > 48:
            self.step_sfx.play()
        if random.randint(0,1000) > 990:
            self.baby_cry_sfx.play()

    def penguin_rects(self):
        if self.size == "small":
            if self.row == 1:
                self.rect = pygame.Rect(self.x+3, self.y + round((49 / 2)), 38, round((49 / 2.3)))
            elif self.row == 2:
                self.rect = pygame.Rect(self.x+3, self.y + round((48 / 2)), 37, round((48 / 2.3)))
            elif self.row == 3:
                self.rect = pygame.Rect(self.x+3, self.y + round((47 / 2)), 36, round((47 / 2.3)))
            elif self.row == 4:
                self.rect = pygame.Rect(self.x+3, self.y + round((46 / 2)), 35, round((46 / 2.3)))
            elif self.row == 5:
                self.rect = pygame.Rect(self.x+3, self.y + round((45 / 2)), 34, round((45 / 2.3)))
            elif self.row == 6:
                self.rect = pygame.Rect(self.x+3, self.y + round((44 / 2)), 33, round((44 / 2.3)))
            elif self.row == 7:
                self.rect = pygame.Rect(self.x+3, self.y + round((43 / 2)), 32, round((43 / 2.3)))
            elif self.row == 8:
                self.rect = pygame.Rect(self.x+3, self.y + round((42 / 2)), 31, round((42 / 2.3)))
            elif self.row == 9:
                self.rect = pygame.Rect(self.x+3, self.y + round((41 / 2)), 30, round((41 / 2.3)))
            elif self.row == 10:
                self.rect = pygame.Rect(self.x+3, self.y + round((40 / 2)), 29, round((40 / 2.3)))
            elif self.row == 11:
                self.rect = pygame.Rect(self.x+3, self.y + round((39 / 2)), 28, round((39 / 2.3)))
        else:
            if self.row == 1:
                self.rect = pygame.Rect(self.x+6, self.y + round((98 / 2)), 76, round((98 / 2.3)))
            elif self.row == 3:
                self.rect = pygame.Rect(self.x+6, self.y + round((96 / 2)), 74, round((96 / 2.3)))
            elif self.row == 5:
                self.rect = pygame.Rect(self.x+6, self.y + round((94 / 2)), 72, round((94 / 2.3)))
            elif self.row == 7:
                self.rect = pygame.Rect(self.x+6, self.y + round((91 / 2)), 70, round((91 / 2.3)))
            elif self.row == 9:
                self.rect = pygame.Rect(self.x+6, self.y + round((89 / 2)), 68, round((89/2.3)))
    def drawing(self):
        if self.jump:
            if self.size == "small":
                if self.x <= 56 and self.x >= 30:
                    self.penguin_rects()
                    screen.blit(self.imgs[round(self.jump_animation_counter)], (self.x, self.y))
                    self.rect_splash = self.img_splash.get_rect(topleft=(self.x, self.y))
                    screen.blit(self.img_splash, self.rect_splash)
                elif self.x < 30:
                    self.penguin_rects()
                    screen.blit(self.imgs[round(self.jump_animation_counter)], (self.x, self.y))
                    self.rect_swimming = self.img_swimming.get_rect(topleft=(self.x, self.y))
                    screen.blit(self.img_swimming, self.rect_swimming)
                else:
                    self.penguin_rects()
                    screen.blit(self.imgs[round(self.jump_animation_counter)], (self.x, self.y))
            else:
                if self.x <= 46 and self.x >= 20:
                    self.penguin_rects()
                    screen.blit(self.imgs[round(self.jump_animation_counter)], (self.x, self.y))
                    self.rect_splash = self.img_splash.get_rect(topleft=(self.x, self.y))
                    screen.blit(self.img_splash, self.rect_splash)
                elif self.x < 20:
                    self.penguin_rects()
                    screen.blit(self.imgs[round(self.jump_animation_counter)], (self.x, self.y))
                    self.rect_swimming = self.img_swimming.get_rect(topleft=(self.x, self.y))
                    screen.blit(self.img_swimming, self.rect_swimming)
                else:
                    self.penguin_rects()
                    screen.blit(self.imgs[round(self.jump_animation_counter)], (self.x, self.y))
        else:
            self.penguin_rects()
            screen.blit(self.imgs[round(self.walk_animation_counter)], (self.x, self.y))
        #pygame.draw.rect(screen, (000, 000, 000), self.rect)  # for help with rect based methods
    def destroy(self):
        if self.x <= -82:
            self.kill()
    def update(self):
        self.destroy()
        self.moving()
        self.animation()
        self.sfx()
        self.drawing()