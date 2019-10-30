# Mininet - VXLAN
## Note, this is a Python 2.7 project
Please go through the following steps to start the virtualization:
1. Start the hosting systems for mininet.
2. Start the hosting systems for the ryu controller.
2. Change the files located in src:  
 1.1 Write down the IP addresses from all the mininet hosting systems.  
 1.2 Change the IPs located in ./src/hosts/peer_addresses.txt to all IPs from the hosting systems from mininet.  
 1.3 Change the IPs located in ./putFiles.txt to upload the scripts to the mininet hosting systems.    
 1.4 Change the IP in ./putFiles.txt to upload the scripts to the ryu controller system.
3. Run the ./upload_to_servers.bat file and allow all  
