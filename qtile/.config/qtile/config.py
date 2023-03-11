from libqtile import hook

from settings.keys import keys, mod, myTerm
from settings.groups import groups
from settings.layouts import layouts, floating_layout, layout_theme
from settings.widgets import widget_defaults
from settings.screens import screens
from settings.mouse import mouse
from settings.path import *

from os import path
import subprocess
from typing import List

@hook.subscribe.startup_once
def start_once():
    home = path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "focus"
wmname = "LG3D"
