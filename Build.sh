#!/usr/bin/bash
: <<'END'
tools to be verified
	drupwn
	joomlavs
	joomblah
END

#give full permissions to all tools in the TireFire directory and subdirectories
chmod 755 -R $PWD/*

#tools that end in .py
PyModulelist=("SquidsDnsTool" "SquidsSmbTool" "SquidsProtoBruteTool" "SquidsSqlMapTool" "SquidsWfuzzTool") 
#combination of the tool list and TireFire.py
tfcombilist+=( "${PyModulelist[@]}" "TireFire")

#Remove any logical links to tools in the TireFire toollist and wordlist
for tool in "${tfcombilist[@]}"
do
	if [ "/usr/bin/$tool" ]
	then
		rm "/usr/bin/$tool"
	fi
done

#Add a logical link for each .py tool in the TireFire/PyModules directory to /usr/bin 
for tool in "${PyModulelist[@]}"
do
	ln -s "$PWD/PyModules/$tool.py" "/usr/bin/$tool"
done

#Add a logical link for TireFire to /usr/bin 
ln -s "$PWD/TireFire.py" "/usr/bin/TireFire"

#Add tools to the sudoers list
sudoersadd=("netdiscover")
tail=$(tail /etc/sudoers)
for tool in "${sudoersadd[@]}"
do
	command="ALL ALL=NOPASSWD: /usr/sbin/$tool"
	if [[ $tail != *"$command"* ]];
	then
		echo "ALL ALL=NOPASSWD: /usr/sbin/$tool" >> /etc/sudoers
	fi
done

#git clone dirsearch
if test ! -f "./dirsearch/dirsearch.py"
then
	git clone https://github.com/maurosoria/dirsearch.git
	chmod -R 777 dirsearch/
fi

#Install terminator
apt-get install terminator -y

#Verify wordlists
wordlists=("/usr/share/wordlists/rockyou.txt" "/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt" "/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt" "/usr/share/seclists/Usernames/Names/names.txt")
for wordlist in "${wordlists[@]}"
do
	if test ! -f "$wordlist"
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


