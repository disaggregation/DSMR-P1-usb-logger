# DSMR P1 uitlezen
# (c) 10-2012 - GJ - gratis te kopieren en te plakken
# update Arne Kaas 10-08-2017

version = "2.0"
import sys
import serial
import signal
import os

# Variables
cwd = os.path.dirname(os.path.realpath(__file__))
logfile = cwd + "/logs/lastP1read.txt"

# Create "logs" folder if not exists.
if not os.path.exists(os.path.dirname(logfile)):
  os.makedirs(os.path.dirname(logfile))

##############################################################################
#Main program
##############################################################################
print ("USB DSMR P1 telegram reader, version "+  version)
print ("Control-C to exit")

#Set COM port config
try:
	ser
except:
	ser = serial.Serial()
	ser.baudrate = 9600
	ser.bytesize=serial.SEVENBITS
	ser.parity=serial.PARITY_EVEN
ser.stopbits=serial.STOPBITS_ONE
ser.xonxoff=0
ser.rtscts=0
ser.timeout=20
ser.port="/dev/ttyUSB0" #use on raspberrypi ser.port="/dev/tty.usbserial-P11KXDOA"  # use for testing on macs


#Initialize empty telegram
telegram = ''

#set timeonut
def handler(signum, frame):
	ser.close()
	print("Error handler called with errornum: ", signum)
	raise OSError("No proper DSMR P1 telegram recieved.")

def read_DSMR_telegram():
	global ser
	global telegram
	global signal
	global handler

	#Open COM port
	ser.open()
#	except:
#		sys.exit ("Coul not open serial '%s'. Aaaaarch."  % ser.name)
	
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

	signal.alarm(0)		  # Disable the alarm

try:
    read_DSMR_telegram()
except:
	print ("Increased baudrate to 115200, retrying serial")	
#	try:
	try:
		ser.close()
	except:
		print("could not close serial")
		ser.baudrate = 115200
		ser.parity=serial.PARITY_NONE
		ser.bytesize=serial.EIGHTBITS
		try:
			read_DSMR_telegram()
		except:
			print("115200 also faile, faling back to 9600")
			ser.baudrate = 9600
			ser.bytesize=serial.SEVENBITS
			ser.parity=serial.PARITY_EVEN

text_file = open(logfile, "w")
text_file.write(telegram)
text_file.close()
