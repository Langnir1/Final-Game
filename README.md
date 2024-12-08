Final Game Document
----------------------
Overview / idea

   The player needs to defend a planet from incoming asteroids. The asteroids approach from all sides and if they hit the planet, game over.
   Using a mouse, the player needs to move click in the general direction of an asteroid to launch a lazer. If the lazer hits the asteroid, it is destroyed as long as the asteroid is weaker then the lazer.
   Should the astroid be of higher "level", it will require more shots to destroy. 
   The asteroids will approach at different speeds and sizes and some (future idea) might split when destroyed.
   Once the intial gameplay of shooting and destroying asteroids is complete, ideas for special asteroids and powerups can be considered.
---------------------
Import simpleGE and Random

Main
 * calls the game class

Updated method:
 * Use keepGoing = True
 * set score to 0
 * While keepGoing, run instructions
    * if response == "Play", start game
    * else, keepGoing = False     
----------------------
Class Game
* call simpleGE (parameter)
* call self using def __init__(self)
* Set background to Star_Space.png
* Create self variables that get the sprite
   * planet, asteroids, laser, labelScore
* Sound effects
   * laserShoot and explosion
* If mouse is is clicked (using pygame.mouse)
   * Fire laser
   * Play laser sound effect
* If asteroid collides with planet, STOP GAME
* If laser collides with asteroid, Asteroids.reset()
   * Play explosion sound effect 
   * score +1
   * Update labelScore text
   * reset asteroid
   * hide laser

* buttonQuit = simpleGE.Button()
   * Position, top right of screen
   * Img: hopefully a red box with an X
   * When clicked, game.Stop() 
------------------------
Class planet
 * call simpleGE (paremeter)
 * call planet image
 * set position and size

* future ideas involve a rotating planet or an image that moves to shoot the asteroids   
------------------------
Class Asteroids

This class is for the asteroids and creates, checks, and positions them.
 * call simpleGE (parameter)
 * setSize
   
 * Create reset method
    * creates asteroids at a random point on the outside of the screen
    * Variable location gets spawn direction (north, south, east, west)
    * Asteroids move towards center/planet location
       * Utilize moveAngle and dirTo
    * Set Speed to 1
|Once gameplay is working, add a large asteroid that requires multiple shots|
----------------------------
Class Laser(simpleGE.Scene)
def __init__(self):
   * Initialize and create laser
   * hide laser
def fire(self):
   * show laser
   * set position to planet location/center of screen
   * Utilize moveAngle and set dirTo towards mouse position
   * Set speed to 10
---------------------------
Class labelScore()

* text "score = 0"
* Position to top middle of screen
-----------------------
Class Instructions():
   def __init__(self, score):
      * variable response = "Play"
      * create a multiLabel called instructions and input needed text
      * create lastScore which gets score
      * create labelScore which shows what the previous socre is
      * Create two buttons
         * One labled "Play" the other "Quit"
         * When the respective button is clicked, Close game or start game
