import requests

payload = {
	'username':'akhilaryan@ymail.com',
	'password':'oneshopio'
}

import logging
# these two lines enable debugging at httplib level (requests->urllib3->httplib)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
import httplib
httplib.HTTPConnection.debuglevel = 1

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

c = requests.post('https://www.tumblr.com/login', data=payload)
r = requests.get('https://www.tumblr.com/customize/itsakhilaryan')
print r.text
