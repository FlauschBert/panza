class Panza:
  def __init__(self, joystick):
    self.joystick = joystick
    self.joystick.init ()

    self.pos = (0, 0)
    self.color = (0, 0, 0)
    # tank orientation
    self.orientation = 0
    # gun orientation
    self.direction = 0

  def update (self, axis: int, value: float):
    print ("panza {}".format (self.joystick.get_instance_id ()))
    if axis == 0 or axis == 1:
      print ("tank {}".format (value))
    elif axis == 3 or axis == 4:
      print ("gun {}".format (value))