#! /bin/bash

case $1 in
    up) pactl set-sink-volume @DEFAULT_SINK@ +5% ;;
    down) pactl set-sink-volume @DEFAULT_SINK@ -5% ;;
esac

notify() {
    msg=$($DWM/statusbar/statusbar.py update vol)
    num=$(echo "$msg" | awk '{print $4}' | tr -d '%')
    notify-send -r 9527 -u low -h int:value:$num "$msg" -i audio-volume-medium
}

notify
