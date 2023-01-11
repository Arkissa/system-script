#! /bin/bash

case $1 in
    up) light -A 5;;
    down) light -U 5;;
esac

notify() {
    msg=$($DWM/statusbar/statusbar.py update light)
    num=$(echo "$msg" | awk '{print $4}' | tr -d '%')
    notify-send -r 9527 -u low -h int:value:$num "  $msg"
}
notify
