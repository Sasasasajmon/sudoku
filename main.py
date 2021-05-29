import pygame
import GUI
import solver
from GUI_values import *

example_sudoku = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
example_sudoku_solution = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'


def main():
    pygame.font.init()
    window = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
    pygame.display.set_caption("Sudoku")
    board = solver.get_sudoku_board(example_sudoku)

    game_grid = GUI.GameGrid(board, 9, 9, WINDOW_SIZE, WINDOW_SIZE)
    game_grid.draw_grid(window)
    key = None
    game_run = True

    while game_run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_RETURN:
                    if game_grid.curr_selected:
                        row, col = game_grid.curr_selected
                        game_grid.put_value(game_grid.cells[row][col].temp)
                if event.key == pygame.K_DELETE:
                    game_grid.remove_value()
                    key = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = game_grid.get_clicked_cell(pos)
                if clicked:
                    game_grid.select_cell(clicked[0], clicked[1])
                    game_grid.cells[clicked[0]][clicked[1]].draw(window)
                    key = None

            if game_grid.curr_selected and key:
                game_grid.mark_value(key)

            game_grid.draw_grid(window)

        pygame.display.update()


main()
pygame.quit()
