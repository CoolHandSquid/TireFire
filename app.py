#!/usr/bin/env python3
import os
import re
import sys
import click
import shlex
import psutil
import argparse
import subprocess
from netaddr    import *
from colorama   import Fore, Style
from tabulate   import tabulate
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import db

##################################################
#Begin Start 
##################################################
def termstat():
    #Determine if app.py was kicked off with TireFire.py 
    tfpid   = os.getpgid(psutil.Process(os.getppid()).ppid()) 
    psline  = subprocess.getoutput("ps -efj | grep {} | grep -v grep".format(tfpid))
    if "/usr/bin/TireFire" not in psline:
        return False
    else:
        return True

def check_ping(IP):
    #Attempt to ping target and return TTL
    cmd     = "ping -c 1 {}".format(IP)
    try:
        ping    = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
        response= ping.wait(1)
    except:
        response = 1
    if response == 0:
        ttl         = str(ping.communicate()[0]).split()[11]
        return ttl
    else:
        error   = "The ping was unsuccsessful..."
        return error

def start(IP):
    if termstat() == False:
        print("Please run TireFire with the syntax like: TireFire 10.10.10.5")
        quit()
    if click.confirm("Do you want to kick this off with an Nmap scan?", default=True):
        print(Fore.GREEN + check_ping(IP) + Style.RESET_ALL)
        print(Fore.YELLOW + "Reference TTL Table\n" + Fore.CYAN + display_ttl() + Style.RESET_ALL)
        command = "nmap -Pn {} && nmap -sC -sV -Pn {} && nmap -p- -Pn {} && nmap -Pn -p- -sU {}".format(IP, IP, IP, IP)
        doit("Nmap", "Kickoff", command)
    return

def get_network(IP):
    try: 
        IP      = IP +"/24"
        IP      = IPNetwork(IP)
        Network = IP.network
        CIDR    = IP.prefixlen
    except:
        Network = "10.10.10.0"
        CIDR    = "/24"
    return Network, CIDR

##################################################
#Begin Display
##################################################
def display_main():
    items   = db.get_display_main()
    items.insert(0, ("Variables", "Vars", "Set Global Variables"))
    headers = ["Name", "Port", "Description"]
    rawin   = input(Fore.YELLOW + "MAIN Table\n" + Style.RESET_ALL + tabulate(items, headers=headers, tablefmt="psql", showindex="always")+ "\n> ")
    if input_validation(items, rawin) == True:        
        proto   = eval("items[{}][0]".format(int(rawin)))
        if proto == "Variables":
            display_variables()
        else:
            display_sub(eval("items[{}][0]".format(int(rawin))))

def display_sub(proto):
    items   = db.get_display_sub(proto) 
    fullcmd = db.get_fullcommand(proto)
    subheaders  = ["Cmd Name", "Description", "Command", "Comment"]
    rawin   = input(Fore.YELLOW + proto + " Table\n" + Style.RESET_ALL + tabulate(items, headers=subheaders, tablefmt="psql", showindex="always")+ "\n> ")
    rawin = re.split(',|\.| ',rawin)
    for rawin in rawin:
        if input_validation(items, rawin) == True:
            try:
                scan    = eval("items[{}][0]".format(rawin))
                command = eval("fullcmd[{}][0]".format(rawin)) 
                if command[0] == '#':
                    showit(proto, scan, command)    
                elif "&&&&" in command:
                    #command     = (eval("f'" + command + "'"))
                    command     = command.format(**globals())
                    commands    = command.split("&&&&")
                    for cmd in commands:
                        doit(proto, scan, cmd)
                else:
                    #command = (eval("f'" + command + "'"))
                    command = command.format(**globals())
                    doit(proto, scan, command)
            except:
                try:
                    print(rawin + " May be out of range.")
                except:
                    print("That command didn't seem to work...")
                display_main()

