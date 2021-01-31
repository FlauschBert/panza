# Simple pygame program

# Import and initialize the pygame library
import pygame
from panza import Panza
from collections import defaultdict

def initPanzas () -> defaultdict(dict):
  # Initialize all joysticks connected right now
  pygame.joystick.init()

  if pygame.joystick.get_count() < 2:
    print ("At least two joysticks have to be connected")
    return defaultdict(dict)

  panzas = defaultdict(dict)
  for x in range (pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick (x)
    print ("Found joystick {}".format(joystick.get_instance_id ()))
    # we have to hold the created joystick instance here alive,
    # otherwise no events are sent
    panzas [joystick.get_instance_id ()] = Panza (joystick, x)

  return panzas


def main () -> None:
  pygame.init()

  # Initialize all joysticks connected right now
  # and remember instance id as dictionary key
  panzas = initPanzas ()
  if len (panzas) < 2:
    pygame.quit ()
    return

  # Set up the drawing window
  screen = pygame.display.set_mode(size=[500, 500])

  # Run until the user asks to quit
  running = True
  while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.JOYAXISMOTION:
        panzas [event.instance_id].update (axis=event.axis, value=event.value)
      elif event.type == pygame.JOYBUTTONUP:
        print ("id {} fire button".format (event.instance_id)) 

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(surface=screen, color=(0, 0, 255), center=(250,250), radius=75)

    # Flip the display
    pygame.display.flip()

  # Done! Time to quit.
  pygame.quit()


main ()