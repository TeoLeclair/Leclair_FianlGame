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
    self.player_1_rects = []
    self.player_2_rects = []
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
 
  def is_valid_meld(self, cards):
    if len(cards) != 3: #if card number chosen is not 3 return false
        return False
 
    # Check for three of a kind
    if all(card.value == cards[0].value for card in cards): #check first card value then check next two if match
        if len(set(card.suit for card in cards)) == 3: #make sure we have three suits
            return True
    if all(card.suit == cards[0].suit for card in cards):#three of a kind suit is valid
      return True
 
    # Check for a straight of three
    cards = sorted(cards, key=lambda card: card.points)  # sorting cards before check 
    if all(cards[i+1].points == cards[i].points + 1 for i in range(2)):#check to make sure card value only 1 different
        return True
 
    return False
 
  def play(self, key):
    # Handling player input during the game
    if key is None:
      return
    if self.game_over:
      return