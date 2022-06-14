
class GameStats:
    """Track Stats for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialise statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #start the game in an inactive state
        self.game_active = False

        #High score should never be reset
        self.high_score = 0


    def reset_stats(self):
        """Initialise stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

