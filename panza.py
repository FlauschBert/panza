from pygame import math, display, Rect, Color

class Panza:
  def __initPosition (self, playerId: int) -> math.Vector2:
    size = display.get_window_size ()
    rect = Rect (0, 0, size[0]/2, size[1]/2)
    if (0 == playerId):
      return math.Vector2 (rect.center)
    else:
      rect.move_ip (size [0]/2, size [1]/2)
      return math.Vector2 (rect.center)

  def __initColor (self, playerId: int) -> Color:
    if (0 == playerId):
      return Color(255, 0, 0)
    else:
      return Color(0,0,255)

  def __initTankDirection (self, playerId: int) -> math.Vector2:
    if (0 == playerId):
      return math.Vector2 (0,1)
    else:
      return math.Vector2 (0,-1)

  def __initGunDirection (self, playerId: int) -> math.Vector2:
    return self.__initTankDirection (playerId)

  def __init__(self, joystick, playerId: int):
    # Testing has no joysticks
    if None != joystick:
      self.joystick = joystick
      self.joystick.init ()

    self.position = self.__initPosition (playerId)
    self.color = self.__initColor (playerId)
    self.tankDirection = self.__initTankDirection (playerId)
    self.gunDirection = self.__initGunDirection (playerId)

  def update (self, axis: int, value: float):
    print ("panza {}".format (self.joystick.get_instance_id ()))
    if axis == 0 or axis == 1:
      print ("tank {}".format (value))
    elif axis == 3 or axis == 4:
      print ("gun {}".format (value))