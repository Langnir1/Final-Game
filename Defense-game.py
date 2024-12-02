import simpleGE, pygame, random

class Asteroids(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        
        self.setImage = "Layered Rock.png"
        #self.setSize = (30, 30)
        self.reset()
        
    def reset(self):
       # self.y = 0
       # self.x = random.randint(0, self.screenWidth)
       # self.dy = random.randint(3, 5)
        
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
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
      #  self.setImage = "Star-space.jpg"
        self.numAsteroid = 10
        self.asteroid = []
        for i in range(self.numAsteroid):
            self.asteroid.append(Asteroids(self))
        
        self.sprites = [self.asteroid]
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()