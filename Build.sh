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

cat <<'END'
TireFire is installing...
END

#Make TireFire links
rm /usr/bin/TireFire 2> /dev/null
ln -s "$PWD/TireFire.py" "/usr/bin/TireFire"

apt update
apt remove tilix
apt-get install gobuster seclists dconf-cli g++ pip libreoffice smtp-user-enum leafpad enum4linux smbmap dbus-x11 -y
wait
python3 -m pip install -r ./requirements.txt | egrep -v "Requirement already satisfied:"

wget https://github.com/gnunn1/tilix/releases/download/1.9.3/tilix.zip
unzip tilix.zip -d /
glib-compile-schemas /usr/share/glib-2.0/schemas/

if [[ ! -d 'dirsearch' ]]; then git clone https://github.com/maurosoria/dirsearch.git; fi
chmod -R 755 dirsearch/
if [[ ! -d 'impacket' ]]; then git clone https://github.com/SecureAuthCorp/impacket.git; fi
chmod -R 755 impacket/
cd impacket
python3 -m pip install -r ./requirements.txt --quiet
python3 ./setup.py install > /dev/null 2>&1
cd ..

mkdir /etc/TireFire 2>/dev/null
cp "$PWD/Tire_Fire.jpg" "/etc/TireFire/Tire_Fire.jpg"
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

echo "TireFire Installed Successfully."
