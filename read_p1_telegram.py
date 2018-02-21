# DSMR P1 uitlezen
# (c) 10-2012 - GJ - gratis te kopieren en te plakken
# update Matthijs Danes 27-12-2017

version = "2.0"
import sys
import serial
import signal
import os

#set timeonut
def handler(signum, frame):
    ser.close()
    print("Error handler called with errornum: ", signum)
    raise OSError("No proper DSMR P1 telegram recieved.")
    return

def read_DSMR_telegram(ser, telegram = ''):
    #global ser
    #global telegram
    #global signal
    #global handler

    #Open COM port
    ser.open()
#    except:
#        sys.exit ("Coul not open serial '%s'. Aaaaarch."  % ser.name)
    
	# Set the signal handler and a 15-second alarm
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(15)
    
    while True:
        #proces serial line to string
        p1_raw = ser.readline()
        p1_str=str(p1_raw)
        p1_line=p1_str.strip()
    
        #print for debugging purpose
        print (p1_line) 
    
        #add line to telegram
        telegram += str(p1_line) + '\n'
    
        # stop reading if '!' was found (DSMR telegram ends with it.)
	if len(p1_line) > 0:
            if p1_line[0] == '!':
    	    #Close port and show status
    	    	try:
    	             ser.close()
    	    	except:	
    	             sys.exit ("Oops %s. Program aborted. Could not close serial port" % ser.name )
    	        break

    signal.alarm(0)          # Disable the alarm
    return telegram

def create_log_folder(dirout=os.path.dirname(os.path.realpath(__file__)),
                     logfolder="logs"):
    # Create "logs" folder if not exists.
    if not os.path.exists(os.path.join(dirout,logfolder)):
        os.makedirs(os.path.join(dirout,logfolder))
    return

def read_p1_telegram(dirout=os.path.dirname(os.path.realpath(__file__)),
                     logfolder="logs",
                     logfile="lastP1read.txt"):
    global type
    create_log_folder(dirout=dirout,logfolder=logfolder)

#    print ("USB DSMR P1 telegram reader, version " + version)
    print ("Waiting for next telegram... Control-C to exit")

    # Set COM port config
    try:
        ser
    except:
	ser = serial.Serial()
	if type == 9600:
        	ser.baudrate = 9600
        	ser.bytesize = serial.SEVENBITS
        	ser.parity = serial.PARITY_EVEN
    	else:
		ser.baudrate = 115200
       		ser.parity=serial.PARITY_NONE
        	ser.bytesize=serial.EIGHTBITS

    ser.stopbits = serial.STOPBITS_ONE
    ser.xonxoff = 0
    ser.rtscts = 0
    ser.timeout = 20
    ser.port = "/dev/ttyUSB0"  # use on raspberrypi ser.port="/dev/tty.usbserial-P11KXDOA"  # use for testing on macs

    try:
        telegram = read_DSMR_telegram(ser)
    except:
	try:
            ser.close()
        except:
            print("could not close serial")
	print ("Increasing baudrate to 115200, retrying serial")
        if type == 9600:
		type = 115200
	        telegram = read_p1_telegram()
	else:
		type = 9600
		telegram = 'read failed'

#        ser.baudrate = 115200
#        ser.parity=serial.PARITY_NONE
#        ser.bytesize=serial.EIGHTBITS
#        try:
#            telegram = read_p1_telegram()
#        except:
#            print("115200 also failed, faling back to 9600")
#	    type = 9600
#        ser.baudrate = 9600
#        ser.bytesize=serial.SEVENBITS
#        ser.parity=serial.PARITY_EVEN

    text_file = open(os.path.join(dirout,logfolder,logfile), "w")
    text_file.write(telegram)
    text_file.close()
    return telegram

def main():
    telegram = read_p1_telegram()
    return

if __name__ == "__main__":
    main()
