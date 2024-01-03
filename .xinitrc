#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

## DWM
#feh --bg-fill ~/Pictures/endor.png
#xrdb ~/.Xresources
#picom &
#slstatus &
#exec dwm

## KDE
export DESKTOP_SESSION=plasma
exec startplasma-x11
