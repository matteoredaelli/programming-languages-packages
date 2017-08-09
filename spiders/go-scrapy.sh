#!/usr/bin/env bash

for lang in dotnet elixir haskell lua php python r
do
  file=data/$lang.json
  touch $file
  rm $file
  scrapy runspider spiders/spider-$lang-packages.py -o $file -t jsonlines
done
