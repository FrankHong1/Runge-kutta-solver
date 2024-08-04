import matplotlib.pyplot as plt

def f_x(x, y, params):
  a = params[0]
  b = params[1]
  dx_dt = a * x - (b * x * y)
  return dx_dt


def f_y(x, y, params):
  c = params[2]
  d = params[3]
  dy_dt = c * x * y - (d * y)
  return dy_dt


class RK_4:
  
  def __init__(self, approximation, h):
      self.approximation = approximation
      self.step = h
      
  def K_1(self, x, y):
      K1 = self.approximate(x, y)
      K1 = self.step * K1
      return K1
      
  def K_2(self, x, y):
      K1 = K_1(self, x, y)
      x = x + (0.5 * h)
      y = y + (0.5 * K1)
      K2 = self.approximate(x, y)
      K2 = self.step * K2
      return K2
  
  def K_3(self, x, y):
      K2 = K_2(self, x, y)
      x = x + (0.5 * h)
      y = y + (0.5 * K2)
      K3 = self.approximate(x, y)
      K3 = self.step * K3
      return K3
  
  def K_4(self, x, y):
      K3 = K_3(self, x, y)
      x = x + h
      y = y + K3
      K4 = self.approximate(x, y)
      K4 = self.step * K4
      return K4
    
  def operation(x, y):
    val = (1/6) * (K_1(self, x, y) + 2 * K_2(self, x, y) + 2 * K_3(self, x, y) + K_4(self, x, y))
    return val
      
      
x_deriv = RK4(self, f_x, h)
y_deriv = RK4(self, f_y, h)