#function: Upload to server
import ftplib

def upload_to_server(path_to_file):
    session = ftplib.FTP('ftp.allianders.nl','disaggregation@allianders.nl','uploadyourdata')
    file = open(path_to_file,'rb')                      # file to send

    try:
        print ("Upload started...")
        session.storbinary('STOR '+path_to_file, file)     # send the file
        print ("Upload succeded")
    except:
        print ("Upload failed...")

    file.close()                                      # close file and FTP
    session.quit()


#save all files in de folder data to server
path= "./upload/"
from os import listdir
from os.path import isfile, join, realpath

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print (onlyfiles)

for file in onlyfiles:
    path_to_file = path + file
    upload_to_server(path_to_file)



#test download
import ftplib
ftp = ftplib.FTP()
host = "ftp.allianders.nl"
path = join(realpath(__file__),"logs")
filename = 'example.db'

port = 21
ftp.connect(host, port)
print (ftp.getwelcome())
try:
    print ("Logging in...")
    ftp.login('disaggregation@allianders.nl','uploadyourdata')
    ftp.cwd(path)
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
        print ("Downloaded: " +filename)
    except:
        print("Error during download")
except:
    print ("Failed to login")

