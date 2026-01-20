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

#creating variables within the game
score = 0
message = "Catch the fly!"

#fly (game character/actor)
fly = Actor("cartoon_fly")

#positioning the actor at a random position
fly.x = random.randint(50,950)
fly.y = random.randint(50,550)

#draw the screen using a system function
def draw():
    screen.fill("orange")
    
    #displaying actor on the screen
    fly.draw()
    
    #displaying text on the screen
    screen.draw.text(message,center = (WIDTH/2,50),color = "black",fontsize = 40)
    screen.draw.text(f"Score: {score}",topright = (900,40),color = "black",fontsize = 40)

#detects when the user clicks and where
def on_mouse_down(pos):
    #using global variable message
    global message, score

    #checking if clicked on fly
    if fly.collidepoint(pos):
        fly.x = random.randint(50,950)
        fly.y = random.randint(50,550)
        message = "You got me!"
        score += 1
    
    else:
        message = "Good luck next time!"

#instruction to keep the screen running
pgzrun.go()
