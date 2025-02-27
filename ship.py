import pygame

class Ship:
    """ship class"""
    def __init__(self, game):
        """initialise ship"""
        self.image = pygame.image.load("images/myship.png").convert_alpha()
        #scale image
        self.image= pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.move_xdir = game.move_xdir
        self.move_ydir = game.move_ydir
        self.settings = game.game_settings
        self.rect.midbottom = self.screen_rect.midbottom
        #use float to store exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def handle_event(self):
        pass

    def update(self):
        if self.move_xdir[0] == 1 and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.move_xdir[1] == 1 and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_ydir[0] == 1 and self.rect.bottom < self.screen_rect.bottom:
            self.y += 10
        if self.move_ydir[1] == 1 and self.rect.y > 0:
            self.y -= 10

        self.rect.x = self.x 
        self.rect.y = self.y 

    def render(self):
        """render ship"""
        self.screen.blit(self.image, self.rect)