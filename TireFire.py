#!/usr/bin/env python3
import os
import sys

if len(sys.argv) != 2:
    print("The syntax I am looking for is more like TireFire 10.10.10.5")
    exit()
ip  = sys.argv[1]
os.system("tilix -t 'TireFire Main Page' -x $SHELL -c '/Yeet/Random/Udemy/TireFire/app.py {} ; $SHELL'".format(ip))
