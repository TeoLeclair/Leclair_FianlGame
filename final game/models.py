from enum import Enum #Enum for enumerations (which we'll use for defining the card suits).
import pygame #pygame, to load up the card images.
import random#random, to use when we shuffle the deck.
from settings import *

class Suits(Enum):
  CLUB = 0
  SPADE = 1
  HEART = 2
  DIAMOND = 3

  class Card:
  suits = None
  value = None
  image = None

  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
    self.image = pygame.image.load('images/' + self.suit.name + '-' + str(self.value) + '.svg')

    class Deck:
  cards = None

  def __init__(self):
    self.cards = []
    for suit in Suits:
      for value in range(1,14):
        self.cards.append(Card(suit, value))

  def shuffle(self):
    random.shuffle(self.cards)

  def deal(self):
    return self.cards.pop()

  def length(self):
    return len(self.cards)