import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error



url = 'http://py4e-data.dr-chuck.net/comments_1334544.xml'
xml = urllib.request.urlopen(url, context=ctx).read()
print('Retrieving', url)
print('Retrieved', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)
