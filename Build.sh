#!/usr/bin/env bash
: <<'END'
TireFire is installing...
END

if [ 1 -d dirsearch ]; then git clone https://github.com/maurosoria/dirsearch.git; fi
chmod -R 755 dirsearch/

rm /usr/bin/TireFire 2> /dev/null
ln -s "$PWD/TireFire.py" "/usr/bin/TireFire"

apt update
apt-get install tilix gobuster seclists dconf-cli g++ pandasql -y

cp "$PWD/Tire_Fire.jpg" "/root/Pictures/Tire_Fire.jpg"
dconf load /com/gexperts/Tilix/ < tilix.dconf

wordlists=("/usr/share/wordlists/rockyou.txt" "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt" "/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt" "/usr/share/seclists/Usernames/Names/names.txt")
for wordlist in "${wordlists[@]}"
do
    if test ! -f "$wordlists"
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
chmod +x -R *
