
import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """Initialise button attributes"""

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Build the button's rect object and centre it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #The button message is prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn message into text and render in button"""
        self.msg_image = self.font.render(msg, True, self.text_color, 
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        #draw blank button, then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)