#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def calc(base_grid_list, bomb_locations_grid_list):
    R = len(base_grid_list)
    C = len(base_grid_list[0])
    dx = [0, 0, 1, -1] 
    dy = [1, -1, 0, 0] 

    next_state_grid = [row[:] for row in base_grid_list] 
    explode_cells = set()

    for r in range(R):
        for c in range(C):
            if bomb_locations_grid_list[r][c] == 'O': 
                explode_cells.add((r, c)) 
                for k in range(4):
                    nr, nc = r + dy[k], c + dx[k]
                    if 0 <= nr < R and 0 <= nc < C: 
                        explode_cells.add((nr, nc)) 
    for r, c in explode_cells:
        next_state_grid[r][c] = '.' 

    return next_state_grid
    

def grid_to_string_list(grid_list):
    return ["".join(row) for row in grid_list]

def bomberMan(n, grid):
    G0 = [list(row) for row in grid]
    
    R = len(grid)
    C = len(grid[0])
    all_bomb = [['O'] * C for _ in range(R)]
    if n == 0 or n == 1:
        return grid
    
    G3 = calc(all_bomb, G0)                
    G5 = calc(all_bomb, G3)   
            
    if n % 2 == 0:
        return grid_to_string_list(all_bomb)
    elif n % 4 == 3:
        return grid_to_string_list(G3)
    elif n % 4 == 1:
        return grid_to_string_list(G5)
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
