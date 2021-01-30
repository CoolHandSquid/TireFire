#!/usr/bin/env python3
import os
import sys
import click
import subprocess
from colorama   import Fore, Style
from tabulate   import tabulate
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import db
import variables

##################################################
#Begin Start 
##################################################
def termstat():
    #used to determine if your 
    curuser = subprocess.getoutput("id")
    pid = os.getpid()
    if "uid=0(root)" not in curuser:
        print("Fair Warning: You are gonna wanna run this with root privileges")
    ppid = subprocess.getoutput("ps -o ppid= {}".format(pid))
    gpid = subprocess.getoutput("ps -o ppid= {}".format(ppid))
    psline = subprocess.getoutput("ps -aux | grep {} | grep -v grep".format(gpid))
    if "tilix" not in psline:
        return False
    else:
        return True

def check_ping(IP):
    responce    = os.system("ping -c 1 {}".format(IP))
    if responce == 0:
        responce    = os.popen("ping -c 1 {}".format(IP)).read()
        ttl         = responce.split()[12]
        return ttl
    else:
        error   = "The ping was unsuccsessful..."
        return error

def start(IP):
    if termstat() == False:
        print("Please run TireFire from tilix")
        quit()
    if len(sys.argv) != 2:
        print("The syntax that I am looking for is more like TireFire 10.10.10.5")
        quit()
    if click.confirm("Do you want to kick this off with an Nmap scan?", default=True):
        print(Fore.GREEN + check_ping(IP) + Style.RESET_ALL)
        print(Fore.YELLOW + "TTL Table\n" + Style.RESET_ALL + display_ttl())
        command = "nmap -Pn {} && nmap -sC -sV -Pn {} && nmap -p- -Pn {} && nmap -Pn -p- -sU {}".format(IP, IP, IP, IP)
        doit("Nmap", "Kickoff", command)
    return
##################################################
#Begin Display
##################################################
def display_main():
    items   = db.get_display_main()
    items.append(("Variables", "Z", "Set Global Variables"))
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
    if input_validation(items, rawin) == True:
        try:
            scan    = eval("items[{}][0]".format(rawin))
            command = eval("fullcmd[{}][0]".format(rawin)) 
            if command[0] == '#':
                showit(proto, scan, command)    
            elif command[0] == '%':
                command = command[1:]
                if "&&&&" in command:
                    commands    = command.split("&&&&")
                    for cmd in commands:
                        for Port in Web_Portlist:
                            tcommand    = (eval("f'" + cmd + "'"))
                            doit(proto, scan, tcommand)
                else:
                    for Port in Web_Portlist:
                        tcommand = (eval("f'" + command + "'"))
                        doit(proto, scan, tcommand)
            elif "&&&&" in command:
                command     = (eval("f'" + command + "'"))
                commands    = command.split("&&&&")
                for cmd in commands:
                    doit(proto, scan, cmd)
            else:
                command = (eval("f'" + command + "'"))
                doit(proto, scan, command)
        except:
            input("That command didn't seem to work...\nRemember that if you are going to add a command to the DB, be sure to escape single quotes.")
            display_main()

def display_variables():
    items   = [("IP", IP), ("Domain_Name", Domain_Name), ("Naming_Context", Naming_Context), ("Web_Portlist", Web_Portlist), ("Big_Passwordlist", Big_Passwordlist), ("Small_Passwordlist", Small_Passwordlist), ("Big_Userlist", Big_Userlist), ("Small_Userlist", Small_Userlist), ("Big_Dirlist", Big_Dirlist), ("Small_Dirlist", Small_Dirlist)]
    headers = ["Variable", "Current Value"]
    rawin   = input(Fore.YELLOW + "Variables Table\n" + Style.RESET_ALL + tabulate(items, headers=headers, tablefmt="psql", showindex="always")+ "\n> ")
    if input_validation(items, rawin) == True:
        var = eval("items[{}][0]".format(rawin))
        globals()[var] = variables.set(var)
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
    os.system("tilix -t '{}' -x $SHELL -c 'echo \"{}\"; {}; $SHELL'".format(tab_name, command, command))
    print(Fore.GREEN + "{}".format(command) + Style.RESET_ALL)

def showit(proto, scan, command):
    #Called to write output in new tilix tab
    tab_name    = "{} {}".format(proto, scan)
    os.system("tilix -t '{}' -x $SHELL -c 'echo \"{}\"; $SHELL'".format(tab_name, command))
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
        print(exit_message)
        sys.exit()
        return False
    except:
        print(bad_input)
        return False

IP              = sys.argv[1]
Domain_Name     = "yee.wtf"
Naming_Context  = "DC=YeetCannon,DC=local"
Web_Portlist    = ["80"]
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
