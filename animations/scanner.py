# # Python Module example
import animation
import time
import math

class Animation(animation.Animation):
    def __init__(self, args={}):
        args['delay'] = args.get('delay') or .04
        self.cycle_index = 0
        self.cycle_range = 0

        super().__init__(args)

    def drawFrame(self):
        self.cycle_range = (self.strip.pixel_count - 1) * 1

        if (self.cycle_index >= self.cycle_range):
            self.cycle_index = 0

        for i in range(self.strip.pixel_count):
            if (i == self.cycle_index):
                self.strip.pixels[i] = (255, 0, 0, 0)
            elif (i == (self.strip.pixel_count - self.cycle_index)):
                self.strip.pixels[i] = (255, 0, 0, 0)
            else:
                self.strip.pixels[i] = (0, 0, 0, 0)

        self.cycle_index = self.cycle_index + 1  
