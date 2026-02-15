import logging
import pygame

logger = logging.getLogger(__name__)


class WelcomeScreen:
    def __init__(self, screen, clock):
        logger.info("Initializing Welcome Screen")
        self.on_screen = True
        self.clock = clock
        self.screen = screen
        self.oyster_alpha = 0
        self.in_dev_alpha = 0
        self.credit_alpha = 0
        self.fade_speed = 200

        self.screen_w, self.screen_h = self.screen.get_size()
        pygame.init()

    def start(self):
        while self.on_screen:
            dt = self.clock.tick(60) / 1000
            if self.oyster_alpha < 255:
                self.oyster_alpha += self.fade_speed * dt
                self.oyster_alpha = min(self.oyster_alpha, 255)
            # 2️⃣ Fade in "In-Development" AFTER Oyster fully visible
            elif self.in_dev_alpha < 255:
                self.in_dev_alpha += self.fade_speed * dt
                self.in_dev_alpha = min(self.in_dev_alpha, 255)
            # 3️⃣ Fade in Credit AFTER In-Development
            elif self.credit_alpha < 255:
                self.credit_alpha += self.fade_speed * dt
                self.credit_alpha = min(self.credit_alpha, 255)
            oyster_font = pygame.font.Font(
                r"C:\Users\Yash\Documents\Projects\Oyster-proto\assets\tiny5.ttf", 400
            )
            oyster_rdr = oyster_font.render("Oyster", False, (0, 224, 0))
            oyster_rdr.set_alpha(int(self.oyster_alpha))
            text_rect = oyster_rdr.get_rect(
                center=(self.screen_w // 2, self.screen_h // 2 - 200)
            )

            in_dev_font = pygame.font.SysFont("playbill", 150)
            in_dev_rd = in_dev_font.render("In-Development", False, (0, 224, 0))
            in_dev_rd.set_alpha(int(self.in_dev_alpha))
            in_dev_rect = in_dev_rd.get_rect(
                center=(self.screen_w // 2 - 300, self.screen_h // 2 + 55)
            )

            credit_font = pygame.font.SysFont("playbill", 50)
            credit_rdr = credit_font.render(
                "Thank You - Mihir, Darren, Glen and Vedita", False, (0, 224, 0)
            )
            credit_rdr.set_alpha(int(self.credit_alpha))
            margin = 20
            credit_rect = credit_rdr.get_rect(
                bottomleft=(margin, self.screen_h - margin)
            )

            # Draw to screen
            self.screen.fill((255, 255, 255))
            self.screen.blit(oyster_rdr, text_rect)
            self.screen.blit(in_dev_rd, in_dev_rect)
            self.screen.blit(credit_rdr, credit_rect)
            pygame.display.update()
            pygame.display.flip()
            if self.credit_alpha == 255:
                logging.info("Loading game sequence complete")
                self.on_screen = False
            self.clock.tick(60)
