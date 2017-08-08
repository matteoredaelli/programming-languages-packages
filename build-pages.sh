#!/usr/bin/env bash

. ./common-env.sh

for lang in $LANGUAGES; do
  echo Processing lang ${lang}
  python3 build-package-html-page.py ${lang} > www/${lang}-packages.md
done
cd www && jekyll build
