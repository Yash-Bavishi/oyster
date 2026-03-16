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
        self.show_alpha = True
        self.alpha = 124
        self.platforms()
    
    def switch_off_overlays(self):
        if self.show_alpha:
            print("showing")
            self.alpha = 0
            self.show_alpha = False
        else:
            print("not showing")
            self.alpha = 124
            self.show_alpha = True
        self.platforms()
    
    def platforms(self):
        rect_surface = pygame.Surface((702, 134), pygame.SRCALPHA)
        rect_surface.fill((255, 0, 0, self.alpha))
        self.image = pygame.image.load(constants.ASSETS[self.name])
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (1920, 1080))
        self.image.blit(rect_surface, (1211, 125))

    @property
    def gravity(self) -> int:
        return 1

    @property
    def name(self) -> str:
        return "ocena"
