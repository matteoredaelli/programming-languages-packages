#!/usr/bin/env bash

. ./common-env.sh

for lang in $LANGUAGES; do
  echo Processing lang ${lang}
  /usr/bin/python3 build-package-html-page.py ${lang} < data/${lang}.json > www/${lang}-packages.md
done
cd www && /usr/bin/jekyll build
