#!/usr/bin/python3
import os
import subprocess
import sys
from colorama import Fore, Style

#TireFire is a 19% Security Solution Created by CoolHandSquid and inspired by MaBraFoo


"""
When making a function, be sure to add it into home_lst<<<<<<<<<<<<<<<<<<<<<<
def nmap():					##function name
	nmap_title	= "nmap"	##function title should match the name
	nmap_comment= "#####"	##comment can be ##### or it can be something else, just a comment.
	nmap_lst	= ["SquidsSmartScan", "Quick Scan", "Version Scan", "All Port Scan", "All Vulns Scan"]	##lst will be the list printed to screen to choose from
	nmap 		= Display_class(nmap_title, nmap_comment, nmap_lst)	## needed to create the object nmap
	scan 		= Display(nmap)	##This will be passed and make the variable "scan" a number corresponding to something in lst. 
"""

#Details
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
#Classes and Variable Declarations Begin

class Display_class:
	def __init__(self, title, comment, lst):
		self.title		= title
		self.comment 	= comment	
		self.lst 		= lst

home_title	= "Home"
home_comment= "#####"
home_lst	= ["netdiscover()", "nmap()", "dns()", "web()", "webapp()", "smb()", "ldap()", "ProtoBrute()"]
home 		= Display_class(home_title, home_comment, home_lst)

yes		= [ "yes","y", "yee yee", "yee", "yeah", "yeet", "yeet cannon", "yea", "yeah", "ye"]
no 		= [ "no", "n", "nah", "fuckyou"]
tfpath 	= subprocess.getoutput("readlink /usr/bin/TireFire")
tfpath	= tfpath[:-12]

#Variable Declarations End
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
#Main Modules Begin
def netdiscover():
	netdiscover_title	= "netdiscover"
	netdiscover_comment	= "#####"
	netdiscover_lst		= ["Netdiscover"]
	netdiscover 		= Display_class(netdiscover_title, netdiscover_comment, netdiscover_lst)
	scan				= Display(netdiscover)

	q1	= input("What is the class C subnet you would like to scan?\nExample Syntax: 192.168.11.0\n> ")
	if scan == 1:
		#netdiscover
		command = "sudo netdiscover -r {}".format(q1)
		doit(command)

def nmap():
	nmap_title	= "nmap"
	nmap_comment= "#####"
	nmap_lst	= ["SquidsSmartScan", "Quick Scan", "Version Scan", "All Port Scan", "All Vulns Scan"]
	nmap 		= Display_class(nmap_title, nmap_comment, nmap_lst)
	scan 		= Display(nmap)

	if scan		== 1:
		#SquidsSmartScan
		command = "nmap {} && nmap -sC -sV {} && nmap -p- -Pn {}".format(ip, ip, ip)
	elif scan 	== 2:
		#Quick Scan
		command = "nmap {}".format(ip)
	elif scan 	== 3:
		#Version Scan
		command = "nmap -sC -sV {}".format(ip)
	elif scan 	== 4:
		#All Port Scan
		command = "nmap -p- -Pn {}".format(ip)
	elif scan 	== 5:
		#All Vulns Scan
		command = "nmap --script smb-vuln* -p 139,445 {}".format(ip)
	doit(command)

def dns():
	dns_title	= "dns"
	dns_comment= "#####"
	dns_lst	= ["SquidsDnsTool"]
	dns 		= Display_class(dns_title, dns_comment, dns_lst)
	scan 		= Display(dns)

	if scan 	== 1:
		#SquidsDnsTool
		dn 		= input("What is your best guest at a domain name? (Example: yeet.wtf)\n> ")
		command = "SquidsDnsTool {} {}".format(ip, dn)
	doit(command)

