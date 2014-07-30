from urllib.request import urlopen
response = urlopen('http://www.baidu.com')
html = response.read()
print(html)

# import urllib2
# req = urllib2.request('http://www.baidu.com')
# response = urllib2.urlopen(req)
# the_page = response.read()
# print(the_page)