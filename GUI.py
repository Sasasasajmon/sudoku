import numpy as np
import pygame
import solver
from GUI_values import *


class GameGrid:
    def __init__(self, board, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.cells = [[Cell(board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.update_arr_grid()
        self.curr_selected = None

    def draw_grid(self, window):
        window.fill(WHITE)
        for i in range(self.rows + 1):
            if i % 3 == 0:
                line_thickness = CONTRAST_WIDTH
            else:
                line_thickness = BASE_WIDTH
            pygame.draw.line(window, BLACK, (0, i * CELL_SIZE), (self.width, i * CELL_SIZE), line_thickness)
            pygame.draw.line(window, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, self.height), line_thickness)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(window)

    def select_cell(self, row, col):
        if self.curr_selected:
            self.cells[self.curr_selected[0]][self.curr_selected[1]].selected = False

        self.cells[row][col].selected = True
        self.curr_selected = (row, col)

    def get_clicked_cell(self, position):
        if position[0] < self.width and position[1] < self.height:
            x = position[0] // CELL_SIZE
            y = position[1] // CELL_SIZE
            return int(y), int(x)
        return None

    def mark_value(self, value):
        x, y = self.curr_selected
        self.cells[x][y].set_temp_value(value)

    def put_value(self, value):
        row, col = self.curr_selected
        if self.cells[row][col].value == 0:
            self.cells[row][col].set_value(value)

            if solver.validate_new_value(self.arr_grid, value, row, col):
                self.update_arr_grid()
                return True
            else:
                self.cells[row][col].set_value(0)
                self.cells[row][col].set_temp_value(0)
                self.update_arr_grid()
                return False

    def remove_value(self):
        row, col = self.curr_selected
        if not self.cells[row][col].is_fixed:
            self.cells[row][col].set_value(0)
            self.cells[row][col].set_temp_value(0)

    def update_arr_grid(self):
        temp = [[self.cells[i][j].value for j in range(self.cols)] for i in range(self.rows)]
        self.arr_grid = np.array(temp)

    def is_grid_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].value == 0:
                    return False
        return True


class Cell:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        self.is_fixed = False if value == 0 else True

    def draw(self, win):
        font = pygame.font.SysFont("comicsans", 40)

        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE

        if self.value != 0:
            text = font.render(str(self.value), True, BLACK)
            win.blit(text, (x + (CELL_SIZE / 2 - text.get_width() / 2), y + (CELL_SIZE / 2 - text.get_height() / 2)))
        elif self.temp != 0:
            text = font.render(str(self.temp), True, GREY)
            win.blit(text, (x + (CELL_SIZE / 2 - text.get_width() / 2), y + (CELL_SIZE / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(win, RED, (x, y, CELL_SIZE, CELL_SIZE), 3)

    def set_value(self, val):
        self.value = val

    def set_temp_value(self, val):
        self.temp = val
