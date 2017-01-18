import numpy as np
from matplotlib import pyplot as plt
import time

def main():
  img = plt.imread('lena.png')
  plt.imshow(img)

  start = time.time()
  out1 = sobel_filter(img)
  out2 = blur_filter(img)
  print 'Calculation time:', time.time()-start, 'sec'
  plt.figure()
  plt.imshow(out1.mean(2), vmin=out1.min(), vmax=out1.max(), cmap='gray')
  plt.figure()
  plt.imshow(out2, vmin=out2.min(), vmax=out2.max())
  plt.show()


def convolution(image, kernel):
  """
  Write a general function to convolve an image with an arbitrary kernel.
  """
  return image


def blur_filter(img):
  """
  Use your convolution function to filter your image with an average filter (box filter)
  with kernal size of 11.
  """
  k_size = 11
  kernel = np.zeros((k_size, k_size))
  return convolution(img, kernel)


def sobel_filter(img):
  """
  Use your convolution function to filter your image with a sobel operator
  """
  kernel = np.zeros((3, 3))
  return convolution(img, kernel)


if __name__ == '__main__':
  main()