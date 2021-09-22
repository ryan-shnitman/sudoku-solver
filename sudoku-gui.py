''' based on video: https://www.youtube.com/watch?v=I2lOwRiGNy4&ab_channel=HackerShrine '''

import pygame
import requests
import copy


WIDTH = 550
black = (0,0,0)
DIFFICULTY = "easy"
font = pygame.font.SysFont("COmic Sans MS", 35)

response = requests.get(f"https://sugoku.herokuapp.com/board?difficulty={DIFFICULTY}")
grid = response.json()['board']
grid_orginal = copy.deepcopy(grid)

def insert(screen, position):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                #1. tries to edit orginal file
                #2. edit
                #3. adding the digits


def main():
    pygame.init()
    gameOn = True

    screen = pygame.display.set_mode((WIDTH, WIDTH))
    screen.fill((251,247,245))
    pygame.display.set_caption("SUDOKU")

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, black, (50 + 50 * i, 50), (50 + 50 * i, 500), 4)  # vertical line
            pygame.draw.line(screen, black, (50, 50 + 50 * i), (500, 50 + 50 * i), 4)  # horizontal line
        else:
            pygame.draw.line(screen, black, (50 + 50*i, 50), (50 + 50*i, 500), 2)  # vertical line
            pygame.draw.line(screen, black, (50, 50 + 50*i), (500, 50+ 50*i), 2)  # horizontal line

    for r in range(9):
        for c in range(9):
            if 0 < grid[r][c] < 10:
                value = font.render(str(grid[r][c]), True, black)
                screen.blit(value, ((c+1)*50 + 15, (r+1)*50))

    pygame.display.update()

    while gameOn:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEVUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(screen, (pos//50, )
            if event.type == pygame.QUIT:
                pygame.quit()
                gameOn = False


main()

