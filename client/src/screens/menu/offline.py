import logging
import pygame
from client.src.screens.iscreen import IScreen
from graphics.src.maps.map import Map, MapGroup

logger = logging.getLogger(__name__)


class Offline(IScreen):

    @property
    def name(self):
        return "Offline"

    def __init__(self, screen, clock):
        self.on_screen = True
        self.screen = screen
        self.clock = clock
        self.screen_w, self.screen_h = self.screen.get_size()
        self.group = MapGroup()
        self.map = Map(self.group)
        pygame.init()

    def start(self):
        while self.on_screen:
            dt = self.clock.tick(60) / 1000
            self.main_font = pygame.font.Font(
                r"C:\Users\Yash\Documents\Projects\Oyster-proto\assets\tiny5.ttf", 400
            )
            self.main_font_rdr = self.main_font.render("Offline", False, (0, 224, 0))
            self.text_rect = self.main_font_rdr.get_rect(
                center=(self.screen_w // 2, self.screen_h // 2 - 200)
            )

            self.screen.blit(self.main_font_rdr, self.text_rect)
            self.group.draw(self.screen)
            self.group.update(dt)
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)
