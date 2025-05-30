import pygame
from constants import SCREEN_WIDTH , SCREEN_HEIGHT, PLAYER_TURN_SPEED, SHOT_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    run = True



    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = updateable
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (updateable, drawable)

    player =  Player ((SCREEN_WIDTH/ 2), (SCREEN_HEIGHT/2), shots)
    asteroid_field = AsteroidField()





    while run == True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                 run = False
                
        screen.fill((0, 0, 0))
        updateable.update(dt)

        for draw_item in drawable:
            draw_item.draw(screen)

            

        for asteroid in asteroids:
            for shot in shots:
                shot_hit = asteroid.collission(shot)
                if shot_hit == True:
                    asteroid.split()
                    shot.kill()

            boom = asteroid.collission(player)
            if boom == True:
                print("GAME OVER!")
                run = False

        pygame.display.flip()
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()