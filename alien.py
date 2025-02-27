import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """alien class"""
    def __init__(self, game_screen):
        super().__init__()
        self.image = pygame.image.load("images/alien.png")
        #scale image
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.dir = 1
        self.screen = game_screen

    def render(self):
        self.screen.blit(self.image, self.rect)