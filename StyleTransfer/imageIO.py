

# Importing the libraries 

import tensorflow as tf
import numpy as np
import scipy.io
import PIL.Image

"""*Load/Save Image functions*"""

#Converts an image to a floating point array.
#If specified it also resizes the input.

def loadImage(filePath, shape=None, max_size=None):
  image = PIL.Image.open(filePath)
  
  if max_size is not None:
    ratio = float(max_size)/np.max(img.size)
    size = np.array(image.size) * ratio
    size = size.astype(int)
    image = image.resize(size,PIL.Image.LANCZOS)
    
  if shape is not None:
    image = image.resize(shape,PIL.Image.LANCZOS)
    
  return np.float32(image)

#Write the array pixels as a jpeg

def saveImage(image, filePath):
  image = np.clip(image, 0.0, 255.0)
  image = image.astype(np.uint8)
  with open(filePath, 'wb') as file:
    PIL.Image.fromarray(image).save(file,'jpeg')
    
