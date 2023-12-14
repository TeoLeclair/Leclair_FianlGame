#this file was created by: Teo Leclair
# source: 
# python library
# Cozort
# Joseph
# Chris Bradfield
# ChatGPT
 
# Title:
# Rummy
 
# Overview: 
# create basic impleation of card game rummy
 
# Goals:
# Game Design
# -card images
# -buttons
# Code game logic
# - shuffling
# - dealing
# - turns
# - scoring
# - winning
# Interaction
# - how should player interact with cards, deck, etc
# Opponent
# - implement turn based 2 player or simple AI opponent
# Game loop
# - update game, redraw
 
 
import random
import os
import pygame
from models import *  # calling code from models
from settings import * #calling code from settings 
# Initializing the Rummy game engine
gameEngine = RummyEngine()
# Initializing Pygame
pygame.init()
 
# folder paths
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
 
# Setting up window dimensions
bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Rummy")
 
# uploading back of card image and building measurments
cardBack = pygame.image.load(os.path.join(img_folder, 'BACK.png')).convert()
cardBack = pygame.transform.scale(cardBack, (int(238 * 0.8), int(332 * 0.8)))
smallCard = pygame.transform.scale(cardBack, (int(238 * 0.3), int(332 * 0.3)))
 
 
def display_hand(hand, x_start, y, window, scale_factor=0.5, card_spacing=40):
   card_rects = []
   for i, card in enumerate(hand):
       card_width, card_height = int(238 * scale_factor), int(332 * scale_factor)
       card_image = pygame.transform.scale(card.image, (card_width, card_height))
       card_pos = (x_start + i * card_spacing, y)
       window.blit(card_image, card_pos)
       card_rects.append(pygame.Rect(card_pos, (card_width, card_height)))
   return card_rects 
 
 
def render_game(window):
    window.fill((34, 139, 34))  # Background color
 
    font = pygame.font.SysFont('comicsans', 60, True)
 
    # Display player 1's hand at the bottom of the screen
    display_hand(gameEngine.player_1.hand, 45, 650, window)
 
    # Display player 2's hand (or the back of the cards if you want to hide them)
    display_hand(gameEngine.player_2.hand, 600, 650, window)
 
 
    # number of cards for each player
    text = font.render(str(len(gameEngine.player_1.hand)) + " cards", True, (255, 255, 255))
    window.blit(text, (100, 500))
    text = font.render(str(len(gameEngine.player_2.hand)) + " cards", True, (255, 255, 255))
    window.blit(text, (700, 500))
 
    if gameEngine.game_over:
        # If the game is over, display the winner and game over message
        p1_score = gameEngine.player_1.calculate_hand_score()
        p2_score = gameEngine.player_2.calculate_hand_score()
 
        # TODO: Calculate melds and decide the winner based on scores
        if p1_score > p2_score:
            winner = "player 1"
        else:
            winner = "player 2"
 
        message = "Game Over! " + winner + " wins!"
        text = font.render(message, True, (255, 255, 255))
        window.blit(text, (20, 50))
    else:
        return 0
        # TODO: 

def get_clicked_card(x, y, card_rects, cards):
   for rect, card in zip(card_rects, cards):
    if rect.collidepoint(x, y):
        return card
   return None
 
# Main game loop
run = True
while run:
    key = None
 
    # Pygame events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 1:  # Left mouse click
                 mouse_x, mouse_y = event.pos
                 clicked_card = get_clicked_card(mouse_x, mouse_y, gameEngine.player_1.hand_card_rects, gameEngine.player_1.hand)
    if get_clicked_card:
               print("Clicked card:", get_clicked_card)
               # Handle the clicked card here
    if event.type == pygame.KEYDOWN:
            key = event.key
 
    # Calling the play method of the game engine with the pressed key
    gameEngine.play(key)
 
    # Rendering the game window
    render_game(window)
 
    # Updating the display
    pygame.display.update()