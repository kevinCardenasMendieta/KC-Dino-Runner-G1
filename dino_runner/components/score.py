import pygame

class Score:
    def __init__(self):
        self.score = 0

    def update(self, game):
        self.score +=1
        if self.score % 100 == 0:
            game.game_speed +=2

    def draw(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 22)
        tex = font.render(f"Score: {self.score}", True, (0, 0, 0))
        tex_rect = tex.get_rect()
        tex_rect.center = (1000, 50)
        screen.blit(tex, tex_rect)