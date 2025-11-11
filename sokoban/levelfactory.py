from .exceptions import *
from .level import Level

class LevelFactory:
    """Loads and validates level files, builds Level objects."""
    VALID_ELEMENTS = {'p', 'o', 'b', 's', '_'}
    GRID_SIZE = 10

    @staticmethod
    def load_level(filename, image_collection):
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        player_count = box_count = slot_count = 0
        grid = []

        for idx, line in enumerate(lines):
            line_chars = list(line)
            # Too many elements
            if len(line_chars) > LevelFactory.GRID_SIZE:
                print(LineTooLongException(filename, idx+1))
                line_chars = line_chars[:LevelFactory.GRID_SIZE]
            # Too few elements
            if len(line_chars) < LevelFactory.GRID_SIZE:
                print(LineTooShortException(filename, idx+1))
                line_chars += ['_'] * (LevelFactory.GRID_SIZE - len(line_chars))

            for j, el in enumerate(line_chars):
                if el not in LevelFactory.VALID_ELEMENTS:
                    raise InvalidElementException(filename, idx+1, el)
                if el == 'p': player_count += 1
                elif el == 'b': box_count += 1
                elif el == 's': slot_count += 1
            grid.append(line_chars)

        missing = []
        if player_count == 0: missing.append('player')
        if box_count == 0: missing.append('box')
        if slot_count == 0: missing.append('box slot')
        if missing:
            raise MissingRequiredElementsException(filename, missing)
        if box_count != slot_count:
            raise BoxSlotCountMismatchException(filename)

        # Return a Level object
        return Level(grid, image_collection)