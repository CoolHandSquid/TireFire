# TireFire ![alt text](https://github.com/CoolHandSquid/TireFire/blob/TireFire_V3/Images/Tire_fire_25.jpg)
# TireFire
*	TireFire is a scalable and straightforward platform for external enumeration to place your operations and workflow order. 
*	Great for HTB and OSCP like machines.
*	The database for TireFire (Main.csv) is easily altered to support your methodologies as they are substituted and appended.
*	TireFire is a product of 19% security solutions. 
## Summary
  - [Interface](#interface)
  - [Usage](#usage)
  - [Demo](#demo)
  - [ProTips](#protips)
  - [Build](#build)
  - [Adding Modules](#adding-modules)
  - [Contact](#contact)
## Interface
![alt text](https://github.com/CoolHandSquid/TireFire/blob/TireFire_V3/Images/3_TireFire.png)
## Usage
*	TireFire will not function well if not run as root.
*	Once Build.sh has been run, TireFire will have been added to your path.
*	Type "TireFire 10.10.10.5" and you will be yeeting with a cyber **cannon!**
*	From the "Main Table," type the corresponding number of a protocol for which you would like to run a scan.
*	From the "Protocol Table," click the corresponding number of a scan you would like to run. The scan will be kicked off in another tab.
*	Hit enter to return to the "Main Table."
*	You can change the variables by going to the "Variables Table."
*	If there is a scan or series of scans for a protocol, you would like to add, edit Main.csv following the guidelines in this README (it's pretty straight forward).
*	Tables and commands can be added while TireFire is running, and it will be populated once Main.csv is saved.
## Demo
![Tire Fire](https://github.com/CoolHandSquid/TireFire/blob/TireFire_V3/Images/TireFireFinal1.gif)
## ProTips
- Run multiple commands from a table at once by splitting the command numbers with commas. EX: 0,1,2 (Spaces and periods work aswell)
![alt text](https://github.com/CoolHandSquid/TireFire/blob/TireFire_V3/Images/4_split.png)
- Ctrl+Z will bring you back to the main TireFire Page.
- Ctrl+PageUp/PageDown will allow you to peruse through open tabs.
- Ctrl+S will split the screen.
- Ctrl+T for a new tab.
- Ctrl+h for help.
## Build
- git clone https://github.com/CoolHandSquid/TireFire.git
- cd TireFire
- ./Build.sh
## Adding Modules
- Open Main.csv with your favorite csv editor (I'm partial to ModernCSV).
- When adding a command, keep in mind Name, Port, and Description are for the primary display screen; Cmd_Name, Cmd_Description, Cmd_Command, Cmd_Comment, and SubDisplayOrder are for the secondary display screen.
![alt text](https://github.com/CoolHandSquid/TireFire/blob/TireFire_V3/Images/2_csv.png)
### Special Characters and Syntax
-	Cmd_Command has a few special characters including &&&&, #, ##, ?, and {}.
### &&&&
-	&&&& Anywhere in the command will split the line and start each command individually in separate tabs.
  -	Example: whoami &&&& id &&&& ifconfig will open three tabs and run the desired command in each. &&&& is useful if you initially run multiple separate commands every time you see a specific port open.
### \# and \#\#
-	"#" is for sending yourself notes to another tab.  
- "#" can be useful if you don't want to run a command, but you want to give yourself copy-paste notes for manual enumeration.
- Set only the first character of the line to # if you want variables to be evaluated.
- Set the first two characters of the line to ## if you do not want variables to be evaluated.
### ?
- "?" is for sending a question to the user. The responce will be set to a numbered variable.
- You can send multiple lines of questions for multiple variables.
- Example:
```
?What is the location of the wp-login.php? Example: /Yeet/cannon/wp-login.php
?What is a known password you would like to brute force?
wpscan --url {Web_Proto}://{IP}{1} --enumerate u,tt,t,vp --password {2} -e 
```
### {}
-	{} is for grabbing a variable from TireFire.
- Available variables can be viewed in the variables table.  

![alt text](https://github.com/CoolHandSquid/TireFire/blob/TireFire_V3/Images/CoolHandSquid.jpg)
## Contact
Please contact me at CoolHandSquid32@gmail.com for contribution, suggestions, and ideas!













