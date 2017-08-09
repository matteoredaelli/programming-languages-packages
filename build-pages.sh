#!/usr/bin/env bash

. ./common-env.sh

for l in $LANGUAGES; do
    lang=$(echo $l | cut -f1 -d':')
    lang_git=$(echo $l | cut -f2 -d':')
    echo Processing lang ${lang}
    python3 build-package-html-page.py ${lang} ${lang_git} > www/${lang}-packages.md
done
cd www && jekyll build
