import pygame
from sys import exit
import random

WIDTH = 800
HEIGHT = 400

PADEL_WIDTH = 10
PADEL_HEIGHT = 75

PADEL_POSITION_TO_BORDER = 20

BALL_DIMENSION = 10

PADEL_SPEED = 5
BALL_SPEED = 2

# start the pygame
pygame.init()

# the display game screen
# display surface (the main surface uses to show the game)
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

# the name of the game
pygame.display.set_caption("Pong")

# the game clock
clock = pygame.time.Clock()

# the game icon
pygame_icon = pygame.image.load('img\cookie.jpg')
pygame.display.set_icon(pygame_icon)


padel_1 = pygame.Surface((PADEL_WIDTH, PADEL_HEIGHT))
padel_1.fill("White")
padel_1_rect = padel_1.get_rect(midleft = (PADEL_POSITION_TO_BORDER, HEIGHT / 2))


padel_2 = pygame.Surface((PADEL_WIDTH, PADEL_HEIGHT))
padel_2.fill("White")
padel_2_rect = padel_2.get_rect(midright = (WIDTH - PADEL_POSITION_TO_BORDER, HEIGHT / 2))


ball = pygame.Surface((BALL_DIMENSION, BALL_DIMENSION))
ball.fill("White")
ball_rect = ball.get_rect(center = (WIDTH / 2, HEIGHT / 2))
ball_y_start_speed = random.randint(1, BALL_SPEED)
ball_x_start_speed = BALL_SPEED

restart = False
game_start = False
score_1, score_2 = 0, 0

# font
font = pygame.font.Font(None, 50)
game_title = font.render("Pong", False, "Pink")
game_title_rect = game_title.get_rect(center = (WIDTH / 2, 25))

def display_score():
    player1_text = font.render(f"{score_1}", False, "Blue")
    player1_text_rect = player1_text.get_rect(center = (WIDTH / 4, 80))

    player2_text = font.render(f"{score_2}", False, "Blue")
    player2_text_rect = player2_text.get_rect(center = (WIDTH * 3 / 4, 80))

    continue_title = font.render("Press space to play", False, "Orange")
    continue_title_rect = continue_title.get_rect(center = (WIDTH / 2, HEIGHT - 50))

    screen.blit(player1_text, player1_text_rect)
    screen.blit(player2_text, player2_text_rect)
    screen.blit(continue_title, continue_title_rect)
    

