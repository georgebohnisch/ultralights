# # Python Module example
import animation
import time
import neopixel


class Animation(animation.Animation):
    def __init__(self, args={}):
        args['delay'] = args.get('delay') or 0.0005
        self.cycle_index = 0
        self.cycle_range = 255
        
        super().__init__(args)

    def drawFrame(self):
        if (self.cycle_index > self.cycle_range):
            self.cycle_index = 0

        for i in range(self.strip.pixel_count):
            pixel_index = (i * 256 // self.strip.pixel_count) + self.cycle_index
            self.strip.pixels[i] = self.wheel(pixel_index & 255)

        self.cycle_index = self.cycle_index + 1

    def wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b) if self.strip.pixel_order in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)