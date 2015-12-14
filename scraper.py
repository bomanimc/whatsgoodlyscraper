import requests

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


pollsURL = 'https://whatsgoodly.com/api/v1/polls/?latitude=0.0&longitude=0.0&page=1&filter=featured&top=0'

pollsHeaders = {
	'Accept': 'application/json',
	'Content-type': 'application/json',
	'Host': 'whatsgoodly.com',
	'Connection': 'Keep-Alive',
	'Accept-Encoding': 'gzip',
	'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1; Custom Phone - 5.1.0 - API 22 - 768x1280 Build/LMY47D)',
	'Authorization'	: 'Token f8db02fcd151cc661a0176a97ca1d9de0616e7b6'
}

polls = requests.get(pollsURL, headers=pollsHeaders, verify=False)
print(polls.status_code)
print(polls.text)