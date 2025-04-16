# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:",  SCREEN_HEIGHT)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    while True:
        
        #handle pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #BEFORE RENDER
        player.update(dt)

        #RENDER START    
        screen.fill(SCREEN_BG_COLOR)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FRAMES_PER_SECOND) / 1000
if __name__ == "__main__":
    main()