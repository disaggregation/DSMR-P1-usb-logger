import time, os
from read_p1_telegram import read_p1_telegram
from process_p1_telegram import process_p1_telegram
from sqlite_log import sqlite_log

# Chang to current work directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def job(logfolder="logs"):
  print "Serial read (P1) started..." + time.strftime("%Y-%m-%d %H:%M:%S")
  telegram = read_p1_telegram(logfolder=logfolder)
  serial_number, values = process_p1_telegram(telegram)
  sqlite_log(serial_number, values, logfolder=logfolder,db_name="P1_observations.db")
  sqlite_log(serial_number, values, logfolder="../data/",db_name="disaggregation.db")

global type
type = 9600
while True:
  job()
  #time.sleep(1)

