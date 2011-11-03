#!/usr/local/bin/python

import os, sys
import Image
import time

start = time.time()

#maxsize = 3000, 3000

dir = sys.argv[1]

list = os.listdir(dir)

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
pixels = [[[0, 0, 0] for j in range(h)] for j in range(w)]

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
  
new.save('/Users/amdavidson/Desktop/stack_' + str(time.time()) + '.jpg', 'JPEG')

print str(count) + ' images processed in ' + str(int(time.time() - start)) + ' seconds.'