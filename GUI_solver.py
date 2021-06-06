import pygame
import solver, GUI
from GUI_values import *

example_sudoku = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
example_sudoku_solution = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'


def solve_sudoku(sudoku_board):
    empty_cell_coords = solver.get_next_empty_cell(sudoku_board)

    if empty_cell_coords is None:
        # print(sudoku_board)
        return True
    game_grid.select_cell(empty_cell_coords[0], empty_cell_coords[1])

    for digit in range(1, 10):
        is_digit_valid = solver.validate_new_value(sudoku_board, digit, *empty_cell_coords)
        if is_digit_valid:
            sudoku_board[empty_cell_coords] = digit
            game_grid.put_value(digit)
            refresh_gui(window)

            if solve_sudoku(sudoku_board):
                return True

            sudoku_board[empty_cell_coords] = 0
            game_grid.remove_value()
            refresh_gui(window)

    return False


def refresh_gui(win):
    game_grid.update_arr_grid()
    game_grid.draw_grid(win)
    pygame.display.update()


pygame.font.init()
window = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
pygame.display.set_caption("Sudoku")
board = solver.get_sudoku_board(example_sudoku)

game_grid = GUI.GameGrid(board, 9, 9, WINDOW_SIZE, WINDOW_SIZE)
game_grid.draw_grid(window)

game_run = False

solve_sudoku(board)

while game_run:
    solve_sudoku(board)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
pygame.quit()


