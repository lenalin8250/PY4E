import urllib.request, urllib.parse, urllib.error
import json

url = "http://py4e-data.dr-chuck.net/comments_1334545.json"
print ("retrieving URL. Stand by.")
link = urllib.request.urlopen(url).read()


count = 0
info = json.loads(link)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	count = count + number
print (count)
