#!/bin/sh
#start touch
adb shell sendevent /dev/input/event5 3 58 63
adb shell sendevent /dev/input/event5 3 53 791
adb shell sendevent /dev/input/event5 3 54 662
adb shell sendevent /dev/input/event5 3 57 0
adb shell sendevent /dev/input/event5 0 2 0
adb shell sendevent /dev/input/event5 1 330 1
adb shell sendevent /dev/input/event5 0 0 0

#hold on once
#adb shell sendevent /dev/input/event5 3 58 63
#adb shell sendevent /dev/input/event5 3 53 791
#adb shell sendevent /dev/input/event5 3 54 662
#adb shell sendevent /dev/input/event5 3 57 0
#adb shell sendevent /dev/input/event5 0 2 0
#adb shell sendevent /dev/input/event5 0 0 0
