import requests
import json
url = "https://bing-image-search1.p.rapidapi.com/images/search"

querystring = {"q":"YOUR QUERY HERE","count": DESIRED NUMBER OF IMAGE URLS }

headers = {
    'x-rapidapi-key': "YOUR BING IMAGE SEARCH API KEY HERE",
    'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
json_obj = json.loads(response.content)
json_formatted = json.dumps(json_obj, indent=2)
#print(json_formatted)
for i in json_obj["value"]:
    #Below line prints out all the urls of the images
    print(i["contentUrl"])
