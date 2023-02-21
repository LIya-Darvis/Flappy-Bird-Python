import pygame
import random
import sys

window_width = 600
window_height = 499

window = pygame.display.set_mode((window_width, window_height))
elevation = window_height * 0.8
game_images = { }
framepersecond = 32
pipeimage = 'images/pipe.png'
background_image = 'images/backround.jpg'
birdplayer_image = 'images/bird.png'
seavel_image = 'images/base.jfif'

def flappygame():
    your_score = 0
    horizontal = int(window_width/5)
    vertical = int(window_width/2)
    ground = 0
    mytempheight = 100
    
    first_pipe = createPipe()
    second_pipe = createPipe()
    
def createPipe():
    offset = window_height/3
    pipeHeight = game_images['pipeimage'][0].get_height()
    y2 = offset + \
        random.randrange(0, int(window_height - game_images['sea_level'.get_height]() - 1.2 * offset))
    pipeX = window_width + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, 
        {'x': pipeX, 'y': y2} 
    ]
    return pipe

if __name__ == "__main__":

    pygame.init()
    framepersecond_clock = pygame.time.Clock()

    pygame.display.set_caption('Flappy Bird')

    game_images['flappybird'] = pygame.image.load(birdplayer_image).convert_alpha()
    game_images['sea_level'] = pygame.image.load(seavel_image).convert_alpha()
    game_images['background'] = pygame.image.load(background_image).convert_alpha()
    game_images['pipeimage'] = (pygame.transform.rotate(pygame.image.load(pipeimage).convert_alpha(), 180), pygame.image.load(pipeimage).convert_alpha())
