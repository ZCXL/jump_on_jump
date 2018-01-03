#!/bin/sh
mv current_gradx.png last_gradx.png
adb shell screencap -p /sdcard/Pictures/Screenshots/touch/current.png
adb pull /sdcard/Pictures/Screenshots/touch/current.png
