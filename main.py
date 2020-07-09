import sys
import os
import time
import board
import neopixel
import strip 

# Load all animation classes
animations = {}
animation_files = [name[:-3] for name in os.listdir('animations')
    if name.endswith('.py') and name != 'animation.py']

for file in animation_files:
    animations[file] = __import__('animations/' + file)

# Define strips
strips = []

strips.append(strip.Strip({
    'animation': animations['rainbow'].Animation(),
    'pin': board.D11,
    'pixel_count': 8,
    'brightness': 1,
}))

strips.append(strip.Strip({
    'animation': animations['rainbow'].Animation(),
    'pin': board.A2,
    'pixel_count': 8,
    'brightness': 1
}))

while True:
    for strip in strips:
        strip.animation.draw()

    for strip in strips:
        strip.pixels.show()
