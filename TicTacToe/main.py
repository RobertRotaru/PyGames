import pygame
import numpy as np
import random
import time


# Initialize
pygame.init()

# Screen
window = pygame.display.set_mode((600, 600))

# Background color
window.fill((255, 255, 255))

# Title and icon
pygame.display.set_caption("Tic-Tac Toe")
icon = pygame.image.load("tic-tac-toe.png")
pygame.display.set_icon(icon)

# Title
font = pygame.font.Font("magnificent.ttf", 48)
titleX = 183
titleY = 50

# Grid
grid = np.zeros((3, 3), dtype=np.int32)
positions = [(150, 151), (250, 151), (350, 151), (150, 251), (250, 251), (350, 251), (150, 351), (250, 351), (350, 351)]

# X and O
x = pygame.image.load("x_player.png")
o = pygame.image.load("o_computer.png")
red_x = pygame.image.load("red_x.png")
red_o = pygame.image.load("red_o.png")

# Turn
turn = 1
game_over = 0

# Scores
player_score = 0
computer_score = 0
s_font = pygame.font.Font("scores.otf", 20)
plX = 10
plY = 10
cpX = 480
cpY = 10

# Lower Text
l_font = pygame.font.Font("magnificent.ttf", 36)
textX = 200
textY = 475
cur_textX = textX
cur_textY = textY

# Play Again Button
paX = 225
paY = 535
cur_paX = 2000
cur_paY = 2000

# Show play again
def show_p_a(x, y):
    text = l_font.render("Play Again", True, (0, 0, 0))
    window.blit(text, (x, y))

def show_p_score(x, y):
    text = s_font.render("Player: {}".format(player_score), True, (0, 0, 0))
    window.blit(text, (x, y))

def show_c_score(x, y):
    text = s_font.render("Computer: {}".format(computer_score), True, (0, 0, 0))
    window.blit(text, (x, y))

def show_text(winner, x, y):
    text = l_font.render(winner, True, (0, 0, 0))
    window.blit(text, (x, y))

def show_title(x, y):
    title = font.render("Tic-Tac Toe", True, (0, 0, 0))
    window.blit(title, (x, y))

def choice_pos():
    rowSum = np.sum(grid, axis=1)
    colSum = np.sum(grid, axis=0)

    # Checking rows and cols
    for i in range(3):
        if rowSum[i] == -2:
            for j in range(3):
                if grid[i][j] == 0:
                    return i, j
        elif rowSum[i] == 2:
            for j in range(3):
                if grid[i][j] == 0:
                    return i, j
        if colSum[i] == -2:
            for j in range(3):
                if grid[j][i] == 0:
                    return j, i
        elif colSum[i] == 2:
            for j in range(3):
                if grid[j][i] == 0:
                    return j, i

    # Checking first diagonal
    sum = 0
    for i in range(3):
        sum += grid[i][i]
    if sum == -2:
        for i in range(3):
            if grid[i][i] == 0:
                return i, i
    elif sum == 2:
        for i in range(3):
            if grid[i][i] == 0:
                return i, i

    # Checking second diagonal
    sum = 0
    for i in range(3):
        sum += grid[i][2 - i]
    if sum == -2:
        for i in range(3):
            if grid[i][2 - i] == 0:
                return i, 2 - i
    elif sum == 2:
        for i in range(3):
            if grid[i][2 - i] == 0:
                return i, 2 - i

    # Choosing a random value
    p = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                p.append((i, j))
    if len(p) > 0:
        return random.choice(p)
    return None

# Make the winning row/col/diagonal red
def make_red(index, type, whatis):
    if type == 1: # is row
        for j in range(3):
            grid[index][j] = 2 * whatis
    elif type == 2: # is col
        for j in range(3):
            grid[j][index] = 2 * whatis
    elif type == 3: # is first diagonal
        for j in range(3):
            grid[j][j] = 2 * whatis
    elif type == 4: # is second diagonal
        for j in range(3):
            grid[j][2 - j] = 2 * whatis

