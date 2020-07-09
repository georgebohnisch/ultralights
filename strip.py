import neopixel

class Strip:
    def __init__(self, args):    
        self.pin = args.get('pin') or None
        self.pixel_count = args.get('pixel_count') or 0
        self.pixel_order = args.get('pixel_order') or neopixel.GRBW
        self.brightness = args.get('brightness') or 0.1
        self.animation = args.get('animation') or None

        if (self.animation != None):
            self.animation.setStrip(self)

        self.pixels = neopixel.NeoPixel(
            self.pin, self.pixel_count, brightness=self.brightness, auto_write=False, pixel_order=self.pixel_order
        )