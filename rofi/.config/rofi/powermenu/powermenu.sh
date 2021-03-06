#!/usr/bin/env bash
theme="circle"
dir="$HOME/.config/rofi/powermenu"

# random colors
styles=($(ls -p --hide="colors.rasi" $dir/styles))
color="${styles[$(($RANDOM % 8))]}"

# comment this line to disable random colors
sed -i -e "s/@import .*/@import \"$color\"/g" $dir/styles/colors.rasi
uptime=$(uptime -p | sed -e 's/up //g')
rofi_command="rofi -theme $dir/$theme"

# Options
shutdown=" ⏻ "
reboot="  "
lock="  "
suspend="  "
hibernate="  "
logout="  "

# Variable passed to rofi
options="$shutdown\n$reboot\n$lock\n$suspend\n$hibernate" #\n$logout
chosen="$(echo -e "$options" | $rofi_command -p "Uptime: $uptime" -dmenu -selected-row 2)"
case $chosen in
$shutdown)
	systemctl poweroff
	;;
$reboot)
	systemctl reboot
	;;
$lock)
	i3lock
	;;
$suspend)
#	mpc -q pause
#	amixer set Master mute
	i3lock
	systemctl suspend
	;;
$hibernate)
#	mpc -q pause
#	amixer set Master mute
	i3lock
	systemctl hibernate
	;;
# $logout)
# 	qtile run-cmd shutdown now
# 	;;
esac
