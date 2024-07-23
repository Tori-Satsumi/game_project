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


screen = pygame.display.set_mode((500, 500))
screen.fill("BLack")



clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.fill("BLack")    
    
    
    pygame.display.update()
    clock.tick(60)
