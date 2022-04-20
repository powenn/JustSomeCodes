#!/bin/bash

IDEVICE_ID_EXEC="idevice_id"
IDEVICE_NAME="idevicename"

UDID=$($IDEVICE_ID_EXEC -l)

get_udid_and_name() {

    if [ "$UDID" == "" ] ;then 
        echo "NO iOS Device connected"
    else
        for udid in $UDID 
        do 
            DEVICENAME=$($IDEVICE_NAME -u "$udid")
            for devicename in "$DEVICENAME"
            do
                printf "iOS Device Name: $devicename\nUDID: $udid\n"
            done
        done
    fi

} 
   
    # info += f"iOS Device Name: {devicename}\nUDID: {udid}\n"

get_udid_and_name