#-*- encode:utf-8 -*-
import commands
import time
import sys
def send_command(command):
    commands.getstatusoutput(command)
time_span=sys.argv[1]
send_command('sh ./start_touch.sh')
time.sleep(float(time_span))
send_command('sh ./finish_touch.sh')
