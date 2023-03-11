from libqtile import widget, qtile
from libqtile.command import lazy
from libqtile.widget import Spacer
from settings.keys import myTerm
from settings.colors import colors
import socket
import os

def base(fg='text', bg='dark'):
    return {'foreground': colors[14],'background': colors[15]}

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 9,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [

                 widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[15],
                        background = colors[15]
                        ),              #
               widget.Image(
                       filename = "~/.config/qtile/icons/garuda-red.png",
                       iconsize = 9,
                       background = colors[15],
                       mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('jgmenu_run')}
                       ),
               widget.GroupBox(

            **base(bg=colors[15]),
            font='UbuntuMono Nerd Font',

                    fontsize = 15,
                    margin_y = 3,
                    margin_x = 2,
                    padding_y = 5,
                    padding_x = 4,
                    borderwidth = 3,

            active=colors[5],
            inactive=colors[6],
            rounded= True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors[16],
            this_current_screen_border=colors[20],
            this_screen_border=colors[17],
            other_current_screen_border=colors[13],
            other_screen_border=colors[17],
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
                    border=colors[7],
                    foreground=colors[9],
                    margin=2,
                    txt_floating='🗗',
                    txt_minimized='>_ ',
                    borderwidth = 1,
                    background=colors[20],
                    #unfocused_border = 'border'
                ),

               widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[5],
                       background = colors[3],
                       padding = 0,
                       scale = 0.7
                       ),

               widget.CurrentLayout(
                      font = "Noto Sans Bold",
                      fontsize = 12,
                      foreground = colors[5],
                      background = colors[3]
                        ),


                widget.Net(
                         font="Noto Sans",
                         fontsize=12,
                        # Here enter your network name
                         interface=["wlp6s0"],
                         format = '{down} ↓↑ {up}',
                         foreground=colors[5],
                         background=colors[19],
                         padding = 0,
                         ),

                widget.CPU(
                        font="Noto Sans",
                        #format = '{MemUsed}M/{MemTotal}M',
                        update_interval = 1,
                        fontsize = 12,
                        foreground = colors[5],
                        background = colors[22],
                        mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                       ),

               widget.Memory(
                        font="Noto Sans",
                        format = '{MemUsed: .0f}M/{MemTotal: .0f}M',
                        update_interval = 1,
                        fontsize = 12,
                        measure_mem = 'M',
                        foreground = colors[5],
                        background = colors[16],
                        mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                       ),

               widget.Clock(
                        foreground = colors[9],
                        background = colors[23],
                        fontsize = 12,
                        format="%Y-%m-%d %H:%M"
                        ),

               widget.Systray(
                       background=colors[10],
                       icon_size=20,
                       padding = 4
                       ),
              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

