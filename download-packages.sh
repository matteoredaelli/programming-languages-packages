#!/usr/bin/env bash

. ./common-env.sh

./spiders/go-custom.sh
./spiders/go-scrapy.sh

for l in $LANGUAGES; do
    lang=$(echo $l | cut -f1 -d':')
    lang_git=$(echo $l | cut -f2 -d':')
    echo Processing lang ${lang} trends
    scrapy runspider -a lang=${lang_git} spiders/spider-github-trendy-repositories.py -t jsonlines -o data/${lang}-github-trendy.json
done
