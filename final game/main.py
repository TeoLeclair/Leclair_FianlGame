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


import tkinter as tk
from tkinter import messagebox
import random
class Rummy:
    def create_board(self):
        for i in range(4):
            for j in range(4):
                button = tk.Button(self.root, text=" ", width=5, height=2, command=lambda i=i, j=j: self.flip_card(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)
    def create_deck():
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [f'{rank} of {suit}' for suit in suits for rank in ranks]
    def shuffle_deck(deck):
        random.shuffle(deck)
        return deck
def deal_cards(deck, num_cards):
    return [deck.pop() for _ in range(num_cards)]

def print_hand(hand):
    print("Your hand:")
    for card in hand:
        print(card)

def main():
    deck = create_deck()
    shuffled_deck = shuffle_deck(deck)

    player_hands = {
        'Player 1': deal_cards(shuffled_deck, 7),
        'Player 2': deal_cards(shuffled_deck, 7)
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

if __name__ == "__main__":
    main()


