import urllib.request
import json


url = "https://rubygems.org/api/v1/activity/latest.json"

req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
results = json.loads(r.decode('utf-8'))

##parsing json
for package in results:
    #print(package["id"])
    if "name" in package and "project_uri" in package:
        item = {"language": "Ruby"}
        item["name"] = package["name"]        
        if "info" in package: 
            item["description"] = package["info"]
        if "version" in package: 
            item["version"] = package["version"]
        item["day"] = ""
        if "license" in package:
            item["license"] = package["license"][0]
        if "project_uri" in package:
            item["url"] = package["project_uri"]
        print(json.dumps(item))
