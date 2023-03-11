from libqtile.config import Screen
from libqtile import bar
from settings.widgets import init_widgets_screen1, init_widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=0.85, background= "000000")),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=0.85, background= "000000"))]
screens = init_screens()