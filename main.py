from gridworld import Grid
import pygame
from functools import partial
from model import Model
import math
import argparse

def draw_Off(grid, cell_dimensions):
    
    LIGHTGRAY = (192, 192, 192)
    GRAY = (128, 128, 128)
    DARKGRAY = (45, 45, 45)
    BROWN= (150, 75, 0)
    GREEN= (0, 255, 0)
    RED= (255, 0, 0)
    WHITE= (255,255,255)
    # Background
    pygame.draw.rect(grid.screen, LIGHTGRAY, cell_dimensions)
    
    # Circle
    x, y, w, h = cell_dimensions
    center = (x + math.floor(w/2), y + math.floor(h/2))
    pygame.draw.circle(grid.screen, WHITE, center, w*2/5 )

def draw_On(grid, cell_dimensions):
    LIGHTGRAY = (192, 192, 192)
    GRAY = (128, 128, 128)
    DARKGRAY = (45, 45, 45)
    BROWN= (150, 75, 0)
    GREEN= (0, 255, 0)
    RED= (255, 0, 0)

    # Background
    pygame.draw.rect(grid.screen, LIGHTGRAY, cell_dimensions)
    
    # Circle
    x, y, w, h = cell_dimensions
    center = (x + math.floor(w/2), y + math.floor(h/2))
    pygame.draw.circle(grid.screen, RED, center, w*2/5 )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                     prog='Synchronization of Pulse-Coupled Biological Oscillators',
                     description='Implements approximation of https://epubs.siam.org/doi/10.1137/0150098'
                     )
    parser.add_argument('-p', required=False,help='Value of P between 0 and 1')
    args = parser.parse_args()
    P = float(args.p) if args.p != None else 1
    R = 0
    grid = Grid(20, 20, 40, 40, title='Sim of Pulse-Coupled Biological Oscillators', margin=1,framerate=20)
    
    grid.set_drawaction('O', draw_Off) # Green
    grid.set_drawaction('X', draw_On) # Red
    
    model = Model(grid,P, R)
 
    grid.set_timer_action(model.run_sim)

    model.setup()
    
    grid.run()

