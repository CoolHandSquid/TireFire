#!/usr/bin/env bash
: <<'END'
TireFire is installing...
END

git clone https://github.com/maurosoria/dirsearch.git
chmod -R 755 dirsearch/

rm /usr/bin/TireFire 2> /dev/null
ln -s "$PWD/TireFire.py" "/usr/bin/TireFire"

apt-get install tilix gobuster seclists -y

wordlists=("/usr/share/wordlists/rockyou.txt" "/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt" "/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt" "/usr/share/seclists/Usernames/Names/names.txt")
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
