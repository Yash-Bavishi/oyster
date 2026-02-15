import pygame

from client.src.screens.welcome_screen import WelcomeScreen


class Engine:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    @staticmethod
    def start():
        WelcomeScreen(Engine.screen, Engine.clock).start()

    pass
