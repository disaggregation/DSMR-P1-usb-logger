# P1 DSMR reader for the open source disaggregation project
Open Source project to log data from the DSMR (P1) meter via usb serial cable

## installation

To install the P1 USB reader run the following commands in your terminal:

```
sudo wget https://raw.githubusercontent.com/disaggregation/logger-DSMR-P1-usb/master/install.sh

chmod +x install.sh && sudo ./install.sh
```

The schedular will launch at reboot and record data every 10 seconds, which leads to about 1Mb per day. Make sure you have enough space..

## hardware requirements
- Raspberry Pi
- USB <> Serial cable (https://www.sossolutions.nl/slimme-meter-kabel)

## Data storage
The data will be stored to a sqlite file 'data/yourhash256edmeterserialnumber.db'
Mysql logging is support, but required more setup skills.

# Disaggregation
This repository will soon be updates with a working disaggregation model that determines which subload are behind your energy meter.
Pleas visit www.allianders.nl/disaggregation/demo/ to see the current disaggregate allogaritems results. An upload page for your data will be provided soon.

