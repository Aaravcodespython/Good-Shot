#shifting the window to the left top corner of the screen
import os

#changing screen coordinate
os.environ["SDL_VIDEO_WINDOW_POS"] = f"{50},{80}"
import pgzrun
import random

#setting window width and window height
WIDTH = 1000
HEIGHT = 600
#the constants dont modify while the code is running

#fly (game character/actor)
fly = Actor("cartoon_fly")

#positioning the actor at a random position
fly.x = random.randint(50,950)
fly.y = random.randint(50,550)
#draw the screen using a system function
def draw():
    screen.fill("green")
    #displaying actor on the screen
    fly.draw()
#instruction to keep the screen running

pgzrun.go()