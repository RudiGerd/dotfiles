from libqtile.config import Key
from libqtile.command import lazy
from settings.path import *
from os import path

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = path.expanduser('~')

myTerm = "alacritty" # My terminal of choice

keys = [
    Key(key[0], key[1], *key[2:])
    for key in [
# SUPER + FUNCTION KEYS
    ([mod], "f", lazy.window.toggle_fullscreen()),
    ([mod], "q", lazy.window.kill()),
    ([mod], "t", lazy.spawn('xterm')),
    ([mod], "v", lazy.spawn('pavucontrol')),
    ([mod], "m", lazy.spawn(path.join(rofi_path, "colorful/launcher.sh"))),
    ([mod], "p", lazy.spawn(path.join(rofi_path, "powermenu/powermenu.sh"))),
    ([mod, "shift"], "m", lazy.spawn(path.join(rofi_path, "text/launcher.sh"))),
    ([mod], "o", lazy.spawn('rofimoji')),
    ([mod], "Escape", lazy.spawn('xkill')),
    ([mod], "Return", lazy.spawn(myTerm)),
    ([mod], "KP_Enter", lazy.spawn('alacritty')),
    ([mod], "x", lazy.shutdown()),
# SUPER + SHIFT KEYS
    ([mod, "shift"], "Return", lazy.spawn('pcmanfm')),
    ([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
#    ([mod, "shift"], "d", lazy.spawn(home + '/.config/qtile/scripts/dmenu.sh')),
    ([mod, "shift"], "q", lazy.window.kill()),
    ([mod, "shift"], "r", lazy.restart()),
    ([mod, "control"], "r", lazy.restart()),
    ([mod, "shift"], "x", lazy.shutdown()),
# CONTROL + ALT KEYS
    (["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    (["mod1", "control"], "t", lazy.spawn('xterm')),
    (["mod1", "control"], "u", lazy.spawn('pavucontrol')),
# ALT + ... KEYS
    (["mod1"], "p", lazy.spawn('pamac-manager')),
    (["mod1"], "f", lazy.spawn('firefox')),
    (["mod1"], "m", lazy.spawn('pcmanfm')),
    (["mod1"], "w", lazy.spawn('garuda-welcome')),
# CONTROL + SHIFT KEYS
    ([mod2, "shift"], "Escape", lazy.spawn('lxtask')),
# SCREENSHOTS
#    ([], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
#    ([mod2], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
#    ([mod2, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),
# MULTIMEDIA KEYS
# INCREASE/DECREASE BRIGHTNESS
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%- ")),
# INCREASE/DECREASE/MUTE VOLUME
    ([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    ([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    ([], "XF86AudioNext", lazy.spawn("playerctl next")),
    ([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    ([], "XF86AudioStop", lazy.spawn("playerctl stop")),
#    ([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    ([], "XF86AudioNext", lazy.spawn("mpc next")),
#    ([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    ([], "XF86AudioStop", lazy.spawn("mpc stop")),
# QTILE LAYOUT KEYS
    ([mod], "n", lazy.layout.normalize()),
    ([mod], "space", lazy.next_layout()),
# CHANGE FOCUS
    ([mod], "Up", lazy.layout.up()),
    ([mod], "Down", lazy.layout.down()),
    ([mod], "Left", lazy.layout.left()),
    ([mod], "Right", lazy.layout.right()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
# RESIZE UP, DOWN, LEFT, RIGHT
    ([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    ([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    ([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    ([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    ([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    ([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    ([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    ([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    ([mod, "shift"], "f", lazy.layout.flip()),
# FLIP LAYOUT FOR BSP
    ([mod, "mod1"], "k", lazy.layout.flip_up()),
    ([mod, "mod1"], "j", lazy.layout.flip_down()),
    ([mod, "mod1"], "l", lazy.layout.flip_right()),
    ([mod, "mod1"], "h", lazy.layout.flip_left()),
# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    ([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    ([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    ([mod, "shift"], "Left", lazy.layout.swap_left()),
    ([mod, "shift"], "Right", lazy.layout.swap_right()),
# TOGGLE FLOATING LAYOUT
    ([mod, "shift"], "space", lazy.window.toggle_floating()),
    ]
]

