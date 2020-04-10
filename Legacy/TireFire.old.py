#!/usr/bin/python3
import os
import sys
null	= """
written by coolhandsquid
TireFire is a product of 19% security solutions
"""
#ln -s /root/Desktop/Tools/TireFire/TireFire.py /usr/local/bin/
#ln -s /root/Desktop/Tools/TireFire/SquidsSqlFinder.sh /usr/local/bin/

yes		= [ "yes","y", "yee yee", "yee", "yeah", "yeet", "yeet cannon", "yea", "yeah", "ye"]
no 		= [ "no", "n", "nah", "fuckyou"]
scans	=	[ "yeet()", "netdiscover()", "nmap('nq1')", "TFwebenum()", "TFsmbenum()", "protobrute()"]

def start():
	print("Welcome to TireFire!")
#	mq0	= input("Would you like to make a directory for the machine you are enumaerating?\n> ")
#	if mq0 in yes:
#		mkdir()
	if len(sys.argv) != 1:
		if sys.argv[1] 		== "TFwebenum":
			TFwebenum()
		elif sys.argv[1] 	== "TFsmbenum":
			TFsmbenum()
	while True:
		mq1	= input("Would you like to kick this off with a netdiscover?\n> ")
		mq1	= mq1.lower()
		try:
			if mq1 in yes:
				netdiscover()
				break
			elif mq1 in no:
				break
			else:
				print("Strong Start... Lets try that again.\n")
				continue
		except KeyboardInterrupt:
			print("Hasta_Lavista... Turd")
			quit()

	global ip
	ip 	= input("""
What is the IP of the machine that we will be enumerating?
Example Syntax:	192.168.11.137
> """)
	mq2	= input("Would you like to kick off a nmap scan?\n> ")
	if mq2 in yes:
		nmap(0) 
	while True:
		try:
			mq3	= input("""
Based on the result of your scans, what would you like to do?
1. netdiscover
2. nmap
3. WebEnum
4. SmbEnum
5. ProtoBrute
> """)
			try:
				mq3	= int(mq3)
				if mq3 not in range(len(scans) + 1):
					print("I would like some valid input please.\n")
					continue
			except ValueError:
				print("I would like some valid input please.\n")
				continue
			eval(scans[mq3])
		except KeyboardInterrupt:
			print("\nLater tater")
			quit()

def mkdir():
	mq1	= input("What is the dir name of the dir you would like to create for these scans?\nExample Syntax: /root/Desktop/Machines/VulnHub/Yeet\n> ")
	command = "mkdir {}; cd {}; cd ..; ls".format(mq1, mq1)
	doit(command)

def netdiscover():
	nq1	= input("What is the class C subnet you would like to scan?\nExample Syntax: 192.168.11.0\n> ")
	command = "netdiscover -r {}".format(nq1)
	doit(command)

def nmap(nq1):
	try:
		nq1 = int(nq1)
	except ValueError:
		while True:
			nq1 = input("""
Which nmap scan would you like to run?
Quick scan 			0
Version scan 			1
All-Ports scan 			2
Scan for smb vulnerabilities	3
Scan for all vulnerabilities	4
SquidsSmartScan			5
> """)
			try:
				nq1 = int(nq1)
				break
			except ValueError:
				continue
	if nq1 == 0:
		qwsq1		= os.popen("ping -c 1 {}".format(ip)).read()
		ttl			= qwsq1.split()[12]
		print("""
Operating System 	TCP	UDP ICMP
Linux				64	64	255
OS/2				64	64	255
Solaris 2.x			255	255	255				
MS Windows 95-ME	32	32	255
MS WIndows 			128	128	255
Windows Other		128	128	255
""")
		command	= "echo -e \"\\e[5m\\e[31m\\e[1m{}\\e[0m\"; echo \"http://www.kellyodonnell.com/content/determining-os-type-ping\"; nmap {}".format(ttl, ip)
	elif nq1 == 1:
		command = "nmap -sC -sV {}".format(ip)
	elif nq1 == 2:
		command = "nmap -p- {}".format(ip)
	elif nq1 == 3:
		command = "nmap --script smb-vuln* -p 139,445 {}".format(ip)
	elif nq1 == 4:
		command = "nmap -v -sV -p- --script vuln -T4 {}".format(ip)
	elif nq1 == 5:
		command = "nmap {} && nmap -sC -sV {} && nmap -p- {}".format(ip, ip, ip)
	else:
		return
	doit(command)

