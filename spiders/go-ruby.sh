#!/usr/bin/env bash

lang=ruby
/usr/bin/python3 ./spiders/spider-$lang-packages.py > data/$lang.json
