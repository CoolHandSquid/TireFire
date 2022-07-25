#!/usr/bin/env bash

#Verify running as root
if [[ "$(id -u)" -ne "0" ]]; then
	echo "You must be root to run this script."
	exit 1
fi

#Verify in TireFire directory
if [[ "$(pwd | awk -F "/" '{print tolower($NF)}')" != "tirefire" ]]; then
	echo "You must be in the TireFire directory to run this script."
	exit 1
fi

printf "\033[1;32mTireFire is installing\n\033[0m"

printf "\033[1;32mMaking TireFire Links\n\033[0m"
rm /usr/bin/TireFire 2> /dev/null
ln -s "$PWD/TireFire.py" "/usr/bin/TireFire"

printf "\033[1;32mApt Installing Neccessary Tools\n\033[0m"
apt -qqq update
sudo apt -qqq remove tilix 2>/dev/null | grep -v Unable
apt-get -qq install gobuster seclists dconf-cli g++ pip libreoffice smtp-user-enum leafpad enum4linux smbmap dbus-x11 -y
wait

printf "\033[1;32mPip Installing Neccessary Tools\n\033[0m"
python3 -m pip install -qq -r ./requirements.txt | egrep -v "Requirement already satisfied:"


printf "\033[1;32mInstalling dirsearch\n\033[0m"
if [[ ! -d 'dirsearch' ]]; then git clone https://github.com/maurosoria/dirsearch.git; fi
chmod -R 755 dirsearch/

printf "\033[1;32mInstalling impacket\n\033[0m"
if [[ ! -d 'impacket' ]]; then git clone https://github.com/SecureAuthCorp/impacket.git; fi
chmod -R 755 impacket/
cd impacket
python3 -m pip install -qq -r ./requirements.txt --quiet
python3 ./setup.py install > /dev/null 2>&1
cd ..

printf "\033[1;32mInstalling tilix\n\033[0m"
if test ! -f 'tilix.zip'
    then wget https://github.com/gnunn1/tilix/releases/download/1.9.3/tilix.zip
fi
unzip -oq tilix.zip -d /
glib-compile-schemas /usr/share/glib-2.0/schemas/
mkdir /etc/TireFire 2>/dev/null
cp "$PWD/Tire_Fire.jpg" "/etc/TireFire/Tire_Fire.jpg"
dconf load /com/gexperts/Tilix/ < tilix.dconf

printf "\033[1;32mChecking for rockyou.txt\n\033[0m"
if [ -f "/usr/share/wordlists/rockyou.txt.gz" ] || [ ! -f "/usr/share/wordlists/rockyou.txt" ]
then
	gzip -d /usr/share/wordlists/rockyou.txt.gz
fi

printf "\033[1;32m\nNotes\n\033[0m"
wordlists=("/usr/share/wordlists/rockyou.txt" "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt" "/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt" "/usr/share/seclists/Usernames/Names/names.txt")
for wordlist in "${wordlists[@]}"
do
    if [[ ! -f "$wordlist" ]]
    then
        echo "You are going to want to install $wordlist"
    fi
done
if test ! -f "`which msfconsole`";then echo "You are going to want to install metasploit if you want to use metasploit mode.";fi

echo "TireFire Installed Successfully."
