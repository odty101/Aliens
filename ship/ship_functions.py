from time import sleep

import pygame

import game_functions
from aliens import fleet_functions
from game_logger import logger
from ship.bullet import Bullet


def fire_bullet(ai_settings, screen, stats, ship, bullets):
    """
    Fire a bullet if the limit is not reached
    """
    # Create a new bullet and add it to the bullets group if less then the max number of bullets
    if len(bullets) < ai_settings.bullets_allowed and stats.game_active:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_game):
    """
    Update the position of the bullets and get rid of old bullets
    """
    # Update the bullets position
    ai_game.bullets.update()

    # Get rid of the bullets that have disappeared
    for bullet in ai_game.bullets.copy():
        if bullet.rect.bottom <= 0:
            ai_game.bullets.remove(bullet)

    # Check for collisions and fleet destruction
    game_functions.check_bullet_alien_collisions(ai_game)


def ship_hit(ai_game):
    """
    Respond to the ship being hit by aliens
    """
    logger.debug('Ship Hit')
    if ai_game.stats.ships_left > 0:
        # Decrement the ships left
        ai_game.stats.ships_left -= 1

        # Update Scoreboard
        ai_game.scoreboard.prep_ships()

        # Empty the list of aliens and bullets
        ai_game.aliens.empty()
        ai_game.bullets.empty()

        # Create a new fleet and center the ship
        fleet_functions.create_fleet(ai_game)
        ai_game.ship.center_ship()

        # Pause
        sleep(.5)
    else:
        ai_game.stats.game_active = False
        pygame.mouse.set_visible(True)
