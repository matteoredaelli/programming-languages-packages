#!/usr/bin/env bash

lang=php
today=$(date +"%Y-%m-%d")
yesterday=$(date -d "1 days ago" +"%Y-%m-%d")
todayfile="data/${lang}-${today}.json"
yesterdayfile="data/${lang}-${yesterday}.json"
touch $todayfile $yesterdayfile

scrapy runspider spiders/spider-${lang}-packages.py -o $todayfile -t jsonlines
sort -u $todayfile $yesterdayfile > data/${lang}.json
