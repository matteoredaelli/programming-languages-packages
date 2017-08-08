#!/usr/bin/env bash

lang=ruby
python3 ./spiders/spider-$lang-packages.py > data/$lang.json
