#!/usr/local/bin/python

import os, sys
import Image
import time
import numpy as np
import scipy as sp

from scipy import misc


start = time.time()

#maxsize = 3000, 3000

dir = sys.argv[1]

list = os.listdir(dir)
first = 0
count = 0

# for file in list:
#   try:
#     im = misc.imread(dir + file)
#   except IOError:
#     continue
# 
#   count +=1
#   print 'Processing image ' + str(count)
#   
#   if first == 0:
#     new = im
#     first = 1
#     continue
#   
#   from numpy import *
#   
#   for nrow, row in np.nditer([new,im], op_flags=['readwrite']):
#     for npixel, pixel in np.nditer([nrow,row], op_flags=['readwrite']):
#       npixel = maximum(npixel, pixel)
# 
# misc.imsave('stack_' + str(int(time.time())) + '.jpg', new)

images = []

for file in list: 
  try:
    im = Image.open(dir + file)
  except IOError:
    continue
  print 'Getting image...'

  if 'maxsize' in globals():        
    im.thumbnail(maxsize, Image.ANTIALIAS)
  
  images.append(im)

count = len(images)
(w, h) = images[0].size
new = Image.new('RGB', (w, h))
i = 1
pixels = np.zeros((w,h,3), dtype=np.uint8)

for im in images:
  print "Image " + str(i) + " of " + str(count)
  (w, h) = im.size
  for x in range(w):
    for y in range(h):
      raw = im.getpixel((x,y))
      if raw[0] > pixels[x][y][0]:
        pixels[x][y][0] = raw[0]
      if raw[1] > pixels[x][y][1]:
        pixels[x][y][1] = raw[1]
      if raw[2] > pixels[x][y][2]:
        pixels[x][y][2] = raw[2]
  i += 1
  
  
for x in range(w):
  for y in range(h):
    new.putpixel((x,y), (pixels[x][y][0], pixels[x][y][1], pixels[x][y][2]))
 
new.save('stack_' + str(time.time()) + '.jpg', 'JPEG')

print str(count) + ' images processed in ' + str(int(time.time() - start)) + ' seconds.'