###########################################################################################################################################
#ProtoBrute
###########################################################################################################################################	
def protobrute():
	while True:
		sbq1	= input("""
Would you like to use a...
1.	username?
2.	username list?
3.	default username list?		
> """)
		try:
			sbq1 = int(sbq1)
			break
		except ValueError:
			print("Valid input would be nice.")
			continue
	if sbq1 	== 1:
		ua 			= "l"
		username	= input("What is the username you want to brute force?\n> ")
	elif sbq1 	== 2:
		ua 			= "L"
		username 	= input("What is the full path to the custom username list you would like to use?\n> ")
	else:
		ua 			= "L"
		username 	= "/Yeet/Tools/Wordlists/names.txt"
	while True:
		sbq2 	= input("""
Would you like to use a...
1. password?
2. password list?
3. default password list?
> """)
		try:
			sbq2 = int(sbq2)
			break
		except ValueError:
			print("Valid input would be nice.")
			continue
	if sbq2 	== 1:
		pa 			= "p"
		password 	= input("What is the password you want to use?\n> ")
	elif sbq2 	== 2:
		pa 			= "P"
		password 	= input("What is the full path to the custom password list you would like to use?\n> ")
	else:
		pa 			= "P"
		password 	= "/Yeet/Tools/Wordlists/rockyou.txt"
	sbq3	= input("""
What is the protocol you would like to brute force?
Example Syntax: ssh
> """)
#	while True:
#		sbq4	= input("What is the port number you would like to brute force?\n> ")
#		try:
#			sbq4	= int(sbq4)
#			break
#		except ValueError:
#			print("Valid input would be nice.")
#			continue
#	command = "hydra -e nsr -{} {} -{} {} -t 6 {}://{} -s {}".format(ua, username, pa, password, sbq3, ip, sbq4)
	sbq4	= input("Are you trying to run hydra on a http-post-form?\n> ")
	if sbq4 in yes:
		dn 		= input("""
What is the ip or domain name of the page you are trying to hit?
Example Syntax internal-01.bart.htb (no http://)
> """)
		url		= input("""
What is the url after the domain name or IP of the page you are trying to hit?
Example Syntax /simple_chat/login.php (find in burp)
> """)
		chain	= input("""
What is the login chain? 
Example Syntax 	uname=^USER^&passwd=^PASS^&submit=Login  (be sure to change out ^USER^ and ^PASS^ so hydra knows what to fuzz)
> """)
		em	= input("""
What is a word or phrase in the error message?
Example Syntax 	Invalid Username or Password	(This is important becasue hydra will assume that the try is good if this phrase is not in the responce)
> """)
		command	= "hydra -{} {} -{} {} {} http-post-form '{}:{}:{}'".format(ua, username, pa, password, dn, url, chain, em)
		#hydra -l harvey -P /Yeet/Tools/Wordlists/rockyou.txt internal-01.bart.htb http-post-form "/simple_chat/login.php:uname=^USER^&passwd=^PASS^&submit=Login:Password"
	else:
		command = "hydra -e nsr -{} {} -{} {} -t 6 {}://{}".format(ua, username, pa, password, sbq3, ip)
	input(command)
	doit(command)
	return
###########################################################################################################################################
#smbenum
###########################################################################################################################################
def TFsmbenum():
	while True:
		try:
			seq1	= input("""
What scans would you like to conduct?
Yeet			=	0
enum4linux		=	1
smbmap			=	2
smbclient		=	3
rpcclient		=	4 
SMB VulnScan		=	5
> """)
			try:
				seq1 = int(seq1)
			except:
				return
			scans	=	[ "yeet()", "enum4linux()", "smbmap()", "smbclient()", "rpcclient()", "vulnscan()"]
			if seq1 > len(scans) - 1:
				continue
			eval(scans[seq1])	
		except KeyboardInterrupt:
			print("\nLater tater")
			quit()

def yeet():
	ip 		= input("Gimmie an ip.\n> ")
	command = "string {}".format(ip)
	doit(command)
	return

def enum4linux():
	command = "enum4linux -a {} | tee e4lresults.txt".format(ip) 
	doit(command)

def smbmap():
	port 	= input("What port would you like to run smbmap against?\n> ")
	input("Take off the '-p yeet' in order to not attempt a null password")
	command	= "smbmap -H {} -P {} -R -p yeet".format(ip, port)
	doit(command)

def smbclient():
	share 	= input("What is the share in which you would like to connect?\nExample Syntax: \\\\192.168.11.140\\share$\n> ")
	command = "smbclient '{}'".format(share)
	doit(command)

def rpcclient():
	command	= "rpcclient {}".format(ip)
	doit(command)

def vulnscan():
	command	= "nmap -p 139,445 -vv --script=smb-vuln-cve2009-3103.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-ms17-010.nse {}".format(ip)
	doit(command)
###########################################################################################################################################
#webenum
###########################################################################################################################################
def CallTFwebenum():
	os.system("terminator --new-tab -x 'TireFire.py TFwebenum'")
	return

