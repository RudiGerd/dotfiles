from libqtile import widget, qtile
from libqtile.command import lazy
from libqtile.widget import Spacer
from settings.keys import myTerm
from settings.colors import colors
from settings.path import *
import socket
import os

def base(fg='text', bg='dark'):
    return {'foreground': colors[0],'background': colors[1]}

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 9,
                padding = 2,
                background=colors[3])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    return [
        widget.Sep(
            linewidth = 1,
            padding = 10,
            foreground = colors[1],
            background = colors[1]
        ),
        widget.TextBox(
            text = ' ',
            fontsize = 15,
            background = colors[1],
            mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('jgmenu_run')}
        ),
        widget.GroupBox(
            **base(bg=colors[1]),
            
            font='UbuntuMono Nerd Font',
            fontsize = 15,
            margin_y = 3,
            margin_x = 2,
            padding_y = 5,
            padding_x = 4,
            borderwidth = 3,

            active=colors[2],
            inactive=colors[4],
            rounded= True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors[6],
            this_current_screen_border=colors[7],
            this_screen_border=colors[5],
            other_current_screen_border=colors[7],
            other_screen_border=colors[5],
            disable_drag=True
        ),
        widget.TaskList(
            highlight_method = 'border', # or block
            icon_size=17,
            max_title_width=150,
            rounded=True,
            padding_x=0,
            padding_y=0,
            margin_y=0,
            fontsize=14,
            border=colors[8],
            foreground=colors[2],
            margin=2,
            txt_floating='🗗',
            txt_minimized='>_ ',
            borderwidth = 1,
            background=colors[7],
            #unfocused_border = 'border'
        ),
        widget.CurrentLayoutIcon(
            # custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground = colors[2],
            background = colors[9],
            padding = 0,
            scale = 0.7
        ),
        widget.CurrentLayout(
            font = "Noto Sans Bold",
            fontsize = 12,
            foreground = colors[2],
            background = colors[9]
        ),                
    ]

primary_widgets = [
    *init_widgets_list(),
    widget.Net(
        font="Noto Sans Bold",
        fontsize=12,
        # Here enter your network name
        interface=["wlp6s0"],
        format = '{down} ↓↑ {up}',
        foreground=colors[2],
        background=colors[10],
        padding = 0,
    ),
    widget.CPU(
        font="Noto Sans Bold",
        #format = '{MemUsed}M/{MemTotal}M',
        update_interval = 1,
        fontsize = 12,
        foreground = colors[2],
        background = colors[11],
        mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
    ),
    widget.Memory(
        font="Noto Sans Bold",
        format = '{MemUsed: .0f}M/{MemTotal: .0f}M',
        update_interval = 1,
        fontsize = 12,
        measure_mem = 'M',
        foreground = colors[2],
        background = colors[13],
        mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
    ),
    widget.Clock(
        font="Noto Sans Bold",
        fontsize = 12,
        foreground = colors[2],
        background = colors[12],
        format="%H:%M %d.%m"
    ),
    widget.Systray(
        background=colors[1],
        icon_size=20,
        padding = 4
    ),
]

secondary_widgets = [
    *init_widgets_list(),
    primary_widgets[9],
]