def web():
	web_title	= "web"
	web_comment= "#####"
	web_lst	= ["QuickWebScan", "SquidsSqlMapTool", "SquidsWfuzzTool", "nikto", "dirsearch", "nmap VulnScan", "Squids ShellShock NSE"]
	web 		= Display_class(web_title, web_comment, web_lst)
	scan 		= Display(web)

	web_portlist(1)
	if scan 	== 1:
		#QuickWebScan
		for port in portlist:
			command		= "nikto -host http://{}:{}".format(ip, port, ip, port)
			doit(command)
			command 	= "python3 {}/dirsearch/dirsearch.py -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -e php -f -t 20 -u http://{}:{} --simple-report dirsearchsimple_{}:{}".format(tfpath, ip, port, ip, port)
			doit(command)
			command		= "nmap -vv --reason -Pn -sV -p {} --script=`banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)` {}".format(port, ip)
			doit(command)
	elif scan 	== 2:
		#SquidsSqlMapTool
		command = "SquidsSqlMapTool"
		doit(command)
	elif scan 	== 3:
		#SquidsWfuzzTool
		command = "SquidsWfuzzTool"
		doit(command)
	elif scan 	== 4:
		#nikto
		port = web_portlist(2)
		command = "nikto -host http://{}:{}".format(ip, port, ip, port)
		doit(command)
	elif scan 	== 5:
		#dirsearch
		dirsearch()
	elif scan 	== 6:
		#nmap VulnScan
		port = web_portlist(2)
		command = "nmap -vv --reason -Pn -sV -p {} --script=`banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)` {}".format(port, ip)
		doit(command)
	elif scan 	== 7:
		#Squids ShellShock NSE
		for port in portlist:
			command = "nmap -vv --reason -Pn -sV -p {} --script={}/http-shellshock.nse {}".format(port, tfpath, ip)
			doit(command)
	return

def webapp():
	webapp_title	= "webapp"
	webapp_comment	= "Drupwn, joomlavs and joomblah are not currently in the build script"
	webapp_lst		= ["wpscan", "drupwn", "joomlavs", "joomblah"]
	webapp 			= Display_class(webapp_title, webapp_comment, webapp_lst)
	scan 			= Display(webapp)

	q1	= input("Where is the webapp located?\nExample Syntax	192.168.11.137:8000/wordpress\n> ")
	if scan 	== 1:
		#wpscan
		command = "wpscan --url http://{} --enumerate u,tt,t,vp --passwords /usr/share/wordlists/rockyou.txt -e ".format(q1)
	elif scan 	== 2:
		#probably busted
		command		= "drupwn enum http://{}".format(q1) 
	elif scan == 3:
		#probably busted
		command		= "ruby joomlavs.rb -u http://{} --scan-all | tee 'joomlahvs_{}'".format(q1)
	elif scan == 4:
		#probably busted
		command		= "python joomblah.py http://{} | tee 'joomblah_{}'".format(q1)
		return
	doit(command)

def smb():
	smb_title	= "smb"
	smb_comment= "#####"
	smb_lst	= ["Enum4Linux", "SmbVulnNmapScan", "SquidsSmbTool"]
	smb 		= Display_class(smb_title, smb_comment, smb_lst)
	scan 		= Display(smb)

	if scan 	== 1:
		#Enum4Linux
		command = "enum4linux -a {}".format(ip)
	elif scan 	== 2:
		#SmbVulnNmapScan
		command	= "nmap --script smb-vuln* -p 139,445 {}".format(ip)
	elif scan 	== 3:
		#SquidsSmbTool
		dn 		= input("What is the domain/workgroup? (example yeet.wtf)\n> ")
		command = "SquidsSmbTool {} {}".format(ip, dn)
	doit(command)

def ldap():
	ldap_title	= "ldap"
	ldap_comment= "#####"
	ldap_lst 	= ["Ldap nmap scan", "ldapsearch", "ldapsearch4base"]
	ldap 		= Display_class(ldap_title, ldap_comment, ldap_lst)
	scan 		= Display(ldap)

	if scan 	== 1:
		command = "nmap -p 389 --script ldap-search -Pn {}".format(ip)
	elif scan 	== 2:
		command = "ldapsearch -h {} -x".format(ip)
	elif scan 	==3:
		command = "ldapsearch -h {} -x -s base namingcontexts".format(ip)
	doit(command)

def ProtoBrute():
	ProtoBrute_title	= "ProtoBrute"
	ProtoBrute_comment= "#####"
	ProtoBrute_lst	= ["SquidsProtoBrute"]
	ProtoBrute 		= Display_class(ProtoBrute_title, ProtoBrute_comment, ProtoBrute_lst)
	scan 		= Display(ProtoBrute)

	if scan 	== 1:
		#SquidsProtoBrute
		command = "SquidsProtoBruteTool {}".format(ip)
	doit(command)

