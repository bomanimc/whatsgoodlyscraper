import requests
import geocoder

# === Incomplete Portions of the Hopeful Token Generation Part ===
# usersURL = 'https://whatsgoodly.com/api/v1/users/'
# sex = '0' # 0 for male, 1 for female

# signInHeaders = {
# 	'Accept': 'application/json',
# 	'Content-type': 'application/json',
# 	'WG-Auth':	'Q~cZL>%&A3RZZz?eA?{zuReRv',
# 	'Host': 'whatsgoodly.com',
# 	'Connection': 'Keep-Alive',
# 	'Accept-Encoding': 'gzip',
# 	'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1; Custom Phone - 5.1.0 - API 22 - 768x1280 Build/LMY47D)'
# }

# # Accept	application/json
# # Content-type	application/json
# # WG-Auth	Q~cZL>%&A3RZZz?eA?{zuReRv
# # Content-Type	application/json; charset=utf-8
# # User-Agent	Dalvik/2.1.0 (Linux; U; Android 5.1; Custom Phone - 5.1.0 - API 22 - 768x1280 Build/LMY47D)
# # Host	whatsgoodly.com
# # Connection	Keep-Alive
# # Accept-Encoding	gzip
# # Content-Length	37

# signInParams = { "username": "botest3", "gender": sex }

# signIn = requests.post(usersURL, params=signInParams, headers=signInHeaders, verify=False)
# print(signIn.status_code)
# print(signIn.text)
# =============================================================





# ==== THIS IS SOME EXAMPLE JSON ====
# {"id":321903,"user":{"id":42030,"username":"DeezNutzFam","gender":0,"karma":2222,"university_short":"Mizzou"},
# "feed":{"id":2,"name":"Global","image_source":"http://d2tyav66cc90rz.cloudfront.net/global.png","category":1,
# "approve_posts":false,"new_polls":0},"question":"Two guys get to a urinal at the same time. Who wins?","gender":2,
# "options":["The guy who pees faster","The guy who pees longer"],"option_counts":[179,256],"response":null,"vote":null,
# "created_date":"2015-12-14T00:05:18.866899Z","favorite":null,"comment_count":4,"favorite_count":1,"recycle_count":0,"deleted":false,
# "banner":"Mizzou","deletable":false,"recyclable":true,"top_comment":{"id":430385,
# "text":"No, it should be girls only. We want to know how to impress you when we urinate.","vote":null,"poll_instance":321903,
# "count":22,"user":{"id":65102,"username":"MisterPotatoHead","gender":0,"karma":2261,"university_short":null},
# "created_date":"2015-12-14T00:40:46.123112Z","deletable":false},"recycled":true,"universal":true,"vote_aggregate":0,"verified":true}

class User:
	def __init__(self, raw):
		self.userID = raw['id']
		self.username = raw['username']
		self.sex = raw['gender']
		self.karma = raw['karma']
		self.university = raw['university_short']

class Comment:
	def __init__(self, raw):
		self.id = raw['id']
		self.text = raw['text']
		self.poll = raw['poll_instance']
		self.user = User(raw['user'])

class Poll:
	def __init__(self, raw):
		#feed = raw['feed']

		if raw != '':
			self.user = User(raw['user'])
			self.id = raw['id']
			self.question = raw['question']
			self.sexes = raw['gender'] # I think it's 0 for male, 1 for femaile, and 2 for both.
			self.options = raw['options']
			self.option_counts = raw['option_counts']
			self.created_date = raw['created_date']
			self.comment_count = raw['comment_count']
			self.favorite_count = raw['favorite_count']
			self.banner = raw['banner']
			self.top_comment = None if (raw['top_comment'] == None) else Comment(raw['top_comment'])


lat = ""
lon = ""

pollsHeaders = {
	'Accept': 'application/json',
	'Content-type': 'application/json',
	'Host': 'whatsgoodly.com',
	'Connection': 'Keep-Alive',
	'Accept-Encoding': 'gzip',
	'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1; Custom Phone - 5.1.0 - API 22 - 768x1280 Build/LMY47D)',
	'Authorization'	: 'Token f8db02fcd151cc661a0176a97ca1d9de0616e7b6'
}
 
def setLocation(lat, lon):
	lat = str(lat)
	lon = str(lon)

def createRequestURL(page):
	pollsURL = 'https://whatsgoodly.com/api/v1/polls/?latitude=' + lat + '&longitude=' + lon + '&top=0' + "&page=" + str(page)
	return pollsURL

#Gather data from each page
def paginateRequests(url):
	pageResults = []
	allObjects = []
	count = 0

	while True:
		pageURL = createRequestURL(count)
		polls = requests.get(pageURL, headers=pollsHeaders, verify=False)
		# print('Status Code: {}, Count: {}'.format(polls.status_code, count))
		pageResults = polls.json()
		allObjects.extend(pageResults)

		if(len(pageResults) != 0):
			break

		count = count + 1 

	return allObjects

#Create a objects from the collected data
def createPollObjects(rawObjects):
	pollObjects = []
	for rawPoll in rawObjects:
		newPoll = Poll(rawPoll)
		pollObjects.append(newPoll)
	return pollObjects

def getPolls():
	pollObjects = createPollObjects(paginateRequests(pollsURL))
	return pollObjects

