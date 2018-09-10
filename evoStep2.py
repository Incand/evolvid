import pygame
import sys
import time
import random


size = ()


class engine_obj(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        
        update_event.add(self.update)
        draw_event.add(self.draw)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class square(engine_obj):
    def __init__(self, image="gfx/blue.png", speed=None):
        engine_obj.__init__(self, image)
        
        self.position = [0, 0]
        self.speed = speed if speed is not None else \
                [random.random() * 4 - 2 for _ in range(2)]

    def update(self):
        if (self.rect.x < 0) or (self.rect.x > size[0]-16):
            self.speed[0] *= -1
        if (self.rect.y < 0) or (self.rect.y > size[1]-16):
            self.speed[1] *= -1

        for _i in range(2):
            self.position[_i] += self.speed[_i]

        self.rect.x = round(self.position[0])
        self.rect.y = round(self.position[1])


class Event():
    def __init__(self):
        self._functions = []

    def add(self, func):
        self._functions.append(func)

    def remove(self, func):
        self._functions.remove(func)

    def invoke(self, *args):
        for _func in self._functions:
            _func(*args)


update_event = Event()
draw_event = Event()

FPS = 60

def main():
    global size
    pygame.init()

    size = width, height = 1366, 768
    screen = pygame.display.set_mode(size)

    for _ in range(100):
        square()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        update_event.invoke()

        screen.fill((0, 0, 0))
        draw_event.invoke(screen)

        pygame.display.flip()
        time.sleep(1/FPS)


if __name__ == '__main__':
    main()
