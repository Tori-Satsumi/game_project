from PIL import Image

im = Image.open('img\flappy_bird_sprite.png')
width, height = im.size

print(width)
print(height)