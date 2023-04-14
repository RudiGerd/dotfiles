from libqtile import widget, qtile
from settings.keys import myTerm
from settings.theme import colors, fonts
from settings.net import active_interfaces
from settings.path import *
import socket
import os

def base(fg='base_dark', bg='base_light'):
    return {"foreground": colors[fg], "background": colors[bg]}

def powerline(fg='base_dark', bg='base_light', pl=""):
    return widget.TextBox(
        **base(fg, bg), text=pl, fontsize=28, padding=0  # Icon: nf-oct-triangle_left
    )

def init_widgets():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    return [
        widget.TextBox(
            font=fonts['font_bold'],
            text = 'Start',
            fontsize = 15,
            background = colors['system6'],
            mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('jgmenu_run')}
        ),
        powerline(fg='system6', pl=""),
        widget.GroupBox(
            **base(),
            font=fonts['font_nerd'],
            fontsize = 15,
            margin_y = 3,
            margin_x = 2,
            padding_y = 5,
            padding_x = 4,
            borderwidth = 3,
            active=colors['cursor'],
            inactive=colors['text_black'],
            rounded= True,
            highlight_method='block',
            urgent_alert_method='block',
            this_current_screen_border=colors['system1'],
            this_screen_border=colors['base_light'],
            other_current_screen_border=colors['system1'],
            other_screen_border=colors['base_light'],
            disable_drag=True
        ),
        powerline(fg='system6'),
        list_widgets('CurrentLayoutIcon', background='system6'),
        widget.Sep(
            **base(bg='system6'),
            linewidth = 0,
            padding = 3,
        ),
        powerline(fg='system6', pl=""),
        widget.TaskList(
            **base(),
            font=fonts['font_bold'],
            fontsize=14,
            highlight_method = 'border',
            max_title_width=150,
            rounded=True,
            padding_x=0,
            padding_y=0,
            margin_y=0,
            border=colors['system1'],
            margin=2,
            txt_floating='🗗',
            txt_minimized='>_ ',
            borderwidth = 1,
            #unfocused_border = 'border'
        )
    ]

def list_widgets(describe, forground='base_dark', background='base_light'):
    widget_font = fonts['font_bold']
    widget_fontsize = 12
    widgets = {
        'CurrentLayoutIcon' : widget.CurrentLayoutIcon(
            **base(fg=forground, bg=background),
            padding = 0,
            scale = 1
        ),
        'CurrentLayout' : widget.CurrentLayout(
            **base(fg=forground, bg=background),
            font = widget_font,
            fontsize = widget_fontsize
        ),
        'Net' : widget.Net(
            **base(fg=forground, bg=background),
            font=widget_font,
            fontsize=widget_fontsize,
            interface=active_interfaces,
            format = '{down} ↓↑ {up}',
            padding = 0,
        ),
        'CPU' : widget.CPU(
            **base(fg=forground, bg=background),
            font=widget_font,
            fontsize = widget_fontsize,
            update_interval = 1,
            mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
        ),
        'Memory' : widget.Memory(
            **base(fg=forground, bg=background),
            font=widget_font,
            fontsize = widget_fontsize,
            format = '{MemUsed: .0f}M/{MemTotal: .0f}M',
            update_interval = 1,
            measure_mem = 'M',
            mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
        ),
        'Clock' : widget.Clock(
            **base(fg=forground, bg=background),
            font=widget_font,
            fontsize = widget_fontsize,
            format="%H:%M %d.%m"
        ),
        'Systray' : widget.Systray(
            **base(fg=forground, bg=background),
            icon_size=20,
            padding = 4
        ),
    }
    return widgets[describe]

primary_widgets = [
    *init_widgets(),
    powerline(fg='widget1'),
    widget.WidgetBox(
        **base(bg='widget1'),
        widgets = [list_widgets(describe = 'Net', background='widget1')],
        text_closed=" ",
        text_open=" ",
        fontsize=24
    ),
    powerline(fg='widget2', bg='widget1'),
    widget.WidgetBox(
        **base(bg='widget2'),
        widgets = [list_widgets(describe = 'CPU', background='widget2')], 
        text_closed=" ",
        text_open=" ",
        fontsize=24
    ),
    powerline(fg='widget3', bg='widget2'),
    widget.WidgetBox(
        **base(bg='widget3'),
        widgets = [list_widgets(describe = 'Memory', background='widget3')],
        text_closed=" ",
        text_open=" ",
        fontsize=24
    ),
    powerline(fg='widget4', bg='widget3'),
    list_widgets(describe = 'Clock', background='widget4'),
    powerline(fg='base_light', bg='widget4'),
    list_widgets(describe = 'Systray'),
]

secondary_widgets = [
    *init_widgets(),
    powerline(fg='widget4'),
    list_widgets(describe = 'Clock', background='widget4'),
]

widget_defaults = {
    "font": fonts['font'],
    "fontsize": 14,
    "padding": 1,
    "background": colors['base_light'],
}
