from pysnmp.hlapi import *

fetch = ["sysName", "sysDescr", "sysUpTime" ]
num = 3
for i in range(3):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(('192.168.1.23', 161)),
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB', fetch[i] , 0 )))
    )
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
