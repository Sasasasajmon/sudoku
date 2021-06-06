import pygame
import graphic
from GUI_values import *


class Game:

    def __init__(self):
        self.window = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
        self.game_font = pygame.font.SysFont("monospace", 24)
        self.game_grid = None

    def draw_sudoku_grid(self):
        outer_rect = pygame.Rect(MARGIN, MARGIN, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(self.window, BLACK, outer_rect, CONTRAST_WIDTH)

        first_inner_line_pos = MARGIN + GRID_SIZE * 0.333
        second_inner_line_pos = MARGIN + GRID_SIZE * 0.666

        pygame.draw.line(self.window, BLACK, [MARGIN, first_inner_line_pos], [GRID_SIZE + MARGIN, first_inner_line_pos],
                         CONTRAST_WIDTH)
        pygame.draw.line(self.window, BLACK, [MARGIN, second_inner_line_pos],
                         [GRID_SIZE + MARGIN, second_inner_line_pos],
                         CONTRAST_WIDTH)
        pygame.draw.line(self.window, BLACK, [first_inner_line_pos, MARGIN], [first_inner_line_pos, GRID_SIZE + MARGIN],
                         CONTRAST_WIDTH)
        pygame.draw.line(self.window, BLACK, [second_inner_line_pos, MARGIN],
                         [second_inner_line_pos, GRID_SIZE + MARGIN],
                         CONTRAST_WIDTH)

    def draw_game(self, board_scheme):
        self.game_grid = graphic.get_game_grid(board_scheme)
        self.game_grid.group.draw(self.window)
        self.update_game_state()
        self.draw_sudoku_grid()

    def update_game_state(self, trigger=None):
        self.game_grid.group.update(self.window, self.game_font, trigger)
