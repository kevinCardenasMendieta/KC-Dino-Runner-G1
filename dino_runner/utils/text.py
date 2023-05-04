import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT , SCREEN_WIDTH


FRONT_COLOR = (0, 0, 0)
FRONT_SIZE = 30
FRONT_STYLE = "freesansbold.ttf"


def draw_message(
    message,
    screen,
    font_color=FRONT_COLOR,
    font_size=FRONT_SIZE,
    pos_y_center=SCREEN_HEIGHT // 2,
    pos_x_center=SCREEN_WIDTH // 2
):
   font = pygame.font.Font(FRONT_STYLE, font_size)
   text = font.render(message, True, font_color)
   text_rect = text.get_rect()
   text_rect.center = (pos_x_center, pos_y_center)
   screen.blit(text, text_rect)