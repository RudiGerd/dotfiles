# https://adamrutter.github.io/pywal-themes-preview/

import json
import os

wallpapers_dir = "~/.config/wallpapers"
color_theme_dir = '~/.cache/wal' # '/usr/lib/python3.10/site-packages/pywal/colorschemes' #
color_theme = '/colors.json' #  '/dark/base16-oceanicnext.json' #

def set_wallpaper(wallpapers_dir):
    path = os.path.expanduser(wallpapers_dir)
    os.system(f"wal -i '{path}'")

def get_colorscheme(color_theme, color_theme_dir):
    default_colorscheme = {"special":{"background":"#282828","foreground":"#ebdbb2","cursor":"#fbf1c7"},
                           "colors":{"color0":"#282828","color1":"#cc241d","color2":"#98971a","color3":"#d79921",
                                     "color4":"#458588","color5":"#b16286","color6":"#689d6a","color7":"#a89984",
                                     "color8":"#928374","color9":"#fb4934","color10":"#b8bb26","color11":"#fabd2f",
                                     "color12":"#83a598","color13":"#d3869b","color14":"#8ec07c","color15":"#ebdbb2"}}
    path = os.path.expanduser(color_theme_dir)
    try:
        with open(f"{path}{color_theme}") as f:
            loaded_colorscheme = json.load(f)
            colorscheme = {key: loaded_colorscheme[key] for key in ['special', 'colors'] if key in loaded_colorscheme}
            return colorscheme    
    except Exception as e:
        return default_colorscheme

def init_colors(special, colors):
    return {
            # Base colors
        'base_dark': special["background"],
        'base_light': colors["color8"],
        'text_dark': colors["color7"],
        'text_light': special["foreground"],
        'text_black': colors["color0"],
        'text_white': colors["color15"],
        'cursor': special["cursor"],
            # System colors
        'system1': colors["color1"],
        'system2': colors["color2"],
        'system3': colors["color3"],
            # Widgets colors
        'widget1': colors["color4"],
        'widget2': colors["color5"],
        'widget3': colors["color6"],
        'widget4': colors["color9"],
        'widget5': colors["color10"],
        'widget6': colors["color11"],
        'widget7': colors["color12"],
        'widget8': colors["color13"],
        'widget9': colors["color14"],
    }

# Set random wallpaper and colors using PyWal
set_wallpaper(wallpapers_dir)

# Get the colorscheme data
colors_data = get_colorscheme(color_theme, color_theme_dir)

colors = init_colors(colors_data['special'], colors_data['colors'])

fonts = {
    "font": "Noto Sans",
    "font_bold": "Noto Sans Bold",
    "font_nerd": "UbuntuMono Nerd Font",
}
