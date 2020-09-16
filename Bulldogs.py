#!/usr/bin/python2
#coding=utf-8
#Coded by 4loneloVerTz
#Don't edit my script look ur self before do it.
#Facebook: ΛᄂӨПΣᄂӨVΣЯƬZ
#Whatsapp:+255 711 928 532
#TANZANIA CYBER ARMY   
#DarkTermuxUser
#410n310v3rTz



import os, sys, subprocess,time
import os, sys, json, urllib, re
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")

def logo():
 print("""  
 
 \033[37m=============================================
\033[31m CODED BY \033[37m✴✴ \033[37m410n310v3rTz✴✴    
\033[31m ☠Youtube :Dark Termux User☠
\033[34m ☠Facebook:ΛᄂӨПΣᄂӨVΣЯƬZ☠
\033[37m ☠Github:https://github.com/4loneloVerTz☠
\033[39m☠Instagram: dark_termux_user☠
\033[32m ☠Whatsapp:+255 711 928 532☠
\033[31m ☠0N3 N4T10N UND3R CCTV ☠
 \033[37m=============================================
  """)
os.system("clear")
os.system("figlet  WAIT.... ")
print "[ INSTALLATION PROCESS.....]"
time.sleep(5)
print "[==========>      ] 35%"
time.sleep(4)
print "[===============>     ] 50%"
time.sleep(5)
print "[====================>   ]  75%"
time.sleep(4)
print "[=========================>  ] 85%"
time.sleep(4)
print "[==============================] 100%"
time.sleep(2)
os.system("clear")
os.system("figlet BULLDOGS  ")


logo()
  

print("""
\033[37mCOMMAND    INFORMATION
       \n\n1.Website    Website info
       \n\n2.IP    IP address location
       \n\n3.Exit    Exit BULLDOGS \033[31m CTRL + C
       
        \033[37m CHOOSE : 1 or 2 
       \033[0m""")
def help():
	print("""\n\n
  Commands :
       \n\n1. web : Website info
       \n2.     IP     :  IP address location
       \n3.     Exit  : Exit BULLDOGS

\n\n\n OPTION : 1 or 2
       """)





	

Bulldogs = raw_input("\n\n  \033[32mBULLDOGS \033[31mONLINE \033[37mOPTION NO \033[0m ")
if Bulldogs == "help":
            help()

elif Bulldogs == '1':
	print "\n\n\t  \033[37m  ▁ ▂ ▄ ▅ ▆ ▇ █ Dark Termux User █ ▇ ▆ ▅ ▄ ▂ ▁ \033[0m\n\n\n example. Target\n\n\033[1m\033[33mWebsite\033[0m : www.millardayo.com\n\n\033[1m\033[33mIp\033[0m      :159.69.57.173"
IP = raw_input("\n\n\033[31mTARGET  \033[37mWebsite   \033[31mAttack   \033[0m")
IP = raw_input("\n\n\033[31mTARGET IP  \033[37m Not necessary")
print "\nSearching for\033[32m\033[31m Target %s" % (IP)
IP2 = IP.split(".")
if IP in ["self", "myself"]:
  urllib.urlretrieve("https://api.ipify.org?format=json", 'data.json')
  file = open('data.json')
  data = json.load(file)
  IP = data["ip"]
urllib.urlretrieve("http://ip-api.com/json/%s" %IP, 'data.json')
file = open('data.json')
data = json.load(file)
if data["status"] != "success": 
  	print "\nSorry!!!  are you sure...\n\n\033[1m\033[33m  "
  	exit()


	print "\033[1m\033[31m\n\t\t[!] Exit Bulldogs...     \n\n\t\033[1m\033[32m\033[0m"
	sys.exit()
	
else:
	print "\n\n\n\t  \033[31m TARGET : \033[32mFOUND\033[0m\n\n"

for k in data:
    if data[k] == "": data[k] = "Unknown"
print "\n       *** .: %s :. ***\n\n\n" %data["query"]
print "\nONLINE                         \033[32m\033[1m%s\033[0m    " %data["status"]
print "\nISP                            \033[1m\033[32m%s\033[0m    "%data["isp"]
print "\nORG. NAME                      \033[32m\033[1m%s\033[0m" %data["org"]
print "\nCITY                           \033[32m\033[1m%s\033[0m    " %data["city"]
print "\nCITY TIMEZONE                  \033[32m\033[1m%s\033[0m    " %data["timezone"]
print "\nREGION NAME                    \033[32m\033[1m%s\033[0m" %data["regionName"]
print "\nREGION CODE                    \033[32m\033[1m%s,\033[0m" %data["region"]
print "\nCOUNTRY                        \033[32m\033[1m%s,\033[0m" %data["country"]
print "\nCOUNTRY CODE                   \033[32m\033[1m%s,\033[0m" %data["countryCode"]
print "\nZIP CODE                       \033[32m\033[1m%s\033[0m" %data["zip"]
print "\nLATITUDE                       \033[32m\033[1m%s\033[0m" %data["lat"]
print "\nLONGITUDE                      \033[32m\033[1m%s\033[0m" %data["lon"]
print "\nAS NUMBER/NAME                 \033[32m\033[1m%s\033[0m" %data["as"]
            

print "\n\n\n\n\033[31m ƬΛПZΛПIΛ YӨЦПG BӨY :  \033[37m ΛЦƬΉӨЯ  : \033[37m ΛᄂӨПΣᄂӨVΣЯƬZ  \n\n\033[0m"
time.sleep(0.5)
print "\n\033[37m            ░▒▓█ KARIBU TANZANIA █▓▒░\n\033[0m"
time.sleep(2)
os.system('rm *.json')
	
sys.exit()
