# README for netconf-script
## Hints
Note to [enable the candidate-datastore](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/169/b_169_programmability_cg/configuring_yang_datamodel.html) to work with this script:
```
enable
configure terminal
    netconf-yang
    netconf-yang feature candidate-datastore
    exit
```
To deploy a BGP neighborship it is relevant to connect to both netconf devices and configure the needed parts.  
If you like to deploy a 

## Usage
1. Start the script and configure your connection if needed
2. Select the needed function by typing a listed key - terminate with exit  
2.1. If needed select an additional key   
2.2. If needed type the right arguments into the console window  
3. Repeat if needed

## Idea
This script could be used to automate the configuration over multiple netconf compatible devices. 
The user input could be deployed over multiple sessions which points to multiple devices simultaneously.
