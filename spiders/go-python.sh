#!/usr/bin/env bash

today=$(date +"%Y-%m-%d")
yesterday=$(date -d "1 days ago" +"%Y-%m-%d")
todayfile="data/python-${today}.json"
yesterdayfile="data/python-${yesterday}.json"
touch $todayfile $yesterdayfile

scrapy runspider spiders/spider-python-packages.py -o $todayfile -t jsonlines
sort -u $todayfile $yesterdayfile > data/python.json
