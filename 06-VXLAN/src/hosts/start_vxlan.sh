#!/bin/bash
cd /home/mininet/mininet/custom/vxlan
sudo mn -c
sudo python2 vxlan.py --vlans 2 --hosts 2 --controller 192.168.72.100