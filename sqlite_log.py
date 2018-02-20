import sqlite3
import os.path
import hashlib

def sqlite_log(serial_number, values, db_name=False, logfolder="logs"):
    #check if serial number is given, else save data to example.db
    if db_name==False:
        try:
            db_name = hashlib.md5(str(serial_number)).hexdigest() #hash serial number for security reasons (eg. data sharing with no backtrace)
            db = os.path.join(os.path.dirname(os.path.realpath(__file__)),logfolder,db_name+'.db')
        except:
            db = os.path.join(os.path.dirname(os.path.realpath(__file__)),logfolder,'example.db')
    else:
        db = os.path.join(os.path.dirname(os.path.realpath(__file__)), logfolder, db_name)

    try: #creating database
        #  Create table (if not database dous not exist)
        if os.path.isfile(db):
            print("Saving data to sqlite db: " + db)
            conn = sqlite3.connect(db)
            c = conn.cursor()

        else:
            print("Creating sqlite db: " + db)
            conn = sqlite3.connect(db)
            c = conn.cursor()

            sql = '''CREATE TABLE loads (date datetime, lowtarif_demand real, hightarif_demand real, 
                                        lowtarif_supply real, hightarif_supply real, demand_power real, 
                                        supply_power real, gas_demand real, demand_power_L1 real, 
                                        demand_power_L2 real, demand_power_L3 real, supply_power_L1 real,
                                        supply_power_L2 real, supply_power_L3 real, voltage real, current real)'''
            c.execute(sql)
            # c.execute('''CREATE VIEW IF NOT EXISTS loadsonly  (datetime,demand) AS SELECT date,demand_power FROM loads''')
            
    except:
        print("Could not create database")
        return

    try:	# Insert a row of data with power for each line and gas
        sql = "INSERT INTO loads VALUES (datetime(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" %(values["lowtarif_demand"],
                                                                                                      values["lowtarif_supply"],
                                                                                                      values["hightarif_demand"],
                                                                                                      values["hightarif_supply"],
                                                                                                      values["demand_power"],
                                                                                                      values["supply_power"],
                                                                                                      values["gas_demand"],
                                                                                                      values["demand_power_L1"],
                                                                                                      values["demand_power_L2"],
                                                                                                      values["demand_power_L3"],
                                                                                                      values["supply_power_L1"],
                                                                                                      values["supply_power_L2"],
                                                                                                      values["supply_power_L3"],
                                                                                                      values["voltage"],
                                                                                                      values["current"])
        c.execute(sql)
        print(sql)
    except:
        print("Could not insert observation into database")



    # Save (commit) the changes and close db
    conn.commit()
    conn.close()
    return

def main():
    serial_number = "KMP5 KA6U001234567890"
    values = {'demand_power_L1': 2340.0, 'demand_power_L3': 'NULL', 'demand_power_L2': 'NULL', 'supply_power_L1': 0.0,
              'hightarif_supply': 1000.0, 'lowtarif_supply': 26000.0, 'voltage': 'NULL', 'voltage': 229.0,
              'hightarif_demand': 5000.0, 'lowtarif_demand': 24000.0, 'gas_demand': 394.562, 'supply_power_L2': 'NULL',
              'supply_power_L3': 'NULL', 'current': 10.0, 'supply_power': 0.0, 'demand_power': 30.0}

    sqlite_log(serial_number, values)
    return

if __name__ == "__main__":
	main()