#Main Modules End
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
#WEB Extra Stuff BEGIN
def web_portlist(use):
	#Called to initially create the portlist (use = 1), then is called later to select a single port to scan (use = 2)
	if use == 1:
		global portlist
		try: 
			if len(portlist) > 0:
				pass
		except:
			portlist	= []
			while True:
				port 	= input("""
What is the port of the machine that we will be enumerating?
Example Syntax: 8000
> """)
				portlist.append(port)
				q1	= input("Would you like to add another port?\n> ")
				if q1.lower() in yes:
					continue
				else:
					break
	elif use == 2:
		while True:
			num = 1
			print("Which of these ports would you like to scan against?(left number please)")
			for i in portlist:
				print("{}. {}".format(num, i))
				num += 1
			port = int(input("> "))

			if port not in range(len(portlist)):
				print(len(portlist))
				continue
			else:
		 		port = port - 1
		 		port = portlist[port]
		 		break
		print(port)
		return port
	else:
		return

def dirsearch():
	#Just dirsearch, but too hefty to put in the main section
	q1	= input("Would you like this scan to be recursive?\n> ")
	print("What is the port of the machine that we will be enumerating?")
	number = 1
	for port in portlist:
		print("{}	{}:{}".format(number, ip, port))
		number += 1
	while True:
		try:	
			port	= int(input("> "))
			break
		except ValueError:
			print("Invalid input, try again... dirtbag")
			continue
	port -= 1
	port = portlist[port]
	
	if q1 in yes:
		command = "python3 {}/dirsearch/dirsearch.py -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -e php,exe,sh,py,html,pl -f -t 20 -u http://{}:{} -r -R 10 --simple-report dirsearchsimple_{}-{}".format(tfpath, ip, port, ip, port)
	else:
		command	= "python3 {}/dirsearch/dirsearch.py -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -e php -f -t 20 -u http://{}:{} --simple-report dirsearchsimple_{}-{}".format(tfpath, ip, port, ip, port)
	doit(command)
	return
#WEB STUFF END
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
#Tire Fire Fundamentals Begin
def start():
	#Everything that happens before main() is called. IP is set here (can also be set manually at bottom of script to eliminate start())
	print("Welcome to TireFire!")
	sq1	= input("Would you like to kick this off with a netdiscover?\n> ")
	sq1	= sq1.lower()
	if sq1 in yes: 
		nq1	= input("What is the class C subnet you would like to scan?\nExample Syntax: 192.168.11.0\n> ")
		command = "sudo netdiscover -r {}".format(nq1)
		doit(command)
	global ip
	ip 	= input("""
What is the IP of the machine that we will be enumerating?
Example Syntax:	192.168.11.137
> """)
	sq2	= input("Would you like to kick off a nmap scan?\n> ")
	if sq2 in yes:
		qwsq1		= os.popen("ping -c 1 {}".format(ip)).read()
		ttl			= qwsq1.split()[12]
		ttl_table= """
**Ping Hop Table**
Operating System 	TCP	UDP ICMP
Linux				64	64	255
OS/2				64	64	255
Solaris 2.x			255	255	255				
MS Windows 95-ME	32	32	255
MS WIndows 			128	128	255
Windows Other		128	128	255
"""
		print(ttl_table)
		command	= "echo -e \"\\e[5m\\e[31m\\e[1m{}\\e[0m\"; echo \"http://www.kellyodonnell.com/content/determining-os-type-ping\" ; nmap {} && nmap -sC -sV {} && nmap -p- {}".format(ttl, ip, ip, ip)
		doit(command)
		main()
	else:
		main()

def Display(foo):
	#used to create the list of options to choose from. Display() calls input_validation() to handle input properly.
	print(Fore.RED + foo.title)
	print(Fore.YELLOW + foo.comment + Fore.WHITE)
	for i in range(len(foo.lst)):
		print("{}. {}".format(i + 1, (foo.lst[i]).replace("()", "")))
	di1 = input_validation(foo) 
	if di1 == False:
		main()
	elif str(")") in foo.lst[di1-1]:
		eval((foo.lst[di1-1]))
	else:
		return di1

def input_validation(objec):
	#minimizes bad charachter errors in the main of the script.
	bad_input	= "Some decent input would be nice..."
	try:
		if len(objec.lst) <= 1:
			return 1
		else:
			foo = int(input("> "))
			if foo in range(len(objec.lst)+1):
				return foo
			else:
				print(bad_input)
				return
	except KeyboardInterrupt:
		print("Later Tater")
		quit()
	except:
		print(bad_input)
		return False

def doit(command):
	#called to execute command in new terminator tab
	os.system("terminator --new-tab -x 'echo \"{}\"; {}; $SHELL'".format(command, command))
	print(Fore.GREEN + "{}\n".format(command))
	print(Style.RESET_ALL)
	return

def main():
	#duh
	while True:
		try:
			Display(home)
		except:
			quit()

#ip = "1.1.1.1"
start()