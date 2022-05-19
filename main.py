from snmp_cmds import snmpwalk
from time import sleep

"""
# Generic class : host (ip, psswd,login)
# Fortigate herited from my host class
# function return fortigate's version using snmp ( community v2c RICH:mdp )

"""
class Host(object):

    def __init__(self, ipadrs, login, password):

        self.ipadrs = ipadrs
        self.login = login
        self.password = password

    def affich(self):

        print("Your is: ip:"+str( self.ipadrs)+" login: "+str(self.login)+" Password: "+ str(self.password))


class FortiGate(Host):

    def __init__(self,ipadrs,login,password): 

        Host.__init__(self,ipadrs,login,password)


    def affiche_Fortigate(self):
        
        print("Your fortigate is: "+ str(self.ipadrs)+" "+str(self.login)+" "+ str(self.password))
       

    def affich_version (self,device_ip,oid,community):
        
        self.device_ip=device_ip
        self.oid=oid
        self.community=community
    
        #result = snmpwalk(ipaddress='172.21.220.143',oid='1.3.6.1.4.1.12356.101.4.1.1',community='Rich')

        result = snmpwalk(ipaddress=device_ip,oid=oid,community=community)
        """
        Print a list of tuples, each tuple containing the OID walked and the value found at that OID.

        for line in result:
            print(line[0],'  ',line[1])

        """

        for line in result:
                print('***your device that has oid : ***\n',line[0],
                
                      '\n**** has a version: ****\n',line[1])

"""
 Class F5 herited from Host class
"""
class F5(Host):

    def __init__(self,ipadrs,login,password): 

        Host.__init__(self,ipadrs,login,password)

    def affiche_F5(self):
        
        print("Your F5 is: "+ str(self.ipadrs)+" "+str(self.login)+" "+ str(self.password))

"""
function return version du F5 using ssh 

"""





#device_ip = '172.21.220.143'
#community='Rich'
#oid='1.3.6.1.4.1.12356.101.4.1.1'

if __name__ == "__main__" :
    #test()
    for_1 = FortiGate(ipadrs="172.21.221.100", login="kawtar", password="toto")
    for_1.affiche_Fortigate()
    sleep(3)


    device_ip = input("Enter device_ip:")
    oid = input("Enter oid:")
    community = input("Enter community:")

    for_1.affich_version(device_ip,oid,community)








