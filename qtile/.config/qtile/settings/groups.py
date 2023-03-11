from libqtile.config import Key, Group
from libqtile.command import lazy
from settings.keys import mod, keys

# Define groups
groups = [
    Group("1", label="1: ", layout="monadtall"),
    Group("2", label="2: ", layout="bsp"),
    Group("3", label="3: ", layout="bsp"),
    Group("4", label="4: ", layout="bsp"),
    Group("5", label="5: ", layout="monadtall"),
    Group("6", label="6: ", layout="bsp"),
    Group("7", label="7: ", layout="monadtall"),
    Group("8", label="8: ", layout="monadtall"),
    Group("9", label="9: ", layout="max"),
    Group("0", label="0: ", layout="max"),
]

for i in groups:
    keys.extend([
#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)
