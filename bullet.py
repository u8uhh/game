import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create rect for bullet y (0, 0) add right position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # save bullet possitions
        self.y = float(self.rect.y)

    def update(self):
        """Посунути кулю нагору екраном"""
        # upgrade 10 bullet position
        self.y -= self.settings.bullet_speed
        # upgrade rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on background"""
        pygame.draw.rect(self.screen, self.color, self.rect)