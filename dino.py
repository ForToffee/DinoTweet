import pibrella
import time
import pygame
import random

pygame.mixer.init()

audio = ['Allosaurus1', 'Torosaurus1','Trex21','Trex31']
song = ['walk.mp3', 'walk2.mp3']

def playSound(play_song=False):

	if play_song:
		pygame.mixer.music.load("sounds/" + random.choice(song))
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue
	else:
		for n in range(0,2):
			pygame.mixer.music.load("sounds/" + random.choice(audio) + ".wav")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue

button_state = False
def buttonPressed(pin):
	global button_state
	button_state = True
	print 'Button pressed'
	pibrella.output.f.on()
	pibrella.output.g.on()
	pibrella.output.h.on()
	
def button():
	global button_state
	ret = button_state
	button_state = False
	pibrella.output.f.off()
	pibrella.output.g.off()
	pibrella.output.h.off()
	return ret
	
def activate(led_id):
	if led_id == 1:
		pibrella.light.red.pulse()
	if led_id == 2:
		pibrella.light.amber.pulse()
	if led_id == 3:
		pibrella.light.green.pulse()
	if led_id == 4:
		pibrella.lights.pulse()
	
	pibrella.output.e.pwm(50,12)
	playSound(led_id == 4)
	pibrella.output.e.off()
	pibrella.lights.off()

pibrella.button.pressed(buttonPressed)

if __name__ == "__main__":
	while True:
		if button() == True:
			activate(4)
