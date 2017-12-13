import sqlite3
import os.path
import hashlib

#check if serial number is given, else save data to example.db
try:
	db_name = hashlib.md5(str(serial_number)).hexdigest() #hash serial number for security reasons (eg. data sharing with no backtrace)
	db = os.path.join(os.path.dirname(os.path.realpath(__file__)),'logs',db_name+'.db')
except:
	db = os.path.join(os.path.dirname(os.path.realpath(__file__)),'logs','example.db')

# Create table (if not database dous not exist)
if os.path.isfile(db):
	print ("Saving data to sqlite db: " + db)
        conn = sqlite3.connect(db)
        c = conn.cursor()
else:
	print("Creating sqlite db: " + db)
        conn = sqlite3.connect(db)
        c = conn.cursor()
	c.execute('''CREATE TABLE loads (date datetime, lowtarif_demand real, hightarif_demand real, lowtarif_supply real, hightarif_supply real, demand_power real, supply_power real, gas_demand real, demand_power_L1 real, demand_power_L2 real, demand_power_L3 real, supply_power_L1 real, supply_power_L2 real, supply_power_L3 real)''')

try:
	# Insert a row of data
	c.execute("INSERT INTO loads VALUES (datetime(),"+str(lowtarif_demand)+","+str(hightarif_demand)+","+str(lowtarif_supply)+","+str(hightarif_supply)+","+str(demand_power)+","+str(supply_power)+","+str(gas_demand)+","+str(demand_power_L1)+","+str(demand_power_L2)+","+str(demand_power_L3)+","+str(supply_power_L1)+","+str(supply_power_L2)+","+str(supply_power_L3)+")")
except:
        try:
		# Insert a row of data
		c.execute("INSERT INTO loads VALUES (datetime(),"+str(lowtarif_demand)+","+str(hightarif_demand)+","+str(lowtarif_supply)+","+str(hightarif_supply)+","+str(demand_power)+","+str(supply_power)+",0.0,"+str(demand_power_L1)+","+str(demand_power_L2)+","+str(demand_power_L3)+","+str(supply_power_L1)+","+str(supply_power_L2)+","+str(supply_power_L3)+")")
		print("INSERT INTO loads VALUES (datetime(),"+str(lowtarif_demand)+","+str(hightarif_demand)+","+str(lowtarif_supply)+","+str(hightarif_supply)+","+str(demand_power)+","+str(supply_power)+",0.0,"+str(demand_power_L1)+","+str(demand_power_L2)+","+str(demand_power_L3)+","+str(supply_power_L1)+","+str(supply_power_L2)+","+str(supply_power_L3)+")")
	except:
	        c.execute("INSERT INTO loads VALUES (datetime(),"+str(lowtarif_demand)+","+str(hightarif_demand)+","+str(lowtarif_supply)+","+str(hightarif_supply)+","+str(demand_power)+","+str(supply_power)+",0.0,0.0,0.0,0.0,0.0,0.0,0.0);")
        	print("INSERT INTO loads VALUES (datetime(),"+str(lowtarif_demand)+","+str(hightarif_demand)+","+str(lowtarif_supply)+","+str(hightarif_supply)+","+str(demand_power)+","+str(supply_power)+",0.0,0.0,0.0,0.0,0.0,0.0,0.0);")


#        c.execute("INSERT INTO loads VALUES (datetime(),"+str(lowtarif_demand)+","+str(hightarif_demand)+","+str(lowtarif_supply)+","+str(hightarif_supply)+","+str(demand_power)+","+str(supply_power)+",0.0,0.0,0.0,0.0,0.0,0.0,0.0);")


# Save (commit) the changes and close db
conn.commit()
conn.close()
