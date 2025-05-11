# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init

    print("Starting Asteroids!")
    print(f"""Screen width: {SCREEN_WIDTH}
    Screen height: {SCREEN_HEIGHT}
    """)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while 1 == 1:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            return
        pygame.display.update()


if __name__ == "__main__":
    main()