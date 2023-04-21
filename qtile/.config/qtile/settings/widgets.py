from libqtile import widget, qtile
from settings.keys import myTerm
from settings.theme import colors, fonts
from settings.net import active_interfaces
from settings.path import *

def base(fg='base_dark', bg='base_light'):
    return {"foreground": colors[fg], "background": colors[bg]}

def powerline(fg='base_dark', bg='base_light', pl=""):
    return widget.TextBox(
        **base(fg, bg), text=pl, fontsize=28, padding=0  # Icon: nf-oct-triangle_left
    )

def init_widgets():
    return [
        widget.TextBox(
            font=fonts['font_bold'],
            text = '',
            fontsize = 14,
            background = colors['system4'],
            mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('jgmenu_run')}
        ),
        powerline(fg='system4', pl=""),
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
        powerline(fg='system4'),
        widget.CurrentLayoutIcon(
            **base(fg='system4', bg='system4'),
            padding = 0,
            scale = 1
        ),
        widget.Sep(
            **base(bg='system4'),
            linewidth = 0,
            padding = 3,
        ),
        powerline(fg='system4', pl=""),
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
            borderwidth = 1
        )
    ]

def list_widgets(list_describe, list_forground='base_dark', list_background='base_light'):
    widget_font = fonts['font_bold']
    widget_fontsize = 12
    widgets = {
        'Net' : [widget.Net(
            **base(fg=list_forground, bg=list_background),
            font=widget_font,
            fontsize=widget_fontsize,
            interface=active_interfaces,
            format = '{down} ↓↑ {up}',
            padding = 0,
        )],
        'CPU' : [widget.CPU(
            **base(fg=list_forground, bg=list_background),
            font=widget_font,
            fontsize = widget_fontsize,
            update_interval = 1,
            mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
        )],
        'Memory' : [widget.Memory(
            **base(fg=list_forground, bg=list_background),
            font=widget_font,
            fontsize = widget_fontsize,
            format = '{MemUsed: .0f}M/{MemTotal: .0f}M',
            update_interval = 1,
            measure_mem = 'M',
            mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
        )],
        'Clock' : [widget.Clock(
            **base(fg=list_forground, bg=list_background),
            font=widget_font,
            fontsize = widget_fontsize,
            format="%H:%M - %d.%m.%Y",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('yad --calendar')},
        )],
        'DF' : [widget.DF(
            **base(fg=list_forground, bg=list_background),
            font=widget_font,
            fontsize = widget_fontsize,
            format = '{uf}{m} - {r:.0f}%',
            visible_on_warn = False,
            warn_space = 10,
            partition = '/',
            update_interval = 1,
            mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e ranger')},
        )],
        'KeyboardLayout' : [widget.KeyboardLayout(
            **base(fg=list_forground, bg=list_background),
            font=widget_font,
            fontsize = widget_fontsize,
            configured_keyboards = ['de', 'eu', 'us'],
            display_map = {'de': 'DE ', 'eu': 'EU ', 'us': 'US '},
            padding = 0,
        )],
        'Sensors' : [widget.NvidiaSensors(
            **base(fg=list_forground, bg=list_background),
            font=widget_font,
            fontsize = widget_fontsize,
            format = 'GPU {temp}°C',
            update_interval = 1,
            forground_alert = colors['system1'],
            mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e nvidia-settings')},
        ),
                    widget.ThermalZone(
            **base(fg=list_forground, bg=list_background),
            font=widget_font,
            fontsize = widget_fontsize,
            format = ' CPU: {temp}°C',
            update_interval = 1,
            threshold = 90,
            forground_alert = colors['system1'],
            mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e sensors')},
        )],
    }
    return widgets[list_describe]

def box_widget(box_describe, box_icon, box_background):
    powercolor = f'widget{int(box_background[-1])-1}' if int(box_background[-1]) > 1 else 'base_light'
    return [
        powerline(fg=box_background, bg=powercolor), 
        widget.WidgetBox(
            **base(bg=box_background),
            widgets=list_widgets(list_describe=box_describe, list_background=box_background),
            text_closed=box_icon,
            text_open=box_icon,
            fontsize=16
        )
    ]

primary_widgets = [
    *init_widgets(),
    *box_widget(box_describe='Net', box_icon=' ', box_background='widget1'),
    *box_widget(box_describe='CPU', box_icon=' ', box_background='widget2'),
    *box_widget(box_describe='Sensors', box_icon=' ', box_background='widget3'),
    *box_widget(box_describe='Memory', box_icon=' ', box_background='widget4'),
    *box_widget(box_describe='DF', box_icon=' ', box_background='widget5'),
    powerline(fg='widget6', bg='widget5'),
    *list_widgets(list_describe = 'Clock', list_background='widget6'),
    powerline(fg='widget7', bg='widget6'),
    *list_widgets(list_describe = 'KeyboardLayout', list_background='widget7'),
    powerline(fg='base_light', bg='widget7'),
    widget.Systray(
        background=colors['base_light'],
        icon_size=20,
        padding = 4
    ),
]

secondary_widgets = [
    *init_widgets(),
    powerline(fg='widget5'),
    *list_widgets(list_describe = 'Clock', list_background='widget5'),
]

widget_defaults = {
    "font": fonts['font'],
    "fontsize": 14,
    "padding": 1,
    "background": colors['base_light'],
}
