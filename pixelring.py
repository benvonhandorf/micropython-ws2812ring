
class PixelRing:
	def __init__(self, offset, count):
		self.offset = offset
		self.count = count

	def fill(self, color):
		for x in range(0, self.count):
			# print("Setting position " + str(x))
			self.set(x, color)

	def rotateCW(self):
		outstandingColor = self.get(self.count - 1)

		for x in reversed(range(1, self.count)):
			self.set(x, self.get(x - 1))

		self.set(0, outstandingColor)

	def rotateCCW(self):
		outstandingColor = self.get(0)

		for x in range(0, self.count - 1):
			self.set(x, self.get(x + 1))

		self.set(self.count - 1, outstandingColor)

	def push(self, newColor):
		for x in range(0, self.count):
			existingColor = self.get(x)
			self.set(x, newColor)
			newColor = existingColor


	def apply(self, func):
		for x in range(0, self.count):
			newValue = func(get(self, x), x)
			self.set(x, newValue)

	def clear(self):
		self.fill((0,0,0))

	def avgColors(self, color1, color1weight, color2, color2weight):
		newColor = (int((color1[0] * color1weight + color2[0] * color2weight) / (color1weight + color2weight)),
			int((color1[1] * color1weight + color2[1] * color2weight) / (color1weight + color2weight)),
			int((color1[2] * color1weight + color2[2] * color2weight) / (color1weight + color2weight)))

		#print("Averaging " + str(color1) + " weight " + str(color1weight) + " with " + str(color2) + " weight " + str(color2weight) + " gave " + str(newColor))

		return newColor

	def flare(self, position, radius, color):
		self.set(position, color)

		for x in range(0, radius):
			existingColor = self.get(position + x + 1)
			flareColor = self.avgColors(color, radius - x, existingColor, x + 1)
			self.set(position + x + 1, flareColor)
			existingColor = self.get(position - x - 1)
			flareColor = self.avgColors(color, radius - x, existingColor, x + 1)
			self.set(position - x - 1, flareColor)

	def rocket(self, position, direction, trail, color):
		self.set(position, color)

		for x in range(0, trail):
			existingColor = self.get(position + (x  * direction))
			flareColor = self.avgColors(color, trail - x, existingColor, x + 1)
			self.set(position + (x  * direction), flareColor)