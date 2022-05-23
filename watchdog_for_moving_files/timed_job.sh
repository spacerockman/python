#!/bin/bash

echo "----------------------------------------------------------------------------"
echo "当前时间":$(date +"%Y-%m-%d %H:%M:%S") >> /home/XuJintao/Desktop/workspace/python/watchdog_for_moving_files/log/log.txt
python3 /home/XuJintao/Desktop/workspace/python/watchdog_for_moving_files/start.py
echo "----------------------------------------------------------------------------"