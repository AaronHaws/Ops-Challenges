# python3
import os
import ipaddress


WhoAmI = (os)
IpA = (ipaddress)

def IpA():
    if(os.name == "nt"):
      os.system("ipconfig")
    else(os.name == "unix"):
      os.system("ifconfig")


print (f"{WhoAmI, ipA}")