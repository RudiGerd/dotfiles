#!/bin/sh
xrandr --output HDMI-0 --mode 1920x1080 --pos 0x0 --rotate normal --output eDP-1-1 --primary --mode 1920x1080 --pos 1920x228 --rotate normal &
feh --randomize --bg-fill -D 2 ~/.config/wallpapers/* &
