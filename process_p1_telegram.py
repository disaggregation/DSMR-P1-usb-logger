# script to process a P1 (DSMR) telegrams
# based on code from http://gejanssen.com/howto/Slimme-meter-uitlezen/
# Author: Arne Kaas, Matthijs Danes

import re


def process_p1_telegram(telegram):
    result = {"lowtarif_demand": "NULL",
              "hightarif_demand": "NULL",
              "lowtarif_supply": "NULL",
              "hightarif_supply": "NULL",
              "demand_power": "NULL",
              "supply_power": "NULL",
              "demand_power_L1": "NULL",
              "demand_power_L2": "NULL",
              "demand_power_L3": "NULL",
              "supply_power_L1": "NULL",
              "supply_power_L2": "NULL",
              "supply_power_L3": "NULL",
              "voltage": "NULL",
              "current": "NULL",
              "gas_demand": "NULL"
              }

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
            result["lowtarif_demand"] = float(m.group(2))*1000
            print("lowtarif_demand", result["lowtarif_demand"],"Wh")
        elif m.group(1) == "1.8.2":
            result["hightarif_demand"] = float(m.group(2))*1000
            print("hightarif_demand", result["hightarif_demand"],"Wh")
        elif m.group(1) == "2.8.1":
            result["lowtarif_supply"] = float(m.group(2))*1000
            print("lowtarif_supply", result["lowtarif_supply"],"Wh")
        elif m.group(1) == "2.8.2":
            result["hightarif_supply"] = float(m.group(2))*1000
            print("hightarif_supply", result["hightarif_supply"],"Wh")
        elif m.group(1) == "1.7.0":
            result["demand_power"] = float(m.group(2))*1000
            print("demand_power", result["demand_power"],"W")
        elif m.group(1) == "2.7.0":
            result["supply_power"] = float(m.group(2))*1000
            print("supply_power", result["supply_power"],"W")
        elif m.group(1) == "21.7.0":
            result["demand_power_L1"] = float(m.group(2))*1000
            print("demand_power_L1", result["demand_power_L1"],"W")
        elif m.group(1) == "41.7.0":
            result["demand_power_L2"] = float(m.group(2))*1000
            print("demand_power_L2", result["demand_power_L2"],"W")
        elif m.group(1) == "61.7.0":
            result["demand_power_L3"] = float(m.group(2))*1000
            print("demand_power_L3", result["demand_power_L3"],"W")
        elif m.group(1) == "22.7.0":
            result["supply_power_L1"] = float(m.group(2))*1000
            print("supply_power_L1", result["supply_power_L1"],"W")
        elif m.group(1) == "42.7.0":
            result["supply_power_L2"] = float(m.group(2))*1000
            print("supply_power_L2", result["supply_power_L2"],"W")
        elif m.group(1) == "62.7.0":
            result["supply_power_L3"] = float(m.group(2))*1000
            print("supply_power_L3", result["supply_power_L3"],"W")

    reg_expression = "\(([0-9]*\.[0-9]*)\*(V)\)"

    # search and loop results
    x = re.finditer(reg_expression, telegram)  # Match
    for m in x:
        # debug results
        # print (m.group(0))

        # find DSMR power and energy readings
        if m.group(0):
            result["voltage"] = float(m.group(1))
            print("voltage", result["voltage"], "V")

    reg_expression = "\(([0-9]*)\*(A)\)"

    # search and loop results
    x = re.finditer(reg_expression, telegram)  # Match
    for m in x:
        # debug results
        # print (m.group(0))

        # find DSMR power and energy readings
        if m.group(0):
            result["current"] = float(m.group(1))
            print("current", result["current"], "A")

    # the regular expression to find DSMR gas meter readings
    reg_expression = "(24\.3\.0).*\((m3)\)\n*\(([0-9]*\.[0-9]*)\)"
    reg_expression = "\(([0-9]*\.[0-9]*)\*(m3)\)"

    # search and loop results
    x=re.finditer(reg_expression, telegram)  # Match
    for m in x:
        # debug results
        #print (m.group(0))

        #find DSMR power and energy readings
        if m.group(0):
            result["gas_demand"] = float(m.group(1))
            print("gas_demand", result["gas_demand"],"m3")

    # match results to the right db vars/colums
    return serial_number, result

def main():
    # test telegram
    telegram = '''/KMP5 KA6U001234567890

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
    1-0:32.7.0(229.0*V)
    1-0:31.7.0(010*A)
    1-0:21.7.0(02.340*kW)
    1-0:22.7.0(00.000*kW)
    0-1:24.1.0(003)
    0-1:96.1.0(4730303339303031373334343438383137)
    0-1:24.2.1(171220074509W)(00394.562*m3)
    !
    '''

    serial_number, values = process_p1_telegram(telegram)
    print serial_number
    print values

    return


if __name__ == "__main__":
    main()
