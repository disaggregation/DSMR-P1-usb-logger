# P1 DSMR reader for the open source disaggregation project
Open Source project to log data from the DSMR (P1) meter via usb serial cable

## Installation
To install the P1 USB reader run the following commands in your terminal:

```
sudo wget https://raw.githubusercontent.com/disaggregation/logger-DSMR-P1-usb/master/install.sh

sudo chmod +x install.sh && sudo ./install.sh
```

After the installer is finisched, the schedular will launch directly and at every reboot!
The P1 data is recorded every 10 seconds, which leads to about aprox. 1MB per day. Make sure you have enough space!

## Hardware requirements
- Raspberry Pi
- USB <> Serial cable (https://www.sossolutions.nl/slimme-meter-kabel)

## Data storage
A SQlite database file (.db) wil be created to store the P1 data, the filename is a MD5 hash name.
(Mysql logging is support, but required more setup skills.)

# Disaggregation
This repository will soon be updates with a working disaggregation model that determines which subload are behind your energy meter.
Pleas visit www.allianders.nl/disaggregation/demo/ to see the current disaggregate allogaritems results. An upload page for your data will be provided soon.

