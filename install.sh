#!/bin/bash

if [ ! -d ~/.openclaw/workspace/.venv ] ; then
    python3 -m venv ~/.openclaw/workspace/.venv
fi
source ~/.openclaw/workspace/.venv/bin/activate
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

npm install
openclaw plugins install -l .
openclaw plugins install zclaw-skills
