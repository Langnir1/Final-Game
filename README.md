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
------------------------
Class planet
 * call simpleGE (paremeter)
------------------------
Class Asteroids

This class is for the asteroids and creates, checks, and positions them.
 * call simpleGE (parameter)
