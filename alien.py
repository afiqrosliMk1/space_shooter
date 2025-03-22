import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """alien class"""
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load("images/alien.png")
        #scale image
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        #1 right, -1 left
        self.dir = 1
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.settings = game.game_settings

    def update(self):
        #add or subtract from rect.x based on direction
        self.rect.x += self.settings.alien_speed * self.dir
        #check if alien over edges
        if (self.rect.right > self.screen_rect.right or self.rect.left < 0):
            self.dir *= -1
            self.rect.y += self.settings.alien_drop_speed
        # if self.dir == 1:
        #     self.rect.x += self.settings.alien_speed
        #     if self.rect.right >= self.screen_rect.right:
        #         self.dir = -1
        #         self.rect.y += self.settings.alien_speed
        # elif self.dir == -1:
        #     self.rect.x -= self.settings.alien_speed
        #     if self.rect.left <= 0:
        #         self.dir = 1
        #         self.rect.y += self.settings.alien_speed

