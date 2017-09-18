
upload:
	ampy --port /dev/tty.SLAB_USBtoUART put ws2812ring.py 

upload_test: upload
	ampy --port /dev/tty.SLAB_USBtoUART put ws2812ringtest.py 	
