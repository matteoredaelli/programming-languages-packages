#!/usr/bin/env bash

. ./common-env.sh

./spiders/go-custom.sh
./spiders/go-scrapy.sh

for lang in $LANGUAGES; do
  echo Processing lang ${lang} trends
  spiders/go-${lang}.sh
  scrapy runspider -a lang=${lang} spiders/spider-github-trendy-repositories.py -t jsonlines -o data/${lang}-github-trendy.json
done
