import pygame
import time
# SRCALPHA
from pygame.locals import *

from panza import Panza


def test(panzaSizeInPixels: int, windowSize: tuple, playerCount: int) -> None:
    panzas = {}
    for x in range(playerCount):
        panzas[x] = Panza(None, panzaSizeInPixels, windowSize, x)

    window = pygame.display.set_mode(windowSize, flags=SRCALPHA)

    # Fill the background with white
    window.fill((255, 255, 255, 255))

    # Draw a solid blue circle in the center
    for index in panzas:
        panzas[index].render(window)

    pygame.display.flip()


pygame.init()
windowSize = (1280, 720)
panzaSizeInPixels = 200
test(panzaSizeInPixels, windowSize, 2)
time.sleep(10)
pygame.quit()
