import pygame

import game_core
from game_logger import logger
from ship import ship_functions


def check_events(ai_game):
    """
    Respond to keyboard and mouse input
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_core.end_game(ai_game)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_mousedown_event(ai_game, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_game)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ai_game)


def check_mousedown_event(ai_game, mouse_x, mouse_y):
    """
    Check what button is pressed
    """
    if not ai_game.stats.game_active:
        if ai_game.play_button.rect.collidepoint(mouse_x, mouse_y):
            game_core.reset_match(ai_game)


def check_keydown_event(event, ai_game):
    """
    Respond to key presses
    """
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        logger.debug('Ship Right: Start')
        ai_game.ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        logger.debug('Ship Left: Start')
        ai_game.ship.moving_left = True
    elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
        logger.debug('Ship firing bullet')
        ship_functions.fire_bullet(ai_game.settings, ai_game.screen, ai_game.stats, ai_game.ship, ai_game.bullets)
    elif event.key == pygame.K_p and not ai_game.stats.game_active:
        game_core.reset_match(ai_game)
    elif event.key == pygame.K_q:
        game_core.end_game(ai_game)


def check_keyup_event(event, ai_game):
    """
    Respond to key releases
    """
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        logger.debug('Ship Right: Stop')
        ai_game.ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        logger.debug('Ship Left: Stop')
        ai_game.ship.moving_left = False
