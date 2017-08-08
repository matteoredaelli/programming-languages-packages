#!/usr/bin/env bash

for lang in nodejs python r ; do
  echo Processing lang ${lang}
  spiders/go-${lang}.sh
done
