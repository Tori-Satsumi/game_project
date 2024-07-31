from PIL import Image

with Image.open('C:\Users\GIGABYTE\OneDrive\Desktop\program\game_project\flappy\img\flappy_bird_sprite.png') as img:
    width, height = img.size

    print(width)
    print(height)