import pygame
from GUI_values import *


class Cell(pygame.sprite.Sprite):
    cell_img = pygame.transform.scale(pygame.image.load("images/cell.png"), (CELL_SIZE, CELL_SIZE))

    def __init__(self, coords, number=0):
        super().__init__()
        self.image = Cell.cell_img
        self.rect = self.image.get_rect()
        self.rect.topleft = coords
        self.number = number
        self.last_number_displayed = None

    def update(self, window, font, v):
        if self.last_number_displayed is None:
            self.draw_digit(window, font, v)
        else:
            self.rect = self.image.get_rect()

    def draw_digit(self, window, font, v):
        if v:
            self.number = 12
        if self.number != self.last_number_displayed:
            digit = ' ' if self.number == 0 else str(self.number)
            digit_render = font.render(digit, True, BLACK)
            digit_coords = digit_render.get_rect(center=self.rect.center)
            window.blit(digit_render, digit_coords)
            pygame.display.flip()
            self.last_number_displayed = self.number


class GameGrid:
    def __init__(self, graphic_cells_list):
        self.group = pygame.sprite.Group(graphic_cells_list)


def get_game_grid(grid):
    sudoku_cell_list = []
    id_counter = 0
    for row in range(9):
        for cell in range(9):
            sudoku_cell_list.append(Cell(coords=(MARGIN + row * CELL_SIZE, MARGIN + cell * CELL_SIZE),
                                         number=grid[row][cell]
                                         )
                                    )
            id_counter += 1

    return GameGrid(sudoku_cell_list)
