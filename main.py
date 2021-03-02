import pygame
from game import Game

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


class GameRunner:
    def __init__(self):
        pygame.init()
        self.game = None
        self.game_running = False

    def run_game(self):
        self.game = Game()
        self.game_running = True

        self.game.draw_sudoku_grid()
        self.game.draw_game(board)
        pygame.display.flip()

        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game.update_game_state()
                    print('game update')
                if event.type == pygame.KEYDOWN:
                    self.game.update_game_state(trigger=True)
                    print('game special update')
        pygame.quit()


runner = GameRunner()
runner.run_game()
