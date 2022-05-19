# /usr/bin/python

from cmath import log
import logging
import json
from time import sleep

class FortiGate(object):

    def __init__(self, ipadrs, login, password):

        self.ipadrs = ipadrs
        self.login = login
        self.password = password

    def affich_fortigate (self):

        print("Your fortigate is: ip:"+ str(self.ipadrs)+" login: "+str(self.login)+" Password: "+ str(self.password))

    def rechercher(self,ip):
        dict = [
            {
                "ipadrs": "172.21.221.100",
                "login": "kawtar",
                "password": "toto",
                
            },
             {
                "ipadrs": "1.1.1.1",
                "login": "root",
                "password": "toto",
                
            }
    ]
        
        with open("fortiget_print.json", "w") as write_file:
            json.dump(dict, write_file, indent=3, separators=(", ", ": "), sort_keys=True)
            
            database = "fortiget_print.json"

            data = json.loads(open(database).read())

            print("***loading data from your JSON file *** ")
            sleep(3)

            """
            data[0]["ipadrs"] = 
                data[0]["login"] = 
                data[0]["password"] = 

            """
        

            #print (data[0]["ipadrs"])

            #if data[0]["ipadrs"] == "172.21.221.0" :
     
            if data[0]["ipadrs"] == ip :
                    print("Fortigate Found.")
                    print(data)
            else :
                    logging.warning("Fortigate NOT Found !")
       

class Fortinet(FortiGate):

    def __init__(self,ipadrs,login,password,port): 

        FortiGate.__init__(self,ipadrs,login,password)

        self.port = port 

    def affiche_Fortinet(self):
        
        print("Your fortigate is: "+ str(self.ipadrs)+" "+str(self.login)+" "+ str(self.password)+" "+str(self.port))
       


def dev_list():
                devices = []
                i = 0
                while 1:
                    i += 1
                    device = input("Enter IP of Device %d: " % i)
                    if device == "":
                        break
                    devices.append(device)

                print(devices, "\n")
                retry = input("Is your list correct? (y/n) ").strip().lower()
                if retry == "no" or retry == "n":
                    dev_list()
                if retry == "yes" or retry == "y":
                    print("\nScript will continue")
                    return devices       
   
if __name__ == '__main__' :

    #for_1 = FortiGate(ipadrs="172.21.221.100", login="kawtar", password="toto")
    ipadrs = input("Enter IP:")
    login = input("Enter Login:")
    password = input("Enter password:")

    for_1 = FortiGate( ipadrs, login, password)
    for_1.affich_fortigate()
    sleep(3)
    
    ip = input("Entrer IP:")
    #rechercher(ip)
         
    forti = Fortinet(ipadrs="0.0.0.0", login="houda", password="toto",port="8080")

    sleep(3)
    print("***affichage Fortigate *** ")
    forti.affich_fortigate()
    sleep(3)
    print("***Affichage fortinet *** ")
    forti.affiche_Fortinet()

    #dev_list()

#"
#
# 
# Generic class : host (ip, psswd,login)
# Fortigate herited from my host class
# function return fortigate's version using snmp ( community v26 RICH:mdp )
# Class F5 herited from Host class
# function return version du F5 using ssh 
# fortigate : login , pwd and snmp community of this fortigate 
# 
# 
# login into vamps machine
# snmp request on linux
#
# 
# import sql 
#
#check fortigate 
#   
# 
# 
#  
# 
# 
# 
# 
# 
# 
# 
#  "