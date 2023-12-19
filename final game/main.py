#this file was created by: Teo Leclair
# source: 
# python library
# ChatGPT
# Cozort
# Joseph
# Chris Bradfield
# replit https://docs.replit.com/tutorials/python/build-card-game-pygame
# code review https://codereview.stackexchange.com/questions/217109/card-game-using-pygame-module
 
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
deck_rect = pygame.Rect((700,100), (int(238 * 0.8), int(332 * 0.8)))
 
# initialize message
deck_message_display = False
deck_message_timer = 0
deck_message_duration = 90  #in frames
meld_message_display = False
meld_message_timer = 0
meld_message_duration = 90  #in frames
 
def draw_button(window, button_position, button_size, button_text, button_color):
    font = pygame.font.SysFont('comicsans', 30)
    button_rect = pygame.Rect(button_position, button_size)
    pygame.draw.rect(window, button_color, button_rect)
 
    text_surface = font.render(button_text, True, (255, 255, 255))  # White text
    text_rect = text_surface.get_rect(center=button_rect.center)
    window.blit(text_surface, text_rect)
 
    return button_rect
 
 
def display_hand(hand, x_start, y, window, scale_factor=0.3, card_spacing=None):
    if card_spacing is None:
        card_width = int(238 * scale_factor)
        card_spacing = card_width  # Set spacing equal to the card width to avoid overlap
 
    card_rects = []
    for i, card in enumerate(hand):
        card_width, card_height = int(238 * scale_factor), int(332 * scale_factor)#sizing cards
        card_image = pygame.transform.scale(card.image, (card_width, card_height))
        card_pos = (x_start + i * card_spacing, y)
        window.blit(card_image, card_pos)
        card_rects.append(pygame.Rect(card_pos, (card_width, card_height)))#keeping track of where cards are
    return card_rects
 
def display_melds(melds, start_x, start_y, window):
    x, y = start_x, start_y
    meld_counter = 0  # Counter to track the number of melds displayed
 
    for meld in melds:
        for card in meld:
            card_image = pygame.transform.scale(card.image, (int(248 * 0.25), int(332 * 0.25)))  # Smaller size for melds
            window.blit(card_image, (x, y))
            x += int(248 * 0.25) + 2  # spacing
 
        meld_counter += 1
        y += int(332 * 0.25) + 2  # Move down to the next line for the next meld
        x = start_x  # Reset x to start position
 
        # Check if 3 melds have been displayed, then move to the next column
        if meld_counter % 3 == 0: #check for multiple of three
            x += int(248 * 0.65) + 10  # Move to the next column
            y = start_y  # Reset y to the start position for the new column
 
 
 
def render_game(window):
    window.fill((34, 139, 34))  # Background color
 
    font = pygame.font.SysFont('comicsans', 60, True)
    small_font = pygame.font.SysFont('comicsans', 20, True)
 
    if deck_message_display:
        warning_text = "Maximum hand size reached. Cannot draw more cards."
        warning_msg = small_font.render(warning_text, True, (255, 0, 0))  # Red color for the warning message
        window.blit(warning_msg, (100, 100))  # Adjust position as needed
    
    if meld_message_display:
        warning_text = "Invalid meld. Try three of a kind or a straight"
        warning_msg = small_font.render(warning_text, True, (255, 0, 0))  # Red color for the warning message
        window.blit(warning_msg, (100, 150))  # Adjust position as needed
 
    # Coordinates for player names and card hands
    y_coord_hand_1 = 425
    y_coord_hand_2 = 550
 
    # Display player 1's hand
    text = small_font.render(gameEngine.player_1.name + " (" + str(len(gameEngine.player_1.hand)) + " cards):", True, (255, 255, 255))
    window.blit(text, (10, y_coord_hand_1))  # Player 1 name and card count on the far left
    gameEngine.player_1.rects = display_hand(gameEngine.player_1.hand, 10 + text.get_width(), y_coord_hand_1, window)
 
    # Display player 2's hand
    text = small_font.render(gameEngine.player_2.name + " (" + str(len(gameEngine.player_2.hand)) + " cards):", True, (255, 255, 255))
    window.blit(text, (10, y_coord_hand_2))  # Player 2 name and card count on the far left
    gameEngine.player_2.rects = display_hand(gameEngine.player_2.hand, 10 + text.get_width(), y_coord_hand_2, window)
 
    if gameEngine.deck.length():
        deck_rect = display_deck(window)
 
    # Display melds for each player
    display_melds(gameEngine.player_1.melds + gameEngine.player_2.melds, 50, 100, window)  # Adjust coordinates as needed
 
    # Assuming each card has a property or method like 'name' to represent it as a string
    selected_cards_str = ', '.join([card.name for card in gameEngine.currentPlayer.last_three_clicked_cards])
    text = small_font.render("Selected cards: " + selected_cards_str, True, (255, 255, 255))
 
    window.blit(text, (20, 50))
 
    if gameEngine.game_over:
        # If the game is over, display the winner and game over message
        p1_score = gameEngine.player_1.calculate_hand_score()
        p2_score = gameEngine.player_2.calculate_hand_score()
 
        if p1_score > p2_score:
            winner = "player 1"
        else:
            winner = "player 2"
 
        message = "Game Over! " + winner + " wins!"
        text = font.render(message, True, (255, 165, 0))
        window.blit(text, (20, 50))
 
        pygame.time.wait(5000)  # Wait for 5 seconds
        exit()
    else:
        return 0
 
