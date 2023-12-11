# if __name__ == "__main__":
#         main()
import pygame
import sys
import os

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
GREEN = (34, 139, 34)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gin Rummy")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Load card images
# You need to have card images in the same directory as this script
# Replace 'card_back.png' with the actual file name of the card back image
card_back = pygame.image.load(os.path.join(img_folder, 'BACK.png')).convert()

# Game variables
player_hand = ['Card1', 'Card2', 'Card3']  # Example cards in the player's hand
computer_hand = ['Card4', 'Card5', 'Card6']  # Example cards in the computer's hand

# Functions
def draw_card(x, y):
    screen.blit(card_back, (x, y))

def draw_hand(hand, is_player=True):
    # Draw the player's hand
    x = 50 if is_player else 50
    y = 400 if is_player else 50

    for card in hand:
        draw_card(x, y)
        x += 20 if is_player else 50

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic here

    # Drawing code
    screen.fill(GREEN)
    draw_hand(player_hand)
    draw_hand(computer_hand, is_player=False)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()


