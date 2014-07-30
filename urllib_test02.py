import urllib.request, urllib.parse, urllib.error
# from urllib.parse import urlencode
# from urllib.request import Request

url = 'http://www.baidu.com'

values = {
	'name': 'WHY',
	'location': 'SDU',
	'language': 'Python'
}

data = urllib.parse.urlencode(values).encode('utf-8')
# binary_data = data.encode(encoding)
req = urllib.request.Request(url, data)
# req = urllib.request.Request(url, binary_data)
response = urllib.request.urlopen(req)
the_page = response.read()