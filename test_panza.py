import pygame
from panza import Panza
from collections import defaultdict

def test (playerCount: int) -> None:
  panzas = defaultdict(dict)
  for x in range (playerCount):
    panzas [x] = Panza (None, x)

pygame.init()
pygame.display.set_mode(size=[500, 500])
test (2)
pygame.quit()