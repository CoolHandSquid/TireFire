#!/usr/bin/env bash

#Verify running as root
if [[ "$(id -u)" -ne "0" ]]; then
	echo "You must be root to run this script."
	exit 1
fi

#Verify in TireFire directory
if [[ "$(pwd | awk -F"/" '{print$NF}')" != "TireFire" ]]; then
	echo "You must be in the TireFire directory to run this script (case sensitive)."
	exit 1
fi

cat <<'END'
TireFire is installing...
END

if [[ ! -d 'dirsearch' ]]; then git clone https://github.com/maurosoria/dirsearch.git; fi
chmod -R 755 dirsearch/

rm /usr/bin/TireFire 2> /dev/null
ln -s "$PWD/TireFire.py" "/usr/bin/TireFire"

apt update
apt-get install tilix dbus-x11 gobuster seclists dconf-cli g++ pip libreoffice smtp-user-enum leafpad -y
wait
python3 -m pip install pandasql

cp "$PWD/Tire_Fire.jpg" "/root/Pictures/Tire_Fire.jpg"
dconf load /com/gexperts/Tilix/ < tilix.dconf

if [ -f "/usr/share/wordlists/rockyou.txt.gz" ] || [ ! -f "/usr/share/wordlists/rockyou.txt" ]
then
	gzip -d /usr/share/wordlists/rockyou.txt.gz
fi

wordlists=("/usr/share/wordlists/rockyou.txt" "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt" "/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt" "/usr/share/seclists/Usernames/Names/names.txt")
for wordlist in "${wordlists[@]}"
do
    if [[ ! -f "$wordlist" ]]
    then
        echo "#"
        echo "#"
        echo "#"
        echo "You are going to want to install $wordlist"
        echo "#"
        echo "#"
        echo "#"
    fi
done
chown 0 -R ./*
chmod +x -R *
