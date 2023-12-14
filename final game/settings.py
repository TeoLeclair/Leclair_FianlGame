# game settings
import pygame
from models import Deck, Player, Card

class RummyEngine:
  def __init__(self):
    # Initializing the RummyEngine with a shuffled deck, players, dealing cards, and initial settings
    self.deck = Deck()
    self.deck.shuffle()
    self.player_1 = Player("Player 1")
    self.player_2 = Player("Player 2")
    self.deal()
    self.currentPlayer = self.player_1
    self.game_over = False

  def deal(self):
    # Dealing cards to players during initialization
    for i in range(7):
      self.player_1.draw_card(self.deck)
      self.player_2.draw_card(self.deck)

  def switch_player(self):
    # Switching the current player for the next turn
    if self.currentPlayer == self.player_1:
      self.currentPlayer = self.player_2
    else:
      self.currentPlayer = self.player_1

  # TODO: Implement game logic
  def play(self, key):
    # Handling player input during the game
    if key is None:
      return
    if self.game_over:
      return

    

