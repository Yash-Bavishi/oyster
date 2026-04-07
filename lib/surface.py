import pygame


class Surface(pygame.Surface):
    def __init__(self, x, y, w, h, flags) -> None:
        super().__init__((w, h), flags)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.flags = flags
