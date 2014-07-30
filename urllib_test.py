from urllib.request import urlopen
response = urlopen('http://www.baidu.com')
html = response.read()
print(html)