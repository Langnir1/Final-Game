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
----------------------
Class Game
 * call simpleGE (parameter)
 * call self using def __init__(self)
 * Set background to space (or solid color if no img is found yet)
 * Create self variables that get the sprite
    * planet, asteroids,
* If laser collides with asteroid, Asteroids.reset()
   * score +1
* buttonQuit = simpleGE.Button()
   * Position, top right of screen
   * Img: hopefully a red box with an X
   * When clicked, game.Stop() 
------------------------
Class planet
 * call simpleGE (paremeter)
 * Create a stationary box in the center of the screen (This will later be a planet)
    * If possible, just get a small planet img without needing to make a box.

* future ideas involve a rotating planet or an image that moves to shoot the asteroids   
------------------------
Class Asteroids

This class is for the asteroids and creates, checks, and positions them.
 * call simpleGE (parameter)
 * setSize
 * asteroid moves to center
   
 * Create reset method
    * creates asteroids at a random point on the outside of the screen
    * Random speed between two numbers
  Once gameplay is working, add a large asteroid that requires multiple shots
----------------------------
Class Laser(simpleGE.Scene)
def __init__(self):

* when mouse (for now) is clicked, send a laser from Planet in that direction.
* If laser hits asteroid, reset astroid and laser
* Laser speed is unknown but needs to be fast 
---------------------------
Class labelScore()

* text "score = 0"
* Position to top middle of screen
-----------------------
