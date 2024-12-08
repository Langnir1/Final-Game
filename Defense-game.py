import simpleGE, pygame, random

class Laser(simpleGE.Sprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("48.png")
        self.setSize(10, 5)
        self.hide()
        
    def fire(self):
        #To fire the laser, first unhide it. Then have the laser move from the planet
        #to a different location by checking where mouse is when clicked
        self.show()
        self.position = (320,240)
        self.moveAngle = self.dirTo(pygame.mouse.get_pos())
        self.speed = 10
        
        
class Planet(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("artificialPlanet.png")
        self.setSize(50, 50)
        self.position = (320, 240)
        
class Asteroids(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Layered Rock.png")
        self.setSize(30, 30)
        self.reset()
        
    def reset(self):
        location = ["North", "South" ,"East", "West"]
        result = random.choice(location)
        print(result)
        
        if result == "North":
            self.y = 0
            self.x = random.randint(0, self.screenWidth)
            #self.dy = random.randint(1, 3)
        if result == "South":
            self.y = self.screenHeight
            self.x = random.randint(0, self.screenWidth)
            #self.dy = random.randint(-3, -1)
        if result == "East":
            self.y = random.randint(0, self.screenHeight)
            self.x = self.screenWidth
            #self.dx = random.randint(-3, -1)
        if result == "West":
            self.y = random.randint(0, self.screenHeight)
            self.x = 0
            #self.dx = random.randint(1, 3)
        
        self.moveAngle =self.dirTo((320, 240))
        self.speed = 1
        
class LabelScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score = 0"
        self.center = (100, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Star_Space.png")
        self.numAsteroid = 10
        self.asteroid = []
        self.score = 0
        
        for i in range(self.numAsteroid):
            self.asteroid.append(Asteroids(self))
        
        self.planet = Planet(self)
        
        self.numLaser = 100
        self.laser = Laser(self)
#         self.laser = []
#         for i in range(self.numLaser):
#             self.laser.append(Laser(self))
            
        self.labelScore = LabelScore()
        self.laserShoot = simpleGE.Sound("laserShoot.wav")
        self.explosion = simpleGE.Sound("explosion.wav")
        
        #self.exit = simpleGE.Button()
        #self.exit
        
        self.sprites = [self.planet,
                        self.asteroid,
                        self.laser,
                        self.labelScore]
        
    def process(self):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            self.laser.fire()
            self.laserShoot.play()
            
        for asteroid in self.asteroid:
            if self.planet.collidesWith(asteroid):
                self.stop()
                print("Game Over!")
#                asteroid.reset()
            if self.laser.collidesWith(asteroid):
                self.explosion.play()
                self.score += 1
                self.labelScore.text = (f"Score = {self.score}")
                asteroid.reset()
                self.laser.hide()

class Instructions(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        
        self.response = "Play"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
            "Welcome to Planet Defence!",
            "You have only one goal, Survive.",
            "Use the mouse to send a laser in the direction you click",
            "and keep the machine planet alive.",
            "You win once the score reaches 40,",
            "but you lose if the planet is hit once!"   
            ]
        
        self.lastScore = score
        self.labelScore = simpleGE.Label()
        self.labelScore.text = (f"Last Score = {self.lastScore}")
        self.labelScore.center = (330, 300)
    
        self.instructions.center = (320, 150)
        self.instructions.size = (600, 200)
    
        self.buttonPlay = simpleGE.Button()
        self.buttonPlay.text = "Play"
        self.buttonPlay.center = (100, 300)
        
        self.buttonQuit = simpleGE.Button()
        self.buttonQuit.text = "Quit"
        self.buttonQuit.center = (540, 300)
        
        self.sprites = [self.instructions,
                        self.labelScore,
                        self.buttonPlay,
                        self.buttonQuit]
        
#         self.sprites = [self.instructions,
#                         self.lastScore,
#                         self.buttonPlay,
#                         self.buttonQuit]
#         
    def process(self):
        if self.buttonPlay.clicked:
            self.response = "Play"
            self.stop()
        if self.buttonQuit.clicked:
            self.response = "Quit"
            self.stop()
                
def main():
    keepGoing = True
    score = 0
#    instructions = Instructions(0)
#    instructions.start()
    while keepGoing:
        instructions = Instructions(score)
        instructions.start()
         
        if instructions.response == "Play":
            game = Game()
            game.start()
            score = game.score
        else:
            keepGoing = False
    
if __name__ == "__main__":
    main()