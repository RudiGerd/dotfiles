#!/usr/bin/env bash

theme="style"

dir="$HOME/.config/rofi/text"
styles=($(ls -p --hide="colors.rasi" $dir/styles))
color="${styles[$(( $RANDOM % 10 ))]}"

# comment this line to disable random colors
sed -i -e "s/@import .*/@import \"$color\"/g" $dir/styles/colors.rasi

rofi -no-lazy-grab -show window -modi window,run,drun -theme $dir/"$theme"

