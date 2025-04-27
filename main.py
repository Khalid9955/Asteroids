import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")

    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Creating objects
    player = Player((SCREEN_WIDTH /2), (SCREEN_HEIGHT/ 2))
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        [sprite.draw(screen) for sprite in drawable]

        for asteroid in asteroids:
            if player.checkCollision(asteroid):
                print("Game over!")
                exit(1)

            for shot in shots:
                if shot.checkCollision(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        
        # Pause the game loop until 1/60th of a second has passed (i.e. 60 FPS)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
