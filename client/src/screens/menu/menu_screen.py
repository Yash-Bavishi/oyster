import logging
import pygame
from client.src.screens.iscreen import IScreen
import client.src.game as game
from client.src.screens.menu.offline import Offline

logger = logging.getLogger(__name__)


class MenuScreen(IScreen):

    @property
    def name(self):
        return "Menu Screen"

    def __init__(self, screen, clock):
        pygame.init()
        self.on_screen = True
        self.screen = screen
        self.clock = clock
        self.fade_speed = 200
        self.screen_w, self.screen_h = self.screen.get_size()

        self.offline_font = pygame.font.SysFont("playbill", 150)
        self.offline_font_rdr = self.offline_font.render(
            "Play Offline", False, (0, 224, 0)
        )

        self.multiplayer_font = pygame.font.SysFont("playbill", 150)
        self.multiplayer_font_rdr = self.multiplayer_font.render(
            "Play Multiplayer", False, (0, 224, 0)
        )

        self.main_font = pygame.font.Font(
            r"C:\Users\Yash\Documents\Projects\Oyster-proto\assets\tiny5.ttf", 400
        )
        self.main_font_rdr = self.main_font.render("Main Menu", False, (0, 224, 0))
        self.text_rect = self.main_font_rdr.get_rect(
            center=(self.screen_w // 2, self.screen_h // 2 - 200)
        )

        self.offline_rect = self.offline_font_rdr.get_rect(
            center=(self.screen_w // 2 - 350, self.screen_h // 2 - 200 + 300)
        )

        self.multiplayer_rect = self.multiplayer_font_rdr.get_rect(
            center=(self.screen_w // 2 - 350, self.screen_h // 2 - 200 + 500)
        )

        self.current_selection = self.offline_font_rdr
        self.selected_rect = self.offline_rect

    def start(self):
        while self.on_screen:
            dt = self.clock.tick(60) / 1000
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if (
                        event.key == pygame.K_DOWN
                        or event.key == pygame.K_UP
                        or event.key == pygame.K_s
                        or event.key == pygame.K_w
                    ):
                        if self.current_selection == self.offline_font_rdr:
                            self.current_selection = self.multiplayer_font_rdr
                            self.selected_rect = self.multiplayer_rect
                        else:
                            self.current_selection = self.offline_font_rdr
                            self.selected_rect = self.offline_rect
                    if event.key == pygame.K_f:
                        if self.current_selection == self.offline_font_rdr:
                            logger.info("Moving to offline screen")
                            self.on_screen = False
                            # pygame.quit()
                            game.Engine.screen_stack.append(
                                Offline(self.screen, self.clock)
                            )

            if self.current_selection == self.offline_font_rdr:
                self.multiplayer_font_rdr.fill((255, 255, 255))
                self.multiplayer_font_rdr = self.multiplayer_font.render(
                    "Play Multiplayer", False, (0, 224, 0)
                )
            elif self.current_selection == self.multiplayer_font_rdr:
                self.offline_font_rdr.fill((255, 255, 255))
                self.offline_font_rdr = self.offline_font.render(
                    "Play Offline", False, (0, 224, 0)
                )

            pygame.draw.rect(
                self.current_selection,
                (224, 222, 22),
                self.current_selection.get_rect(),
                1,
            )
            self.screen.blit(self.main_font_rdr, self.text_rect)
            self.screen.blit(self.offline_font_rdr, self.offline_rect)
            self.screen.blit(self.multiplayer_font_rdr, self.multiplayer_rect)
            # pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)
