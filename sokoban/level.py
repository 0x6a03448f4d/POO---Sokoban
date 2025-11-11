import pygame
from .objects import *
from collections import defaultdict

class Level:
    """Represents a level/grid, manages objects and movement."""
    GRID_SIZE = 10

    def __init__(self, grid, image_collection):
        self.grid = grid
        self.image_collection = image_collection
        self.sprite_group = pygame.sprite.Group()
        self.boxes = []
        self.slots = []
        self.obstacles = []
        self.empty_spaces = []
        self.player = None
        self.load_objects()

    def load_objects(self):
        for y, row in enumerate(self.grid):
            for x, el in enumerate(row):
                if el == 'p':
                    self.player = Player(x, y,
                                         self.image_collection.player_right,
                                         self.image_collection.player_left)
                    self.sprite_group.add(self.player)
                elif el == 'o':
                    obj = Obstacle(x, y, self.image_collection.obstacle)
                    self.obstacles.append(obj)
                    self.sprite_group.add(obj)
                elif el == 'b':
                    obj = Box(x, y, self.image_collection.box)
                    self.boxes.append(obj)
                    self.sprite_group.add(obj)
                elif el == 's':
                    obj = Slot(x, y, self.image_collection.slot)
                    self.slots.append(obj)
                    self.sprite_group.add(obj)
                elif el == '_':
                    obj = Empty(x, y, self.image_collection.empty)
                    self.empty_spaces.append(obj)
                    self.sprite_group.add(obj)

    def draw(self, display):
        # Draw all except slots if player/box is over them
        for sprite in self.sprite_group:
            # Hide slot under player/box
            if isinstance(sprite, Slot):
                if any(
                    (box.x == sprite.x and box.y == sprite.y) for box in self.boxes
                ) or (self.player.x == sprite.x and self.player.y == sprite.y):
                    continue
            display.blit(sprite.image, sprite.rect.topleft)

    def move_player(self, dx, dy):
        """Attempts to move the player. Handles box pushing."""
        nx, ny = self.player.x + dx, self.player.y + dy
        if nx < 0 or ny < 0 or nx >= self.GRID_SIZE or ny >= self.GRID_SIZE:
            return False  # Out of grid
        # Check collision with obstacle
        if any(o.x == nx and o.y == ny for o in self.obstacles):
            return False
        # Check box
        box = next((b for b in self.boxes if b.x == nx and b.y == ny), None)
        if box:
            bx, by = box.x + dx, box.y + dy
            # Can box move?
            if (bx < 0 or by < 0 or bx >= self.GRID_SIZE or by >= self.GRID_SIZE):
                return False
            if any(o.x == bx and o.y == by for o in self.obstacles):
                return False
            if any(b2.x == bx and b2.y == by for b2 in self.boxes):
                return False
            # Move box
            box.x, box.y = bx, by
            box.rect.topleft = (bx*50, by*50)
        # Move player
        self.player.x, self.player.y = nx, ny
        self.player.rect.topleft = (nx*50, ny*50)
        self.player.facing_right = dx > 0
        self.player.update_image()
        return True

    def is_complete(self):
        # All boxes are over slots
        slot_positions = {(s.x, s.y) for s in self.slots}
        return all((b.x, b.y) in slot_positions for b in self.boxes)

    def reset(self):
        self.sprite_group.empty()
        self.boxes = []
        self.slots = []
        self.obstacles = []
        self.empty_spaces = []
        self.player = None
        self.load_objects()