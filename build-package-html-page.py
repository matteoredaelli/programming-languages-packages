import json
import sys
import datetime

lang = sys.argv[1]
timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

header="""---
layout: default
---

### %s packages (updated %s)

| Package      | Description       |
|:-------------|:------------------|""" % (lang, timestamp)

print(header)

def clean_text(text):
  return text.replace("|", " ").replace("#", " ").replace("["," ").replace("]", " ").replace("("," ").replace(")", " ").replace("\n", " ").replace("\r", " ")
  
for line in sys.stdin:
  package = json.loads(line)
  if "description" not in package or "name" not in package or "url" not in package or not package["name"] or not package["description"] or not package["url"]:
    continue
  row = "| [%s](%s) | %s |" % (clean_text(package["name"]), package["url"], clean_text(package["description"]))
  print(row)
