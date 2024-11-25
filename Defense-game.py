import simpleGE, pygame, random

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage = "Star-space.jpg"

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()