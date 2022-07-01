#!/usr/bin/env python3
import os
import sys
import pprint
import pwd
import argparse
import shlex
import subprocess
from netaddr import *

parser = argparse.ArgumentParser(
    #description='TireFire is Powered by book.hacktricks.xyz.',
    usage="\nsudo TireFire 1.1.1.1\nsudo TireFire -i tmux 1.1.1.1\nsudo TireFire --updatedb -m 1.1.1.1",
    epilog='TireFire is Powered by book.hacktricks.xyz.')
parser.add_argument("IP", help="IP adress or hostname of the target", type=str)
parser.add_argument('-i', '--interface', default='tilix', help='Interact via "tmux" or "tilix". tilix is default', metavar='')
parser.add_argument('-u', '--updatedb', action="store_true", help='Update to the latest TireFire database') 
parser.add_argument('-m', '--metasploit', action="store_true", help='Run TireFire with metasploit scans. NOT OSCP SAFE!')

if len(sys.argv) <= 1:
    parser.print_help()
    exit()

args    = parser.parse_args()

cwd     = os.getcwd()
tfdir   = subprocess.getoutput("readlink $(which TireFire)")
tfdir   = tfdir[:-11]

try:
    IP      = IPAddress(args.IP)
    hostname = args.IP.replace('.','_')
except:
    hostname = IP = args.IP

def init_updatedb():
    print("Updating database")
    subprocess.run(shlex.split("curl https://raw.githubusercontent.com/CoolHandSquid/TireFire/TireFire_V4/Main.csv --output {}/Main.csv".format(tfdir)), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Updating database complete")

def init_TireFire_tmux():
    hassession  = subprocess.run(shlex.split("tmux has-session -t TireFire_{}".format(hostname)), stderr=subprocess.DEVNULL)
    if hassession.returncode == 0:
        print("A session for {} already exists. Exiting".format(IP))
        exit()
    else:
        pass
    subprocess.run(shlex.split("tmux new-session -s TireFire_{} -n Main -c {} -d".format(hostname, cwd)))
    subprocess.run(shlex.split("tmux send-keys -t TireFire_{}:0.0 '{}TireFire_tmux.py {} {} {} {} {}' Enter".format(hostname, tfdir, IP, hostname, cwd, tfdir, args.metasploit)))
    print("TireFire session for {} named TireFire_{} has started successfully!".format(IP, hostname))
    if check_nested_tmux() == True:
        print("It looks like you are running TireFire from a user level tmux session. To attach to TireFire open a new tab in your terminal emulator and copy-paste:\nsudo tmux a -t TireFire_{}".format(hostname))
    else:
        print("copy-paste (or hotkey w if already inside tmux):\nsudo tmux a -t TireFire_{}".format(hostname))

def check_nested_tmux():
    """Check if in tmux and not root since user level nested tmux is bugged

    Returns:
        bool: status of current user level and tmux usage
    """
    if subprocess.getoutput("echo $TERM") == "screen":
        try:
            tmuxpid = subprocess.getoutput("cat /proc/{}/environ | grep -z TMUX=".format(os.getppid())).split(',')[1]
            tmuxpiduid  = subprocess.getoutput("ps -p {} -o uid=".format(tmuxpid)).strip()
            if tmuxpiduid != 0:
                return True
        except:
            return False
    else:
        return False

def init_TireFire_tilix():
    if os.environ['USER'] != "root":
        print("The shell environment user must be root. Try: sudo TireFire x.x.x.x -i tilix")
        exit()
    
    os.system("tilix --maximize -t 'TireFire  Main Page' -x $SHELL -c '{}TireFire_tilix.py {} {}; $SHELL'".format(tfdir, IP, args.metasploit))
    
if __name__ == "__main__":
    uid         = subprocess.getoutput("id -u")
    if uid != "0":
        print("TireFire must be run with root permissions.\nExample syntax: {}".format(parser.epilog))
        exit()
    if args.updatedb == True:
        init_updatedb()
    if args.interface == "tmux":
        init_TireFire_tmux()
    elif args.interface == "tilix":
        init_TireFire_tilix()
    else:
        print("That interface is not valid. Please chose tmux or tilix (ex: --interface tilix).")
        exit()

