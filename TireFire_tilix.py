#!/usr/bin/env python3
import os
import re
import sys
import time
import click
import shlex
import psutil
import argparse
import subprocess
from math       import ceil
from netaddr    import *
from colorama   import Fore, Style
from tabulate   import tabulate
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import db

##################################################
#Begin Start 
##################################################
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
    if click.confirm("Do you want to kick this off with an Nmap scan?", default=True):
        sendtext(Fore.GREEN + check_ping(IP) + "\n" + Fore.YELLOW + "Reference TTL Table\n" +Fore.CYAN + display_ttl() + Style.RESET_ALL)
        subprocess.run(shlex.split("cat sendtext.txt"), stdout=subprocess.PIPE, universal_newlines=True) 
        command = "cat {} && nmap -Pn {} && nmap -sC -sV -Pn {} && nmap -p- -Pn {} && nmap -Pn -p- -sU {}".format("sendtext.txt", IP, IP, IP, IP)
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
    subprocess.run(shlex.split("clear"))
    for cmd in cmd_history:
        print(cmd)
    items   = db.get_display_main()
    items.insert(0, ["Variables", "Vars", "Set Global Variables"])
    if os.get_terminal_size()[0] < 130:
        rawin   = input(Fore.YELLOW + "MAIN Table\n" + Style.RESET_ALL + display_vertical(items) + "\n> ")
    else:
        rawin   = input(Fore.YELLOW + "MAIN Table\n" + Style.RESET_ALL + display_horizontal(items) + "\n> ")
    ###Display NormalVVV
    #rawin   = input(Fore.YELLOW + "MAIN Table\n" + Style.RESET_ALL + tabulate(items, headers=["Name", "Port", "Description", "Name"], tablefmt="psql", showindex="always")+ "\n> ")
    ###I should not have to do this. Ask Andrew
    items   = db.get_display_main()
    items.insert(0, ["Variables", "Vars", "Set Global Variables"])
    if input_validation(items, rawin) == True:        
        proto   = eval("items[{}][0]".format(int(rawin)))
        if proto == "Variables":
            display_variables()
        else:
            display_sub(eval("items[{}][0]".format(int(rawin))))

def display_horizontal(items):
    aitems  = items.copy()
    lines   = ceil(len(aitems)/2)
    nitems  = []
    for line in range(lines):
        try:
            aitems[line].insert(0,str(line))
            aitems[lines+line].insert(0,str(lines+line))
            nitems.append(aitems[line]+aitems[line+lines])
        except:
            nitems.append(aitems[line])
    return tabulate(nitems,headers=[" ", "Name", "Port", "Description", " ", "Name", "Port", "Description"], tablefmt="psql")

def display_vertical(items):
    aitems  = items.copy()
    lines   = len(aitems)
    nitems  = []
    
    for line in range(lines):
        aitems[line].insert(0, str(line))
        nitems.append(aitems[line])
    return tabulate(nitems, headers=["Name", "Port", "Description"], tablefmt="psql")

def display_sub(proto):
    items   = db.get_display_sub(proto, metasploit) 
    fullcmd = db.get_fullcommand(proto)
    subheaders  = ["Cmd Name", "Description", "Command"]
    rawin   = input(Fore.YELLOW + proto + " Table\n" + Style.RESET_ALL + tabulate(items, headers=subheaders, tablefmt="psql", showindex="always")+ "\n> ")
    rawin = re.split(',|\.| ',rawin)
    for rawin in rawin:
        if input_validation(items, rawin) == True:
            try:
                scan    = eval("items[{}][0]".format(rawin))
                command = eval("fullcmd[{}][0]".format(rawin)) 
                if command[0] == '?':
                    command = hotvar(command)
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
    items   = [("IP", IP), ("Network", Network), ("CIDR", CIDR), ("Domain_Name", Domain_Name), ("Naming_Context", Naming_Context), ("Web_Proto", Web_Proto), ("Web_Port", Web_Port), ("Username", Username), ("Password", Password), ("Big_Passwordlist", Big_Passwordlist), ("Small_Passwordlist", Small_Passwordlist), ("Big_Userlist", Big_Userlist), ("Small_Userlist", Small_Userlist), ("Big_Dirlist", Big_Dirlist), ("Small_Dirlist", Small_Dirlist), ("Tool_Dir", Tool_Dir), ("Subdomain_List", Subdomain_List), ("Ffuf_Filters", Ffuf_Filters)]
    headers = ["Variable", "Current Value"]
    rawin   = input(Fore.YELLOW + "Variables Table\n" + Style.RESET_ALL + tabulate(items, headers=headers, tablefmt="psql", showindex="always")+ "\n> ")
    if input_validation(items, rawin) == True:
        try:
            var = eval("items[{}][0]".format(rawin))
            globals()[var] = input("What would you like to set the {} to?\n> ".format(var))
            cmd_history.append(Fore.GREEN + "{} has been set to {}".format(var, globals()[var]) + Style.RESET_ALL)
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
    cmd_history.append(Fore.GREEN + "{}".format(command) + Style.RESET_ALL)

def showit(proto, scan, command):
    #Called to write output in new tilix tab from DB
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
    cmd_history.append(Fore.GREEN + "{} {}".format(proto, scan) + Style.RESET_ALL)
    time.sleep(0.5)

def sendtext(text):
    #Called to write to sendtext.txt
    with open('sendtext.txt', 'w') as sfile:
        sfile.write("{}\n".format(text))

def hotvar(command):
    try:
        hotdic  = {}
        key     = 0
        while command[0] == '?':
            key     += 1
            raw_var = input(Fore.CYAN+Style.BRIGHT+"Current Command: "+command.split("\n")[-1]+Style.RESET_ALL+"\n"+str(key)+". "+command[1:command.index('\n')] +"\n> ")
            hotdic[key] = raw_var
            command = command[command.index('\n')+1:]
            command =command.replace("{"+str(key)+"}",hotdic[key])
        return command
    except:
        print("Something went wrong. The error more than likley resides in the DB. Sending the command without HotVariables.")
        return command

def input_validation(items, rawin):
    bad_input       = "Some decent input would be nice..."
    exit_message    = "Later Tater"
    if rawin.lower() == "exit":
        print(exit_message)
        sys.exit()
    try:
        rawin   = int(rawin)
        if rawin in range(len(items)):
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
    parser.add_argument("metasploit", help="If msf scans will populate in db")
    args    = parser.parse_args()

    cmd_history     = []
    IP              = args.IP
    Tool_Dir        = os.getcwd() + "/"
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
    Subdomain_List      = "/usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt"
    Ffuf_Filters        = "-fs 0"
    metasploit      = args.metasploit
    
    start(IP)
    while True:
        try:
            display_main()
        except KeyboardInterrupt:
            if click.confirm("\nDo you want to exit TireFire?", default=False):
                print("Later Tater")
                exit()
            else:
                continue
        except:
            exit()
