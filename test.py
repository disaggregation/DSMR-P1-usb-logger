import time

print ("P1 read test started..." + time.strftime("%Y-%m-%d %H:%M:%S"))

try:
    execfile("read_p1_telegram.py")
except:
    print("DSMR P1 USB read failed, usign test telegram")
    with open('logs/testP1telegram.txt', 'r') as myfile:
        telegram=myfile.read()
    print (telegram)

try:
    execfile("process_p1_telegram.py")
except:
    print("processing failed")

#try:
execfile("sqlite_log.py")
#except:
#    print("Wrong data/telegram recieved?")

try:
    execfile("mysql_logger.py")
except:
    print("mysql save of data failed, please check settings in mysql_logger.py")
