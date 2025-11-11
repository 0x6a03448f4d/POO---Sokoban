import pygame

class ImageCollection:
    """Loads and stores images for all game elements."""
    def __init__(self):
        self.player_right = pygame.transform.scale(
            pygame.image.load('images/player_right.png'), (50, 50))
        self.player_left = pygame.transform.scale(
            pygame.image.load('images/player_left.png'), (50, 50))
        self.obstacle = pygame.transform.scale(
            pygame.image.load('images/obstacle.png'), (50, 50))
        self.box = pygame.transform.scale(
            pygame.image.load('images/box.png'), (50, 50))
        self.slot = pygame.transform.scale(
            pygame.image.load('images/slot.png'), (50, 50))
        self.empty = pygame.Surface((50, 50))
        self.empty.fill((255,255,255))
