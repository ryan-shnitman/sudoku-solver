'''
    based on video: https://www.youtube.com/watch?v=I2lOwRiGNy4&ab_channel=HackerShrine
'''

import pygame
import requests
import copy


pygame.init()

# global variables
WIDTH = 550
pad = WIDTH // 11
buffer = 10

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

DIFFICULTY = "easy"
font = pygame.font.SysFont('Comic Sans MS', 35)

response = requests.get(f"https://sugoku.herokuapp.com/board?difficulty={DIFFICULTY}")
grid = response.json()['board']
grid_original = copy.deepcopy(grid)


def event_handler(screen):
    clicked = False
    old_block = None

    def highlight(screen, r, c, remove):
        color = blue
        if remove:
            color = black
        pygame.draw.line(screen, color, (pad * c, pad * r), (pad * c, pad * r + pad), 2)  # vertical left
        pygame.draw.line(screen, color, (pad * c + pad, pad * r), (pad * c + pad, pad * r + pad), 2)  # vertical right
        pygame.draw.line(screen, color, (pad * c, pad * r), (pad * c + pad, pad * r), 2)  # horizontal top
        pygame.draw.line(screen, color, (pad * c, pad * r + pad), (pad * c + pad, pad * r + pad), 2)  # horizontal bottom
        pygame.display.update()

    def mouse_click(screen, r, c):
        # if valid cell, highlight, dehighlight old block, update old_block
        # if not valid cell, return False
        if grid_original[r-1][c-1] == 0:
            highlight(screen, r, c, remove=False)
            if clicked:
                highlight(screen, old_block[0], old_block[1], remove=True)
            return True
        return False

    def button_press(screen, r, c):
        # if 0, clear, dehilight
        # if 0 < value < 10, fill value, dehighlight
        if event.key == 48:  # checking for 0, functionality: clear cell
            grid[r - 1][c - 1] = 0
            pygame.draw.rect(screen, white, (c * pad + buffer, r * pad + buffer, pad - buffer, pad - buffer))
        elif 0 < event.key - 48 < 10:
            pygame.draw.rect(screen, white, (c * pad + buffer, r * pad + buffer, pad - buffer, pad - buffer))
            value = font.render(str(event.key - 48), True, blue)
            screen.blit(value, (c * pad + 15, r * pad))
            grid[r - 1][c - 1] = event.key - 48
        else:
            return

        highlight(screen, r, c, remove=True)
        pygame.display.update()
        return

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                r, c = int(pos[1]//pad), int(pos[0]//pad)
                if mouse_click(screen, r, c):
                    old_block = (r, c)
                    clicked = True
            elif event.type == pygame.KEYDOWN:
                if clicked:
                    button_press(screen, old_block[0], old_block[1])
                    clicked = False


def main():
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    screen.fill(white)
    pygame.display.set_caption("SUDOKU")

    # build and fill out board
    for i in range(10):
        thickness = 2
        if i % 3 == 0:
            thickness *= 2
        pygame.draw.line(screen, black, (pad + pad * i, pad), (pad + pad * i, WIDTH - pad), thickness)  # vertical line
        pygame.draw.line(screen, black, (pad, pad + pad * i), (WIDTH - pad, pad + pad * i),
                         thickness)  # horizontal line

    for r in range(9):
        for c in range(9):
            if 0 < grid[r][c] < 10:
                value = font.render(str(grid[r][c]), True, black)
                screen.blit(value, ((c + 1) * pad + 15, (r + 1) * pad))

    pygame.display.update()

    event_handler(screen)


main()

