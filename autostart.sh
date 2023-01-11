source ~/.profile

settings() {
  [ $1 ] && sleep $1
  xset -b
  light -N 10
  wmname LG3D
  picom --config ~/.config/picom/picom.conf &
  redshift -t 5800:3400 -l 24.69:108.05 &
  $DWM/statusbar/statusbar.py cron &
}


tools() {
  [ $1 ] && sleep $1
  /usr/lib/polkit-kde-authentication-agent-1 &
  nm-applet &
  fcitx5 &
  xfce4-power-manager &
  xss-lock -- ~/scripts/bin/blurlock.sh &
  flameshot &
  dunst &
  conky &
  libinput-gestures-setup start
}

background() {
  while true; do
    feh --randomize --bg-fill ~/Pictures/background/*
    sleep 300
  done
}

settings 1 &
tools 1 &
background &
hour &
