#!/usr/bin/env bash

. ./common-env.sh

for lang in $LANGUAGES; do
  echo Processing lang ${lang}
  spiders/go-${lang}.sh
done
