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

    def wait(self, DT):
        pygame.time.wait(DT)
        return

class Snake(object):
    def __init__(self, pos):
        self.pos = pos
        self.head = Square(pos, type='head')
        self.body = [self.head]
        self.turns = {} # A turn is (x, y):dir

        return

    def update(self, keys):
        # Move, grow, draw

        self.move(keys)

        return

    def move(self, keys):
        for square in self.body:
            square.move(keys, self.turns)

        return

    def draw(self):
        pass

class Square(object):
    def __init__(self, pos, vel=[1, 0], type=None):
        self.pos = pos
        self.vel = vel
        self.type = type

        return

    def move(self, keys, turns):
        if keys is None:
            return

        if self.type == 'head':
            if keys[K_DOWN]:
                self.vel[1] = 1
            if keys[K_UP]:
                self.vel[1] = -1
            if keys[K_RIGHT]:
                self.vel[1] = 1
            if keys[K_LEFT]:
                self.vel[1] = -1
        else:
            tpos = tuple(self.pos)
            if tpos in turns:
                self.vel = turns[tpos]
                if self.type == 'tail':
                    turns.remove(turns[tpos])

        self.update_pos()

        return

    def update_pos(self):
        self.pos[0] = (self.pos[0] + DX*self.vel[0]) % SCREEN_WIDTH
        self.pos[1] = (self.pos[0] + DY*self.vel[1]) % SCREEN_HEIGHT

        return

def main():

    game = Game()

    pos0 = [X0, Y0]
    snake = Snake(pos0)

    while True:
        keys = game.next_frame()
        snake.update(keys)
        game.wait(DT)

    return

if __name__ == '__main__':
    main()

