#!/usr/bin/python3
import os

def doit(command):
	os.system("terminator --new-tab -x 'echo \"{}\"; {}; $SHELL'".format(command, command))
	print("{}\n".format(command))
	return

while True:
	q1 = input("""
Would you like to WFUZZ?
1. The Input to a page?
2. A URL verb/noun
3. A URL
> """)
	try:
		q1 = int(q1)
		if q1 == 1 or q1 == 2 or q1 == 3:
			break
		else:
			continue
	except:
		print("That was not a valid input. Go Fuck Yourself and Try Again.")
		continue


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
	command = "wfuzz -L -c -z file,/usr/share/wfuzz/wordlist/Injections/SQL.txt -d \"{}\"  {}".format(q3, q2)
	doit(command)

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

elif q1	== 3:
	q2 = input("""
What is the location you would like to scan against?
Example syntax http://192.168.11.8/FUZZ/checklogin.php
> """)
	command = 'wfuzz  -w /usr/share/wordlists/dirb/common.txt --hc 404,500 -u {}'.format(q2)
	doit(command)