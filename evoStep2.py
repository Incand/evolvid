import pygame
import sys
import time


def main():
    pygame.init()

    size = width, height = 320,240

    screen = pygame.display.set_mode(size)


    class square(pygame.sprite.Sprite):
        def __init__(self, image="gfx/blue.png", speed=[2, 2]):

            pygame.sprite.Sprite.__init__(self)
            self.speed = speed
            self.image = pygame.image.load(image)
            self.rect = self.image.get_rect()

        def update(self):
            global size
            if (self.rect.x < 0) or (self.rect.x > 320-16):
                self.speed[0] *= -1
            if (self.rect.y < 0) or (self.rect.y > 240-16):
                self.speed[1] *= -1

            self.rect.x = self.rect.x + self.speed[0]
            self.rect.y = self.rect.y + self.speed[1]

        def draw(self, screen):
            screen.blit(self.image, self.rect)

    square1 = square()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        square1.draw(screen)
        square1.update()
        pygame.display.flip()
        time.sleep(0.01)


if __name__ == '__main__':
    main()