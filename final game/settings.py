# game settings
from enum import Enum
import pygame
from models import *

class GameState(Enum):
  PLAYING = 0
  SNAPPING = 1
  ENDED = 2

class SnapEngine:
  deck = None
  player1 = None
  player2 = None
  pile = None
  state = None
  currentPlayer = None
  result = None
  
    

