import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Su.html'
html = urllib.request.urlopen(url, context=ctx).read()
position = int(input('Enter position: '))
count = int(input('Enter count: '))

soup = BeautifulSoup(html, 'html.parser')

tags_lst = list()
for x in range(0,count):
    tags = soup('a')
    my_tags = tags[position-1]
    needed_tag = my_tags.get('href', None)
    url = str(needed_tag)
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(my_tags.get('href', None))
