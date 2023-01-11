#!/bin/bash

kill -9 "$(ps -ef | grep "/bin/python3 $HOME/scripts/bin/translate/translate.py" | sed 2d |awk '{print $2}')" && notify-send -r 9527 "翻译" "关闭翻译" || ~/scripts/bin/translate/translate.py
