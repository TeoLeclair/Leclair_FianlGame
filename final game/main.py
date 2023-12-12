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
from models import *
from settings import *
gameEngine = RummyEngine()
 
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
pygame.init()
bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Rummy")
cardBack = pygame.image.load(os.path.join(img_folder, 'BACK.png')).convert()
cardBack = pygame.transform.scale(cardBack, (int(238*0.8), int(332*0.8)))
 
def render_game(window):
  window.fill((15,0,169))
  font = pygame.font.SysFont('comicsans',60, True)
 
  window.blit(cardBack, (100, 200))
  window.blit(cardBack, (700, 200))
 
  text = font.render(str(len(gameEngine.player_1.hand)) + " cards", True, (255,255,255))
  window.blit(text, (100, 500))
 
  text = font.render(str(len(gameEngine.player_2.hand)) + " cards", True, (255,255,255))
  window.blit(text, (700, 500))
 
  if gameEngine.game_over:
    p1_score = gameEngine.player_1.calculate_hand_score()
    p2_score = gameEngine.player_2.calculate_hand_score()
    # TODO calculate melds? idk
    if p1_score > p2_score:
      winner = "player 1"
    else:
      winner = "player 2"
    message = "Game Over! " + winner + " wins!"
    text = font.render(message, True, (255,255,255))
    window.blit(text, (20,50))
  else:
    return 0
    # TODO: rest of game logic
 
 
run = True
while run:
  key = None
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      key = event.key
  gameEngine.play(key)
  render_game(window)
  pygame.display.update()