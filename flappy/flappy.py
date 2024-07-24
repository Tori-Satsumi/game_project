import os
import pygame
from sys import exit
from sprite_data import *

from pygame.sprite import _Group

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
    
screen = pygame.display.set_mode((SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE))


pg_sprite_sheet = pygame.image.load(sprite)

def get_image(x, y, width, height, rotate : float = 0, scale : float = SCALE):
    sheet = pg_sprite_sheet
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (x, y, width, height))
    image = pygame.transform.rotozoom(image, rotate, scale)
    image.set_colorkey(Black)
    return image



clock = pygame.time.Clock()

pygame.display.set_caption("Flappy Bird")

bg_color = (50, 50, 50)


class BG_img(pygame.sprite.Sprite):
    def __init__(self, type, x : float = 0, y : float = 0):
        super().__init__()
        if type == "day":
            self.game_bg = get_image(x= 0, y= 0, width= SCREEN_WIDTH, height= SCREEN_HEIGHT)
        else:
            self.game_bg = get_image(x= SCREEN_WIDTH + GAP, y= 0, width= SCREEN_WIDTH, height= SCREEN_HEIGHT)
        
        self.game_bg_rect = self.game_bg.get_rect(topleft = (x, y))
        self.move_speed = 1
    
    def reposition(self):            
        if self.game_bg_rect.right <= 0:
            self.game_bg_rect.left = SCREEN_WIDTH * SCALE
            
    
    def update(self):
        self.game_bg_rect.right -= self.move_speed
        self.reposition()
        self.draw()
        
    def draw(self):
        screen.blit(self.game_bg, self.game_bg_rect)


class BG_Ground(pygame.sprite.Sprite):
    def __init__(self, x: float = 0, y: float = SCREEN_HEIGHT * SCALE):
        super().__init__()
        self.ground_img = get_image(
            x= SCREEN_WIDTH * 2 + GAP * 2,
            y= 0,
            width= SCREEN_WIDTH,
            height= 7 * SQUARE_PIXEL
        )
        self.ground_rect = self.ground_img.get_rect(bottomleft= (x, SCREEN_HEIGHT * SCALE))
        self.move_speed = 1.75

    def reposition(self):
        if self.ground_rect.right <= 0:
            self.ground_rect.left = SCREEN_WIDTH * SCALE
            
    def update(self):
        
        self.ground_rect.right -= self.move_speed
        self.reposition()
        self.draw()

    def draw(self):
        screen.blit(self.ground_img, self.ground_rect)

class Score_Board(pygame.sprite.Sprite):
    def __init__(self, score):
        super().__init__()
        self.image = get_image(
            x= 0, y= SCREEN_HEIGHT, width= 15 * SQUARE_PIXEL, height= 8 * SQUARE_PIXEL
        )
        self.image_rect = self.image.get_rect(center= (SCREEN_WIDTH / 2 * SCALE, SCREEN_HEIGHT / 2 * SCALE))

        medal_rad = 3 * SQUARE_PIXEL
        if score < 10: # bronze medal
            self.medal_img = get_image(
                x= 14 * SQUARE_PIXEL - 1,
                y= 19 * SQUARE_PIXEL + SCREEN_HEIGHT + 8 * SQUARE_PIXEL + 4,
                width= medal_rad, height= medal_rad
            )
        elif score < 25: # silver medal 
            self.medal_img = get_image(
                x= 14 * SQUARE_PIXEL - 1,
                y= 16 * SQUARE_PIXEL + SCREEN_HEIGHT + 8 * SQUARE_PIXEL + 4,
                width= medal_rad, height= medal_rad
            )
        elif score < 150: # gold medal
            self.medal_img = get_image(
                x= 15 * SQUARE_PIXEL,
                y= SCREEN_HEIGHT + medal_rad + 1,
                width= medal_rad, height= medal_rad
            )
        else: # platinum medal
            self.medal_img = get_image(
                x= 15 * SQUARE_PIXEL,
                y= SCREEN_HEIGHT + 1,
                width= medal_rad, height= medal_rad
            )
        self.medal_rect = self.medal_img.get_rect(center= (self.image_rect.left + SCALE*(medal_rad + 3), self.image_rect.centery + 6))

    def draw(self):
        screen.blit(self.image, self.image_rect)
        screen.blit(self.medal_img, self.medal_rect)

    def update(self):
        self.draw()
        

class Pipe(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "day":
            pipe1 = get_image(
                x= 7 * SQUARE_PIXEL,
                y= SCREEN_HEIGHT + 8 * SQUARE_PIXEL,
                width= 3 * SQUARE_PIXEL + GAP,
                height= 21 * SQUARE_PIXEL,
                rotate= 180.0
            )
            pipe2 = get_image(
                x= 7 * SQUARE_PIXEL,
                y= SCREEN_HEIGHT + 8 * SQUARE_PIXEL,
                width= 3 * SQUARE_PIXEL + GAP,
                height= 21 * SQUARE_PIXEL
            )
        else:
            pipe1 = get_image(
                x= 0,
                y= SCREEN_HEIGHT + 8 * SQUARE_PIXEL,
                width= 3 * SQUARE_PIXEL + GAP,
                height= 21 * SQUARE_PIXEL
            )
            pipe2 = get_image(
                x= 0,
                y= SCREEN_HEIGHT + 8 * SQUARE_PIXEL,
                width= 3 * SQUARE_PIXEL + GAP,
                height= 21 * SQUARE_PIXEL,
                rotate= 180.0
            )
        
        self.all_pipe_img = [pipe1, pipe2]
        
        
    def draw(self, time):
        raise NotImplemented



time = "day"
score = 200

all_game_bg = pygame.sprite.Group(
    BG_img(time),
    BG_img(time, x= SCREEN_WIDTH * SCALE),
    BG_Ground(),
    BG_Ground(x= SCREEN_WIDTH * SCALE),
    Score_Board(score)
) 



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.fill(bg_color)    
    
    for game_bg in all_game_bg.copy():
        game_bg.update()
    
    pygame.display.update()
    clock.tick(60)