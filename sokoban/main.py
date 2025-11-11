from .gameengine import GameEngine

if __name__ == "__main__":
    files = [
        'levels/level1.txt',
        'levels/level2.txt',
        'levels/level3.txt',
        'levels/level4.txt',
        'levels/level5.txt'
    ]
    engine = GameEngine(files)
    engine.run()