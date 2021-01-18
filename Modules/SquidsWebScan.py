#!/usr/bin/env python3
import sys
import re
import os
if len(sys.argv) < 5:
    print('The Syntax I am looking for is SquidsWebScan.py 10.10.10.5 Small_Dirlist Big_Dirlist [80,8080]')
    exit()
else:
    ip              = sys.argv[1]
    Small_Dirlist   = sys.argv[2]
    Big_Dirlist     = sys.argv[3]
    portlist        = sys.argv[4:]
    portlist        = portlist[0].split(' ')
    for port in portlist:
        port    = re.sub("[^0-9]", "", port)
        nikto   = "nikto -host http://{}:{}".format(ip, port)
        dirbust = f"gobuster dir -w {Small_Dirlist} -u http://{ip}:{port} && gobuster dir -w {Big_Dirlist} -u http://{ip}:{port}"
        os.system(f"tilix -t '{port} Nikto' -a app-new-session -x $SHELL -c 'tilix -t \"{port} Quick Scan\" -a session-add-right -x $SHELL -c \"{dirbust}; $SHELL\"; $SHELL -c \"{nikto}; $SHELL\"'")



