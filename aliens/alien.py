import pygame

from pygame.sprite import Sprite
from game_logger import logger


class Alien(Sprite):
    """
    A class to represent a singe alien in the fleet
    """
    def __init__(self, ai_settings, screen, alien_number=None):
        """
        Initialize the alien and set its starting position
        """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.alien_number = alien_number

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens position as a float
        self.x = float(self.rect.x)

        logger.debug(self.debug_info('Init'))

    def debug_info(self, message=None):
        return 'Alien {:3} - X: {:5} Y: {:5} - {}'.format(str(self.alien_number), self.rect.x, self.rect.y, str(message))

    def blitme(self):
        """
        Draw the alien at its current position
        """
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """
        Return true if alien is at edge of screen
        """
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """
        Move the alien right or left
        """
        logger.debug(self.debug_info('Before Update'))
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        logger.debug(self.debug_info('After Update'))