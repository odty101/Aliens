import sys
import os
import pygame
import pickle

from aliens import fleet_functions
from game_logger import logger


def reset_match(ai_game):
    """
    Reset the match
    """
    # Reset the dynamic settings
    ai_game.settings.initialize_dynamic_settings()

    # Hide the mouse curser
    pygame.mouse.set_visible(False)

    # Reset the game stats
    ai_game.stats.reset_stats()
    ai_game.stats.game_active = True

    # Reset the Scoreboard images
    ai_game.scoreboard.prep_ships()
    ai_game.scoreboard.prep_score()
    ai_game.scoreboard.prep_high_score()
    ai_game.scoreboard.prep_level()

    # Empty the list of bullets and aliens
    ai_game.aliens.empty()
    ai_game.bullets.empty()

    # Create a new fleet and center the ship
    fleet_functions.create_fleet(ai_game)
    ai_game.ship.center_ship()


def update_screen(ai_game):
    """
    Update images on the screen and flip to the new screen
    """
    logger.debug('Updating Screen')
    # Redraw the screen
    ai_game.screen.fill(ai_game.settings.bg_color)

    # Redraw all bullets behind ship and aliens.
    for bullet in ai_game.bullets.sprites():
        bullet.draw_bullet()

    # Redraw the ships' location
    ai_game.ship.blitme()
    ai_game.aliens.draw(ai_game.screen)

    # Draw the score info
    ai_game.scoreboard.show_score()

    # Draw the play button if the game is inactive
    if not ai_game.stats.game_active:
        ai_game.play_button.draw_button()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def get_save_file(ai_game):
    """
    :return: save_file path to where the game saves data
    """
    game_path = os.path.dirname(os.path.abspath(__file__))
    save_file = '{game_path}/{save}'.format(game_path=game_path, save=ai_game.settings.save_file)

    return save_file


def save_game(ai_game):
    """
    Save the game to a file
    """
    # Open file and save data
    with open(get_save_file(ai_game), 'wb') as save_file:
        pickle.dump(ai_game.stats.high_score, save_file)

    logger.info('Saved High Score: {}'.format(ai_game.stats.high_score))


def load_game(ai_game):
    """
    Load the game file
    """
    # Try to open file and load data
    try:
        with open(get_save_file(ai_game), 'rb') as save_file:
            ai_game.stats.high_score = pickle.load(save_file)

        logger.info('High Score Loaded: {}'.format(ai_game.stats.high_score))
    except FileNotFoundError:
        logger.info('Save file not found')


def end_game(ai_game=None, error=False):
    """
    End the game, saving the high score to a pickle file
    """
    logger.info('Ending Game')

    if ai_game:
        # Save the highscore before exiting
        save_game(ai_game)

    pygame.quit()

    if error:
        sys.exit(1)
    else:
        sys.exit()
