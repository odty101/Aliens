import pygame

from aliens.alien import Alien
from game_logger import logger
from ship import ship_functions


def get_number_aliens_x(ai_settings, alien_width):
    """
    Determine the number of aliens that fit in a row
    """
    # Create a border at both screen edges equal to the width of an alien
    available_space_x = ai_settings.screen_width - 2 * alien_width
    logger.debug('Available Screen X Space: {}'.format(available_space_x))

    # Space between each alien is equal to the width of an alien
    number_aliens_x = int(available_space_x / (2 * alien_width))
    logger.info('Number of Aliens per Row: {}'.format(number_aliens_x))

    return number_aliens_x


def get_number_of_rows(ai_settings, ship_height, alien_height):
    """
    Determine the number of rows of aliens that fit on the screen
    """
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    logger.debug('Available Screen Y Space: {}'.format(available_space_y))

    number_of_rows = int(available_space_y / (2 * alien_height))
    logger.info('Number of Alien Rows: {}'.format(number_of_rows))

    return number_of_rows


def create_alien(ai_game, alien_number, row_number, col_number):
    """
    Create and alien and place it in a row
    """
    logger.debug('Alien {:3} - C: {:5} R: {:5} - Creating'.format(alien_number, col_number, row_number))

    alien = Alien(ai_game.settings, ai_game.screen, alien_number)

    # Set alien's x & y coordinates
    alien.x = alien.rect.width + 2 * alien.rect.width * col_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number + 25

    logger.debug(alien.debug_info('Starting Position'))

    # Add the new alien to the group of aliens
    ai_game.aliens.add(alien)


def create_fleet(ai_game):
    """
    Create a full fleet of aliens
    """
    # Create an alien and find the number of aliens in a row
    alien_number = 0

    alien = Alien(ai_game.settings, ai_game.screen)
    number_aliens_x = get_number_aliens_x(ai_game.settings, alien.rect.width)
    number_rows = get_number_of_rows(ai_game.settings, ai_game.ship.rect.height, alien.rect.height)

    # Create the first row of aliens
    for row_number in range(number_rows):
        for col_number in range(number_aliens_x):
            create_alien(ai_game, alien_number, row_number, col_number)
            alien_number += 1


def check_fleet_edges(ai_game):
    """
    Check if any alien has reached the edge of the screen and respond
    """
    for alien in ai_game.aliens:
        if alien.check_edges():
            change_fleet_direction(ai_game)
            break


def check_fleet_bottom(ai_game):
    """
    Check if any aliens have reached the bottom of the screen
    """
    screen_rect = ai_game.screen.get_rect()
    for alien in ai_game.aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this as a ship hit
            ship_functions.ship_hit(ai_game)


def change_fleet_direction(ai_game):
    """
    Drop the fleet and change it's direction
    """
    for alien in ai_game.aliens.sprites():
        alien.rect.y += ai_game.settings.fleet_drop_speed
    ai_game.settings.fleet_direction *= -1


def update_aliens(ai_game):
    """
    Check if the fleet is at the edge and update the position of the fleet
    """
    check_fleet_edges(ai_game)
    check_fleet_bottom(ai_game)
    ai_game.aliens.update()

    # check for alien-ship collisions
    if pygame.sprite.spritecollideany(ai_game.ship, ai_game.aliens):
        ship_functions.ship_hit(ai_game)
