# TireFire
* Scalable Python tool for initial enumeration.
* TireFire is a simple enumeration platform to place your order of operations and workflow for enumeration. The database for TireFire (Main.csv) is easily altered to support your methodologies as they are maleated and appeneded.
* TireFire is a product of *19% security solutions.*
* ReReleased March 1 2021 with a CSV backend for straightforward command adding.
![alt text](https://github.com/CoolHandSquid/TireFire/blob/TireFire_V3/Images/Tire_fire.jpg)
## Friendly (GUI-ish) Interface
![alt text](https://github.com/CoolHandSquid/TireFire/blob/TireFire_V3/Images/2_kickoff.png)
![alt text](https://github.com/CoolHandSquid/TireFire/blob/TireFire_V3/Images/3_TireFire.png)
## Useage
* TireFire will not function well if not run as root.
* Once Build.sh has been run TireFire will have been added to your path. 
* Type "TireFire 10.10.10.5" and you will be yeeting with a cyber **cannon!**
* From "Main Table" click the corresponding number of a protocol you would like to run a scan for.
* From the "Protocol Table" click the corresponding number of a scan you would like to run. The scan will be kicked off in another tab.
* Hit enter to return to the "Main Table."
* You can change the variables by going to the "Variables Table."
* If you would like to go back to the "Main Table," just hit enter.
* If there is a scan or series of scans for a protocol you would like to add, edit Main.csv following the guidelines in this README (it's pretty straight forward).
* Tables and commands can be added while TireFire is running and it will be populated once Main.csv is saved.
## ProTips
- Ctrl+Z will bring you back to the main TireFire Page.
- Ctrl+PageUp/PageDown will allow you to peruse through open tabs.
## How to Build
- git clone https://github.com/CoolHandSquid/TireFire.git
- cd TireFire
- sudo /bin/bash ./Build.sh 
## Easily Add modules
- Open Main.csv with your favorite csv editor (I'm partial to ModernCSV).
- When adding a command, keep in mind Name, Port, and Description are for the primary display screen; Cmd_Name, Cmd_Description, Cmd_Command, Cmd_Comment, and SubDisplayOrder are for the secondary display screen.
## Special Characters and Syntax
- Cmd_Command has a few special characters including %, &&&&, #, and {}.
- % As the first Character will run the command on every port in Web_Portlist.
- &&&& Any where in the command will split the line and start each command individually in seperate tabs.
  - Example: whoami &&&& id &&&& ifconfig will open three tabs and run the desired command in each. This is useful if you initially run multiple seperate commands every time you see a specific port open. 
- % and &&&& can be used together to run multiple commands on all Ports in Web_Portlist.
- "#" is for sending yourself notes to another tab. This will only work if the first character of the first line is #. This is useful if you don't want to run a command but you want to give yourself copy-paste notes for manual enumeration.
- {} is for grabbing a variable from TireFire. Available variables are IP, Domain_Name, Naming_Context, Web_Portlist, Big_Passwordlist, Small_Passwordlist, Big_Userlist, Small_Userlist, Big_Dirlist, Small_Dirlist.
- Use " instead of ' due to the way that the string is being passed into TireFire.
![alt text](https://github.com/CoolHandSquid/TireFire/blob/TireFire_V3/Images/1_csv.png)
![alt text](https://github.com/CoolHandSquid/TireFire/blob/TireFire_V3/Images/CoolHandSquid.jpg)
## Contact
Please contact me at CoolHandSquid32@gmail.com for suggestions and ideas!













