import time
import os

# Chang to current work directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def job():
  print "P1 read started..." + time.strftime("%Y-%m-%d %H:%M:%S")
  execfile("read_p1_telegram.py")
  execfile("process_p1_telegram.py") 
  execfile("sqlite_log.py")

while True:
  job()
  time.sleep(10)

