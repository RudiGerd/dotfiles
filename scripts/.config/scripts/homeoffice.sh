#!/bin/sh
xrandr --output DP-0.3 --mode 1920x1080 --pos 1920x0 --rotate left --output eDP-1-1 --primary --mode 1920x1080 --pos 0x840 --rotate normal &
feh --randomize --bg-fill -D 2 ~/.config/wallpapers/* &
