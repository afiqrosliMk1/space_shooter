import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 40, 8)
        self.rect.midtop = game.ship.rect.midtop
        self.rect.y = game.ship.rect.top
        self.screen = game.screen
        self.settings = game.game_settings
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, "red", self.rect)