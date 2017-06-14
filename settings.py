from game_logger import logger


class Settings(object):
    def __init__(self):
        """
        Initialize the game settings
        """

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_limit = 2

        # Bullet Settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien Settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # Misc Settings
        self.save_file = 'ai_highscore'

    def initialize_dynamic_settings(self):
        """
        Initialize the settings that change throughout the game
        """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction of 1 is right; -1 is left
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

        logger.info('Initial - Bullet Speed: {:3}'.format(self.bullet_speed_factor))
        logger.info('Initial - Alien Speed: {:3}'.format(self.alien_speed_factor))
        logger.info('Initial - Ship Speed: {:3}'.format(self.ship_speed_factor))
        logger.info('Initial - Kill Points: {:3}'.format(self.alien_points))

    def increase_speed(self):
        """
        Increase the speed settings and the points per kill
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

        logger.info('SpeedUp - Bullet Speed: {:3.3}'.format(self.bullet_speed_factor))
        logger.info('SpeedUp - Alien Speed: {:3.3}'.format(self.alien_speed_factor))
        logger.info('SpeedUp - Ship Speed: {:3.3}'.format(self.ship_speed_factor))
        logger.info('SpeedUp - Kill Points: {:3}'.format(self.alien_points))
