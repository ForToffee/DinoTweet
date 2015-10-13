import time
import picamera
import os

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	raw_input("Press Enter to continue...")
	camera.stop_preview()
