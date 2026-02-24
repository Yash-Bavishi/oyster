import logging
import pygame
from client.src.screens.iscreen import IScreen
from client.src.screens.welcome_screen import WelcomeScreen
import sys

logger = logging.getLogger(__name__)


class Engine:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, display=1)
    clock = pygame.time.Clock()
    screen_stack: list[IScreen] = []
    running = False

    @staticmethod
    def start():
        Engine.screen_stack.append(WelcomeScreen(Engine.screen, Engine.clock))
        Engine.running = True

    @staticmethod
    def run():
        while Engine.running:
            if not Engine.screen_stack:
                logger.error("Not screen found to run.. Exiting the code.")
                sys.exit(1)

            logger.info("Commencing Engine in 1.. 2.. and 3..")
            current_screen = Engine.screen_stack[0]
            Engine.screen_stack.pop()
            logger.info(f"Starting {current_screen.name}")
            current_screen.start()
