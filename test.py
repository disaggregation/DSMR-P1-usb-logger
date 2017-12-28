import time,os
from process_p1_telegram import process_p1_telegram
from sqlite_log import sqlite_log

print ("P1 read test started..." + time.strftime("%Y-%m-%d %H:%M:%S"))
def test(dirout=os.path.dirname(os.path.realpath(__file__)),
         logfolder="logs"):
    try:
        from read_p1_telegram import read_p1_telegram
        telegram = read_p1_telegram(logfolder=logfolder)
    except:
        print("DSMR P1 USB read failed, usign test telegram")
        with open(os.path.join(dirout,logfolder,'testP1telegram.txt'), 'r') as myfile:
            telegram=myfile.read()
        print (telegram)

    #try:
    serial_number, values = process_p1_telegram(telegram)
    #except:
    #    print("processing failed")
    #    return

    sqlite_log(serial_number, values, logfolder=logfolder,db_name="P1_observations.db")

    try:
        execfile("mysql_logger.py")
    except:
        print("mysql save of data failed, please check settings in mysql_logger.py")
    return

def main():
    test()
    return

if __name__ == "__main__":
    main()