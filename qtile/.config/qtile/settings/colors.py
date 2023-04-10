import json
import os

def set_random_wallpaper_and_colors(wallpapers_dir):
    os.system(f"wal -i '{wallpapers_dir}'")

def get_colorscheme_file():
    cache_dir = os.path.expanduser("~/.cache/wal/")
    with open(os.path.join(cache_dir, "colors.json"), "r") as file:
        return json.load(file)

def init_colors(wal_colors):
    return [
        "#212121", # 0 foreground
        "#6272a4", # 1 groupbox-bg/systray-bg
        "#ffffff", # 2 active font
        "#2F343F", # 3 inactive screen/tasklist-bg
        "#ffd47e", # 4 inactive font
        "#abb2bf", # 5 active screen
        "#2aa899", # 6 unsigned
        "#44475a", # 7 background
        "#ff5555", # 8 border
        wal_colors["color0"], # 9 CurrentLayout
        wal_colors["color1"], # 10 Net
        wal_colors["color2"], # 11 CPU
        wal_colors["color3"], # 12 Clock
        wal_colors["color4"], # 13 Memory
        wal_colors["color5"], # 14
    ]

wallpapers_dir = "/home/rudigerd/.config/wallpapers"

# Set random wallpaper and colors using PyWal
set_random_wallpaper_and_colors(wallpapers_dir)

# Get the colorscheme data
colors_data = get_colorscheme_file()

# Initialize colors with PyWal colors
colors = init_colors(colors_data['colors'])
