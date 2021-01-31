import pygame, time
# SRCALPHA
from pygame.locals import *

from panza import Panza
from collections import defaultdict

def test (panzaSizeInPixels: int, windowSize: tuple, playerCount: int) -> None:
  panzas = defaultdict(dict)
  for x in range (playerCount):
    panzas [x] = Panza (None, panzaSizeInPixels, windowSize, x)

  screen = pygame.display.set_mode(windowSize,flags=SRCALPHA)

  # Fill the background with white
  screen.fill((255, 255, 255, 255))

  # Draw a solid blue circle in the center
  for index in panzas:
    panzas[index].render (screen)

  pygame.display.flip()



pygame.init()
windowSize = (1280,720)
panzaSizeInPixels = 200
test (panzaSizeInPixels, windowSize, 2)
time.sleep(10)
pygame.quit()