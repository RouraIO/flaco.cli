#!/bin/bash

# exit when any command fails
set -e

if [ -z "$1" ]; then
  ARG=-r
else
  ARG=$1
fi

if [ "$ARG" != "--check" ]; then
  tail -1000 ~/.flacoai/analytics.jsonl > flacoai/website/assets/sample-analytics.jsonl
  cog -r flacoai/website/docs/faq.md
fi

# README.md before index.md, because index.md uses cog to include README.md
cog $ARG \
    README.md \
    flacoai/website/index.html \
    flacoai/website/HISTORY.md \
    flacoai/website/docs/usage/commands.md \
    flacoai/website/docs/languages.md \
    flacoai/website/docs/config/dotenv.md \
    flacoai/website/docs/config/options.md \
    flacoai/website/docs/config/flacoai_conf.md \
    flacoai/website/docs/config/adv-model-settings.md \
    flacoai/website/docs/config/model-aliases.md \
    flacoai/website/docs/leaderboards/index.md \
    flacoai/website/docs/leaderboards/edit.md \
    flacoai/website/docs/leaderboards/refactor.md \
    flacoai/website/docs/llms/other.md \
    flacoai/website/docs/more/infinite-output.md \
    flacoai/website/docs/legal/privacy.md
