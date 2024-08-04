import matplotlib.pyplot as plt

params = {'prey_birthrate': 1,
          'predator_eatrate': 0.01,
          'predator_birthrate': 0.01,
          'predator_deathrat': 0.5}


def f_x(x, y, params):
  a = params['prey_birthrate']
  b = params['predator_eatrate']
  dx_dt = a * x - (b * x * y)
  return dx_dt


def f_y(x, y, params):
  c = params['predator_birthrate']
  d = params['predator_deathrate']
  dy_dt = c * x * y - (d * y)
  return dy_dt


class RK_4:
  
  def __init__(self, deriv, h):
      self.deriv = deriv
      self.step = h
      
  def K_1(self, x, y, *args):
      K1 = self.deriv(x, y, *args)
      K1 = self.step * K1
      return K1
      
  def K_2(self, x, y, *args):
      K1 = self.K_1(x, y, *args)
      x = x + (0.5 * self.step)
      y = y + (0.5 * K1)
      K2 = self.deriv(x, y, *args)
      K2 = self.step * K2
      return K2
  
  def K_3(self, x, y, *args):
      K2 = self.K_2(x, y, *args)
      x = x + (0.5 * self.step)
      y = y + (0.5 * K2)
      K3 = self.deriv(x, y, *args)
      K3 = self.step * K3
      return K3
  
  def K_4(self, x, y, *args):
      K3 = self.K_3(x, y, *args)
      x = x + self.step
      y = y + K3
      K4 = self.deriv(x, y, *args)
      K4 = self.step * K4
      return K4
    
  def operation(self, x, y, *args):
    val = (1/6) * (self.K_1(x, y, *args) + 2 * self.K_2(x, y, *args) + 2 * self.K_3(x, y, *args) + self.K_4(x, y, *args))
    return val
      
h = 0.001
x_deriv = RK_4(f_x, h)
x = x_deriv.operation(2, 3, params)