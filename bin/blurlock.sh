#!/bin/bash

BLANK='#00000000'
CLEAR='#ffffff22'
DEFAULT='#4D506D'
TEXT='#1A1A1A'
WRONG='#C4905D'
VERIFYING='#903631'

i3lock \
    --bar-indicator \
    --bar-pos y+h \
    --bar-direction 1 \
    --bar-max-height 50 \
    --bar-base-width 50 \
    --bar-color 00000000 \
    --insidever-color=$CLEAR     \
    --ringver-color=$DEFAULT     \
    --insidewrong-color=$CLEAR   \
    --ringwrong-color=$WRONG     \
    --inside-color=$BLANK        \
    --ring-color=$DEFAULT        \
    --line-color=$BLANK          \
    --separator-color=$DEFAULT   \
    --verif-color=$TEXT          \
    --wrong-color=$TEXT          \
    --time-color=$TEXT           \
    --date-color=$TEXT           \
    --layout-color=$TEXT         \
    --keyhl-color=$DEFAULT         \
    --bshl-color=$WRONG          \
    --screen 1                   \
    --blur 7                     \
    --clock                      \
    --indicator                  \
    --time-str="%H:%M:%S"        \
    --date-str="%A, %Y-%m-%d"       \
    --keylayout 1                \
xdotool mousemove_relative 1 1
