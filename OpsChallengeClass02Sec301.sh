#! /bin/bash

NOW=`date '+%F_%H:%M:%S'`;

filename="/var/log/syslog/$NOW.jpg"

raspistill -n -v -t 500 -o $NOW.jpg;

echo $filename;