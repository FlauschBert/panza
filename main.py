# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame import time
# SRCALPHA
from pygame.locals import *

from panza import Panza


def initPanzas(panzaSizeInPixels: int, windowSize: tuple) -> dict[int,Panza]:
    # Initialize all joysticks connected right now
    pygame.joystick.init()

    if pygame.joystick.get_count() < 2:
        print("At least two joysticks have to be connected")
        return {}

    panzas = {}
    for x in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(x)
        print("Found joystick {}".format(joystick.get_instance_id()))
        # we have to hold the created joystick instance here alive,
        # otherwise no events are sent
        panzas[joystick.get_instance_id()] = Panza(joystick, panzaSizeInPixels, windowSize, x)

    return panzas


def main() -> None:
    pygame.init()

    windowSize = (1280, 720)
    panzaSizeInPixels = 200

    # Initialize all joysticks connected right now
    # and remember instance id as dictionary key
    panzas = initPanzas(panzaSizeInPixels, windowSize)
    if len(panzas) < 2:
        pygame.quit()
        return

    # Set up the drawing window
    window = pygame.display.set_mode(size=windowSize, flags=SRCALPHA)

    # Run until the user asks to quit
    running = True
    ticks = time.get_ticks()
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONUP:
                print("id {} fire button".format(event.instance_id))

        # Fill the background with white
        window.fill((255, 255, 255, 255))

        # Update speed and direction
        for index in panzas:
            panzas[index].update(time.get_ticks() - ticks)
        ticks = time.get_ticks()

        # Draw a solid blue circle in the center
        for index in panzas:
            panzas[index].render(window)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


main()
