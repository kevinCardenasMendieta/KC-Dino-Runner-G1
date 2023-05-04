import pygame
import os

pygame.init()
pygame.mixer.init()

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))
DINO_START = pygame.image.load(os.path.join(IMG_DIR, "Dino/c0.png"))
RESET = pygame.image.load(os.path.join(IMG_DIR, "Dino/c11.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/c1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/c2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/c6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/c7.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/c14.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/c14.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/c4.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/c8.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/c14.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/c3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/c3.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/c3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/c3.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/c14.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/c14.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/c12.png')) 

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
POPE =  pygame.mixer.Sound(os.path.join(IMG_DIR, 'Dino/pope.mp3'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
