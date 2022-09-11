import pygame
from settings import *
from player import Player


class Level:
    def __init__(self):

        # get the display surface
        self.player = None  # just resolve warning
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player((0.2*SCREEN_WIDTH, 0.6*SCREEN_HEIGHT), self.all_sprites, 'goods')
        self.player = Player((0.8*SCREEN_WIDTH, 0.6*SCREEN_HEIGHT), self.all_sprites, 'goods')
        n = 15
        jianju = 15
        for i in range(n):
            # (n-1)*jianju/2
            self.player = Player((0.5 * SCREEN_WIDTH-(n-1)*jianju/2+i*jianju, 0.75 * SCREEN_HEIGHT), self.all_sprites, 'cards')
        # self.player = Player((640, 360), self.all_sprites)

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
        # print('run game')
