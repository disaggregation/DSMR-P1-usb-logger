# script to process a P1 (DSMR) telegrams
# based on code from http://gejanssen.com/howto/Slimme-meter-uitlezen/
# Author: Arne Kaas

import re

#test telegram
telegram2 = '''/KMP5 KA6U001234567890

0-0:96.1.1(204B413655303031363630323937393132)
1-0:1.8.1(00024.000*kWh)
1-0:1.8.2(00005.000*kWh)
1-0:2.8.1(00026.000*kWh)
1-0:2.8.2(00001.000*kWh)
0-0:96.14.0(0002)
1-0:1.7.0(0000.03*kW)
1-0:2.7.0(0000.00*kW)
0-0:17.0.0(999*A)
0-0:96.3.10(1)
0-0:96.13.1()
0-0:96.13.0()
0-1:24.1.0(3)
0-1:96.1.0(3238313031353431303034303232323131)
0-1:24.3.0(121030140000)(00)(60)(1)(0-1:24.2.1)(m3)
(00024.123)
0-1:24.4.0(1)
!
'''

# search meter serial number
x=re.finditer("\/[\s]*(.*)[\s]*\n", telegram)  # Match
for m in x:
    serial_number = m.group(1)
    print ("serial_number '"+serial_number+"'")

# the regular expression to find DSMR power and energy electricity meter readings
reg_expression = ":([0-9]?[1-2]\.[7-8]\.[0-2])\(([0-9]*\.[0-9]*)\*(kW[h]?)\)"

# search and loop results
x=re.finditer(reg_expression, telegram)  # Match
for m in x:
    # debug results
    # print (m.group(0),m.group(1),m.group(2),m.group(3))
    
    #find DSMR power and energy readings
    if m.group(1) == "1.8.1":
        lowtarif_demand = float(m.group(2))*1000
        print("lowtarif_demand", lowtarif_demand,"Wh")
    elif m.group(1) == "1.8.2":
        hightarif_demand = float(m.group(2))*1000
        print("hightarif_demand", hightarif_demand,"Wh")
    elif m.group(1) == "2.8.1":
        lowtarif_supply = float(m.group(2))*1000
        print("lowtarif_supply", lowtarif_supply,"Wh")
    elif m.group(1) == "2.8.2":
        hightarif_supply = float(m.group(2))*1000
        print("hightarif_supply", hightarif_supply,"Wh")
    elif m.group(1) == "1.7.0":
        demand_power = float(m.group(2))*1000
        print("demand_power", demand_power,"W")
    elif m.group(1) == "2.7.0":
        supply_power = float(m.group(2))*1000
        print("supply_power", supply_power,"W")
    elif m.group(1) == "21.7.0":
        demand_power_L1 = float(m.group(2))*1000
        print("demand_power_L1", demand_power_L1,"W")
    elif m.group(1) == "41.7.0":
        demand_power_L2 = float(m.group(2))*1000
        print("demand_power_L2", demand_power_L2,"W")
    elif m.group(1) == "61.7.0":
        demand_power_L3 = float(m.group(2))*1000
        print("demand_power_L3", demand_power_L3,"W")
    elif m.group(1) == "22.7.0":
        supply_power_L1 = float(m.group(2))*1000
        print("supply_power_L1", supply_power_L1,"W")
    elif m.group(1) == "42.7.0":
        supply_power_L2 = float(m.group(2))*1000
        print("supply_power_L2", supply_power_L2,"W")
    elif m.group(1) == "62.7.0":
        supply_power_L3 = float(m.group(2))*1000
        print("supply_power_L3", supply_power_L3,"W")

# the regular expression to find DSMR gas meter readings
reg_expression = "(24\.3\.0).*\((m3)\)\n*\(([0-9]*\.[0-9]*)\)"

# search and loop results
x=re.finditer(reg_expression, telegram)  # Match
for m in x:
    # debug results
    # print (m.group(0))
    
    #find DSMR power and energy readings
    if m.group(1) == "24.3.0":
        gas_demand = float(m.group(3))
        print("gas_demand", gas_demand,"m3")

# match results to the right db vars/colums
