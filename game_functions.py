import pygame

from aliens import fleet_functions
from game_logger import logger


def check_bullet_alien_collisions(ai_game):
    # Check for any bullets that have hit aliens, if so get rid of the bullet and alien
    collisions = pygame.sprite.groupcollide(ai_game.bullets, ai_game.aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            ai_game.stats.score += ai_game.settings.alien_points * len(aliens)
            ai_game.scoreboard.prep_score()
        check_high_score(ai_game)

    # If fleet is 0 destroy existing bullets and create a new fleet
    if len(ai_game.aliens) == 0:
        logger.debug('Fleet Destroyed')
        ai_game.bullets.empty()
        ai_game.settings.increase_speed()
        fleet_functions.create_fleet(ai_game)

        # Increase the level
        ai_game.stats.level += 1
        ai_game.scoreboard.prep_level()


def check_high_score(ai_game):
    """
    Check if there is a new high score
    """
    if ai_game.stats.score > ai_game.stats.high_score:
        ai_game.stats.high_score = ai_game.stats.score
        ai_game.scoreboard.prep_high_score()
