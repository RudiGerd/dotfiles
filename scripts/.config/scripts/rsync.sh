#!/bin/sh
rsync -a --delete --quiet .config/btop OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/conky OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/dunst OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/gtk-3.0 OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/htop OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/neofetch OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/nvim OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/picom OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/qtile OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/ranger OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/rofi OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/scripts OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/wallpapers OneDrive/freespace/dotfiles/.config
rsync -a --delete --quiet .config/picom.conf OneDrive/freespace/dotfiles/.config

rsync -a --delete --quiet .bash_history OneDrive/freespace/dotfiles
rsync -a --delete --quiet .bashrc OneDrive/freespace/dotfiles
rsync -a --delete --quiet .p10k.zsh OneDrive/freespace/dotfiles
rsync -a --delete --quiet .xinitrc OneDrive/freespace/dotfiles
rsync -a --delete --quiet .zsh_history OneDrive/freespace/dotfiles
rsync -a --delete --quiet .zshrc OneDrive/freespace/dotfiles
