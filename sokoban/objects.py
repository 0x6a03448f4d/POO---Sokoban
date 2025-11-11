import pygame

class GameObject(pygame.sprite.Sprite):
    """Base class for all game objects in the grid."""
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x*50, y*50)
        self.x = x
        self.y = y

class Player(GameObject):
    def __init__(self, x, y, image_right, image_left):
        super().__init__(x, y, image_right)
        self.image_right = image_right
        self.image_left = image_left
        self.facing_right = True

    def update_image(self):
        self.image = self.image_right if self.facing_right else self.image_left

class Box(GameObject): pass

class Obstacle(GameObject): pass

class Slot(GameObject): pass

class Empty(GameObject): pass