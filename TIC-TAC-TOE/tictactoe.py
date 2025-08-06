import numpy as np
import pygame
import math

ROWS = 3
COLUMNS = 3
HEIGHT = 600  # Fixed typo (was HIEGHT)
WIDTH = 600
SIZE = (WIDTH, HEIGHT)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

CIRCLE = pygame.image.load('circle.png')
CROSS = pygame.image.load('x.png')

def mark(rows, columns, player):
    board[rows][columns] = player

def is_valid_mark(rows, columns):  # Fixed parameter name from 'colums' to 'columns'
    return board[rows][columns] == 0

def is_board_full():
    for i in range(ROWS):
        for j in range(COLUMNS):
            if board[i][j] == 0:
                return False
    return True

def draw_board():
    for i in range(COLUMNS):
        for j in range(ROWS):
            if board[j][i] == 1:
                window.blit(CIRCLE, ((i * 200) + 50, (j * 200) + 50))
            elif board[j][i] == 2:
                window.blit(CROSS, ((i * 200) + 50, (j * 200) + 50))
    pygame.display.update()

def is_winning_move(player):
    if player == 1:
        win_color = BLUE
    else:
        win_color = RED

    for i in range(ROWS):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            pygame.draw.line(window, win_color, (10, (i * 200) + 100), (WIDTH - 10, (i * 200) + 100), 10)
            return True

    for j in range(COLUMNS):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            pygame.draw.line(window, win_color, ((j * 200) + 100, 10), ((j * 200) + 100, HEIGHT - 10), 10)
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        pygame.draw.line(window, win_color, (10, 10), (590, 590), 10)
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        pygame.draw.line(window, win_color, (590, 10), (10, 590), 10)
        return True

def draw_lines():
    pygame.draw.line(window, BLACK, (200, 0), (200, 600), 10)
    pygame.draw.line(window, BLACK, (400, 0), (400, 600), 10)
    pygame.draw.line(window, BLACK, (0, 200), (600, 200), 10)
    pygame.draw.line(window, BLACK, (0, 400), (600, 400), 10)

board = np.zeros((ROWS, COLUMNS))

game_over = False
turn = 0

pygame.init()
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("TIC-TAC-TOE")
window.fill(WHITE)
draw_lines()
pygame.display.update()
pygame.time.wait(2000)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # Ensures program exits fully

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

            row = math.floor(event.pos[1] / 200)
            col = math.floor(event.pos[0] / 200)

            if turn % 2 == 0:
                if is_valid_mark(row, col):
                    mark(row, col, 1)
                    if is_winning_move(1):
                        game_over = True
                else:
                    turn = turn - 1
            else:
                if is_valid_mark(row, col):
                    mark(row, col, 2)
                    if is_winning_move(2):
                        game_over = True
                else:
                    turn = turn - 1

            turn = turn + 1
            print(board)
            draw_board()

    if is_board_full():
        game_over = True

    if game_over == True:
        print("Game Over")
        pygame.time.wait(2000)
        board.fill(0)
        window.fill(WHITE)
        draw_lines()
        draw_board()
        game_over = False
        pygame.display.update()





