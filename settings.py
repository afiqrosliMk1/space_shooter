
class Settings:
    """store game settings"""
    def __init__(self):
        self.screen_size = (400, 400)
        self.bg_color = "grey"
        self.ship_speed = 5.5

        # bullet settings
        self.bullet_speed = 7.5