def get_clicked_card(x, y, card_rects, cards): #for card
    for rect, card in zip(card_rects, cards):
        if rect.collidepoint(x, y): #checking for collide inside cordinates x and y
            return card
    return None #no match found return none
 
def get_clicked_deck(x, y):
    if deck_rect.collidepoint(x,y):
        return True
    else:
        return False
 
def display_deck(window):
    card_pos = (700,100)
    window.blit(cardBack, card_pos)
 
# Main game loop
run = True
while run:
    key = None
 
    # Pygame events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse click
                mouse_x, mouse_y = event.pos
                if quit_button.collidepoint(mouse_x, mouse_y):
                    run = False  # Quit the game
 
                if end_turn_button.collidepoint(mouse_x, mouse_y):
                    # Logic to handle end of players turn
                    print("End Turn button clicked")
                    gameEngine.switch_player() #switcehs player
                    gameEngine.currentPlayer.last_three_clicked_cards = [] #when turn is over- reset 
 
                if submit_meld_button.collidepoint(mouse_x, mouse_y): #Logic for collison with meld check
                    selected_cards = gameEngine.currentPlayer.last_three_clicked_cards
                    if gameEngine.is_valid_meld(selected_cards):
                        gameEngine.currentPlayer.melds.append(selected_cards)
                        # Removes vaild meld of players hand
                        for card in selected_cards:
                            gameEngine.currentPlayer.hand.remove(card)
                        print("Meld submitted successfully.")
                        gameEngine.currentPlayer.last_three_clicked_cards = []
 
                    else:
                        meld_message_display = True
                        meld_message_timer = meld_message_duration
                clicked_card = get_clicked_card(mouse_x, mouse_y, gameEngine.currentPlayer.rects, gameEngine.currentPlayer.hand)
                #identifies when player click on hand
                if clicked_card:
                    # Check if the card is already in the last three clicked cards
                    if clicked_card in gameEngine.currentPlayer.last_three_clicked_cards:
                        # Remove the card if it's already there
                        gameEngine.currentPlayer.last_three_clicked_cards.remove(clicked_card)
                    else:
                        # Add the clicked card to the last three clicked cards list
                        gameEngine.currentPlayer.last_three_clicked_cards.append(clicked_card)
                        # Keep only the last three cards
                        gameEngine.currentPlayer.last_three_clicked_cards = gameEngine.currentPlayer.last_three_clicked_cards[-3:]
                if get_clicked_deck(mouse_x, mouse_y):
                    if len(gameEngine.currentPlayer.hand) >= 10: #doesnt allow more than 10 cards
                        deck_message_display = True
                        deck_message_timer = deck_message_duration # display message for some time
                    else:
                        gameEngine.currentPlayer.draw_card(gameEngine.deck)
 
    # Inside the game loop
    if len(gameEngine.player_1.hand) == 0 or len(gameEngine.player_2.hand) == 0:#if a player hand empty then game is over
        gameEngine.game_over = True

 
    if deck_message_display: #for how long message is displayed for too many cards
        if deck_message_timer > 0:
            deck_message_timer -= 1
        else:
            deck_message_display = False
 
    if meld_message_display:#invalid meld message timer
        if meld_message_timer > 0:
            meld_message_timer -= 1
        else:
            meld_message_display = False
 
    # Calling the play method of the game engine with the pressed key
    gameEngine.play(key)
 
    # Rendering the game window
    render_game(window)
 
    # Draw the quit button and get its rect
    submit_meld_button = draw_button(window, (700, 700), (150, 50), "Submit Meld", (0, 0,255))# Inside the main game loop
    end_turn_button = draw_button(window, (500, 700), (150, 50), "End Turn", (0, 100, 200))
    quit_button = draw_button(window, (900, 700), (100, 50), "Quit", (255, 0, 0))
 
    # Updating the display
    pygame.display.update()