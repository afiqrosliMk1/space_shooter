import sys
import pygame
import pygame.freetype
from ship import Ship
from bullet import Bullet
from alien import Alien
from settings import Settings
from gamestats import GameStats
from time import sleep

class SpaceShooter:
    def __init__(self):
        #initialise pygame
        pygame.init()

        self.game_settings = Settings()
        #setup display
        self.screen = pygame.display.set_mode(self.game_settings.screen_size)
        self.screen_rect = self.screen.get_rect()

        self.icon = pygame.image.load("images/myship.png")
        pygame.display.set_caption("spaceship shooter")
        pygame.display.set_icon(self.icon)

        #create stats object
        self.stats = GameStats(self)

        #move_xdir[0] = 1 -->left key, move_xdir[1] = 1 -->right key
        #move_ydir[0] = 1 --> bottom arrow key, move_ydir[1] = 1 --> up arrow is pressed
        self.move_xdir = [0, 0]
        self.move_ydir = [0, 0]

        #setup ship
        self.ship = Ship(self)

        #setup alien
        self.aliens = pygame.sprite.Group()
        self._create_alien()

        #setup font
        self.font = pygame.freetype.Font(None, 36)

        #explosion
        self.explosion = pygame.image.load("images/explosion.png")
        self.explosion_location = [0, 0] #where to spawn explosion

        #setup clock
        self.clock = pygame.time.Clock()

        #setup bullets
        self.bullets = pygame.sprite.Group()
        self.bullet_sound = pygame.mixer.Sound("sfx/bullet.wav")
        self.explosion_sound = pygame.mixer.Sound("sfx/boom.wav")

        self.show_font = False
        self.running = True
        self.game_active = True

    #leading underscore indicates helper function (not intended to use outside class)
    def _create_bullet(self):
        """creating bullet"""
        bullet = Bullet(self)
        self.bullets.add(bullet)

    def _create_alien(self):
        """creating aliens"""
        current_x = 0
        current_y = 0
        for j in range(2):
            for i in range(4):
                alien = Alien(self)
                alien.rect.x = current_x
                alien.rect.y = current_y
                current_x = current_x + alien.rect.width + 30
                self.aliens.add(alien)
            # finished a row, reset x, increment y
            current_x = 0
            current_y = current_y + alien.rect.height

    def handle_event(self):
        #event handling 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_xdir[0] = 1
                if event.key == pygame.K_RIGHT:
                    self.move_xdir[1] = 1
                if event.key == pygame.K_DOWN:
                    self.move_ydir[0] = 1
                if event.key == pygame.K_UP:
                    self.move_ydir[1] = 1
                if event.key == pygame.K_a:
                    self.show_font = True   
                if event.key == pygame.K_SPACE:
                    if len(self.bullets) < 5:
                        self._create_bullet()
                        self.bullet_sound.play() 
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.move_xdir[0] = 0
                if event.key == pygame.K_RIGHT:
                    self.move_xdir[1] = 0
                if event.key == pygame.K_DOWN:
                    self.move_ydir[0] = 0
                if event.key == pygame.K_UP:
                    self.move_ydir[1] = 0

    def update_state(self):
        if self.game_active == True:
            self.ship.update() 

            self.bullets.update()
            for bullet in self.bullets.sprites():
                if bullet.rect.y < 0:
                    self.bullets.remove(bullet)

            if not self.aliens:
                self._create_alien()

            self.aliens.update()
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
            if collisions:
                self.explosion_sound.play()
                print(collisions)

            if pygame.sprite.spritecollideany(self.ship, self.aliens):
                if self.stats.life_left > 0:
                    self.stats.life_left -= 1
                    self.stats.die = True
                    self.explosion_location = self.ship.rect.midtop
                    #reset the game
                    self.aliens.empty()
                    self.bullets.empty()

                    self._create_alien()
                    self.ship.center_ship()
                    
                else:
                    self.game_active = False

            for alien in self.aliens.sprites():
                if alien.rect.bottom > self.screen_rect.bottom:
                    self.game_active = False
                    break

    def render(self):
        if self.stats.die == True:
            self.screen.blit(self.explosion, self.explosion_location)
            pygame.display.flip()
            sleep(1.0)
            #reset die flag
            self.stats.die = False

        self.screen.fill(self.game_settings.bg_color)
        self.font.render_to(self.screen, (100, 100), "You lose", (255, 255, 255))
        
        # remember, always copy a list before making changes to it in a loop
        for bullet in self.bullets.sprites()[:]:
            bullet.draw()

        # we can call draw method directly because alien Group has both rect and image, while bullet Group don't.
        self.aliens.draw(self.screen)

        self.ship.render()
        pygame.display.flip()


    def run(self):
        #main game loop
        while self.running:
            #event handling
            self.handle_event()
            #update game state
            self.update_state()
            #render
            self.render()
            #control frame rate
            self.clock.tick(30)


if __name__ == '__main__':
    game = SpaceShooter()
    game.run()





