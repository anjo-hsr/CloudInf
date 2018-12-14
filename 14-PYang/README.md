#README for netconf-script
Note to [enable the candidate-datastore](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/169/b_169_programmability_cg/configuring_yang_datamodel.html) to work with this script:
```
enable
configure terminal
    netconf-yang
    netconf-yang feature candidate-datastore
    exit
```

## Usage
1. Start the script and configure your connection if needed
2. Select the needed function by typing a listed key - terminate with exit  
2.1. If needed select an additional key   
2.2. If needed type the right arguments into the console window  
3. Repeat if needed