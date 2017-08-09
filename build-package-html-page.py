import json
import sys
import datetime

from utils import clean_text

lang = sys.argv[1]
timestamp = '{:%Y-%m-%d %H:%M:%S %Z}'.format(datetime.datetime.now())

header="""---
layout: default
---

Last update: %s

""" % timestamp

header_packages="""
## %s packages

| Package      | Description       |
|:-------------|:------------------|""" % lang

header_trendy="""
## %s trendy repositories

[Trendy %s repositories](https://github.com/trending/%s?since=daily)

| Repository   | Description       |
|:-------------|:------------------|""" % (lang, lang, lang)


print(header)

print(header_trendy)
fname = "data/%s-github-trendy.json" % lang
with open(fname) as f: 
    for line in f:
        package = json.loads(line)
        if "description" not in package or "name" not in package or "url" not in package or not package["name"]  or not package["url"]:
            continue
        if package["description"] is None:
            package["description"]  = ""
        row = "| [%s](%s) | %s |" % (clean_text(package["name"]), package["url"], clean_text(package["description"]))
        print(row)


print(header_packages)
fname = "data/%s.json" % lang
with open(fname) as f: 
    for line in f:
        package = json.loads(line)
        if "description" not in package or "name" not in package or "url" not in package or not package["name"] or not package["url"]:
            continue
        if package["description"] is None:
            package["description"]  = ""
        row = "| [%s](%s) | %s |" % (clean_text(package["name"]), package["url"], clean_text(package["description"]))
        print(row)
