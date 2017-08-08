#!/usr/bin/env bash

lang=nodejs
python3 ./spiders/spider-$lang-packages.py > data/$lang.json
