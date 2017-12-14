#!/bin/bash

# Installation script for: disaggregation_logger-DSMR-P1-usb
# OS/HW: Raspbian / Raspberry Pi
# Path: /home/pi/disaggregation

# Get started:
# Download with: sudo wget https://raw.githubusercontent.com/disaggregation/logger-DSMR-P1-usb/master/install.sh
# Start with: sudo chmod +x install.sh && sudo ./install.sh

#***************************************************************************
printf "\e[33mInstallation - disaggregation_logger-DSMR-P1-usb v1.12\n\n"
#***************************************************************************
log_dir="/home/pi/dissagregation"
read -e -i "$log_dir" -p "Please enter your name: " input
log_dir="${input:-$name}"

printf "\e[96m* CHECK\n"
printf "\e[96m  - Check if USB Serial port is found..."
if ls /dev | grep 'ttyUSB0' >/dev/null 2>&1; then
  printf "\e[92mOK\e[0m\n"
else
  printf "\e[91mNOT FOUND!, aborting installation!\e[0m\n"
  exit
fi
#***************************************************************************
printf "\e[96m* GENERAL\n"
printf "\e[96m  - Update apt-get lists..."
sudo apt-get update &>/dev/null
sudo apt-get install screen
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m  - Set timezone..."
sudo sudo cp /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m  - Generate languages..."
sudo bash -c "echo 'nl_NL.UTF-8 UTF-8' >> /etc/locale.gen"
sudo bash -c "echo 'nl_NL ISO-8859-1' >> /etc/locale.gen"
sudo locale-gen &>/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m* DSRM LOGGER FILES\n"
printf "\e[96m  - Creating folder structure(s)..."
sudo mkdir $log_dir &>/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m  - Downloading files..."
sudo rm ${log_dir}/master.zip &>/dev/null
sudo wget -q https://github.com/disaggregation/logger-DSMR-P1-usb/archive/master.zip -O ${log_dir}/master.zip &>/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m  - Extracting files..."
sudo unzip -q -o ${log_dir}/master.zip -d ${log_dir} &>/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m  - Cleanup files..."
sudo rm ${log_dir}/master.zip &>/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m  - Changing file permissions and rights to pi..."
sudo chmod -R 777 ${log_dir} &>/dev/null
sudo chown -R pi ${log_dir} &>/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m* PYTHON DEPENDENCIES\n"
printf "\e[96m  - Downloading and installing pyserial..."
pip install pyserial >/dev/null
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m* CONFIGURE\n"
printf "\e[96m  - Set CRON-job..."
sudo cd ${log_dir}/logger-DSMR-P1-usb-master
echo "@reboot screen -dmS atboot_P1_logger python schedule_p1_reader.py 2>&1" >> tempcron
crontab tempcron
sudo rm tempcron
printf "\e[92mOK\e[0m\n"
#***************************************************************************
printf "\e[96m  - Start DSMR P1 script..."
screen -dmS atboot_P1_logger python schedule_p1_reader.py 2>&1 &>/dev/null 
printf "\e[92m - OK\e[0m\n"
#***************************************************************************
printf "\n\e[33mEnd of installation - disaggregation_logger-DSMR-P1-usb\n"
#***************************************************************************
