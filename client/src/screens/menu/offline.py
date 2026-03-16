import logging
import pygame
from client.src.screens.iscreen import IScreen
from graphics.src.maps.map import Map, MapGroup
from graphics.src.player.player import Player

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
        self.player = Player(self.group)
        self.group.add(self.player)
        pygame.init()

    def apply_gravity(self):
        self.player.rect.y = self.player.rect.y + 1
        self.player.is_air = True
        # self.v2.rect.y = self.v2.rect.y + self.m1.gravity
        if self.player.rect.y < 0 or self.player.rect.y > self.screen_h:
            # print(self.player.rect.x, self.player.rect.y)
            # maintain position
            # Remove 0.5 in future
            self.player.rect.y = self.player.rect.y - 1
            pass

    def start(self):
        while self.on_screen:
            dt = self.clock.tick(60) / 1000
            self.screen.fill((0, 0, 0, 0))
            self.main_font = pygame.font.Font(
                r"C:\Users\Yash\Documents\Projects\Oyster-proto\assets\tiny5.ttf", 400
            )
            self.main_font_rdr = self.main_font.render(
                "Offline", 
                False, 
                (0, 224, 0))
            self.text_rect = self.main_font_rdr.get_rect(
                center=(self.screen_w // 2, self.screen_h // 2 - 200)
            )

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.map.switch_off_overlays()

            self.screen.blit(self.main_font_rdr, self.text_rect)
            self.group.draw(self.screen)
            self.group.update(dt)
            self.apply_gravity()
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)
