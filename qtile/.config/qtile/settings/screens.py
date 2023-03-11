from libqtile.config import Screen
from libqtile import bar
from settings.widgets import primary_widgets, secondary_widgets

def init_screens():
    return [Screen(top=bar.Bar(widgets=primary_widgets, size=20, opacity=0.85, background= "000000")),
            Screen(top=bar.Bar(widgets=secondary_widgets, size=20, opacity=0.85, background= "000000"))]
screens = init_screens()