# keep running forever when needed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if keys := pygame.key.get_pressed():
        if game_start:        
            # player 1
            if keys[pygame.K_w]:
                if padel_1_rect.top > 0: padel_1_rect.y -= PADEL_SPEED
                if padel_1_rect.top < 0: padel_1_rect.top = 0
            if keys[pygame.K_s]:
                if padel_1_rect.bottom < HEIGHT: padel_1_rect.y += PADEL_SPEED
                if padel_1_rect.bottom > HEIGHT: padel_1_rect.bottom = HEIGHT        
            # player 2
            if keys[pygame.K_UP]:
                if padel_2_rect.top > 0: padel_2_rect.y -= PADEL_SPEED
                if padel_2_rect.top < 0: padel_2_rect.top = 0
            if keys[pygame.K_DOWN]:
                if padel_2_rect.bottom < HEIGHT: padel_2_rect.y += PADEL_SPEED
                if padel_2_rect.bottom > HEIGHT: padel_2_rect.bottom = HEIGHT        
        
            # bot 
            if ball_x_start_speed < 0:
                distant_to_padel = abs(ball_rect.left - padel_1_rect.right)
                player = 1
            else:
                distant_to_padel = abs(ball_rect.right - padel_2_rect.left)
                player = 2
            
            time_to_padel = round(distant_to_padel / abs(ball_x_start_speed), 2) 
                        
            next_y = round(time_to_padel * ball_y_start_speed + ball_rect.y, 2)
            if next_y < 0:
                next_y = abs(next_y)
            elif next_y > HEIGHT:
                next_y = HEIGHT * 2 - next_y
            
            next_y = round(next_y, 2)
            while next_y < 0 or next_y > HEIGHT:
                next_y = next_y + HEIGHT if next_y < 0 else next_y - HEIGHT
            
            # bot 1
            if player == 1:                
                if not (padel_1_rect.top + 10 <= next_y <= padel_1_rect.bottom - 10):
                    if padel_1_rect.top + 10 > next_y:
                        padel_1_rect.y -= PADEL_SPEED 
                    elif padel_1_rect.bottom - 10 < next_y:
                        padel_1_rect.y += PADEL_SPEED
            
                if not (padel_2_rect.top + 10 <= HEIGHT / 2 <= padel_2_rect.bottom - 10):
                    if padel_2_rect.top + 10> next_y:
                        padel_2_rect.y -= PADEL_SPEED
                    elif padel_2_rect.bottom - 10 < next_y:
                        padel_2_rect.y += PADEL_SPEED
                    
            # bot 2
            else:
                if not (padel_2_rect.top + 10 <= next_y <= padel_2_rect.bottom - 10):
                    if padel_2_rect.top + 10> next_y:
                        padel_2_rect.y -= PADEL_SPEED
                    elif padel_2_rect.bottom - 10 < next_y:
                        padel_2_rect.y += PADEL_SPEED
            
                if not (padel_1_rect.top + 10 <= HEIGHT / 2 <= padel_1_rect.bottom - 10):
                    if padel_1_rect.top + 10 > next_y:
                        padel_1_rect.y -= PADEL_SPEED 
                    elif padel_1_rect.bottom - 10 < next_y:
                        padel_1_rect.y += PADEL_SPEED

            if padel_1_rect.top < 0:
                padel_1_rect.top = 0
            elif padel_1_rect.bottom > HEIGHT:
                padel_1_rect.bottom = HEIGHT

            if padel_2_rect.top < 0:
                padel_2_rect.top = 0
            elif padel_2_rect.bottom > HEIGHT:
                padel_2_rect.bottom = HEIGHT

        else:
            if keys[pygame.K_SPACE]: 
                game_start = True
                restart = False
                
    if game_start:
        ball_rect.y += ball_y_start_speed
        ball_rect.x += ball_x_start_speed
        
        if ball_rect.bottom > HEIGHT: 
            ball_rect.bottom = HEIGHT
            ball_y_start_speed *= -(1 + round(random.uniform(-0.2, 0.2), 2))
        
        if ball_rect.top < 0:
            ball_rect.top = 0
            ball_y_start_speed *= -(1 + round(random.uniform(-0.2, 0.2), 2)) 

        if ball_rect.left < 0:
            ball_x_start_speed *= -1
            game_start = False
            score_2 += 1
        
        if ball_rect.right > WIDTH:
            ball_x_start_speed *= -1
            game_start = False
            score_1 += 1
        
        if padel_1_rect.colliderect(ball_rect):
            ball_x_start_speed *= -1
            ball_x_start_speed += 0.25
            ball_rect.left = padel_1_rect.right
                    
        if padel_2_rect.colliderect(ball_rect):
            ball_x_start_speed *= -1
            ball_x_start_speed -= 0.25
            ball_rect.right = padel_2_rect.left
    
    elif not restart:
        restart = True
        ball_y_start_speed = random.randint(1, BALL_SPEED)
        ball_x_start_speed = BALL_SPEED
        padel_1_rect.midleft = (PADEL_POSITION_TO_BORDER, HEIGHT / 2)
        padel_2_rect.midright = (WIDTH - PADEL_POSITION_TO_BORDER, HEIGHT / 2)
        ball_rect.center = (WIDTH / 2, HEIGHT / 2)
    else:
        display_score()
        screen.blit(game_title, game_title_rect)

    
    # set the test surface on the main display surface at a given cordinate
    screen.blit(padel_1, padel_1_rect)
    screen.blit(padel_2, padel_2_rect)
    screen.blit(ball, ball_rect)
    
    # update the game display
    pygame.display.update()

    screen.fill(0)
    
    # control the while true loop to not run over 60 time/s
    clock.tick(60)