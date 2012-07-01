from instagram.client import InstagramAPI
from urlparse import urlparse, parse_qs
from progressbar import ProgressBar, SimpleProgress, Bar
import sys, string

max_photos_per_request = 100
total_likes = num_returned = 0

access_token = string.strip(open("token.txt").read())
api = InstagramAPI(access_token=access_token)

if len(sys.argv) ==	 2:
	user = api.user_search(sys.argv[1], 1)[0] #optional argument: user id (default: self)
else:
	user = api.user("self")

media_count = api.user(user.id).counts['media']

pbar = ProgressBar(widgets=[SimpleProgress(), ' photos ',Bar()], maxval=media_count).start()

next_max_id = ""

while True:
	recent_media, next = api.user_recent_media(user_id=user.id, count=max_photos_per_request, max_id = next_max_id)

	num_returned +=len(recent_media)
	if num_returned > pbar.maxval:	# Instagram media count isn't always accurate :(
		pbar.maxval = num_returned	
	pbar.update(num_returned)

	for media in recent_media:
   		total_likes += len(media.likes)

	if next:
		next_max_id = parse_qs(urlparse(next).query)['max_id'][0] 
	else:
		break

pbar.finish()
print "Hello, "+ user.full_name + "." 
print "Your " + str(num_returned) + " photos have been liked " + str(total_likes) + " times."
print "That's an average of " + "%.2f" % (total_likes/float(num_returned)) + " likes per photo."