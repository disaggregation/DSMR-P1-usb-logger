from __future__ import print_function
import time
import mysql.connector
import re

user="p1logger"
password="p1logger"
database="EnergyLogs"
#table = "test"

print("Saving data to MYSQL: (will fail if correct user/datebase is not there)")
print("user: "+user)
print("pass: "+password)
print("db: "+database)

#CREAT LOCAL USER AND PRIVILEGES
	#CREATE USER 'p1logger'@'localhost' IDENTIFIED BY 'p1logger';
	#CREATE DATABASE  EnergyLogs;
	#GRANT ALL ON EnergyLogs.* TO 'p1logger'@'localhost';
	#GRANT SELECT ON EnergyLogs.* TO 'p1logger'@'*'; #for remote acces

# mysql connect
cnx = mysql.connector.connect(user=user,password=password,database=database)
cursor = cnx.cursor()


# creata table
#QUERY = "DROP TABLE test"
#cursor.execute(QUERY)
QUERY = "CREATE TABlE `EnergyLogs`.`test` ( id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, datetime DATETIME, power_used INT, power_produced INT);"
#cursor.execute(QUERY)


# get local time
now = time.strftime('%Y-%m-%d %H:%M:%S')

# Insert data
cursor.execute("INSERT INTO test "
               "(datetime,power_used,power_produced) "
               "VALUES (%s,%s,%s)",(now,demand_power,supply_power))

# Make sure data is committed to the database
cnx.commit()
cursor.close()
cnx.close()

