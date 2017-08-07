import urllib.request
import json

limit = 200
url = "https://skimdb.npmjs.com/registry/_changes?descending=true&limit=%d&include_docs=true" % limit


req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
results = json.loads(r.decode('utf-8'))

##parcing json
for package in results['results']:
    #print(package["id"])
    if "doc" in package and "name" in package["doc"]:
        item = {"language": "Nodejs"}
        item["name"] = package["doc"]["name"]        
        if "dist-tags" in package["doc"]:
            item["release"] = package["doc"]["dist-tags"]["latest"]
        if "description" in package["doc"]: 
            item["description"] = package["doc"]["description"]
        if "time" in package["doc"]:
            item["day"] = package["doc"]["time"]["modified"][:10]
        if "license" in package["doc"]:
            item["license"] = package["doc"]["license"]
        print(json.dumps(item))
