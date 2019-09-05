#!/bin/bash
while true; do
    python temp.py # define python file 
    # curl command for the send data on the data.txt file.
    # First define a influxdb api address with 8086/tcp port( "http://xxx.xxx.xxx.xxx:8086/ ) 
    # and add databse name  ( /write?db=DATABASE-NAME")
    curl -i -XPOST "http://xxx.xxx.xxx.xxx:8086/write?db=db_name" --data-binary @data.txt
    #loop time 
    sleep 5s
done



