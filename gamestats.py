class GameStats:
    """game statistics"""
    def __init__(self, game):
        self.settings = game.game_settings
        self.life_left = self.settings.life
        self.die = False