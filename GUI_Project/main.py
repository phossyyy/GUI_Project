import pygame
import math
import time
from Utilities import scale_image, blit_rotate_center

#Initialize Pygame
pygame.init()

pygame.mixer.music.load('GUI_Project/assets/daisy.mp3')
pygame.mixer.music.play(-1)


#Loading Images
GRASS = scale_image(pygame.image.load("GUI_Project/assets/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("GUI_Project/assets/track.png"), 0.75)

TRACK_BORDER = scale_image(pygame.image.load("GUI_Project/assets/track-border.png"), 0.75)
FINISH = pygame.image.load("GUI_Project/assets/finish.png")

RED_CAR = scale_image(pygame.image.load("GUI_Project/assets/red-car.png"), 0.3)
GREEN_CAR = scale_image(pygame.image.load("GUI_Project/assets/green-car.png"), 0.3)

# Assuming TRACK_BORDER is the surface of the track border
track_border_mask = pygame.mask.from_surface(TRACK_BORDER)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()

class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.max_vel = max_vel
        self.img = self.IMG
        self.vel  = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.acceleration = 0.01
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
        self.move(track_border_mask)

    def move(self, track_mask):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        new_y = self.y - vertical
        new_x = self.x - horizontal

        car_mask = pygame.mask.from_surface(self.img)
        car_rect = self.img.get_rect(topleft=(new_x, new_y))
        offset = (int(car_rect.x), int(car_rect.y))
        collision_point = track_mask.overlap(car_mask, offset)

        if collision_point is None:
            self.y = new_y
            self.x = new_x
        else:
            # If collision, stop the car (set velocity to 0)
            self.vel = 0

    def reduce_speed(self, track_mask):
        self.vel = max(self.vel - self.acceleration/2, 0)
        self.move(track_mask)
        
        # # Check for border collision
        # if 0 <= new_x <= WIDTH - self.img.get_width() and 0 <= new_y <= HEIGHT - self.img.get_height():
        #     self.y = new_y
        #     self.x = new_x
        # else:
        #     # If collision, stop the car (set velocity to 0)
        #     self.vel = 0
        


class PlayerCar(AbstractCar): 
    IMG = RED_CAR
    START_POS = (120 , 200)

class PlayerCar_2(AbstractCar): 
    IMG = GREEN_CAR
    START_POS = (160 , 200)

    
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
def draw(Screen, images, player_car, player_2_car):
    for img, pos in images:
        Screen.blit(img, pos)

    player_car.draw(screen)
    player_car_2.draw(screen)
    pygame.display.update()

images = [(GRASS, (0, 0)), (TRACK, (0,0))]
player_car = PlayerCar (5, 5)
player_car_2 = PlayerCar_2 (5, 2)

#GAME LOOP
run = True

while run:
    
    #FRAMERATE
    clock.tick(FPS)

    draw(screen, images, player_car, player_car_2)
    #UPDATE THE SCREEN

    # Pass the track border mask to the move method
    player_car.move(track_border_mask)
    player_car_2.move(track_border_mask)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    moved = False
    moved2 = False

    if key[pygame.K_a]:
        player_car.rotate(left = True)
    if key[pygame.K_d]:
        player_car.rotate(right = True)
    if key[pygame.K_w]:
        moved = True
        player_car.move_foward()

    if key[pygame.K_LEFT]:
        player_car_2.rotate(left = True)
    if key[pygame.K_RIGHT]:
        player_car_2.rotate(right = True)
    if key[pygame.K_UP]:
        moved2 = True
        player_car_2.move_foward()

    if not moved:
        player_car.reduce_speed(track_border_mask)
    if not moved2:
        player_car_2.reduce_speed(track_border_mask)
    

    #Update Display
    pygame.display.update()

#should run after run is false (Close game)
pygame.quit()
