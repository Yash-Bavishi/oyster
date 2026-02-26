from abc import abstractmethod
import pygame


class MapGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.group_name = "MapGroup"


class Map(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load(
            r"C:\Users\Yash\Documents\Projects\Oyster-proto\assets" +
            r"\background-image.jpg")
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (1920, 1080))
        self.rect = self.image.get_rect()
        self.rect.center = 1920//2, 1080//2
        # pygame.draw.rect(self.image, (255, 224, 19), self.rect, 1)