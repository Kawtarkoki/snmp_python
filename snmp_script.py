from pysnmp import hlapi
#import netsnmp


"""
target (IP or name of the remote device)
the list of Object IDs (oids) we want to get
a set of credentials to authenticate our session. 
We can also specify a different UDP port if we want, and use an existing SNMP engine or custom context. 

"""

def get(target, oids, credentials, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.getCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        *construct_object_types(oids)
    )
    return fetch(handler, 1)[0]


def construct_object_types(list_of_oids):
    object_types = []
    for oid in list_of_oids:
        object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))
    return object_types

def fetch(handler, count):
    result = []
    for i in range(count):
        try:
            error_indication, error_status, error_index, var_binds = next(handler)
            if not error_indication and not error_status:
                items = {}
                for var_bind in var_binds:
                    items[str(var_bind[0])] = cast(var_bind[1])
                result.append(items)
            else:
                raise RuntimeError('Got SNMP error: {0}'.format(error_indication))
        except StopIteration:
            break
    return result

def cast(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            try:
                return str(value)
            except (ValueError, TypeError):
                pass
    return value


hlapi.CommunityData('Rich')


#hlapi.UsmUserData('testuser', authKey='authenticationkey', privKey='encryptionkey', authProtocol=hlapi.usmHMACSHAAuthProtocol, privProtocol=hlapi.usmAesCfb128Protocol)



##########Getting the hostname!#################
## test get()
print(get('172.21.220.143', ['1.3.6.1.4.1.12356.101.4.1.1'], hlapi.CommunityData('Rich')))




#session=netsnmp.Session(DestHost='172.21.220.143', Version=2, Community='Rich', RemotePort=161)


#myoid=netsnmp.VarList('.1.3.6.1.4.1.28507.14.1.3.1.1.2.2')
"""
res=snmp.walk(myoid)
for i in res:
  print (i)

"""



  