# Analysis
def analise():
    global player_score, computer_score

    rowSum = np.sum(grid, axis=1)
    colSum = np.sum(grid, axis=0)

    # Checking rows and cols
    for i in range(3):
        if rowSum[i] == 3:
            make_red(i, 1, 1)
            return "Player wins!"
            break
        elif rowSum[i] == -3:
            make_red(i, 1, -1)
            return "Computer wins!"
            break
        if colSum[i] == 3:
            make_red(i, 2, 1)
            return "Player wins!"
            break
        elif colSum[i] == -3:
            make_red(i, 2, -1)
            return "Computer wins!"
            break

    # Checking diagonals
    sumFirst = 0
    sumSecond = 0
    for i in range(3):
        sumFirst += grid[i][i]
        sumSecond += grid[i][2 - i]
    if sumFirst == 3:
        make_red(1, 3, 1)
        return "Player wins!"
    elif sumFirst == -3:
        make_red(1, 3, -1)
        return "Computer wins!"
    if sumSecond == 3:
        make_red(1, 4, 1)
        return "Player wins!"
    elif sumSecond == -3:
        make_red(1, 4, -1)
        return "Computer wins!"

    # Check for draw
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return None
    return "Draw!"

# Board
board = pygame.image.load("board.png")
boardX = 150
boardY = 150

# Game Loop
running = True
winner = ""
while running:

    window.fill((255, 255, 255))

    # Showing the Board
    window.blit(board, (boardX, boardY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_over == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] > 225 and pos[0] < 325 and pos[1] > 535 and pos[1] < 565:
                    game_over = 0
                    turn = 1
                    cur_textY = 2000
                    cur_textX = 2000
                    cur_paX = 2000
                    cur_paY = 2000
                    grid = np.zeros((3, 3), dtype=np.int32)
        elif game_over == 0:
            if turn == 1:
                # Player's move
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for i in range(len(positions)):
                        if pos[0] > positions[i][0] and pos[0] < positions[i][0] + 90 and pos[1] > positions[i][1] and pos[1] < positions[i][1] + 90:
                            row = int(i / 3)
                            col = i % 3
                            if grid[row][col] == 0:
                                grid[row][col] = 1
                                turn = -1
            elif turn == -1:
                # Computer's move
                choice = choice_pos()
                if choice:
                    time.sleep(1)
                    grid[choice[0]][choice[1]] = -1
                    turn = 1

    # Make the analysis
    if game_over == 0:
        output = analise()
        if output:
            winner = output
            print(grid)
            if winner == "Player wins!":
                cur_textY = textY
                cur_textX = textX
                player_score += 1
            elif winner == "Computer wins!":
                cur_textY = textY
                cur_textX = textX
                computer_score += 1
            elif winner == "Draw!":
                cur_textX = 250
                cur_textY = textY
            cur_paX = paX
            cur_paY = paY
            game_over = 1

    # Showing the X's and O's
    for i in range(3):
        for j in range(3):
            num = i * 3 + j
            if grid[i][j] != 0:
                if grid[i][j] == 1:
                    window.blit(x, (positions[num][0], positions[num][1]))
                elif grid[i][j] == -1:
                    window.blit(o, (positions[num][0], positions[num][1]))
                elif grid[i][j] == 2:
                    window.blit(red_x, (positions[num][0], positions[num][1]))
                elif grid[i][j] == -2:
                    window.blit(red_o, (positions[num][0], positions[num][1]))

    # Showing the Title
    show_title(titleX, titleY)

    # Showing text
    show_text(winner, cur_textX, cur_textY)

    # Showing scores
    show_p_score(plX, plY)
    show_c_score(cpX, cpY)

    if cur_paX < 2000 and cur_paY < 2000:
        show_p_a(cur_paX, cur_paY)

    pygame.display.flip()
