# import libqtile.lazy as lazy

# walcolors = []
# cache='/home/username/.cache/wal/colors'
# def load_colors(cache):
#     with open(cache, 'r') as file:
#         for i in range(8):
#             colors.append(file.readline().strip())
#     colors.append('#ffffff')
#     lazy.reload()
# load_colors(cache)

def init_colors():
    return [
            ["#212121", "#212121"], # 0 foreground
            ["#6272a4", "#6272a4"], # 1 groupbox-bg/systray-bg
            ["#ffffff", "#ffffff"], # 2 active font
            ["#2F343F", "#2F343F"], # 3 inactive screen/tasklist-bg
                # groupbox colors
            ["#ffd47e", "#ffd47e"], # 4 inactive font
            ["#abb2bf", "#abb2bf"], # 5 active screen
            ["#2aa899", "#2aa899"], # 6 unsigned
                # tasklist colors
            ["#44475a", "#44475a"], # 7 background
            ["#ff5555", "#ff5555"], # 8 border
                # widget colors
            ["#ff5555", "#ff5555"], # 9 CurrentLayout
            ["#56b6c2", "#56b6c2"], # 10 Net
            ["#bd93f9", "#bd93f9"], # 11 CPU
            ["#ffb86c", "#ffb86c"], # 12 Clock
            ["#2aa899", "#2aa899"], # 13 Memory
            ["#6790eb", "#6790eb"], # 14
        ]
colors = init_colors()
