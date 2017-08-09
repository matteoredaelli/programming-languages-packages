#!/usr/bin/env bash

lang=$1
file="data/$lang.json"
touch $file
rm $file
scrapy runspider spiders/spider-$lang-packages.py -o $file -t jsonlines
