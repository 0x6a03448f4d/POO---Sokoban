class InvalidElementException(Exception):
    def __init__(self, filename, line_number, char):
        super().__init__(f"Invalid element '{char}' in file '{filename}', line {line_number}")

class LineTooLongException(Exception):
    def __init__(self, filename, line_number):
        super().__init__(f"Too many elements on line {line_number} in file '{filename}'")

class LineTooShortException(Exception):
    def __init__(self, filename, line_number):
        super().__init__(f"Too few elements on line {line_number} in file '{filename}'")

class MissingRequiredElementsException(Exception):
    def __init__(self, filename, missing):
        super().__init__(f"Missing required elements {missing} in file '{filename}'")

class BoxSlotCountMismatchException(Exception):
    def __init__(self, filename):
        super().__init__(f"Box and Box Slot element counts do not match in '{filename}'")