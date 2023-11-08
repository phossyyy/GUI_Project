import pygame
from game import user

#Initialize Pygame
pygame.init()

#Make Framerate
clock = pygame.time.Clock()
FPS = 60

#colors
RED =  (255, 0, 0)
GREEN =  (0, 255, 0)
WHITE =  (255, 255, 255)
BLACK = (0, 0, 0)

#making a game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("GUI_Project")

#GAME LOOP
run = True

while run:
    
    #FRAMERATE
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Update Display
    pygame.display.update()

#should run after run is false (Close game)
pygame.quit()