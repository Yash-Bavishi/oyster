import pygame
import constants
from graphics.src.maps.imap import IMap


class MapGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.group_name = "MapGroup"


class Map(IMap, pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load(constants.ASSETS[self.name])
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (1920, 1080))
        self.rect = self.image.get_rect()
        self.rect.center = 1920 // 2, 1080 // 2

    @property
    def gravity(self) -> int:
        return 1

    @property
    def name(self) -> str:
        return "ocean"
