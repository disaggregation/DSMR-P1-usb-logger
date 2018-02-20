import time, os
from read_p1_telegram import read_p1_telegram
from process_p1_telegram import process_p1_telegram
from sqlite_log import sqlite_log

# Chang to current work directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def job(logfolder="logs"):
  print "P1 read started..." + time.strftime("%Y-%m-%d %H:%M:%S")
  telegram = read_p1_telegram(logfolder=logfolder)
  serial_number, values = process_p1_telegram(telegram)
  sqlite_log(serial_number, values, logfolder=logfolder,db_name="P1_observations.db")

while True:
  job()
  time.sleep(10)

