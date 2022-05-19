

import ipaddress
from snmp_cmds import snmpwalk


device_ip = '172.21.220.143'
community='Rich'
oid='1.3.6.1.4.1.12356.101.4.1.1'

def test():
    result = snmpwalk(ipaddress=device_ip,oid='1.3.6.1.4.1.12356.101.4.1.1',community='Rich')


    """
    Prints a list of tuples, each tuple containing the OID walked and the value found at that OID.
    """
    for line in result:
        print(line[0],'  ',line[1])
        #print(line.value)


if __name__ == "__main__" :
    test()