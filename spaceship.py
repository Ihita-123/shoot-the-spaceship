import pgzrun
import random

WIDTH=600
HEIGHT= 500

spaceship=Actor("spaceship")
spaceship.x= 200
spaceship.y=300

def draw():
    screen.fill("Black")
    spaceship.draw()

def on_mouse_down(pos):
    if spaceship.collidepoint(pos):
        print("You shot thhe spaceship!")
        spaceship.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
    else:
        print("Try again, you missed")

pgzrun.go()