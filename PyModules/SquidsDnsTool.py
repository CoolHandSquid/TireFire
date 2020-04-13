#!/usr/bin/python3
import os
import sys
from colorama import Fore, Style

try:
	ip = sys.argv[1]
except:
	ip = "1.1.1.1"
try:
	dn = sys.argv[2]
except:
	dn = "yeet.wtf"
network = ip
while True:
	if network[-1] != ".":
		network = network[:-1]
		continue
	else:
		network = network + "0/24"
		break
command1	= "dnsrecon -r 127.0.0.0/24 -n {}".format(ip)
command2 = "dnsrecon -r 127.0.1.0/24 -n {}".format(ip)
command3 = "dnsrecon -r {} -n {}".format(network, ip)
command4 = "dig axfr @{}".format(ip)
command5 = "dig axfr {} @{}".format(dn, ip)
print(Fore.GREEN + """Split the Term and Type these puppies in.
##############
nslookup
	SERVER {}
	127.0.0.1
	{}
	{}
	exit
##############""".format(ip, ip, dn))
#		input(Fore.GREEN + command )
#		print(Style.RESET_ALL)

input(Fore.GREEN + command1)
print(Style.RESET_ALL)
os.system(command1)
input(Fore.GREEN + command2)
print(Style.RESET_ALL)
os.system(command2)
input(Fore.GREEN + command3)
print(Style.RESET_ALL)
os.system(command3)
input(Fore.GREEN + command4)
print(Style.RESET_ALL)
os.system(command4)
input(Fore.GREEN + command5)
print(Style.RESET_ALL)
os.system(command5)

print("Useage examle: python3 SquidsStupidDnsTool.py 192.168.11.1 yeet.wtf")
quit()