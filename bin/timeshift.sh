#!/bin/bash

if [ -n "$(ps aux | grep timeshift-gtk | grep -v 'grep\|rofi\|nvim')" ];
then pkexec killall timeshift-gtk;
else pkexec timeshift-gtk
fi
