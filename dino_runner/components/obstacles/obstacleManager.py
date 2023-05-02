import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactusBig import CactusBig
from dino_runner.utils.constants import SMALL_CACTUS , LARGE_CACTUS

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacles = random.randint(0, 1)
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS) if obstacles ==0 else CactusBig(LARGE_CACTUS ))
    
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)