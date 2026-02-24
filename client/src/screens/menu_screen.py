import logging
import pygame
from client.src.screens.iscreen import IScreen

logger = logging.getLogger(__name__)


class MenuScreen(IScreen):

    @property
    def name(self):
        return "Menu Screen"
    
    def __init__(self, screen, clock):
        self.on_screen = True
        self.oyster_alpha = 0
        self.screen = screen
        self.clock = clock
        self.fade_speed = 200
        self.screen_w, self.screen_h = self.screen.get_size()
        pygame.init()

    def start(self):
        while self.on_screen:
            dt = self.clock.tick(60) / 1000
            if self.oyster_alpha < 255:
                self.oyster_alpha += self.fade_speed * dt
                self.oyster_alpha = min(self.oyster_alpha, 255)

            oyster_font = pygame.font.Font(
                r"C:\Users\Yash\Documents\Projects\Oyster-proto\assets\tiny5.ttf", 400
            )
            oyster_rdr = oyster_font.render("Oyster", False, (0, 224, 0))
            oyster_rdr.set_alpha(int(self.oyster_alpha))
            text_rect = oyster_rdr.get_rect(
                center=(self.screen_w // 2, self.screen_h // 2 - 200)
            )

            self.screen.fill((255, 255, 255))
            self.screen.blit(oyster_rdr, text_rect)

            pygame.display.update()
            pygame.display.flip()
            if self.oyster_alpha == 255:
                logging.info("Menu loading completed awaiting instructions")
            self.clock.tick(60)