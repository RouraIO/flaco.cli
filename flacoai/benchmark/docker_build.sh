#!/usr/bin/env zsh

emulate -LR bash

set -e

docker build \
       --file benchmark/Dockerfile \
       -t flacoai-benchmark \
       .
