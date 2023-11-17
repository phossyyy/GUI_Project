import pygame

#SCALING IMAGES
def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

#ROTATING IMAGES

def blit_rotate_center(screen, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect (topleft = top_left).center)
    screen.blit(rotated_image, new_rect.topleft)