#!/usr/bin/env bash

for lang in nodejs python r ; do
  echo Processing lang ${lang}
  /usr/bin/python3 build-package-html-page.py ${lang} < data/${lang}.json > www/${lang}-packages.md
done
