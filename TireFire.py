#!/usr/bin/env python3
import os
import sys
import subprocess

if len(sys.argv) != 2:
    print("The syntax I am looking for is more like TireFire 10.10.10.5")
    exit()
ip      = sys.argv[1]
path    = subprocess.getoutput("readlink /usr/bin/TireFire")
path    = path[:-12]
os.system("tilix --maximize -t 'TireFire Main Page' -x $SHELL -c '{}/app.py {} ; $SHELL'".format(path, ip))
