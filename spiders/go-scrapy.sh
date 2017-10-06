#!/usr/bin/env bash

for lang in clojure dotnet elixir haskell lua php python r scala
do
  file=data/$lang.json
  touch $file
  rm $file
  scrapy runspider spiders/spider-$lang-packages.py -o $file -t jsonlines
done
