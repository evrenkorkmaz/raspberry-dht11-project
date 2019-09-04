#!/bin/bash
while true; do
    python3 tempmail.py
    curl -i -XPOST "http://35.198.129.164:8086/write?db=finally" --data-binary @data.txt
    sleep 5s
done



