#!/usr/bin/bash

x=3
y=2
echo " 

                                                                           ##    ## ######## ########   #######
                                                                           ###   ##    ##    ##     ## ##     ##
                                                                           ####  ##    ##    ##     ## ##     ##
                                                                           ## ## ##    ##    ########  ##     ##
                                                                           ##  ####    ##    ##   ##   ##     ##
                                                                           ##   ###    ##    ##    ##  ##     ##
                                                                           ##    ##    ##    ##     ##  ######
"
echo "ENTER AUTHORIZATION"
read auth;
sleep 1; echo "ENTER STATE"
read state;


if [ $state ==  "fucked" ]; then 
        sleep 3; echo "Abort order received from $auth: KILO LIMA 3 in effect"; sleep 2;
	echo "Operational Detachment compromised"; sleep 1;
        echo "HQ notified for exfil"; sleep 2;
        echo "Mission abort protocol initiated"; sleep 2;
        echo "Starting full scrub"; sleep 3;
        while [[ $x -ge 1 ]]
        do 
	        echo "SCRUB IN-PROCESS. Actions remaining before secure state achieved: $x"
	        ((x --))
         sleep $y;
        done


        echo "
        SECURE STATE ACHIEVED"; sleep 3;
else
sleep 3; echo "BEEP BOOP"; 

fi
