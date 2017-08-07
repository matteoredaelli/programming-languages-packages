#!/usr/bin/env bash

file="data/r.json"
touch $file
rm $file
scrapy runspider spiders/spider-r-packages.py -o $file -t jsonlines