def TFwebenum():
	print("Welcome to TireFire WebEnum!")
	global portlist	
	portlist	= []
	while True:
		port 	= input("""
What is the port of the machine that we will be enumerating?
Example Syntax: 8000
> """)
		portlist.append(port)
		tfweq1	= input("Would you like to add another port?\n> ")
		if tfweq1.lower() in yes:
			continue
		else:
			break
	while True:
		try:
			tfweq1	= input("""
What scans would you like to conduct?
QuickWebScan 		=	0
WebappScan		=	1
SqlMap			=	2
BruteForce		=	3
SquidsSqlFinder		=	4 
Nikto			=	5
Dirsearch 		=	6
NmapWebScan		=	7
> """)	
			try:
				tfweq1 = int(tfweq1)
			except ValueError:
				return
			scans	=	[ "quickwebscan()", "webappscan()", "sqlmap()", "wfuzz()", "squidssqlfinder()", "nikto()", "dirsearch()", "nmapwebscan()"]
			if tfweq1 > len(scans) - 1:
				continue
			eval(scans[tfweq1])
		except KeyboardInterrupt:
			print("\nLater tater")
			quit()

def quickwebscan():
	for port in portlist:
		
		command		= "nikto -host http://{}:{} | tee 'nikto_{}:{}'".format(ip, port, ip, port)
		doit(command)
		command 	= "python3 /Yeet/Tools/dirsearch/dirsearch.py -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -e php -f -t 20 -u http://{}:{} --simple-report dirsearchsimple_{}:{}".format(ip, port, ip, port)
		doit(command)
		command		= "nmap -vv --reason -Pn -sV -p {} --script=`banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)` {}".format(port, ip)
		doit(command)
	return

def webappscan():
	webapp	= input("""
Now what advanced webapp scan would you like to run?
WPscan			= 	1
Drupwn			=	2
Joomlavs		=	3
Joomblah		=	4
> """)
	ipp	= input("Where is the webapp located?\nExample Syntax	192.168.11.137:8000/wordpress\n> ")
	if webapp == "1":
		command = "wpscan --url http://{} --enumerate u,ap,tt,t,vp --passwords /Yeet/Tools/Wordlists/rockyou.txt -e | tee 'wpscan_{}'".format(ipp, ipp)
	elif webapp == "2":
		command		= "drupwn enum http://{} | tee 'drupwn_{}'".format(ipp, ipp) 
	elif webapp == "3":
		command		= "ruby joomlavs.rb -u http://{} --scan-all | tee 'joomlahvs_{}'".format(ipp, ipp)
	elif webapp == "4":
		command		= "python joomblah.py http://{} | tee 'joomblah_{}'".format(ipp, ipp)
	webapplist = ("1", "2", "3", "4")
	if webapp not in webapplist:
		return
	doit(command)
	return

def sqlmap():
	sq1	= input("What is the location you would like to scan against?\nExample Syntax	192.168.11.137:8000/?nid=2\n> ")
	while True:
		sq2	= input("""
What are you trying to do?
Step 1. Quick General Enumeration	=	1
Step 2.	Try to get a sql SHELL 		=	2 <you need a database name for this to work which you may get from step 1>
Step 3. Try to dump tables		=	3
Step 4. Try to dump users		=	4
Step 5.	Use burp to Brute Force		=	5
> """)
		try:
			sq2 = int(sq2)
			break
		except TypeError:
			print("That was not a valid input. Go Fuck Yourself and Try Again.")
			return
		except ValueError:
			return
	if sq2	== 1:
		command		= 'sqlmap -u "{}" --risk=3 --level=5 --dbs --dump'.format(sq1)
	elif sq2	== 2:
		sq3	=	input("What is the name of the database you would like to make a shell from?\n> ")
		command = 'sqlmap -u “{}” --risk=3 --level=5 --os-shell -D {}'.format(sq1, sq3)
	elif sq2	== 3:
		command = 'sqlmap -u "{}" --risk=3 --level=5 --threads=4 --dbs --tables --batch'.format(sq1)
	elif sq2	== 4:
		command = 'sqlmap -u "{}" --risk=3 --level=5 --threads=4 --dbs  --batch -T users --dump'.format(sq1)
	elif sq2	== 5:
		sq4	= input("""
This one has a few extra steps, but it's pretty neat.
catch a POST to login page (or whatever) with burp
Send that to repeater, and copy the text out (by highlighting it)
put that text into a .txt file named post.txt
Make sure to note what the sql-injectable element is

What is the sql-injectable element? (uname, pword, username, etc...)\n> """)
		while True:
			sq5	= input("What is the full path to the post.txt file? (/root/Desktop/Machines/yee/post.txt)\n> ")
			if os.path.isfile(sq5) == True:
				break
			else:
				print("I can't seem to find that file...Try again.")
				continue
		command = 'sqlmap -r {} -p {}'.format(sq5, sq4)
	else:
		return
	doit(command)
	return

