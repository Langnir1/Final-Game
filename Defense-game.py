import simpleGE, pygame, random

class Planet(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage = ("artificialPlanet.png")
        self.position = (320, 240)
        
class Asteroids(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage = ("Layered Rock.png")
        #self.setSize = (30, 30)
        self.reset()
        
    def reset(self):
        location = ["North", "South" ,"East", "West"]
        result = random.choice(location)
        print(result)
        
        if result == "North":
            self.y = 0
            self.x = random.randint(0, self.screenWidth)
            self.dy = random.randint(1, 3)
        if result == "South":
            self.y = self.screenHeight
            self.x = random.randint(0, self.screenWidth)
            self.dy = random.randint(-3, -1)
        if result == "East":
            self.y = random.randint(0, self.screenHeight)
            self.x = self.screenWidth
            self.dx = random.randint(-3, -1)
        if result == "West":
            self.y = random.randint(0, self.screenHeight)
            self.x = 0
            self.dx = random.randint(1, 3)

class LabelScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score = 0"
        self.center = (100, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage = ("Star_Space.png")
        self.numAsteroid = 10
        self.asteroid = []
        for i in range(self.numAsteroid):
            self.asteroid.append(Asteroids(self))
        
        self.planet = Planet(self)
        self.labelScore = LabelScore()
        
        self.sprites = [self.planet,
                        self.asteroid,
                        self.labelScore]
        
    def process(self):
        for asteroid in self.asteroid:
            if self.planet.collidesWith(asteroid):
                asteroid.reset()
                
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()