from sprite_data import *
import pygame
import os

def check_file_exist(file_name : str = "") -> str:
    # find the file path in the user desktop
    if file_name:
        for root, dirs, files in os.walk("C:\\Users\\GIGABYTE\\OneDrive\\Desktop"):
            for name in files:
                if name == file_name:
                    return os.path.abspath(os.path.join(root, name))
            for directory in dirs:
                if directory == file_name:
                    return os.path.abspath(os.path.join(root, directory))                    
    return ""

pygame.init()

if not (sprite := check_file_exist("flappy_bird_sprite.png")):
    pygame.quit()
    exit()

pg_sprite_sheet = pygame.image.load(sprite)
def get_image(x, y, width, height, rotate : float = 0, scale : float = SCALE):
    sheet = pg_sprite_sheet
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (x, y, width, height))
    image = pygame.transform.rotozoom(image, rotate, scale)
    image.set_colorkey(Black)
        
    return image



screen = pygame.display.set_mode((500, 500))
screen.fill("BLack")

clock = pygame.time.Clock()

bird = get_image(*sprite_data["blue_bird_1"], scale= 10)
bird_rect = bird.get_rect(center= (SCREEN_WIDTH / 2 * SCALE, SCREEN_HEIGHT / 2 * SCALE))
screen.fill("White")    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(bird, bird_rect)
            
    pygame.display.update()
    clock.tick(60)
