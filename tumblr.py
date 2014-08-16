import requests
import logging
import httplib

s = requests.Session()

payload = {
	'username':'akhilaryan@ymail.com',
	'password':'oneshopio'
}

httplib.HTTPConnection.debuglevel = 1

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

c = s.post('https://www.tumblr.com/login', data=payload)

r = s.get('https://www.tumblr.com/customize/itsakhilaryan')
print r.status_code

print (r.text)
