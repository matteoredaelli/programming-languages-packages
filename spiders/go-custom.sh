#!/usr/bin/env bash

for lang in nodejs ruby
do
    python3 ./spiders/spider-$lang-packages.py > data/$lang.json
done
