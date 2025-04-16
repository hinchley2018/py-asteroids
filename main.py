# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame,sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:",  SCREEN_HEIGHT)
    #init
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    
    #create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #create asteroid field
    AsteroidField()
    while True:
        
        #handle pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #BEFORE RENDER
        updateable.update(dt)

        #RENDER START    
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        screen.fill(SCREEN_BG_COLOR)
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(FRAMES_PER_SECOND) / 1000
if __name__ == "__main__":
    main()