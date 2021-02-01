from pygame import math, joystick, Rect, Color, Surface, draw, transform
# SRCALPHA
from pygame.locals import *
from math import sqrt

# x/y size of the panza
RATIO = 0.8


class Panza:

    # INITIALIZATION

    def __initPosition(self, windowSize: tuple, playerId: int) -> math.Vector2:
        rect = Rect(0, 0, windowSize[0] / 2, windowSize[1] / 2)
        if (0 == playerId):
            return math.Vector2(rect.center)
        else:
            rect.move_ip(windowSize[0] / 2, windowSize[1] / 2)
            return math.Vector2(rect.center)

    def __initColor(self, playerId: int) -> Color:
        if 0 == playerId:
            return Color(255, 0, 0, 255)
        else:
            return Color(0, 0, 255, 255)

    def __initTankDirection(self, playerId: int) -> math.Vector2:
        if 0 == playerId:
            return math.Vector2(0, 1)
        else:
            return math.Vector2(0, -1)

    def __initGunDirection(self, playerId: int) -> math.Vector2:
        return self.__initTankDirection(playerId)

    '''Calculate size in pixels of the panza: the effective size is smaller
       than sizeInPixels because the panza has to fit in the surface
       also if it is rotated: (x, y); x < y
  
       If we use D as diameter of the circle and C as ratio of the two rectangle
       sides we get the formulas (pythagoras):
       1) D^2 = x^2 + y^2
       2) C   = x   / y
  
       With 2) inserted in to 1) we get
       y = D / sqrt (C^2 + 1)
  
       With known y we can solve x when inserted into 1) or 2)'''
    def __initPanzaSize(self, sizeInPixels: int, ratio: float) -> tuple:
        D = sizeInPixels
        C = ratio
        y = D / sqrt(C * C + 1)
        x = C * y
        if x > y:
            return (y, x)
        else:
            return (x, y)

    def __init__(self, joystick: joystick.Joystick, sizeInPixels: int, windowSize: tuple, playerId: int):
        # Testing has no joysticks
        if joystick is not None:
            joystick.init()
            self.joystickInstanceId = joystick.get_instance_id()
            self.joystick = joystick

        self.position = self.__initPosition(windowSize, playerId)
        self.color = self.__initColor(playerId)
        self.tankDirection = self.__initTankDirection(playerId)
        self.gunDirection = self.__initGunDirection(playerId)
        self.size = self.__initPanzaSize(sizeInPixels, RATIO)

        self.tankSurface = Surface(size=(sizeInPixels, sizeInPixels), flags=SRCALPHA)
        self.__updateTankSurface(self.tankSurface, self.color, self.tankDirection)

    # UPDATES

    def __updateTankSurface(self, surface: Surface, color: Color, direction: math.Vector2):
        surface.fill((0, 0, 0, 0))

        # rect inside surface
        surfaceSize = surface.get_size()
        surfaceRect = Rect (0, 0, surfaceSize[0], surfaceSize[1])
        tankRect = Rect(0, 0, self.size[0], self.size[1])
        diff = math.Vector2(surfaceRect.center) - math.Vector2(tankRect.center)
        tankRect.move_ip(diff)

        temp = surface.copy()
        draw.rect(temp, color, tankRect)

        # apply tank direction to surface
        degree = math.Vector2 (0, -1).angle_to(direction)
        temp = transform.rotate(temp, degree)

        # temp was enlarged by rotate (wtf):
        # calculate diff so that temp surface is positioned outside
        # of the destination surface below
        tempRectSize = temp.get_size()
        diff = math.Vector2(tempRectSize) - math.Vector2(surfaceSize)

        # copy back wanted portion from rotation
        surface.blit (temp, -diff/2)

    def update(self, axis: int, value: float):
        if axis == 0 or axis == 1:
            direction = self.tankDirection
            direction [axis] = value
            self.tankDirection = direction.normalize ()
            self.__updateTankSurface(self.tankSurface, self.color, self.tankDirection)
        elif axis == 3 or axis == 4:
            print("gun {}".format(value))

    # DRAWING

    def render(self, screen: Surface):
        offset = self.tankSurface.get_rect().center
        position = self.position - math.Vector2(offset)
        screen.blit(self.tankSurface, position)