def wfuzz():
	wq0 = input("""
Would you like to WFUZZ?
The Input to a page?	1
A URL 			2
> """)
	try:
		wq0 = int(wq0)
	except TypeError:
		print("That was not a valid input. Go Fuck Yourself and Try Again.")
		return
	except ValueError:
		return
	if wq0 == 1:
		wq1 = input("""
What is the location you would like to scan against?
Example syntax http://192.168.11.8/checklogin.php
> """)
		wq2 = input("""
What is the post request look like (catch in burp)?
NOTE: the FUZZ is important
Example syntax myusername=john&mypassword=FUZZ&Submit=Login
> """)
		input("If you do not want to follow the redirect, rerun and take out the -L.\n")
		command = "wfuzz -L -c -z file,/usr/share/wfuzz/wordlist/Injections/SQL.txt -d \"{}\"  {}".format(wq2, wq1)
		doit(command)
		return
	elif wq0 == 2:
		wq1	= input("""
What is the location you would like to scan against?
NOTE: the FUZZ and FUZ2Z is important!
Example syntax http://192.168.11.130/thankyou.php?FUZZ=FUZ2Z
> """)
		while True:
			wq2	= input("""
Would you like to wfuzz a verb (v), a thing (t), or both (b)?
example http://192.168.11.130/yee.php?verb=thing
> """) 
			if wq2 not in ["v", "t", "b"]:
				print("I am looking for a v, t, or b.")
				continue
			else:
				break
		if wq2 == "v":
			command = 'wfuzz -c -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -u {}'.format(wq1)
		elif wq2 == "t":
			command = 'wfuzz -c -w /usr/share/seclists/Fuzzing/LFI/LFI-LFISuite-pathtotest.txt -u {}'.format(wq1)
		elif wq2 == "b":
			command 	= 'wfuzz -c -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -w /usr/share/seclists/Fuzzing/LFI/LFI-LFISuite-pathtotest.txt -u {}'.format(wq1)
		doit(command)
		return

def squidssqlfinder():
	while True:
		ssfq1		= input("""
Where is the dirsearchsimple output you would like me to parse?
example: /root/Desktop/Machines/HTB/Jarvis/dirsearchsimple10.10.10.143:80
> """)
		if os.path.isfile(ssfq1) == True:
			print("File found!")
			break
		else:
			print("I can't seem to find that file...Try again.")
			continue
	path 		= ssfq1
	while True:
		if path[-1] != "/":
			path = path[:-1]
			continue
		else:
			break
	command 	= "bash SquidsSqlFinder.sh {} {}".format(ssfq1, path)
	doit(command)
	return

def nikto():
	print("What is the port of the machine that we will be enumerating?")
	number = 1
	for port in portlist:
		print("{}	{}:{}".format(number, ip, port))
		number += 1
	while True:
		try:
			port	= int(input("> "))
		except ValueError:
			print("Invalid input, you are being sent back to the WebEnum main page.")
			return
	port 	-= 1
	port	= portlist[port]
	command 	= "nikto -host http://{}:{} | tee 'nikto_{}-{}'".format(ip, port, ip, port)
	doit(command)
	return

def dirsearch():
	wdsq1	= input("Would you like this scan to be recursive?\n> ")
	rec = 0
	if wdsq1 in yes:
		rec = 1
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
			print("Invalid input, you are being sent back to the WebEnum main page.")	
			return
	port -= 1
	port = portlist[port]
	if rec == 0:
		command		= "python3 /Yeet/Tools/dirsearch/dirsearch.py -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -e php -f -t 20 -u http://{}:{} --simple-report dirsearchsimple_{}-{}".format(ip, port, ip, port)
	elif rec == 1:
		command		= "python3 /Yeet/Tools/dirsearch/dirsearch.py -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -e php,exe,sh,py,html,pl -f -t 20 -u http://{}:{} -r -R 10 --simple-report dirsearchsimple_{}-{}".format(ip, port, ip, port)
	doit(command)
	return
def nmapwebscan():
	for port in portlist:
		command		= "nmap -vv --reason -Pn -sV -p {} --script=`banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)` {}".format(port, ip)		
		doit(command)


###########################################################################################################################################
#doit
###########################################################################################################################################


def doit(command):
	if "fuck" in command:
		return
	os.system("terminator --new-tab -x 'echo \"{}\"; {}; $SHELL'".format(command, command))
	print("{}\n".format(command))

start()
