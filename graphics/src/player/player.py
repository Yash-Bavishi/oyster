import logging
import pygame

import constants
logger = logging.getLogger(__name__)


class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        logger.info("Initializing player")
        logger.info("Initializing sprite sheet for zoro")
        self.sheet = pygame.image.load(constants.ASSETS["zoro"])

        self.launch_frames = [
            pygame.Rect(831, 100, 67, 60),
            pygame.Rect(945, 101, 71, 57),
            pygame.Rect(1052, 102, 90, 41),
        ]

        self.idle = pygame.transform.smoothscale(
            self.sheet.subsurface(pygame.Rect(381, 17, 50, 60)),
            (60, 60)
        )
        self.in_air_frame = pygame.transform.smoothscale(
            self.sheet.subsurface(self.launch_frames[1]), (60, 60)
        )
        self.image = self.in_air_frame
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 0
        self.is_air = True
        pygame.draw.rect(self.image, (224, 22, 1), self.rect, 1)
        self.velocity_x = 0
        self.velocity_y = 0

        def draw_player(self, dt):
            self.image = self.in_air_frame
            self.rect.move_ip(self.velocity_x, self.velocity_y)

        def update(self, dt):
            self.draw_player(dt)
