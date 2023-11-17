import pygame
import math
import time
from game import user

#Initialize Pygame
pygame.init()

#Loading Images
GRASS = pygame.image.load("assets/imgs/grass.jpg")
TRACK = pygame.image.load("assets/imgs/track.png")

TRACK_BORDER = pygame.image.load("assests/imgs/track-border.png")
FINISH = pygame.image.load("assets/imgs/finish.png")

RED_CAR = pygame.image.load("assets/imgs/red-car.png")
GREEN_CAR = pygame.image.load("assets/imgs/green-car.png")

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_hieght()


#Make Framerate
clock = pygame.time.Clock()
FPS = 60

#colors
RED =  (255, 0, 0)
GREEN =  (0, 255, 0)
WHITE =  (255, 255, 255)
BLACK = (0, 0, 0)

#making a game window
screen = pygame.display.set_mode(( WIDTH , HEIGHT ))
pygame.display.set_caption("GUI_Project")

#GAME LOOP
run = True

while run:
    
    #FRAMERATE
    clock.tick(FPS)

    screen.blit(GRASS (0, 0))

    #UPDATE THE SCREEN
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Update Display
    pygame.display.update()

#should run after run is false (Close game)
pygame.quit()