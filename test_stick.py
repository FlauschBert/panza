import pygame
from pygame import joystick, math, draw, Surface


def init_joystick() -> joystick.Joystick or None:
    # Initialize all joysticks connected right now
    pygame.joystick.init()
    
    if pygame.joystick.get_count() < 1:
        print("No joystick connected")
        return None
    
    return pygame.joystick.Joystick(0)


def get_direction(joystick_: joystick.Joystick) -> math.Vector2:
    return math.Vector2(joystick_.get_axis(0), joystick_.get_axis(1))


def render(direction: math.Vector2, window_size: tuple, surface: Surface) -> None:
    start_pos = math.Vector2 (window_size[0]/2, window_size[1]/2)
    if direction is None or direction.length() < 0.05:
        draw.circle(surface, (255, 0, 0), start_pos, 5, 1)
    else:
        # copy, no reference
        vector = math.Vector2(direction)
        length = vector.length()
        vector.scale_to_length(length * 100)
        draw.aaline(surface, (0, 255, 0), start_pos, start_pos + vector)


def main() -> bool:
    joystick_ = init_joystick()
    if joystick_ is None:
        return False
    
    window_size = (1280, 720)
    window = pygame.display.set_mode(size=window_size)

    # Run until the user asks to quit
    running = True
    direction = None
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYAXISMOTION:
                direction = get_direction(joystick_)

        # Fill the background with white
        window.fill((255, 255, 255, 255))

        render(direction, window_size, window)

        # Flip the display
        pygame.display.flip()

    return True


pygame.init()
main()
pygame.quit()
