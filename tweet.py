import tweepy
import time
import picamera
from datetime import datetime

# Consumer keys and access tokens, used for OAuth
consumer_key = '<your value>'
consumer_secret = '<your value>'
access_token = '<your value>'
access_token_secret = '<your value>'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

searches = [["#eghamjam",1],
			['#camjam',2],
			['#wakedino',3],
			['#tofftest',4]]

searchstring = ''
for pairs in searches:
	searchstring += pairs[0] + " OR "
	
searchstring = searchstring[:-4]

last_id = 0
def searchHashTag():
	global last_id
	ret = api.search(q=searchstring,count=1, since_id=last_id)
	if len(ret) > 0:
		tweet = ret[0]
		print '===== START ====='
		print '{} (@{}) - {}\n{}'.format(tweet.author.name.encode('utf-8'), tweet.author.screen_name.encode('utf-8'), tweet.created_at, tweet.text.encode('utf-8'))
		print '====== END ======'
		last_id = tweet.id
		for pairs in searches:
			if pairs[0].lower() in tweet.text.lower():		#GOTCHA - case sensitive!
				return pairs[1]
	
	return -1
	
def sendTweet():
	print 'Starting photo capture.... smile!'
	i = datetime.now()
	now = i.strftime('%Y%m%d-%H%M%S')
	photo_name = now + '.jpg'
	
	with picamera.PiCamera() as camera:
		camera.resolution = (800,600)
		camera.start_preview()
		time.sleep(3)
		camera.capture(photo_name)
		camera.stop_preview()
		
	photo_path = photo_name
	api.update_with_media(photo_path, status='This puny human made me Roar and Stomp!')
	print 'Tweet sent'
