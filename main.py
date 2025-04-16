# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:",  SCREEN_HEIGHT)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill(SCREEN_BG_COLOR)
        #handle pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(FRAMES_PER_SECOND) / 1000
if __name__ == "__main__":
    main()