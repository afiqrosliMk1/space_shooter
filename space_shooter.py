import sys
import pygame
import pygame.freetype
from ship import Ship
from bullet import Bullet
from alien import Alien
from settings import Settings


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

        #setup clock
        self.clock = pygame.time.Clock()

        #setup bullets
        self.bullets = pygame.sprite.Group()
        self.bullet_sound = pygame.mixer.Sound("sfx/bullet.wav")
        self.explosion_sound = pygame.mixer.Sound(b"\x00\x00")

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
        for i in range(4):
            alien = Alien(self.screen)
            alien.rect.x = current_x
            current_x = current_x + alien.rect.width + 30
            self.aliens.add(alien)

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
                    #print(len(bullets))

            for alien in self.aliens.sprites():
                if alien:
                    if alien.dir == 1:
                        alien.rect.x += 10
                        if alien.rect.right >= self.screen_rect.right:
                            alien.dir = -1
                            alien.rect.y += 50
                    elif alien.dir == -1:
                        alien.rect.x -= 10
                        if alien.rect.left <= 10:
                            alien.dir = 1
                            alien.rect.y += 50

                    if alien.rect.colliderect(self.ship.rect):
                        self.game_active = False

                    for bullet in self.bullets:
                        if bullet.rect.colliderect(alien.rect):
                            self.explosion_sound.play()
                            alien = None
                            print("hit")
                            break
                        else:
                            pass

    def render(self):
        self.screen.fill(self.game_settings.bg_color)
        self.font.render_to(self.screen, (100, 100), "You lose", (255, 255, 255))
        
        # remember, always copy a list before making changes to it in a loop
        for bullet in self.bullets.sprites()[:]:
            bullet.draw()

        self.aliens.draw(self.screen)

        self.ship.render()

        if self.game_active == False:
            self.screen.blit(self.explosion, self.ship.rect.midtop)
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





