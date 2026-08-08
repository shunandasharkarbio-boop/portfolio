import urllib.request
import json

url = "https://en.wikipedia.org/w/api.php?action=query&list=allimages&aiprop=url|mime&aimime=image/png&aiprefix=Leaf&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    for img in data['query']['allimages'][:10]:
        print(img['title'], img['url'])
