
import pygame, random

screen = pygame.display.set_mode((800, 600))

class Background:
    def __init__(self, bg):
        self.bg = bg
        if self.bg == "sea":
            self.img = pygame.image.load("graphics/game/background/sea.png").convert()
            self.y = 0
        elif self.bg == "sea_lower_edge":
            self.img = pygame.image.load("graphics/game/background/sea_lower_edge.png").convert_alpha()
            self.y = 450
            self.animation_turn = False
        elif self.bg == "ice_floe":
            self.img = pygame.image.load("graphics/game/background/ice_floe.png").convert_alpha()
            self.y = 0
        self.x = 0
    def draw(self):
        screen.blit(self.img, (self.x, round(self.y)))
    def animation(self):
        if self.bg == "sea_lower_edge":
            if self.animation_turn == False and (round(self.y - 0.1) == 440):
                self.animation_turn = True
            if self.animation_turn == False:
                self.y -= 0.1
            if self.animation_turn == True and (round(self.y + 0.1) == 450):
                self.animation_turn = False
            if self.animation_turn == True:
                self.y += 0.1


class Wave(pygame.sprite.Sprite):
    def __init__(self, wave_no):
        super().__init__()
        self.wave_no = wave_no
        if self.wave_no == 1:
            self.img = pygame.image.load("graphics/game/background/waves/wave1.png").convert_alpha()
        elif self.wave_no == 2:
            self.img = pygame.image.load("graphics/game/background/waves/wave2.png").convert_alpha()
        else:
            self.img = pygame.image.load("graphics/game/background/waves/wave3.png").convert_alpha()
        self.x = 800
        self.random_y = random.randint(1,10)
        if self.random_y <= 3:
            self.y = random.randint(21, 26)
        if self.random_y > 3 and self.random_y <= 6:
            self.y = random.randint(27, 32)
        if self.random_y > 6:
            self.y = random.randint(33, 38)
    def moving(self):
        self.x -= 3
    def destroy(self):
        if self.x <= -200:
            self.kill()
    def drawing(self):
        screen.blit(self.img, (self.x, self.y))
    def update(self):
        self.moving()
        self.destroy()
        self.drawing()
