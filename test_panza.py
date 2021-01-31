import pygame
from panza import Panza
from collections import defaultdict

def test (playerCount: int, windowSize: tuple) -> None:
  panzas = defaultdict(dict)
  for x in range (playerCount):
    panzas [x] = Panza (None, windowSize, x)

pygame.init()
windowSize = (500,500)
pygame.display.set_mode(windowSize)
test (2, windowSize)
pygame.quit()