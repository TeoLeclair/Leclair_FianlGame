from enum import Enum #Enum for enumerations (which we'll use for defining the card suits).
import pygame #pygame, to load up the card images.
import random#random, to use when we shuffle the deck.
 
 
class Card:
  # Initializing a card with suit, value, points, and loading its image
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
    points_table = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':15, 'Q':15, 'K':15, 'A':15}
    self.points = points_table[value]
    self.image = pygame.image.load('images/' + str(self.suit) + '-' + str(self.value) + '.svg')
 
class Deck:
  def __init__(self):
    self.cards = []
    for suit in ['CLUB', 'DIAMOND', 'SPADE', 'HEART']:
      for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
        self.cards.append(Card(suit, value))
 
  def shuffle(self):
    random.shuffle(self.cards)
 
  def deal(self):
    return self.cards.pop()
 
  def length(self):
    return len(self.cards)
 
class Player:
  def __init__(self, name):
    self.name = name
    self.hand = []
    self.melds = []
 
  def draw_card(self, deck): # Draws a card from the deck and adds it to the player's hand
    if deck.length() > 0:
      card = deck.deal()
      self.hand.append(card)
      return card
    else:
      return None
 
  def print_hand(self):
      for card in self.hand:
        print(f"{card.value} of {card.suit.name}")
 
  def calculate_hand_score(self):
      """Calculates and returns the score of the hand."""
      # Placeholder for score calculation logic
      score = 0
      for card in self.hand:
        score += card.points