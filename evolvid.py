import sys
import pygame


def main():
    pygame.init()

    size = width, height = 320, 240

    screen = pygame.display.set_mode(size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        #screen.blit(ball, ballrect)
        pygame.display.flip()
    


if __name__ == '__main__':
    main()
