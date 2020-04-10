#!/bin/bash


#path2pull="/root/Desktop/Machines/HTB/Jarvis/dirsearchsimple10.10.10.143:80"
#path2write="/root/Desktop/Machines/HTB/Jarvis/"
path2pull=$1
path2write=$2




cd $path2write
dir=$path2write"SquidsSqlFinder"
if test -r "$dir"; then
	echo ""
else
	mkdir SquidsSqlFinder
fi
cd SquidsSqlFinder
n=0
dirs="dirs.txt"
while true
do
	if test -r "$dirs"; then
		dirs="dirs.txt"
		n=$(($n + 1))
		dirs=$dirs$n
		continue
	else
		touch "$dirs"
		break
	fi
done
cp "$path2pull" "$dirs"
n=0
grep="grep.txt"
while true
do
	if test -r "$grep"; then
		grep="grep.txt"
		n=$(($n + 1))
		grep=$grep$n
		continue
	else
		touch "$grep"
		break
	fi
done
n=0
curl="curl.txt"
while true
do
	if test -r "$curl"; then
		curl="curl.txt"
		n=$(($n + 1))
		curl=$curl$n
		continue
	else
		touch "$curl"
		break
	fi
done
ls="$(ls $path2pull)"
for file in $ls
do
	cat $file | while read line
	do
		curl $line >> "$curl"
	done
done
echo "!!!!!!!!!sql potential stuff!!!!!!!!!!!!!!"
cat "$curl" |  grep --color=always -E '\.(.{3}|.{4})\?.*='  >> $grep
echo "!!!!!!!!!base 64 stuff!!!!!!!!!!!!!!!!!!!!!" >> $grep
cat "$curl"	|  grep --color=always -E '[[:alnum:]/+]{20,}'
echo "!!!!!!!!!comments stuff!!!!!!!!!!!!!!!!!!!!!" >> $grep
cat "$curl" |  grep --color=always -E '<!*>'
# grep --color=always -E '\.(.{3}|.{4})\?.*=' | awk -F '=' '{print $2}' | grep '?'