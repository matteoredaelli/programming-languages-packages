#!/usr/bin/env bash

lang=nodejs
/usr/bin/python3 ./spiders/spider-$lang-packages.py > data/$lang.json
