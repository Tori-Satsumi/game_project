from sprite_data import *
import pygame

pygame.init()

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
