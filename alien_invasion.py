import pygame
from pygame.sprite import Group

import game_core
import user_events
from aliens import fleet_functions
from button import Button
from game_logger import logger
from game_stats import GameStats
from score_board import Scoreboard
from settings import Settings
from ship import ship_functions
from ship.ship import Ship


class AlienInvasion(object):
    """
    Simple class to keep track of the AI game
    """
    def __init__(self):
        self._screen = None

        self.settings = Settings()
        self.stats = GameStats(self.settings)
        self.play_button = Button(self.settings, self.screen, 'Play')
        self.scoreboard = Scoreboard(self.settings, self.screen, self.stats)
        self.ship = Ship(self.settings, self.screen)
        self.bullets = Group()
        self.aliens = Group()

    @property
    def screen(self):
        """
        Create a game screen and set the caption
        :return: pygame.display
        """
        if not self._screen:
            # Create the game screen
            screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            logger.info('Screen created with H: {} W: {}'.format(self.settings.screen_height,
                                                                 self.settings.screen_width))

            # Set screen caption
            pygame.display.set_caption('Alien Invasion')

            self._screen = screen

        return self._screen


def run_game():
    """
    Initiate the pygame, settings, and create a screen object
    """
    logger.info('Game Loaded')

    pygame.init()

    ai_game = AlienInvasion()

    game_core.load_game(ai_game)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        user_events.check_events(ai_game)

        if ai_game.stats.game_active:
            ai_game.ship.update()
            ship_functions.update_bullets(ai_game)
            fleet_functions.update_aliens(ai_game)

        # Redraw the screen and flip to new
        game_core.update_screen(ai_game)


if __name__ == '__main__':
    try:
        run_game()
    except(SystemExit):
        logger.info('System Exited')
    except:
        logger.exception('Traceback Triggered')
        game_core.end_game(error=True)