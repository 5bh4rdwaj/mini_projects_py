#!/usr/bin/bash
c=0
for x in hackthebox.com protonmail.com wttr.in youtube.com crypt.ee;
do
	if ping  -c 3    -W 1 $x > /dev/null; then
		echo "$x is active"
		((c ++))
	else
		echo "CAUTION: $x is inactive"
	fi 
done

if [ $c == 5 ] ; then 
    echo "All hosts are active, you may proceed"
else
    echo "Not all hosts are currently active"
fi
