#!/usr/bin/env bash

. ./common-env.sh

for l in $LANGUAGES; do
    lang=$(echo $l | cut -f1 -d':')
    echo Processing lang ${lang}
    python3 build-package-html-page.py ${lang} > www/${lang}-packages.md
done
cd www && jekyll build
