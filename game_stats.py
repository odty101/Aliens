from game_logger import logger


class GameStats(object):
    """
    A simple class to keep track of game stats
    """
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # Set the high score
        self.high_score = 0

        self.game_active = False

    def reset_stats(self):
        """
        Initialize the stats that can be changed during the game
        """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        logger.info('Game Stats reset - Ship Limit: {} - Score: {}'.format(self.ships_left, self.score))