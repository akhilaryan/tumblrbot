import requests
import logging
import httplib

s = requests.Session()

s.auth = {
	'username':'akhilaryan@ymail.com',
	'password':'oneshopio'
}

httplib.HTTPConnection.debuglevel = 1

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

c = requests.post('https://www.tumblr.com/login', data=s.auth)
cookie = {'enwiki_session': '53ef4f105f71c70907296410'}

r = requests.get('https://www.tumblr.com/customize/itsakhilaryan', cookies=cookie)

print (r.text)
