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

import pygame
pygame.init()
bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Rummy")
from models import *
from settings import *
import random

import os
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

gameEngine = SnapEngine()

run = True
while run:
  key = None
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      key = event.key


class Rummy:


    def create_deck():
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [f'{rank} of {suit}' for suit in suits for rank in ranks]
    def shuffle_deck(deck):
        random.shuffle(deck)
        return deck
    def deal_cards(deck, num_cards):
        return [deck.pop() for _ in range(num_cards)]

cardBack = pygame.image.load(os.path.join(img_folder, 'BACK.png')).convert()
cardBack = pygame.transform.scale(cardBack, (int(238*0.8), int(332*0.8)))

def renderGame(window):
  window.fill((15,0,169))
  font = pygame.font.SysFont('comicsans',60, True)

  window.blit(cardBack, (100, 200))
  window.blit(cardBack, (700, 200))

  text = font.render(str(len(gameEngine.player1.hand)) + " cards", True, (255,255,255))
  window.blit(text, (100, 500))

  text = font.render(str(len(gameEngine.player2.hand)) + " cards", True, (255,255,255))
  window.blit(text, (700, 500))

  topCard = gameEngine.pile.peek()
  if (topCard != None):
    window.blit(topCard.image, (400, 200))
    if gameEngine.state == GameState.PLAYING:
        text = font.render(gameEngine.currentPlayer.name + " to flip", True, (255,255,255))
    window.blit(text, (20,50))

  if gameEngine.state == GameState.SNAPPING:
    result = gameEngine.result
    if result["isSnap"] == True:
      message = "Winning Snap! by " + result["winner"].name
    else:
      message = "False Snap! by " + result["snapCaller"].name + ". " + result["winner"].name + " wins!"
    text = font.render(message, True, (255,255,255))
    window.blit(text, (20,50))

  if gameEngine.state == GameState.ENDED:
    result = gameEngine.result
    message = "Game Over! " + result["winner"].name + " wins!"
    text = font.render(message, True, (255,255,255))
    window.blit(text, (20,50))

def print_hand(hand):
    print("Your hand:")
    for card in hand:
        print(card)

def main():
    deck = Rummy.create_deck()
    shuffled_deck = Rummy.shuffle_deck(deck)

    player_hands = {
        'Player 1': Rummy.deal_cards(shuffled_deck, 7),
        'Player 2': Rummy.deal_cards(shuffled_deck, 7)
    }

    current_player = 'Player 1'
    while True:
        print(f"\n{current_player}'s turn. Enter 'p' to print your hand or 'f' to finish your turn.")
        action = input("Enter action: ").strip().lower()

        if action == 'p':
            print_hand(player_hands[current_player])
        elif action == 'f':
            current_player = 'Player 2' if current_player == 'Player 1' else 'Player 1'
        elif action == 'q':
            print("quitting game...")
            exit()
        else:
            print("Invalid action. Please enter 'p' or 'f'.")

