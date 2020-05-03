import pygame
import random

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

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
SPRITE_SIZE = 15

DX, DY = 15, 15
DT = 25 #ms
X0, Y0 = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        return

    def next_frame(self):
#        for event in pygame.event.get():
#            if event.type == KEYDOWN:
#                if event.key == K_ESCAPE:
#                    break
#            elif event.type == QUIT:
#                break

        keys = pygame.key.get_pressed()
        self.screen.fill((50,56,62))

        return keys

    def draw(self):
        pygame.display.update()
        return

    def wait(self, DT):
        pygame.time.wait(DT)
        return

class Snake(object):
    def __init__(self, pos):
        self.pos = pos
        self.head = Square(pos, type='head')
        self.body = [self.head,Square([pos[0]-DX,pos[1]]),Square([pos[0]-2*DX,pos[1]], type='tail')]
        self.turns = {} # A turn is (x, y):dir

        return

    def update(self, keys, snack):
        # Move, grow

        self.move(keys)
        if pygame.sprite.collide_rect(self.head,snack):
            snack.update()
            self.body[-1].type = None
            tpos=[self.body[-1].pos[0]-DX*self.body[-1].vel[0], self.body[-1].pos[1]-DY*self.body[-1].vel[1]]    
            self.body.append(Square(tpos, self.body[-1].vel, type='tail'))

        return

    def move(self, keys):
        for square in self.body:
            square.move(keys, self.turns)

        return

    def draw(self,game):
        for square in self.body:
            game.screen.blit(square.surf, square.rect)
        return

class Square(pygame.sprite.Sprite):
    def __init__(self, pos, vel=[0, 0], type=None):
        super(Square,self).__init__()
        self.pos = pos
        self.vel = vel
        self.type = type
        self.surf=pygame.Surface((SPRITE_SIZE,SPRITE_SIZE))
        self.surf.fill((0,250,250))
        self.rect = self.surf.get_rect(topleft=(pos))
        return

    def move(self, keys, turns):
        #if keys is None:
         #   return
                
        if self.type == 'head':
            if keys[K_DOWN] and self.vel!=[0,-1]:
                self.vel[0] = 0
                self.vel[1] = 1
                turns[tuple(self.pos)]='down'
            if keys[K_UP] and self.vel!=[0,1]:
                self.vel[0] = 0
                self.vel[1] = -1
                turns[tuple(self.pos)]='up'
            if keys[K_RIGHT] and self.vel!=[-1,0]:
                self.vel[0] = 1
                self.vel[1] = 0
                turns[tuple(self.pos)]='right'
            if keys[K_LEFT] and self.vel!=[1,0]:
                self.vel[0] = -1
                self.vel[1] = 0
                turns[tuple(self.pos)]='left'
        else:
            tpos = tuple(self.pos)
            if tpos in turns:
                if turns[tpos] == 'down':
                    self.vel = [0,1]
                if turns[tpos] == 'up':
                    self.vel = [0,-1]
                if turns[tpos] == 'right':
                    self.vel = [1,0]
                if turns[tpos] == 'left':
                    self.vel = [-1,0]
                if self.type == 'tail':
                    turns.pop(tpos)

        self.update_pos()

        return

    def update_pos(self):
        self.pos[0] = (self.pos[0] + DX*self.vel[0]) % SCREEN_WIDTH
        self.pos[1] = (self.pos[1] + DY*self.vel[1]) % SCREEN_HEIGHT
        self.rect.move_ip(DX*self.vel[0],DY*self.vel[1])
        return

class Snack(pygame.sprite.Sprite):
    def __init__(self):
        super(Snack,self).__init__()
        self.pos = [SCREEN_WIDTH-SCREEN_WIDTH/4, SCREEN_HEIGHT/2]
        self.surf = pygame.Surface((SPRITE_SIZE,SPRITE_SIZE))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(topleft=(self.pos[0],self.pos[1]))
        
        return

    def update(self): 
        self.pos = [random.randint(SPRITE_SIZE,SCREEN_WIDTH-SPRITE_SIZE), random.randint(SPRITE_SIZE,SCREEN_HEIGHT-SPRITE_SIZE)]
        self.rect = self.surf.get_rect(topleft=(self.pos[0],self.pos[1]))

        return
    
    def draw(self,game):
        game.screen.blit(self.surf,self.rect)
        
        return


pygame.init()

def main():

    game = Game()
    snack = Snack()
    pos0 = [X0, Y0]
    snake = Snake(pos0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False
       
        keys = game.next_frame()
        snake.update(keys,snack)
        snack.draw(game)
        snake.draw(game)
        game.draw()

        game.wait(DT)

    return

if __name__ == '__main__':
    main()

