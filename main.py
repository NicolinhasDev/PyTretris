import pygame
import random

WIN_W = 800
WIN_H = 700

GAME_W = 300
GAME_H = 600

SIZE = 30

topx = (WIN_W - GAME_W) // 2
topy = WIN_H - GAME_H

S = [['-----',
      '-----',
      '--11-',
      '-11--',
      '-----'],
     ['-----',
      '--1--',
      '--11-',
      '---1-',
      '-----',
      ]]

Z = [['-----',
      '-----',
      '-11--',
      '--11-',
      '-----'],
     ['-----',
      '---1--',
      '--11-',
      '--1--',
      '-----',
      ]]

I = [['--1--',
      '--1--',
      '--1--',
      '--1--',
      '-----'],
     ['-----',
      '1111-',
      '-----',
      '-----',
      '-----',
      ]]

O = ['-----',
     '-----',
     '-11--',
     '-11--',
     '-----']

J = [['-----',
      '-1---',
      '-111-',
      '-----',
      '-----'],
     ['-----',
      '--11-',
      '--1--',
      '--1--',
      '-----',],
      ['-----',
      '-----',
      '-111-',
      '---1-',
      '-----'],
     ['-----',
      '--1--',
      '--1--',
      '-11--',
      '-----']]

L = [['-----',
      '---1-',
      '-111-',
      '-----',
      '-----'],
     ['-----',
      '--1--',
      '--1--',
      '--11-',
      '-----',],
      ['-----',
      '-----',
      '-111-',
      '-1---',
      '-----'],
     ['-----',
      '-11--',
      '--1--',
      '--1--',
      '-----']]

T = [['-----',
      '--1--',
      '-111-',
      '-----',
      '-----'],
     ['-----',
      '--1--',
      '--11-',
      '--1--',
      '-----',],
      ['-----',
      '-----',
      '-111-',
      '--1--',
      '-----'],
     ['-----',
      '--1--',
      '-11--',
      '--1--',
      '-----']]

SHAPES = [S, Z, I, O, J, L, T]
COLORS = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = COLORS[SHAPES.index(shape)]
        self.rotation = 0

def create_grid(locked_pos={}):
    grid = [[(0,0,0)for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c
    return grid

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    return random.choice(SHAPES)

def draw_text_middle(text, size, color, surface):  
    pass
   
def draw_grid(surface, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (topx + j*SIZE, topy + i*SIZE, SIZE, SIZE), 0)

    pygame.draw.rect(surface, (255,0,0), (topx, topy, GAME_W, GAME_H), 4)

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface, grid):
    surface.fill(0,0,0)

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255,255,255))

    surface.blit(label, (topx + GAME_W/2 - (label.get_width()/2), 30))

    pygame.display.update()

def main():
    pass

def main_menu():
    pass

main_menu()