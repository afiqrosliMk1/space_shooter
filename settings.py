
class Settings:
    """store game settings"""
    def __init__(self):
        self.screen_size = (400, 400)
        self.bg_color = "grey"
        self.ship_speed = 5.5
        self.life = 3

        # bullet settings
        self.bullet_speed = 7.5

        # alien settings
        self.alien_speed = 5.0
        self.alien_drop_speed = 128