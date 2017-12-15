from pixelring import PixelRing

class APA102Ring(PixelRing):
	def __init__(self, apa102, offset, count):
		super.__init(offset, count)
		self.apa102 = apa102

	def set(self, position, color):
		if(position < 0):
			position = position + self.count

		position = position % self.count

		self.apa102[self.offset + position] = color

	def get(self, position):
		if(position < 0):
			position = position + self.count

		position = position % self.count

		return self.apa102[self.offset + position]

	def write(self):
		self.apa102.write()
		self.apa102.write()