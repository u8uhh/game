import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """Inicializate button attribute"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # size and button character
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # create rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # повідомлення на кнопці треба показати 1 раз
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """change text to image and place on center"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw empty button after that image
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)