# # Python Module example
import animation
import time

class Animation(animation.Animation):
    def __init__(self, args={}):
        args['delay'] = args.get('delay') or 0.05
        self.cycle_index = 0

        super().__init__(args)

    def drawFrame(self):
        if (self.cycle_index in [0, 2, 4, 6, 8]):
            self.strip.pixels.fill((255,255,255,255))
        else:
            self.strip.pixels.fill((0,0,0,0))
        
        if (self.cycle_index == 9):
            self.delayDraw(1.5)
            self.cycle_index = 0
        else:
            self.cycle_index = self.cycle_index + 1
        
