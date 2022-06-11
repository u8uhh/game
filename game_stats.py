class GameStats:
    """follow game statistik"""

    def __init__(self, ai_game):
        """Stats inicialization"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # start game in active stan
        self.game_active = True

        # score not 0
        self.high_score = 0

    def reset_stats(self):
        """Stats inicialization"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
