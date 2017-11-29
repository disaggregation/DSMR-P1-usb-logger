#!/bin/bash

# Installation script for: disaggregation_logger-DSMR-P1-usb
# OS/HW: Raspbian / Raspberry Pi
# Path: /home/pi/disaggregation

# Get Started:
# Download with: sudo wget https://github.com/disaggregation/logger-DSMR-P1-usb/blob/master/install.sh
# Start with: chmod +x install.sh && sudo ./install.sh

#***************************************************************************
printf "\e[33mInstallation - disaggregation_logger-DSMR-P1-usb\n\n"
#***************************************************************************
printf "\e[96m* Update apt-get lists..."
sudo apt-get update &>/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m* Set timezone..."
sudo sudo cp /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m* Generate languages..."
sudo bash -c "echo 'nl_NL.UTF-8 UTF-8' >> /etc/locale.gen"
sudo bash -c "echo 'nl_NL ISO-8859-1' >> /etc/locale.gen"
sudo locale-gen &>/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m* Creating folder structure(s)..."
sudo mkdir /home/pi/disaggregation &>/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m* Downloading files..."
sudo rm /home/pi/disaggregation/master.zip &>/dev/null
sudo wget -q https://github.com/disaggregation/logger-DSMR-P1-usb/archive/master.zip -O /home/pi/disaggregation/master.zip &>/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m* Extracting files..."
sudo unzip -q -o /home/pi/disaggregation/master.zip -d /home/pi/disaggregation &>/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m* Cleanup files..."
sudo rm /home/pi/disaggregation/master.zip &>/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m* Set CRON-job..."
echo "@reboot /usr/bin/python /home/pi/disaggregation/logger-DSMR-P1-usb-master/schedule_p1_reader.py 2>&1" >> tempcron
crontab tempcron
sudo rm tempcron
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[33mEnd of installation - disaggregation_logger-DSMR-P1-usb\n\n"
#***************************************************************************