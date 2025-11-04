import numpy as np
from numpy import linspace, array
from matplotlib import pyplot as plt


t: array = linspace(0,1,1001)

xt: int = t**2 + 2*t + 1

def plot(t: array, xt: array):
  plt.plot(t,xt,color='red', label='test')
  plt.xlabel('t')
  plt.ylabel('xt')
  plt.grid()
  plt.legend()
  plt.show


def main() -> None:
  print('hhhhh')
  plot(t=t, xt=xt)

if __name__ == '__main__':
  main()
