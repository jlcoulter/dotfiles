from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn Rofi"),
    Key([mod], "b", lazy.spawn("brave"), desc="Spawn brave"),
    Key([mod], "t", lazy.spawn("alacritty -e nnn -eEHn"), desc="Spawn nnn"),
    Key(["shift", "control"], "space", lazy.spawn("flameshot gui"), desc="Spawn Flameshot Screenshot"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"], 
                i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)
                ),
        ]
    )

layouts = [
    layout.MonadThreeCol(
        single_margin = [0, 1300, 0, 1300],
        ratio = 0.55,
        margin = 8,
        border_focus = "#3e91ff",
        border_normal = "#ff0c00",
        border_width = 4
    ),
]

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(
                     linewidth = 0,
                     padding = 20
                ),
                widget.GroupBox(
                    active = "#98d3ff",
                    inactive = "#98d3ff",
                    padding = 6,
                    highlight_method='block'
                ),
                widget.Prompt(
                    active = "#98d3ff",
                    inactive = "#98d3ff"
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    padding = 2185
                    ),
            ],
            24,
            border_width=[2, 0, 2, 0],
            border_color=["000000", "000000", "000000", "000000"],
            background="#50000000"
        ),
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"
