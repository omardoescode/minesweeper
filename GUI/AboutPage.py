import json
import pygame
import sys

# Dictionary to hold the credits of each creator
credits = {
    "Omar Mohammed": "Creator 1",
    "Mohammed Waleed": "Creator 2",
    "Ahmed Youssef": "Creator 3",
    "Omar Hisham": "Creator 4"
}

# Function to display the credits
def display_credits():
    print("Credits:")
    for person, role in credits.items():
        print(f"{person}: {role}")

def check_credits():
    try:
        with open('credits.json', 'r') as file:
            return True
    except FileNotFoundError:
        return False

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 28)

# Function to display the credits in a Pygame window
def display_credits_gui():
    credits_data = retrieve_credits()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Credits')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        text_y = 20
        for person, role in credits_data.items():
            text = f"{person}: {role}"
            text_surface = FONT.render(text, True, BLACK)
            screen.blit(text_surface, (20, text_y))
            text_y += 30

        pygame.display.flip()

    pygame.quit()