def display_variables():
    items   = [("IP", IP), ("Network", Network), ("CIDR", CIDR), ("Domain_Name", Domain_Name), ("Naming_Context", Naming_Context), ("Web_Proto", Web_Proto), ("Web_Port", Web_Port), ("Username", Username), ("Password", Password), ("Big_Passwordlist", Big_Passwordlist), ("Small_Passwordlist", Small_Passwordlist), ("Big_Userlist", Big_Userlist), ("Small_Userlist", Small_Userlist), ("Big_Dirlist", Big_Dirlist), ("Small_Dirlist", Small_Dirlist)]
    headers = ["Variable", "Current Value"]
    rawin   = input(Fore.YELLOW + "Variables Table\n" + Style.RESET_ALL + tabulate(items, headers=headers, tablefmt="psql", showindex="always")+ "\n> ")
    if input_validation(items, rawin) == True:
        try:
            var = eval("items[{}][0]".format(rawin))
            globals()[var] = input("What would you like to set the {} to?\n> ".format(var))
            print(Fore.GREEN + "{} has been set to {}".format(var, globals()[var]) + Style.RESET_ALL)
        except:
            print("That did not seem to work. There was no variable change.")
    display_main()

def display_ttl():
    items   = db.get_display_ttl()
    headers = ["Operating Systems", "TCP", "UDP", "ICMP"]
    return tabulate(items, headers=headers, tablefmt="psql")

##################################################
#Begin Execution 
##################################################
def doit(proto, scan, command):
    #Called to execute command in new tilix tab
    tab_name    = "{} {}".format(proto, scan)
    cmd = "tilix -t '{}' -x bash -c 'echo \"{}\"; {}; bash'".format(tab_name, command, command) 
    subprocess.Popen(shlex.split(cmd)) 
    #os.system("tilix -t '{}' -x $SHELL -c 'echo \"{}\"; {}; $SHELL'".format(tab_name, command, command))
    print(Fore.GREEN + "{}".format(command) + Style.RESET_ALL)

def showit(proto, scan, command):
    #Called to write output in new tilix tab
    tab_name    = "{} {}".format(proto, scan)
    with open('showit.txt', 'w') as sfile:
        scommand = command.split('\n')
        if command[1] == "#":
            sfile.write("\n{}\n".format(command))
        else:
            for line in scommand:
                try:
                    #line = (eval("f'" + line + "'"))
                    line    = line.format(**globals())
                except:
                    pass
                sfile.write("{}\n".format(line))
    command = "cat showit.txt"
    cmd     = "tilix -t '{}' -x bash -c 'echo \"{}\"; {}; bash'".format(tab_name, tab_name, command) 
    subprocess.Popen(shlex.split(cmd))
    #os.system("tilix -t '{}' -x $SHELL -c 'echo \"{}\"; {}; $SHELL'".format(tab_name, tab_name, command))
    print(Fore.GREEN + "{} {}".format(proto, scan) + Style.RESET_ALL)

def input_validation(items, rawin):
    bad_input       = "Some decent input would be nice..."
    exit_message    = "Later Tater"
    if rawin.lower() == "exit":
        print(exit_message)
        sys.exit()
    try:
        rawin   = int(rawin)
        if rawin in range(len(items) + 1):
            return True
        else:
            raise
    except KeyboardInterrupt:
        sys.exit()
        return False
    except:
        if rawin != "":
            print(bad_input)
        return False

if __name__ == "__main__":
    parser  = argparse.ArgumentParser()
    parser.add_argument("IP", help="IP address of the target", type=str)
    args    = parser.parse_args()

    IP              = args.IP
    Network         = get_network(IP)[0]
    CIDR            = get_network(IP)[1]
    Domain_Name     = "yee.wtf"
    Naming_Context  = "DC=YeetCannon,DC=local"
    Web_Proto       = "http"
    Web_Port        = "80"
    Username        = "Squid"
    Password        = "Y337C4nn0n!"
    Big_Passwordlist    = "/usr/share/wordlists/rockyou.txt"
    Small_Passwordlist  = "/usr/share/seclists/Passwords/darkweb2017-top1000.txt"
    Big_Userlist        = "/usr/share/seclists/Usernames/Names/names.txt"
    Small_Userlist      = "/usr/share/seclists/Usernames/top-usernames-shortlist.txt"
    Big_Dirlist         = "/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt"
    Small_Dirlist       = "/usr/share/seclists/Discovery/Web-Content/common.txt"

    start(IP)
    while True:
        try:
            display_main()
        except:
            exit()
