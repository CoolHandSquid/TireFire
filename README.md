# TireFire
* Scalable Python tool for initial enumeration.
* TireFire is a simple enumeration platform to place your order of operations for enumeration and is easily altered to support your methodologies as they are maleated and appeneded.
* TireFire is a product of *19% security solutions.*
* ReReleased March 1 2021 with a CSV backend for straightforward command adding.
![alt text](https://github.com/CoolHandSquid/TireFire/blob/master/Images/Tire_fire.jpg)
## Easily add modules
- Open Main.csv with your favorite csv editor (I'm partial to ModernCSV).
- When adding a command, keep in mind Name, Port, and Description are for the primary display screen; Cmd_Name, Cmd_Description, Cmd_Command, Cmd_Comment, and SubDisplayOrder are for the secondary display screen.
## Special Charachters and Syntax
- Cmd_Command has a few special charachters including %, &&&&, #, and {}.
- % As the first Charachter will run the command on every port in Web_Portlist.
- &&&& Any where in the command will split the line and start each command individually in seperate tabs.
  - Example: whoami &&&& id &&&& ifconfig will open three tabs and run the desired command in each. This is useful if you initially run multiple seperate commands every time you see a specific port open. 
- % and &&&& can be used together to run multiple commands on all Ports in Web_Portlist.
- "#" is for sending yourself notes to another tab. This will only work if the first charachter of the first line is #. This is useful if you don't want to run a command but you want to give yourself copy-paste notes for manual enumeration.
- {} is for grabbing a variable from TireFire. Available variables are IP, Domain_Name, Naming_Context, Web_Portlist, Big_Passwordlist, Small_Passwordlist, Big_Userlist, Small_Userlist, Big_Dirlist, Small_Dirlist.
- Use " instead of ' due to the way that the string is being passed into TireFire.
![alt text](https://github.com/CoolHandSquid/TireFire/blob/master/Images/1_csv.png)
## Friendly Interface
![alt text](https://github.com/CoolHandSquid/TireFire/blob/master/Images/2_kickoff.png)
![alt text](https://github.com/CoolHandSquid/TireFire/blob/master/Images/3_TireFire.png)
## How to build
- git clone https://github.com/CoolHandSquid/TireFire.git
- cd TireFire
- sudo /bin/bash ./Build.sh 
## Useage
* TireFire will not function well if not run as root.
* Once Build.sh has been run TireFire will have been added to your path. 
* Type "TireFire 10.10.10.5" and you will be yeeting with a cyber **cannon!**
## ProTips
- Ctrl+Z will bring you back to the main TireFire Page
- Ctrl+PageUp/PageDown will allow you to peruse through open tabs
![alt text](https://github.com/CoolHandSquid/TireFire/blob/master/Images/CoolHandSquid.jpg)
## Contact
Please contact me at CoolHandSquid32@gmail.com for suggestions and ideas!













