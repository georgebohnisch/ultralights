# # Python Module example
import animation
import time
import math

class Animation(animation.Animation):
    def __init__(self, args={}):
        args['delay'] = args.get('delay') or .07
        self.cycle_index = 0
        self.spacing = 3

        super().__init__(args)

    def drawFrame(self):
        if (self.cycle_index >= self.spacing):
            self.cycle_index = 0

        for i in range(self.strip.pixel_count):
            if ((i + self.cycle_index) % self.spacing == 0):
                self.strip.pixels[i] = (255, 0, 0, 0)
            else:
                self.strip.pixels[i] = (0, 0, 0, 0)

        self.cycle_index = self.cycle_index + 1  
