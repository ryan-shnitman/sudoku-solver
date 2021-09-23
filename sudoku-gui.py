'''
    based on video: https://www.youtube.com/watch?v=I2lOwRiGNy4&ab_channel=HackerShrine
'''

import pygame
import requests
import copy


pygame.init()

# global variables
WIDTH = 550
pad = WIDTH//11
buffer = 10

black = (0,0,0)
white = (255, 255, 255)
blue = (0, 0, 255)

DIFFICULTY = "easy"
font = pygame.font.SysFont('Comic Sans MS', 35)

response = requests.get(f"https://sugoku.herokuapp.com/board?difficulty={DIFFICULTY}")
grid = response.json()['board']
grid_original = copy.deepcopy(grid)


def insert(screen, position):
    r, c = int(position[1] // pad), int(position[0] // pad)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if grid_original[r-1][c-1] != 0:  # can't alter the originally filled cells
                    return
                if event.key == 48:  # checking for 0, functionality: clear cell
                    grid[r-1][c-1] = 0
                    pygame.draw.rect(screen, white, (c*pad + buffer, r*pad + buffer, pad-buffer, pad-buffer))
                    pygame.display.update()
                    return
                if 0 < event.key - 48 < 10:
                    pygame.draw.rect(screen, white, (c*pad + buffer, r*pad + buffer, pad-buffer, pad-buffer))
                    value = font.render(str(event.key-48), True, blue)
                    screen.blit(value, (c*pad + 15, r*pad))
                    grid[r-1][c-1] = event.key - 48
                    pygame.display.update()
                    return




def main():

    screen = pygame.display.set_mode((WIDTH, WIDTH))
    screen.fill(white)
    pygame.display.set_caption("SUDOKU")

    # build and fill out board
    for i in range(10):
        thickness = 2
        if i % 3 == 0:
            thickness = 4
        pygame.draw.line(screen, black, (pad + pad*i, pad), (pad + pad*i, WIDTH-pad), thickness)  # vertical line
        pygame.draw.line(screen, black, (pad, pad + pad*i), (WIDTH-pad, pad + pad*i), thickness)  # horizontal line

    for r in range(9):
        for c in range(9):
            if 0 < grid[r][c] < 10:
                value = font.render(str(grid[r][c]), True, black)
                screen.blit(value, ((c+1) * pad + 15, (r+1) * pad))

    pygame.display.update()

    # game loop
    gameOn = True
    while gameOn:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                insert(screen, pygame.mouse.get_pos())
            if event.type == pygame.QUIT:
                pygame.quit()
                gameOn = False


main()

