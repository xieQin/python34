import urllib.request
from urllib.parse import urlencode

url = 'http://www.baidu.com'

values = {
	'name': 'WHY',
	'location': 'SDU',
	'language': 'Python'
}

data = urlencode(values)
req = urllib.request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read()