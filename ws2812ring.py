import machine, neopixel
from pixelring import PixelRing

class WS2812Ring(PixelRing):
	def __init__(self, neopixel_strand, offset, count, brightnessReduction):
		super().__init__(offset, count, brightnessReduction)
		self.neopixel_strand = neopixel_strand

	def set(self, position, color):
		color = self.reduceBrightness(color)
		
		if(position < 0):
			position = position + self.count

		position = position % self.count

		self.neopixel_strand[self.offset + position] = color

	def get(self, position):
		if(position < 0):
			position = position + self.count

		position = position % self.count

		return self.neopixel_strand[self.offset + position]

	def write(self):
		self.neopixel_strand.write()
		self.neopixel_strand.write()
