#!/bin/sh
adb shell screencap -p /sdcard/Pictures/Screenshots/touch/current.png
adb pull /sdcard/Pictures/Screenshots/touch/current.png
