import machine, neopixel, ws2812ring, utime
from machine import Timer

neopixel_strand = neopixel.NeoPixel(machine.Pin(4), 44)

outer_ring = ws2812ring.Ring(neopixel_strand, 0, 24)

middle_ring = ws2812ring.Ring(neopixel_strand, 24, 12)

inner_ring = ws2812ring.Ring(neopixel_strand, 36, 8)

outer_ring.fill((20, 0, 0))

middle_ring.fill((0, 20, 0))

inner_ring.fill((0, 0, 20))

neopixel_strand.write()

outer_ring.rocket(0, 1, 6, (50, 50, 50))

middle_ring.rocket(11, -1, 4, (50, 50, 50))

inner_ring.rocket(0, 1, 3, (50, 50, 50))

neopixel_strand.write()

x = 0

def timerCallback(timer):
	global x

	if x == 6000:
		x = 0

	inner_ring.rotateCCW()

	if x % 2 == 0:
		middle_ring.rotateCW()

	if x % 3 == 0:
		outer_ring.rotateCCW()

	neopixel_strand.write()

	x = x + 1

readingTimer = Timer(-1)

readingTimer.init(period=100, mode=Timer.PERIODIC, callback=timerCallback)
