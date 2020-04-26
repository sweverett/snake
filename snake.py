import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

DX, DY = 1, 1
DT = 25 #ms
X0, Y0 = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        return

    def next_frame(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                break

        keys = pygame.key.get_pressed()

        return

    def update(self):
        pygame.display.update()
        return

    def wait(self):
        pygame.time.wait(DT)
        return

class Snake(object):
    def __init__(pos, self):
        self.pos = pos0
        self.head = Square(pos, head=True)
        self.body = [self.head]

        return

class Square(object):
    def __init__(self, pos, head=False):
        self.pos = pos
        self.head = head

        return

def main():

    game = Game()

    pos0 = [X0, Y0]

    snake = Snake(pos0)

    while True:
        game.next_frame()

        game.wait(DT)

    return

if __name__ == '__main__':
    main()

