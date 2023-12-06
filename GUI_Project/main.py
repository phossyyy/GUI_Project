import pygame
import math
import time
from Utilities import scale_image, blit_rotate_center

#Initialize Pygame
pygame.init()

#Loading Images
GRASS = scale_image(pygame.image.load("GUI_Project/assets/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("GUI_Project/assets/track.png"), 0.75)

TRACK_BORDER = scale_image(pygame.image.load("GUI_Project/assets/track-border.png"), 0.9)
FINISH = pygame.image.load("GUI_Project/assets/finish.png")

RED_CAR = scale_image(pygame.image.load("GUI_Project/assets/red-car.png"), 0.45)
GREEN_CAR = scale_image(pygame.image.load("GUI_Project/assets/green-car.png"), 0.45)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()

class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.max_vel = max_vel
        self.img = self.IMG
        self.vel  = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.acceleration = 0.1
        self.x, self.y = self.START_POS

    def rotate(self, left = False, right = False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    
    def draw (self, screen):
        blit_rotate_center(screen, self.img, (self.x, self.y), self.angle)

    def move_foward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        new_y = self.y - vertical
        new_x = self.x - horizontal

        # Check for border collision
        if 0 <= new_x <= WIDTH - self.img.get_width() and 0 <= new_y <= HEIGHT - self.img.get_height():
            self.y = new_y
            self.x = new_x
        else:
            # If collision, stop the car (set velocity to 0)
            self.vel = 0
        

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration/2, 0)
        self.move()

class PlayerCar(AbstractCar): 
    IMG = RED_CAR
    START_POS = (120, 180)

    
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

#Draw
def draw(Screen, images, player_car):
    for img, pos in images:
        Screen.blit(img, pos)

    player_car.draw(screen)
    pygame.display.update()

images = [(GRASS, (0, 0)), (TRACK, (0, 0))]
player_car = PlayerCar( 5, 5)

#GAME LOOP
run = True

while run:
    
    #FRAMERATE
    clock.tick(FPS)

    draw(screen, images, player_car)
    #UPDATE THE SCREEN
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    moved = False

    if key[pygame.K_a]:
        player_car.rotate(left = True)
    if key[pygame.K_d]:
        player_car.rotate(right = True)
    if key[pygame.K_w]:
        moved = True
        player_car.move_foward()
    
    if not moved:
        player_car.reduce_speed()
    

    #Update Display
    pygame.display.update()

#should run after run is false (Close game)
pygame.quit()