import requests



usersURL = 'https://whatsgoodly.com/api/v1/users/'
sex = '0' # 0 for male, 1 for female

signInHeaders = {
	'Accept': 'application/json',
	'Content-type': 'application/json',
	'Host': 'whatsgoodly.com',
	'Connection': 'Keep-Alive',
	'Accept-Encoding': 'gzip',
	'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1; Custom Phone - 5.1.0 - API 22 - 768x1280 Build/LMY47D)'
}

# Accept	application/json
# Content-type	application/json
# WG-Auth	Q~cZL>%&A3RZZz?eA?{zuReRv
# Content-Type	application/json; charset=utf-8
# User-Agent	Dalvik/2.1.0 (Linux; U; Android 5.1; Custom Phone - 5.1.0 - API 22 - 768x1280 Build/LMY47D)
# Host	whatsgoodly.com
# Connection	Keep-Alive
# Accept-Encoding	gzip
# Content-Length	37

signInParams = { "username": "botest3", "gender": sex }

signIn = requests.post(usersURL, params=signInParams, headers=signInHeaders, verify=True)
print(signIn.status_code)
print(signIn.text)