import time

class Animation:
    def __init__(self, args={}):    
        self.delay = args.get('delay') or 0
        self.draw_at = time.monotonic() + self.delay
        self.delay_draw = False

    def setStrip(self, strip):
        self.strip = strip

    def delayDraw(self, seconds):
        self.draw_at = time.monotonic() + seconds
        self.delay_draw = True

    def draw(self):
        if (self.draw_at > time.monotonic()):
            return

        self.drawFrame()

        if (self.delay_draw == False):
            self.draw_at = time.monotonic() + self.delay

        self.delay_draw = False