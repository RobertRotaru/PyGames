import pygame
import os
import math
import random

# Set the window
pygame.init()
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)

# Load images
images = []
for i in range(7):
    img = pygame.image.load(f'images/hangman{i}.png')
    images.append(img)

# Game variables
hangman_status = 0
words = ["PAGE", "DOG", "CAT", "BED", "TEETH", "TSHIRT", "BLANCKET", "NOSE", "BRUSH", "DOOR", "WINDOW", "BOX", "PHONE", "RADIO", "BOOK", "MIRROR", "PICTURE", "FRAME", "FOCUS", "PATERN", "DIRECTION", "CASTLE", "HAT", "BACKPACK", "CACTUS", "CLOCK"]
word = random.choice(words)
guessed = []

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Draw
def draw():
    window.fill(WHITE)

    # Draw title
    text = TITLE_FONT.render("HANGMAN", True, BLACK)
    window.blit(text, (WIDTH / 2 - text.get_width() / 2, 30))

    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, True, BLACK)
    window.blit(text, (400, 200))

    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(window, BLACK, (x, y), RADIUS, 2)
            text = LETTER_FONT.render(ltr, True, BLACK)
            window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    window.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    window.fill(WHITE)
    text = WORD_FONT.render(message, True, BLACK)
    window.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)

# Game loop
running = True
FPS = 60
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    draw()

    if won:
        display_message("You won!")
        break

    if hangman_status == 6:
        display_message("You lost!")
        break


pygame.quit()
