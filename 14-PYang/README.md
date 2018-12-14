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
1. Start the script and configure your connection
2. Select the needed function - terminate with exit
4. Provide the needed variables
5. Repeat if needed