#!/usr/bin/env bash

. ./common-env.sh

for lang in $LANGUAGES; do
  echo Processing lang ${lang}
  spiders/go-${lang}.sh
  scrapy runspider -a lang=${lang} spiders/spider-github-trendy-repositories.py -t jsonlines -o data/${lang}-github-trendy.json
done
