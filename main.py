import pygame
from constants import SCREEN_WIDTH , SCREEN_HEIGHT



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    clock.dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    run = True

    while run == True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                             return
                
        screen.fill((0, 0, 0))
        clock.dt = clock.tick(60) / 1000
        pygame.display.flip()




if __name__ == "__main__":
    main()