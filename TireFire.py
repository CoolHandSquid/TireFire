#!/usr/bin/env python3
import os
import pwd
import argparse
import subprocess

parser  = argparse.ArgumentParser()
parser.add_argument("IP", help="IP address of the target", type=str)
args    = parser.parse_args()

if pwd.getpwuid(os.getuid())[0] != "root":
    print("TireFire needs to be run as root. Try again.")
    exit()
IP      = args.IP
path    = subprocess.getoutput("readlink /usr/bin/TireFire")
path    = path[:-12]
os.system("tilix --maximize -t 'TireFire Main Page' -x $SHELL -c '{}/app.py {} ; $SHELL'".format(path, IP))
