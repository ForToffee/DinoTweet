import tweet
import dino
import time

counter = 0
while True:
	if counter == 0:
		#dino rock
		ret = tweet.searchHashTag()
		if ret > 0:
			dino.activate(ret)
			
	if dino.button() == True:
		tweet.sendTweet()
		dino.activate(4)
		
	time.sleep(0.5)
	counter +=1
	if counter >= 20: #wait 10 seconds between twitter checks to avoid API limits
		counter = 0
		
